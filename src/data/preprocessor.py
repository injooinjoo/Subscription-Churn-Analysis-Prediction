import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.impute import SimpleImputer

class DataPreprocessor:
    def __init__(self):
        self.numerical_imputer = SimpleImputer(strategy='median')
        self.categorical_imputer = SimpleImputer(strategy='most_frequent')
        self.scaler = MinMaxScaler()
    
    def preprocess_data(self, df: pd.DataFrame) -> pd.DataFrame:
        # 수치형 데이터 전처리
        numerical_columns = ['streaming_hours', 'login_frequency', 'payment_amount']
        df[numerical_columns] = self.numerical_imputer.fit_transform(df[numerical_columns])
        df[numerical_columns] = self.scaler.fit_transform(df[numerical_columns])
        
        # 범주형 데이터 전처리
        categorical_columns = ['subscription_plan', 'content_category']
        df[categorical_columns] = self.categorical_imputer.fit_transform(df[categorical_columns])
        
        # One-hot 인코딩
        df = pd.get_dummies(df, columns=categorical_columns)
        
        return df 