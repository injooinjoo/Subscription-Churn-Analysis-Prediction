import pandas as pd
from typing import List

class FeatureEngineer:
    def __init__(self):
        pass
    
    def create_behavioral_features(self, df: pd.DataFrame) -> pd.DataFrame:
        # 최근 30일 시청 시간 계산
        df['last_30_days_streaming'] = df.groupby('user_id')['streaming_hours'].rolling(
            window=30, min_periods=1).sum().reset_index(0, drop=True)
        
        # 주간 로그인 빈도 계산
        df['weekly_login_frequency'] = df.groupby('user_id')['login_frequency'].rolling(
            window=7, min_periods=1).mean().reset_index(0, drop=True)
        
        # 선호 콘텐츠 카테고리 추출
        df['preferred_category'] = df.groupby('user_id')['content_category'].agg(
            lambda x: x.value_counts().index[0])
        
        return df
    
    def create_transactional_features(self, df: pd.DataFrame) -> pd.DataFrame:
        # 결제 실패 횟수
        df['payment_failures'] = df.groupby('user_id')['payment_status'].apply(
            lambda x: (x == 'failed').sum()).reset_index(0, drop=True)
        
        # 구독 기간
        df['subscription_duration'] = (df['current_date'] - df['signup_date']).dt.days
        
        return df 