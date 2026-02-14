# preprocessing.py
import pandas as pd

def preprocess_data(df):
    """
    Preprocess the uploaded DataFrame:
    - Fill numeric missing values with mean
    - Fill categorical missing values with mode
    - Strip spaces and standardize column names
    """
    df = df.copy()
    
    for col in df.columns:
        # Remove leading/trailing spaces in column names
        df[col] = df[col].astype(str).str.strip()
        
        # Numeric columns
        if pd.api.types.is_numeric_dtype(df[col]):
            df[col] = pd.to_numeric(df[col], errors='coerce')
            mean_val = df[col].mean()
            df[col] = df[col].fillna(mean_val)
        
        # Categorical columns
        else:
            mode_val = df[col].mode()
            if not mode_val.empty:
                df[col] = df[col].fillna(mode_val[0])
            else:
                df[col] = df[col].fillna("Unknown")
    
    # Standardize column names: lowercase and underscores
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
    
    return df
