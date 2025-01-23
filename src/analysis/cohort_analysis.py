import pandas as pd
import numpy as np

class CohortAnalyzer:
    def __init__(self):
        pass
    
    def create_cohort_analysis(self, df: pd.DataFrame) -> pd.DataFrame:
        # 가입월 추출
        df['cohort_month'] = df['signup_date'].dt.to_period('M')
        
        # 현재까지의 사용 기간 계산
        df['months_active'] = ((df['current_date'].dt.to_period('M') - 
                              df['signup_date'].dt.to_period('M')).astype(int))
        
        # 코호트 테이블 생성
        cohort_data = df.groupby(['cohort_month', 'months_active'])['user_id'].count().unstack()
        
        # 리텐션 비율 계산
        cohort_sizes = cohort_data.iloc[:, 0]
        retention_table = cohort_data.divide(cohort_sizes, axis=0) * 100
        
        return retention_table 