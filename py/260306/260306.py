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
