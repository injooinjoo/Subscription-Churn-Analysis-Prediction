import pandas as pd
from typing import Dict

class AAARRAnalyzer:
    def __init__(self):
        pass
    
    def calculate_acquisition_metrics(self, df: pd.DataFrame) -> Dict:
        return {
            'total_new_users': len(df['user_id'].unique()),
            'acquisition_by_channel': df.groupby('acquisition_channel')['user_id'].count().to_dict()
        }
    
    def calculate_activation_metrics(self, df: pd.DataFrame) -> Dict:
        df['days_to_first_payment'] = (df['first_payment_date'] - df['signup_date']).dt.days
        return {
            'avg_days_to_first_payment': df['days_to_first_payment'].mean(),
            'activation_rate': (df['days_to_first_payment'] <= 7).mean()
        }
    
    def calculate_retention_metrics(self, df: pd.DataFrame) -> Dict:
        monthly_churn_rate = df.groupby('month')['churned'].mean()
        return {
            'overall_churn_rate': df['churned'].mean(),
            'monthly_churn_rates': monthly_churn_rate.to_dict()
        } 