from statsmodels.tsa.arima.model import ARIMA
from pandas_datareader import data as web
import yfinance as yfin
import datetime as dt
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error
from typing import List
import warnings
from expiring_lru_cache import lru_cache, DAYS
from fastapi import APIRouter


# Config
yfin.pdr_override()
warnings.filterwarnings("ignore")
router = APIRouter()

# Params

start = dt.datetime(2010, 1, 1)
end = dt.datetime.now()


def find_lagged_return(data: pd.DataFrame,
                       ticker: str,
                       shift_period: int = None,
                       return_period: int = 5) -> pd.Series:
    if shift_period:
        return np.log(data.loc[:, ticker]
                      ).diff(return_period).shift(-return_period)
    else:
        return np.log(data.loc[:, ticker]).diff(return_period)


@lru_cache(maxsize=1, expires_after=0.5*DAYS)
def get_data():
    # Getting Microsoft, IBM, and Google data from yahoo finance
    stk_tickers = ['MSFT', 'IBM', 'GOOGL']
    stk_data = web.get_data_yahoo(stk_tickers, start, end)

    # Getting the Japan US Exchange rate & US UK exchange rate
    ccy_tickers = ['DEXJPUS', 'DEXUSUK']
    ccy_data = web.get_data_fred(ccy_tickers, start, end)

    # Getting the index data
    idx_tickers = ['SP500', 'DJIA', 'VIXCLS']
    idx_data = web.get_data_fred(idx_tickers, start, end)
    return stk_data, ccy_data, idx_data


def prepare_data(weekly_return_period: int, validation_size: float):
    # Get the data
    stk_data, ccy_data, idx_data = get_data()

    # find the value to be predicted, i.e., MSFT weekly return
    Y = find_lagged_return(stk_data, ('Adj Close', 'MSFT'),
                           weekly_return_period, weekly_return_period)
    Y.name = Y.name[-1] + '_pred'

    # get the weekly return of google and ibm data
    X1 = find_lagged_return(
        stk_data, ('Adj Close', ('GOOGL', 'IBM')), None, weekly_return_period)
    X1.columns = X1.columns.droplevel()

    # get the index and currency returns
    X2 = np.log(ccy_data).diff(weekly_return_period)
    X3 = np.log(idx_data).diff(weekly_return_period)

    # get the msft data for weekly period* [1,3,6,12]
    X4 = pd.concat([find_lagged_return(stk_data, ('Adj Close', ('MSFT')), None, i)
                    for i in [weekly_return_period,
                              weekly_return_period*3,
                              # 15 days if weekly_return_period is 5
                              weekly_return_period*6,
                              # 30 days if weekly_return_period is 5
                              weekly_return_period*12,
                              # 60 days if weekly_return_period is 5
                              weekly_return_period*18,
                              # 90 days if weekly_return_period is 5
                              ]], axis=1).dropna()
    X4.columns = ['MSFT_DT', 'MSFT_3DT', 'MSFT_6DT', 'MSFT_12DT', 'MSFT_18DT']

    # Let's merge them all
    X = pd.concat([X1, X2, X3, X4], axis=1)
    print(
        f"X has minimum date of {min(X.index)} and maximum" +
        f" date of {max(X.index)}")

    X['DEXJPUS'] = X['DEXJPUS'].fillna(method='ffill')
    X['DEXUSUK'] = X['DEXUSUK'].fillna(method='ffill')
    Y = Y.fillna(method='ffill')
    # Let's create the dataset and remove all the rows containing NA in either of the column
    dataset = pd.concat([Y, X], axis=1).dropna(
    ).iloc[::-weekly_return_period, :].sort_index()

    Y = dataset[[Y.name]]
    X = dataset[X.columns]

    train_size = int(len(X) * (1-validation_size))
    # Note - not doing a random split because we want to do a prediction in
    # future based on previous sequence; so ordered data is must
    X_train, X_test = X[0:train_size], X[train_size:len(X)]
    Y_train, Y_test = Y[0:train_size], Y[train_size:len(X)]

    # Let's only take exogenous variables
    X_train_ARIMA = X_train[['GOOGL', 'IBM', 'DEXJPUS',
                             'DEXUSUK', 'SP500', 'DJIA', 'VIXCLS']]
    X_test_ARIMA = X_test[['GOOGL', 'IBM', 'DEXJPUS',
                           'DEXUSUK', 'SP500', 'DJIA', 'VIXCLS']]

    # convert the index datetime index with frequency
    # X_train_ARIMA.index = pd.DatetimeIndex(
    # X_train_ARIMA.index).to_period('W')
    # X_test_ARIMA.index = pd.DatetimeIndex(
    # X_test_ARIMA.index).to_period('W')
    Y_train_ARIMA = Y_train
    # Y_train_ARIMA.index = pd.DatetimeIndex(
    # Y_train_ARIMA.index).to_period('W')
    Y_test_ARIMA = Y_test.copy()
    # Y_test_ARIMA.index = pd.DatetimeIndex(
    # Y_test_ARIMA.index).to_period('W')
    return X_train_ARIMA, Y_train_ARIMA, X_test_ARIMA, Y_test_ARIMA, Y_test


