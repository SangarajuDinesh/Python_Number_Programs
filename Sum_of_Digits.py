num=int(input("Enter the Number = "))
sum1=0
while(num>0):
    rem=num%10
    sum1+=rem
    num//=10
print(sum1)
