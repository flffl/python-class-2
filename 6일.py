# -*- coding: utf-8 -*-
"""6일

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1m3hZmPlTHH0SFfKqFP1lWCDU7qgQqaQa
"""

str = input("How old are you: ")
print(str)

str = input("How old are you: ")
print(str+'years old')

x =int(input('number :'))
print(x)

x=float(input('number :'))
print(x)

year =input("This year")
year =eval(year)
year =year +1
print("Next year:",year)

i=0
result =0
while i<5:
  a=input("성적 입력 :")
  result += int(a)
  i += 1

1print(f'평균: {result / 5}')

test_list =['one','two','three']
for i in test_list:
      print(i)

for i in range(10):
  print(i)

for i in range(1,10):
  print(i)

result=0
for a in range(1,101): #1~100
     result = result + a

print(result)

result=0
for a in range(1,101):  #1~100
     result = result+a   # a를 더해주고

     if result>100: #result가 100이 넘었을때
         print(a)    #그때의 a값을 출력
         break

print(result)

index =0
s="BlockMask"
for a in s:
  print(a,end='')
  if a == 'k':
       break  #'k'를 찾았으니 for문에서 나와라

  index = index+1

print(index)      #"k"가 첫번째로 존재하는 위치 출력

student = [180,170,164,199,182,172,177]
for a in student:
     if a > 170:
         continue #키가 170보다 크면 continue

     print(a)

l = ['Alice' , 'Bob' , 'Charlie']

for name in l:
    if name == 'Bob':
        print('!!BREAK!!')
        break
    print(name)
else:
    print('!!FINISH!!')

l = ['Alice', 'Bob', 'Charlie']

for name in l:
    print(name)

for i, name in enumerate(l):
    print(i, name)

sr = ['father', 'mother', 'brother']
cnt = 0
for s in sr:
        for c in s:
            if c == 'r':
                cnt += 1
print(cnt)

a = []

for i in range(10):
    a.append(0)

print(a)

a = []

for i in range(3):
    line = []
    for j in range(2):
        line.append(0)
    a.append(line)

print(a)