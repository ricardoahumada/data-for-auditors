import pandas as pd
import sqlite3

# ************* Function definitions *************

def get_data_from_api():
    print('Reading...')
    dfj = pd.read_json('https://raw.githubusercontent.com/ricardoahumada/data-for-auditors/refs/heads/main/3.%20Procesamiento%20de%20Datos%20con%20ETLs/3.1.ETL/api/data.json')
    return dfj

def write_data(data):
    print('Writing...')
    print(data)
    data.to_csv('data.csv')

def agg_data():
    df = pd.read_csv('data.csv')
    print('Aggregating...')
    df['date']=pd.to_datetime(df['date']).dt.date    
    select_col=['store','date','price']
    new_df = df.groupby([df["store"],df["date"]]).sum().reset_index()
    new_df.rename(columns={"price":"revenue"},inplace=True)
    new_df.drop(columns=['Unnamed: 0','transaction_id'], inplace=True)
    print(new_df)
    return new_df


def load_data_sqlite(pdf):
    try:
        conn_string = 'database.db'
        engine = sqlite3.connect(conn_string)
        print('Loading...')
        print(pdf)
        pdf.to_sql('agg_data', engine, if_exists='replace', index=False)
        print('Loaded!!')
    except NameError:
        print('Exception..')
    finally:
        if 'engine' in locals():
            engine.close()

# ************* ETL Steps *************

# Pull Data from API
data = get_data_from_api()
data
## Output Data to CSV
write_data(data)
## Transformation to Aggregate Data
proc_data = agg_data()
## Load Data to DB
load_data_sqlite(proc_data)