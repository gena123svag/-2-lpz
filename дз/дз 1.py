def Proc1(x,y):
 RES=0
 for i in range(x,y+1):
  if i%2==0:
   RES=RES+i
 return RES

def pRintRes(num):
    print("Результат:",num)

a=int(input("Введите A: "))
b=int(input("Введите B: "))
if a<b:
    r=Proc1(a,b)
else:
    r=Proc1(b,a)
pRintRes(r)
