import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
import pandas as pd
import numpy as np

class ChurnPredictor:
    def __init__(self):
        self.model = xgb.XGBClassifier(
            max_depth=6,
            learning_rate=0.1,
            n_estimators=100,
            objective='binary:logistic'
        )
    
    def train(self, X: pd.DataFrame, y: pd.Series):
        X_train, X_val, y_train, y_val = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        
        self.model.fit(
            X_train, 
            y_train,
            eval_set=[(X_val, y_val)],
            early_stopping_rounds=10
        )
        
        return self.evaluate(X_val, y_val)
    
    def predict(self, X: pd.DataFrame) -> np.ndarray:
        return self.model.predict(X)
    
    def evaluate(self, X: pd.DataFrame, y: pd.Series) -> dict:
        predictions = self.predict(X)
        return {
            'accuracy': accuracy_score(y, predictions),
            'precision': precision_score(y, predictions),
            'recall': recall_score(y, predictions),
            'f1': f1_score(y, predictions),
            'auc_roc': roc_auc_score(y, predictions)
        } 