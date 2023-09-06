import pandas as pd
import requests
from flask import Flask, render_template
import init_tables
import json


app = Flask(__name__)


@app.route('/')
def welcome_page():
    return render_template('welcome.html')


@app.route("/area_chart")
def area_chart():
    response = requests.get(f"{init_tables.QUESTDB_HOST}/exec", params={
        "query": f"SELECT * FROM {init_tables.TABLE_NAME_ETH}"
    })

    resp_json = response.json()
    dataset = resp_json["dataset"]
    columns = resp_json["columns"]
    col_names = [item["name"] for item in columns]

    pd_data = pd.DataFrame(dataset, columns=col_names)
    data_json = pd_data.to_json(orient="records", date_format="iso")
    data_json = json.loads(data_json)

    return render_template('area_chart.html', data=data_json)


@app.route("/bar_chart")
def bar_chart():
    btc_year_avg_query = f'''
    SELECT year(Date), avg(Close)
    FROM {init_tables.TABLE_NAME_BTC}
    SAMPLE BY 1y ALIGN TO CALENDAR;
    '''
    payload = {
        'query': btc_year_avg_query
    }
    response = requests.get(f"{init_tables.QUESTDB_HOST}/exec", payload)

    resp_json = response.json()
    dataset = resp_json["dataset"]
    columns = resp_json["columns"]
    col_names = [item["name"] for item in columns]

    pd_data = pd.DataFrame(dataset, columns=col_names)
    data_json = pd_data.to_json(orient="records", date_format="iso")
    data_json = json.loads(data_json)

    return render_template('bar_chart.html', data=data_json)

@app.route("/candle_chart")
def candle_chart():
    btc_2023_query = f'''
    SELECT  * FROM {init_tables.TABLE_NAME_BTC}
    Where Date in '2023';
    '''
    payload = {
        'query': btc_2023_query
    }
    response = requests.get(f"{init_tables.QUESTDB_HOST}/exec", payload)

    resp_json = response.json()
    dataset = resp_json["dataset"]
    columns = resp_json["columns"]
    col_names = [item["name"] for item in columns]

    pd_data = pd.DataFrame(dataset, columns=col_names)
    data_json = pd_data.to_json(orient="records", date_format="iso")
    data_json = json.loads(data_json)

    return render_template('candle_chart.html', data=data_json)


@app.route("/line_chart")
def line_chart():
    response = requests.get(f"{init_tables.QUESTDB_HOST}/exec", params={
        "query": f"SELECT * FROM {init_tables.TABLE_NAME_BTC}"
    })

    resp_json = response.json()
    dataset = resp_json["dataset"]
    columns = resp_json["columns"]
    col_names = [item["name"] for item in columns]

    pd_data = pd.DataFrame(dataset, columns=col_names)
    data_json = pd_data.to_json(orient="records", date_format="iso")
    data_json = json.loads(data_json)

    return render_template('line_chart.html', data=data_json)


init_tables.init_tables()
if __name__ == "__main__":
    app.run(debug=True)
