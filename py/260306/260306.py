import pandas as pd

#DAY 7
# 1번. employees.csv 부서별 평균 급여
# department 컬럼 기준으로 그룹화, salary 평균 계산

df = pd.read_csv('py/260306/employeesDay7.csv')
department_salary = df.groupby('department')['salary'].mean()
print(department_salary)

#---------------------------------------------------------------
# 2번. 나이 30 이상 + 급여 5000 이상 직원 추출

department_emp = df[(df['age'] >= 30) & (df['salary'] >= 5000)]
print(department_emp)

#---------------------------------------------------------------
# 3번. 파생 컬럼 생성
# bonus 컬럼 추가: 급여의 10%로 계산, DataFrame에 bonus 컬럼 추가 후 출력

df['bonus'] = df['salary'] * 0.1
print(df)

#---------------------------------------------------------------
# 4번. 부서별 최대 급여 직원
# 부서별 최고 급여를 받는 직원 이름 출력

max_salary_emp = df.loc[df.groupby('department')['salary'].idxmax()] # idxmax() 그룹별 최대값 인덱스
print(max_salary_emp)
print(max_salary_emp[['name']])

#=================================================================
#DAY 8
# 1번. CSV 읽기 employees.csv, departments.csv 읽어서 DataFrame 생성

employees_df = pd.read_csv('py/260306/employeesDay8.csv')
departments_df = pd.read_csv('py/260306/departmentsDay8.csv')
print(employees_df)
print(departments_df)

# 2번. 부서 정보 merge
# employees + departments merge, department 컬럼 기준, 결과 DataFrame 출력

merged_df = pd.merge(employees_df, departments_df, on='department', how='inner')
print(merged_df)

# 3번. JSON bonus merge
# bonuses.json 읽기 → DataFrame
# emp_id 기준으로 employees DataFrame과 merge
# bonus_amount 컬럼 추가 (salary * bonus_percent)
# 결과 출력

bonuses_df = pd.read_json('py/260306/bonusesDay8.json')
merged_bonus_df = pd.merge(employees_df, bonuses_df, on='emp_id', how='inner')
merged_bonus_df['bonus_amount'] = merged_bonus_df['salary'] * merged_bonus_df['bonus_percent']
print(merged_bonus_df)

# 4번. Excel 저장
# 최종 DataFrame을 py/employees_final.xlsx로 저장, Sheet 이름: EmployeeData

merged_bonus_df.to_excel('py/260306/employees_final.xlsx', sheet_name='EmployeeData', index=False)
