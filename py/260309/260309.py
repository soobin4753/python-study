# Day 9~10
# 1번 employees.csv, departments.csv, bonuses.json 모두 DataFrame으로 읽기

import pandas as pd

employees_df = pd.read_csv('py/260309/employeesDay9.csv', encoding='utf-8')
departments_df = pd.read_csv('py/260309/departmentsDay9.csv', encoding='utf-8')
bonuses_df = pd.read_json('py/260309/bonusesDay9.json', encoding='utf-8')

# 2번 데이터 결합
# employees + departments → department 기준 merge
# employees + bonuses → emp_id 기준 merge
# 하나의 최종 DataFrame 생성

merged_dept_df = pd.merge(employees_df,departments_df, on='department', how='inner')
final_df = pd.merge(merged_dept_df, bonuses_df, on='emp_id', how='inner')
final_df['bonus_amount'] = final_df['salary'] * final_df['bonus_percent']
print(final_df)

# 3번 결측치 처리
# salary가 없으면 평균으로 채우기
# department/manager가 없으면 'Unknown' 처리

#final_df['salary'].fillna(final_df['salary'].mean(), inplace=True)
#final_df['department'].fillna('Unknown', inplace=True)
#final_df['manager'].fillna('Unknown', inplace=True)

final_df.fillna({
    'salary': final_df['salary'].mean(),
    'department': 'Unknown',
    'manager': 'Unknown'
}, inplace=True)

# 4번 파생 컬럼 생성
# bonus_amount = salary * bonus_percent
# total_compensation = salary + bonus_amount

final_df['bonus_amount'] = final_df['salary'] * final_df['bonus_percent']
final_df['total_compensation'] = final_df['salary'] + final_df['bonus_amount']
print(final_df)

# 5번 그룹화/집계
# 부서별: 평균 급여, 총 보너스
# 결과 출력

dept_group = final_df.groupby('department').agg({
    'salary': 'mean',
    'bonus_amount': 'sum'
}).rename(columns={'salary': 'avg_salary', 'bonus_amount': 'total_bonus'})
print(dept_group)

# 6번 파일 저장
# 최종 DataFrame → CSV: employees_etl.csv
# Excel: employees_etl.xlsx, Sheet 이름 EmployeeETL

final_df.to_csv('py/260309/employees_etl.csv', index=False)
final_df.to_excel('py/260309/employees_etl.xlsx', sheet_name='EmployeeETL', index=False)

# 7번 
# 각 부서별 최고 급여자 + 최고 보너스 수령자 추출
# 출력: name, salary, bonus_amount

max_salary_emp = final_df.loc[final_df.groupby('department')['salary'].idxmax()]
max_bonus_emp = final_df.loc[final_df.groupby('department')['bonus_amount'].idxmax()]
print("최고 급여자:")
print(max_salary_emp[['department', 'name', 'salary']])
print("최고 보너스 수령자:")
print(max_bonus_emp[['department', 'name', 'bonus_amount']])

