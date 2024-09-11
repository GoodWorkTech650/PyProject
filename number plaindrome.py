question=int(input("enter the number"))
reverse=0
length=int(question)
number=int(question)
temp=number
for i in range(0,4):
  remainder=number%10
  reverse=reverse*10+remainder
  number=number//10
print("orignal number is" ,temp)
print("reversed number is" ,reverse)
if temp==reverse:
   print("it's a palindrome number")
else:
  print("it's not a palindrome number")