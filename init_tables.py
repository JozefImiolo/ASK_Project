import csv
from datetime import datetime
import requests
import sys
from questdb.ingress import Sender, IngressError

QUESTDB_HOST = "http://localhost:9000"
TABLE_NAME_ETH = 'ETH_USD'
TABLE_NAME_BTC = 'BTC_USD'

csv_filename_ETH = 'ETH_USD.csv'
csv_filename_BTC = 'BTC_USD.csv'

TABLES = {TABLE_NAME_ETH: csv_filename_ETH, TABLE_NAME_BTC: csv_filename_BTC}


def create_table_if_not_exist(table_name):
    create_table_query = f'''
     CREATE TABLE IF NOT EXISTS {table_name}(
      Date timestamp,
      Open DOUBLE,
      High DOUBLE,
      Low DOUBLE,
      Close DOUBLE,
      AdjClose DOUBLE,
      Volume LONG
    ) timestamp (Date) PARTITION BY DAY WAL;
    '''

    payload = {
        'query': create_table_query
    }

    response = requests.get(f"{QUESTDB_HOST}/exec", payload)
    if response.status_code == 200:
        print("Table created successfully.")
    else:
        print(f"Table creation failed. Status code: {response.status_code}")
        print(response.text)


def insert_data(table_name, csv_filename):
    with open(f'data/{csv_filename}', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        data = list(csv_reader)

    try:
        with Sender('localhost', 9009) as sender:
            for row in data:
                datetime_obj = datetime.strptime(row['Date'], "%Y-%m-%dT%H:%M:%S.%fZ")
                tstamp = int(datetime_obj.timestamp()) * 1000000000
                sender.row(
                    table_name,
                    columns={
                        'Date': tstamp,
                        'Open': float(row['Open']),
                        'High': float(row['High']),
                        'Low': float(row['Low']),
                        'Close': float(row['Close']),
                        'AdjClose': float(row['AdjClose']),
                        'Volume': int(row['Volume'])
                    }
                )
            sender.flush()
    except (IngressError, IngressError) as e:
        sys.stderr.write(f'Got error: {e}\n')


def init_tables():
    for table_name, csv_filename in TABLES.items():
        create_table_if_not_exist(table_name)
        insert_data(table_name, csv_filename)