def evaluate_arima_model(arima_order, data):
    (X_train_ARIMA, Y_train_ARIMA, _, _, _) = data
    # predicted = list()
    modelARIMA = ARIMA(endog=Y_train_ARIMA,
                       exog=X_train_ARIMA, order=arima_order)
    model_fit = modelARIMA.fit()
    error = mean_squared_error(Y_train_ARIMA, model_fit.fittedvalues)
    return error


def evaluate_models(p_values, d_values, q_values, data, verbose=0):
    best_score, best_cfg = float("inf"), None
    for p in p_values:
        for d in d_values:
            for q in q_values:
                order = (p, d, q)
                try:
                    mse = evaluate_arima_model(order, data)
                    if mse < best_score:
                        best_score, best_cfg = mse, order
                    if verbose:
                        print(f'ARIMA {order} MSE {mse}')
                except Exception as e:
                    print(e)
                    continue
    print(f'Best ARIMA {best_cfg} MSE {best_score}')
    return best_cfg


def final_tuned_model(
        data: tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame],
        order: List[int]) -> pd.Series:
    # unpack
    (X_train_ARIMA, Y_train_ARIMA, X_test_ARIMA, Y_test_ARIMA, _) = data
    # find lengths
    tr_len = len(X_train_ARIMA)
    to_len = len(X_train_ARIMA) + len(X_test_ARIMA)
    # tune the best order
    modelARIMA_tuned = ARIMA(
        endog=Y_train_ARIMA, exog=X_train_ARIMA, order=order)
    model_fit_tuned = modelARIMA_tuned.fit()
    # estiamte accuracy on validation set
    predicted_tuned = model_fit_tuned.predict(
        start=tr_len - 1, end=to_len - 1, exog=X_test_ARIMA)[1:]
    print(mean_squared_error(Y_test_ARIMA, predicted_tuned))
    return predicted_tuned


def recent_results(predicted_values: pd.Series, Y_test: pd.Series):
    # Let's just pull the recent data
    final_res = web.get_data_yahoo(
        ['MSFT'],
        min(predicted_values.index) - dt.timedelta(days=50),
        dt.datetime.now())[['Adj Close']]
    new = pd.concat([final_res, Y_test, predicted_values], axis=1).dropna()
    new.columns = ['Stock Value', 'Actual', 'Pred']
    new['Log Stock Value'] = np.log(new['Stock Value'])
    # new['Anti Log Actual'] = np.exp(new['Log Stock Value'] + new['Actual'])
    return np.exp(new['Log Stock Value'] + new['Pred'])


def run_model_and_get_results(weekly_return_period: int = 5,
                              validation_size: float = 0.2):
    data = prepare_data(weekly_return_period=weekly_return_period,
                        validation_size=validation_size)
    order = evaluate_models(range(0, 3), range(0, 2), range(0, 2), data)
    predicted_values = final_tuned_model(data=data, order=order)
    Y_test = data[4]
    predicted_values.index = Y_test.index
    final_result = recent_results(
        predicted_values=predicted_values, Y_test=Y_test)
    return final_result


@router.get("/api/stockPrediction")
@lru_cache(maxsize=1, expires_after=0.5*DAYS)
def api_response():
    res = []
    for p in range(2, 6):
        for q in range(1, 5):
            print(p, q/100)
            res.append(run_model_and_get_results(p, q/100))

    recent_data = pd.concat(res, axis=1).dropna().iloc[-1]
    response = {
        "recent_date": recent_data.name.strftime("%B'%d,%Y"),
        "minimum_expectation": min(recent_data),
        "average_expectation": np.mean(recent_data),
        "maximum_expectation": max(recent_data)
    }
    return response
