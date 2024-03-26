FROM python:3.9-slim

RUN apt-get update && apt-get install -y xclip && rm -rf /var/lib/apt/lists/*

RUN mkdir /streamlit

COPY requirements.txt /streamlit

WORKDIR /streamlit

RUN pip install -r requirements.txt

COPY . /streamlit

EXPOSE 8501

CMD ["streamlit", "run", "main.py"]


