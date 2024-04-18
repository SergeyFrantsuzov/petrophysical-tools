import pyodbc
import pandas as pd


def data_from_mssql(connect_parameters, table_name):
    connection_to_db = pyodbc.connect(connect_parameters)
    df = pd.read_sql('SELECT * FROM {0}'.format(table_name), connection_to_db)
    return df
