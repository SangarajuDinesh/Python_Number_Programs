num=int(input("Enter the Number = "))
temp=num
sum1=0
while(num>0):
    rem=num%10
    sum1=(sum1*10)+rem
    num//=10
if(sum1==temp):
    print("Palindrome")
else:
    print("Not a Palindrome")
