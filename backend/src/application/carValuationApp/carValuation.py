import pickle
from fastapi import APIRouter
from src.application.carValuationApp.carValuationParams import (
    carValuationParams, decodeJson)
import pandas as pd

router = APIRouter()


@router.post("/api/predictCarValuation")
def predictCarValuation(input: carValuationParams):
    with open("data/models/carValuationV001.pickle", 'rb') as pickle_file:
        loaded_model = pickle.load(pickle_file)
    decodedInput = decodeJson(input)
    df = pd.DataFrame.from_records([decodedInput])
    res = loaded_model.predict(df)
    print(res)
    return res[0]
