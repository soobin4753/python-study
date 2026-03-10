# Day 11
# 1. JSON → DataFrame 변환
# 2. purchase 데이터만 필터링
# 3. user별 구매 금액 합계
# 4. 구매 많은 순 정렬
# 5. CSV 저장 (user_purchase_summary.csv)

import pandas as pd

log_df = pd.read_json('py/260310/logs.json', encoding='utf-8')
purchase_df = log_df[log_df['action'] == 'purchase']
user_purchase_summary = purchase_df.groupby('user')['amount'].sum().reset_index()
print(f"user_purchase_summary 1 :\n{user_purchase_summary}")
user_purchase_summary = user_purchase_summary.sort_values(by='amount', ascending=False)
print(f"user_purchase_summary 2 :\n{user_purchase_summary}")
user_purchase_summary.to_csv('py/260310/user_purchase_summary.csv', index=False)