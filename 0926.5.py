a=int(input("請輸入一個三位數:"))
b=a%10
c=a//10%10
d=a//100
e=b*100+c*10+d
print("結果為:",e)