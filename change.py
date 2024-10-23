import math

print("お金を入れてください")
n = int(input())
print("金額を入力してください")
m = int(input())
if m < n :
  a = n - m
  if a >= 500 :
    print("500円玉:",a // 500)
    a = a % 500
    print("100円玉:",a // 100)
    a = a % 100
    print("50円玉:",a // 50)
    a = a % 50
    print("10円玉:",a//10)
  elif a < 500 and a >=100 :
    print("100円玉:",a // 100)
    a = a % 100
    print("50円玉:",a // 50)
    a = a % 50
    print("10円玉:",a//10)
  elif a < 100 and a >= 50:
    print("50円玉:",a // 50)
    a = a % 50
    print("10円玉:",a//10)
  elif a < 50:
    print("10円玉:",a//10)
else :
  print("足りません")