FROM python:3.8-slim-buster

EXPOSE 80

WORKDIR /app

COPY requirements.txt ./requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

COPY .streamlit/config.toml ~/.streamlit/config.toml

CMD streamlit run app.py