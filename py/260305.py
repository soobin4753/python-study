# Day1 
# 1번. 아래 데이터를 반복문으로 출력해라.
users = [
    {"name": "kim", "age": 30},
    {"name": "lee", "age": 25},
    {"name": "park", "age": 28}
]

for user in users :
    #print(f"name: {user['name']}, age: {user['age']}")
    print(f"{user['name']} {user['age']}")

#---------------------------------------------------------------
# 2번. 위 users에서 나이가 28 이상인 사람만 출력하라

for user in users :
    if user['age'] >= 28 :
        print(f"{user['name']} {user['age']}")

#===============================================================
# Day2
# 1번. 나이만 모아서 리스트로 만들어라

age=[]
for user in users :
    age.append(user['age'])

print(age) # 확인하는 방법

#---------------------------------------------------------------
# 2번. users에서 28세 이상인 사람의 name만 모아서 리스트로 만들어라. 한줄로

name =[user['name'] for user in users if user['age'] >= 28]
print(name)

#---------------------------------------------------------------
# 3번. 다음 JSON 문자열을 파이썬 객체로 변환하고 반복문으로 name만 출력해라.

import json
from tkinter.filedialog import test

data = '[{"name": "choi", "age": 40}, {"name": "jung", "age": 22}]'

result = json.loads(data)
for user in result:
    print(user['name'])

#===============================================================
# DAY3
# 1번. 파일 users.txt 생성하고 아래 내용 저장해라

with open('py/users.txt', 'w') as f:
    f.write('name,age\n')
    f.write('kim,30\n')
    f.write('lee,25\n')
    f.write('park,28\n')

with open('py/users.txt', 'r') as f:
    for line in f:
        print(line.strip())

#---------------------------------------------------------------
# 2번. users.txt 파일에서 나이가 28 이상인 사람의 name만 출력해라

with open('py/users.txt', 'r') as f:
    for line in f:
        name, age = line.strip().split(',') # strip()으로 줄바꿈 제거
        if age.isdigit() and int(age) >= 28: # isdigit() → 문자열 숫자 체크, int 변환 후 조건 확인
            print(f"name: {name}, age: {age}")

#---------------------------------------------------------------
#3번 파일 읽을 때 나이가 숫자가 아닐 경우 에러를 무시하고 넘어가라.
with open('py/users.txt', 'r') as f:
    for line in f:
        name, age = line.strip().split(',')
        try:
            if age.isdigit():  # 숫자인지 체크
                print(f"name: {name}, age: {age}")
        except ValueError:
            continue