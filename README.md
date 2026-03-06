Python Data Engineering Practice

Python, Pandas, File I/O, JSON 처리 연습을 위한 코드 정리입니다.
데이터 엔지니어 공부 과정에서 반복문, 파일 처리, 데이터 정제, pandas 사용을 연습했습니다.

[Day1]

1. 리스트 안의 딕셔너리 데이터를 반복문으로 출력
2. 사용자 리스트에서 나이가 28 이상인 데이터만 필터링

[Day2]
1. 사용자 리스트에서 나이만 추출하여 새로운 리스트 생성
2. 리스트 컴프리헨션으로 28세 이상 사용자 이름 리스트 생성
3. JSON 문자열을 파이썬 객체로 변환하고 name 출력

[Day3]
1. 사용자 데이터를 파일(users.txt)로 저장하고 파일 읽기
2. 파일 데이터를 읽어 나이가 28 이상인 사용자 출력
3. 나이가 숫자가 아닐 경우 예외 처리로 에러 무시

[Day4]
1. users.txt 파일을 Pandas DataFrame으로 변환 후 나이 28 이상 필터링
2. 필터링된 데이터를 CSV 파일(users_filtered.csv)로 저장

[Day5]
1. 나이가 28 이상이거나 이름이 'lee'인 데이터 필터링 후 CSV 저장

[Day6]
1. age 컬럼의 결측치를 평균값으로 채우기
2. 특정 컬럼 결측치가 있는 행 삭제
3. 각 컬럼의 결측치 개수와 비율 확인

[Day7]
1. employees.csv 데이터를 부서(department) 기준으로 그룹화하여 평균 급여 계산
2. 나이 30 이상이면서 급여 5000 이상인 직원 데이터 필터링
3. 급여의 10%를 계산하여 bonus 파생 컬럼 생성
4. 부서별 최고 급여를 받는 직원 추출

[Day8]
1. employees.csv와 departments.csv 파일을 읽어 DataFrame 생성
2. department 컬럼을 기준으로 직원 정보와 부서 정보 merge
3. bonuses.json 데이터를 읽어 emp_id 기준으로 직원 데이터와 merge 후 보너스 금액 계산
4.최종 DataFrame을 Excel 파일(employees_final.xlsx)로 저장
