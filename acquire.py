import pandas as pd
import numpy as np
import os

# JSON API
import requests
import json

def get_items():
    #gets items from Zachs lol server for time series analysis project
    # if os.path.exists('items.csv'):
    #     print('Reading items from local csv')
    # return pd.read_csv('items.csv')
    base_url = 'https://python.zach.lol'
    response = requests.get('https://python.zach.lol/api/v1/items')
    data = response.json()
    items = pd.DataFrame(data['payload']['items'])
    response = requests.get(base_url + data['payload']['next_page'])
    data = response.json()
    while data['payload']['page'] <= data['payload']['max_page']:
        items = pd.concat([items, pd.DataFrame(data['payload']['items'])]).reset_index(drop=True)
        if data['payload']['page'] == data['payload']['max_page']:
            break
        response = requests.get(base_url + data['payload']['next_page'])
        data = response.json()
    return items

def all_items():
    #triggers items function, names the df and writes to csv
    print('getting items...')
    items = get_items()
    print('writing items.csv...')
    items.to_csv('items.csv', index=False)
    print('finished writing items.csv.  Part 1 done.\n')
    print('items.tail:\n')
    print(items.tail())
    print('\n')
    return items

def get_stores():
    # #gets stores from Zachs lol server for time series analysis project
    # if os.path.exists('stores.csv'):
    #     print('Reading stores from local csv')
    # return pd.read_csv('stores.csv')
    response = requests.get('https://python.zach.lol/api/v1/stores')
    data = response.json()
    stores = pd.DataFrame(data['payload']['stores'])
    return stores

def all_stores():
    #triggers items function, names the df and writes to csv
    print('getting stores...')
    stores = get_stores()
    print('writing stores.csv...')
    stores.to_csv('stores.csv', index=False)
    print('finished writing stores.csv.  Part 2 done.\n')
    print('stores.tail:\n')
    print(stores.tail())
    print('\n')
    return stores

def get_sales():
    #gets sales from Zachs lol server for time series analysis project
    # if os.path.exists('sales.csv'):
    #     print('Reading sales from local csv')
    # return pd.read_csv('sales.csv')
    base_url = 'https://python.zach.lol'
    response = requests.get('https://python.zach.lol/api/v1/sales')
    data = response.json()
    sales = pd.DataFrame(data['payload']['sales'])
    response = requests.get(base_url + data['payload']['next_page'])
    data = response.json()
    while data['payload']['page'] <= data['payload']['max_page']:
        sales = pd.concat([sales, pd.DataFrame(data['payload']['sales'])]).reset_index(drop=True)
        if data['payload']['page'] == data['payload']['max_page']:
            break
        response = requests.get(base_url + data['payload']['next_page'])
        data = response.json()
    return sales

def all_sales():
    #triggers sales function, names the df and writes to csv
    print('getting sales...')
    sales = get_sales()
    print('writing sales.csv...')
    sales.to_csv('sales.csv', index=False)
    print('finished writing sales.csv.  Part 3 done.\n')
    print('sales.tail:\n')
    print(sales.tail())
    print('\n')
    return sales

def tsa_acquire_all():
    items = all_items()
    stores = all_stores()
    sales = all_sales()
    sales.rename(columns={'store': 'store_id', 'item': 'item_id'}, inplace=True)
    df = pd.merge(sales, items, on='item_id')
    df = pd.merge(df, stores, on='store_id')
    print('writing final df.csv...')
    df.to_csv('df.csv', index=False)
    print('finished writing final df.csv.  Final df done.\n')
    print('HEADS UP: finished all tsa acquire.  Full Stop!')
    return df

# tsa_acquire_all()

def peekatdata(df):
    print("\n \n SHAPE:")
    print(df.shape)

    print("\n \n COLS:")
    print(df.columns)

    print("\n \n INFO:")
    print(df.info())

    print("\n \n Missing Values:")
    missing_vals = df.columns[df.isnull().any()]
    print(df.isnull().sum())

    print("\n \n DESCRIBE:")
    print(df.describe())

    print('\n \n HEAD:')
    print(df.head(5))

    print('\n \n TAIL:' )
    print(df.tail(5))



# ======================================================================== #
#                       DELETE BELOW LATER IF NOT USED                     #
# ======================================================================== #

# def tsa_acquire_all():
#     all_items()
#     all_stores()
#     all_sales()
#     print('HEADS UP: finished all tsa acquire.  Full Stop!')

