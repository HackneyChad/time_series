import pandas as pd
import numpy as np

# JSON API
import requests
import json

def get_items():
    #gets items from Zachs lol server for time series analysis project
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
#.rename(columns={'item_id':'item'}, inplace=True)

def all_items():
    #triggers items function, names the df and writes to csv
    print('getting items...')
    items = get_items()
    print('writing items.csv...')
    items.to_csv('items.csv')
    print('finished writing items.csv.  Part 1 done.\n')
    print('items.tail:\n')
    print(items.tail())
    print('\n')
    return items

def get_stores():
    #gets stores from Zachs lol server for time series analysis project
    response = requests.get('https://python.zach.lol/api/v1/stores')
    data = response.json()
    stores = pd.DataFrame(data['payload']['stores'])
    return stores

def all_stores():
    #triggers items function, names the df and writes to csv
    print('getting stores...')
    stores = get_stores()
    print('writing stores.csv...')
    stores.to_csv('stores.csv')
    print('finished writing stores.csv.  Part 2 done.\n')
    print('stores.tail:\n')
    print(stores.tail())
    print('\n')
    return stores

def get_sales():
    #gets sales from Zachs lol server for time series analysis project
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
    sales.to_csv('sales.csv')
    print('finished writing sales.csv.  Part 3 done.\n')
    print('sales.tail:\n')
    print(sales.tail())
    print('\n')
    return sales

def tsa_acquire_all():
    all_items()
    all_stores()
    all_sales()
    print('HEADS UP: finished all tsa acquire.  Full Stop!')

# add language here to merge the 3 dfs on item_id <-> id, and store <-> store_id
tsa_acquire_all()



# ======================================================================== #
#                       DELETE BELOW LATER IF NOT USED                     #
# ======================================================================== #

#.rename(columns={'item_id':'item'}, inplace=True)

# def all_zillow_data():
#     zillow_chunks = [get_2016_property_data(),get_2017_property_data()]
#     all_zillow = pd.concat(zillow_chunks, ignore_index=True)
#     all_zillow.dropna(subset=['latitude', 'longitude'], inplace=True)
#     all_zillow.to_csv('zillow.csv')
#     return all_zillow

