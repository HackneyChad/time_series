import acquire as acq
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler

def time_convert(df):
    datetime_format = '%a, %d %b %Y %H:%M:%S %Z'
    df['sale_date'] = pd.to_datetime(df.sale_date,format=datetime_format)
    return df

def new_index(df):
    df = df.set_index('sale_date')
    return df

def data_prepped(df):
    df = time_convert(df)
    df = new_index(df)
    print('Please wait for df preparations to process...')
    return df
    

#data_prepped()

# The code below inspires by Michael P. Moran's missing_vals_df().
def missing_values_col(df):
	"""
	Write or use a previously written function to return the
	total missing values and the percent missing values by column.
	"""
	null_count = df.isnull().sum()
	null_percentage = (null_count / df.shape[0]) * 100
	empty_count = pd.Series(((df == ' ') | (df == '')).sum())
	empty_percentage = (empty_count / df.shape[0]) * 100
	nan_count = pd.Series(((df == 'nan') | (df == 'NaN')).sum())
	nan_percentage = (nan_count / df.shape[0]) * 100
	return pd.DataFrame({'num_missing': null_count, 'missing_percentage': null_percentage,
	                     'num_empty': empty_count, 'empty_percentage': empty_percentage,
	                     'nan_count': nan_count, 'nan_percentage': nan_percentage})

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