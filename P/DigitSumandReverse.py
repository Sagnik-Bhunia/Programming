n=int(input("Enter an integer"))
temp=n
sum_digits=0
reverse=0
while temp> 0:
 digit=temp%10
 sum_digits=sum_digits+digit
 reverse=reverse*10+digit
 temp=temp//10    
print("Sum of digits: ",sum_digits)
print("Reversed digit: ",reverse)
