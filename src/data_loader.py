import pandas as pd
from src.config import DATA_PATH

def load_and_clean_data():
    df = pd.read_csv(DATA_PATH)
    
    df.columns = df.columns.str.strip()
    
    duplicates = df.duplicated().sum()
    print(f"✅ Number of duplicated rows: {duplicates}")
    df.drop_duplicates(inplace=True)
    
    nulls = df.isnull().sum() / len(df)
    print(f"✅ Percentage of missing values: \n{nulls}")
    df.dropna(inplace=True)
    
    df["Date"] = pd.to_datetime(df['Date'], dayfirst=True)
    
    df['Month'] = df['Date'].dt.month
    df['Year'] = df['Date'].dt.year
    
    print(f"✅ Final dataset: {df.shape[0]} row, {df.shape[1]} column")
    return df

def get_data_info(df):
    print("\n" + "="*50)
    print("📊 Dataset information:")
    print("="*50)
    print(df.info())
    print("\n📈 Descriptive statistics:")
    print(df.describe())
    return df
