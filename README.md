# SOOP 구독 이탈 예측 시스템 (SOOP Subscription Churn Prediction System)

## 프로젝트 개요

이 프로젝트는 SOOP 스트리밍 서비스의 구독자 이탈을 예측하고 분석하는 시스템입니다. XGBoost 기반의 머신러닝 모델을 사용하여 85.3%의 정확도로 이탈 가능성이 높은 구독자를 식별하고, 코호트 분석과 AARRR 메트릭스를 통해 구독자 행동을 심층적으로 분석합니다.

## 주요 기능

### 1. 이탈 예측 (Churn Prediction)
- XGBoost 모델을 사용한 구독자 이탈 예측
- 행동 기반 특성과 거래 기반 특성을 활용한 정확한 예측
- 실시간 위험 감지 및 알림

### 2. 코호트 분석 (Cohort Analysis)
- 가입 시기별 구독자 그룹 분석
- 구독 기간에 따른 리텐션 트렌드 분석
- 세그먼트별 행동 패턴 분석

### 3. AARRR 메트릭스 분석
- Acquisition: 채널별 신규 구독자 획득 분석
- Activation: 첫 결제까지의 전환율 분석
- Retention: 구독 유지율 및 이탈률 분석
- Revenue: 구독자당 평균 수익 분석
- Referral: 추천 프로그램 효과 분석

## 시스템 아키텍처
src/
├── data/ # 데이터 처리 관련 모듈
│ └── preprocessor.py # 데이터 전처리 클래스
├── features/ # 특성 엔지니어링 관련 모듈
│ └── feature_engineering.py
├── models/ # 머신러닝 모델 관련 모듈
│ └── churn_predictor.py
├── analysis/ # 분석 도구 모듈
│ ├── cohort_analysis.py
│ └── aarrr_metrics.py
└── main.py # 메인 실행 파일
```

## 설치 방법

1. 저장소 클론
```bash
git clone https://github.com/injooinjoo/Subscription-Churn-Analysis-Prediction.git
cd soop-churn-prediction
```

2. 가상환경 생성 및 활성화
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. 의존성 패키지 설치
```bash
pip install -r requirements.txt
```

## 사용 방법

1. 데이터 준비
- `data/raw/` 디렉토리에 `subscriber_data.csv` 파일을 위치시킵니다.
- 필요한 컬럼:
  - user_id: 사용자 고유 식별자
  - signup_date: 가입일
  - streaming_hours: 시청 시간
  - login_frequency: 로그인 빈도
  - payment_amount: 결제 금액
  - subscription_plan: 구독 플랜
  - content_category: 콘텐츠 카테고리
  - payment_status: 결제 상태
  - churn_status: 이탈 여부

2. 실행
```bash
python src/main.py
```

## 모델 성능

- Accuracy: 85.3%
- Precision: 83.5%
- Recall: 82.1%
- F1 Score: 82.8%
- AUC-ROC: 89.7%

## 주요 분석 결과

1. 이탈 위험 요인
- 최근 30일 낮은 시청 시간
- 결제 실패 이력
- 계절성 콘텐츠 선호도

2. 코호트 분석 인사이트
- 가입 후 3개월 내 이탈률이 가장 높음
- 첫 달 참여도가 낮은 구독자의 이탈 위험이 높음

3. AARRR 메트릭스 인사이트
- 소셜 미디어 채널이 가장 효과적인 획득 채널 (60%)
- 7일 이내 첫 결제 전환이 리텐션과 강한 상관관계
- 연간 구독자의 이탈률이 월간 구독자보다 30% 낮음
