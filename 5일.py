# -*- coding: utf-8 -*-
"""5일

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1V-js32W9ke2wDQH3gOWLbUMQAJjiyW82
"""

name ="test"
 if name == "test":
    print("이름이 맞습니다")
 else:
    print("이름이 틀립니다")

pocket = 500
if pocket == 100:
    print("복권구매")
elif pocket == 500:
    print("껌 구매")
else:
    print("집")

a = "사과"
b="바나나"
c="치즈"

if a =="사고" or b=="안바나나":
      print("사과 이거나 바나나 입니다.")

if a =="사고" or b=="바나나":
      print("사과이고 바나나 입니다.")

if not c =="사과":
      print("사과가 아니어야 합니다.")

a=[1,2,3,4,5,6,7,8,]

if 1 in a:
  print("1 is in a")
if 10 in a:
  print("10 is in a")

a=[1,2,3,4,5,6,7,8,9,10]

if 1 in a:
  print("1 is in a")
if 10 in a:
  print("10 is in a")

p_class = "Z"
sel_amount = 79900

if p_class == "A":
    sel_amount *= 0.7
    print(sel_amount)
elif p_class == "B":
    sel_amount *= 0.85
    print(sel_amount)
elif p_class == "C":
    sel_amount *= 0.92
    print(sel_amount)
elif p_class == "Z":
    sel_amount += 5000
    print(sel_amount)

p_class = "A"
sel_amount = 79900

if p_class == "A":
    sel_amount *= 0.7
    print(f'판매가는 {sel_amount}원 입니다.')
elif p_class == "B":
    sel_amount *= 0.85
    print(f'판매가는 {sel_amount}원 입니다.')
    print('판매가는 %f입니다' % sel_amount)

x=11

if x<10:
  print('x는 10보다 작아!')
else:
  print('x는 10보다 작지 않아!')

x = 2

if x%2 == 0:
  print('x는 짝수야!')
else:
  print('x는 홀수야!')

x=3
if x<10:
  print("x는 10보다 작아")
  if x%2 ==0:
     print("x는 짝수야!")
  else:
     print("x는 홀수야!")
else:
  print("x는 10보다 커!")
  if x%2 ==0:
      print("x는 짝수야!")
  else:
      print("x는 홀수야!")

x=12
if x<10:
  print("x는 10보다 작아")
  if x%2 ==0:
     print("x는 짝수야!")
  else:
     print("x는 홀수야!")
else:
  print("x는 10보다 커!")
  if x%2 ==0:
      print("x는 짝수야!")
  else:
      print("x는 홀수야!")

x=12
if x<10 and x%2==0:
   print("x는 10보다 작으면서 짝수야!")
if x<10 and not x%2==0:
   print("x는 10보다 작으면서 홀수야!")
if not x<10 and x%2==0:
   print("x는 10보다 크면서 짝수야!")
if not x<10 and not x%2==0:
   print("x는 10보다 크면서 홀수야!")

treeHit =0

while treeHit < 10:
    treeHit = treeHit +1
    print("나무를 %d번 찍었습니다." % treeHit)
    if treeHit == 10:
      print("나무 넘어갑니다.")

coffee =10
money=300
while money:
  print("돈을 받았으니 커피를 줍니다.")
  coffee = coffee -1
  print("남은 커피와 양은 %d개입니다."%coffee)
  if coffee ==0:
     print("커피가 다 떨어졌습니다.판매를 중지합니다.")
     break

i=0
result1 = 0
while i<100:
   i=i+1
   if i % 2 == 0:
      result1 = result1+i

print('1번 방법: {0}'.format(result1))