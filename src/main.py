from data.preprocessor import DataPreprocessor
from features.feature_engineering import FeatureEngineer
from models.churn_predictor import ChurnPredictor
from analysis.cohort_analysis import CohortAnalyzer
from analysis.aarrr_metrics import AAARRAnalyzer
import pandas as pd

def main():
    # 데이터 로드
    df = pd.read_csv('data/raw/subscriber_data.csv')
    
    # 데이터 전처리
    preprocessor = DataPreprocessor()
    df_processed = preprocessor.preprocess_data(df)
    
    # 특성 엔지니어링
    feature_engineer = FeatureEngineer()
    df_featured = feature_engineer.create_behavioral_features(df_processed)
    df_featured = feature_engineer.create_transactional_features(df_featured)
    
    # 모델 학습
    X = df_featured.drop(['churn_status'], axis=1)
    y = df_featured['churn_status']
    
    predictor = ChurnPredictor()
    metrics = predictor.train(X, y)
    print("Model Performance:", metrics)
    
    # 코호트 분석
    cohort_analyzer = CohortAnalyzer()
    retention_table = cohort_analyzer.create_cohort_analysis(df)
    print("Retention Table:\n", retention_table)
    
    # AARRR 메트릭스 분석
    aarrr_analyzer = AAARRAnalyzer()
    acquisition_metrics = aarrr_analyzer.calculate_acquisition_metrics(df)
    activation_metrics = aarrr_analyzer.calculate_activation_metrics(df)
    retention_metrics = aarrr_analyzer.calculate_retention_metrics(df)
    
    print("AARRR Metrics:", {
        'acquisition': acquisition_metrics,
        'activation': activation_metrics,
        'retention': retention_metrics
    })

if __name__ == "__main__":
    main() 