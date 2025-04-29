weight=float(input('enter a number'))
tax=0
if weight <= 15:
  tax=0
else:
     if weight >=25:
         extra=weight - 15
         tax = extra * 50
print('total tax to be paid:' ,tax)'''

'''num=int(input('enter a number'))
if num>0:
  print('number is odd')
else:
  print('number is even')'''

#Program to Find the Greater of FIVE Numbers
'''num=int(input('enter a number'))
if num>5:
  print('number is greater than five')
else:
  print('number is less than five')'''

#Write a Program to Prompt for a Score between 0.0 and 1.0. If the Score Is Out of Range, Print an Error. If the Score Is between 0.0 and 1.0, Print a Grade Using the Following Table
# Score   Grade
# >= 0.9   A
# >= 0.8   B
# >= 0.7   C
# >= 0.6   D
# < 0.6    F
'''num=int(input('enter a number'))
if num>=0.9:
  print('number is greater than 0.9')
elif num>=0.8:
  print('number is greater than 0.8')
elif num>=0.7:
  print('number is greater than 0.7')
elif num>=0.6:
  print('number is greater than 0.6')
else:
  print('number is less than 0.6')'''

#Program to Display the Cost of Each Type of Fruit
'''fruit=(input('enter a name of fruit'))
if fruit=='apple':
  print('cost of apple is 100')
elif fruit=='orange':
  print('cost of orange is 150')'''

#Program to Check If a Given Year Is a Leap Year
'''n=int(input('enter a year:'))
if (n%4==0 and n%100!=0) or (n%400==0):
  print(n, 'is a leap year')
else:
  print(n, 'is not a leap year')'''

#Write Python Program to Display First Numbers Using while Loop Starting from 0
'''num=int(input('enter a  number)'))
#while loop
while num<=10:
  print(num)
  num+=1'''
'''a=6
b=9
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a&b)
print(a**b)
print(a//b)'''

#write a python to calculate interest for the given principle amount
'''p=10000
r=2
t=12
#i=ptr/100
i=p*t*r/100
print("interest:",i)'''

#write a python program to calcate 10% of discount using
#promocode applied
'''price=(36000)
discount=price*10/100
payable_amount=price-discount
print("payable amount:",payable_amount)'''

#write a program to calculate speed of the car using s=ut+1/2at2
'''s=900
t=60
a=30
speed=u*t+0.5*a*t*t
print("speed:",speed)'''
'''u_velocity=10
a_acceleration=5
t_time=3
s_speed=u_velocity+a_acceleration*t_time
print("speed:",s_speed)'''

##write a python program using BMI
#inputs temperature, cough, breathing
#tkniter builtin module with BMI
#Write a python program to calculate BMI ?
'''height=5.8
weight=65

bmi=weight/height*height
if(bmi<18):
    print("under weight")
elif(bmi>18 and bmi<25):
    print("normal")
else:
    print("obesity")'''

#function to calculate BMI
'''def calculate_bmi(height, weight):
    bmi = weight / (height ** 2)
    return bmi

#input height in meters weight in kilograms
height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))
bmi = calculate_bmi(height, weight)
#determine weight category
if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal")
elif bmi < 30:
    print("Overweight")
else:
    print("Obesity")
#print the BMI value
print(f"Your BMI is: {bmi:.2f}")'''

'''from tkinter import *
from tkinter import messagebox

window=Tk()
window.title("COVID-19")
window.config(bg="sky blue")
window.geometry("600x900")


#user defined function
def covid_19():
    temperature=int(e1.get())
    cough = int(e2.get())
    breathing = int(e3.get())
    if temperature>=98 and cough>=90 and breathing>=60:
        messagebox.showinfo("COVID-19","You are at risk of COVID-19")
    else:
        messagebox.showinfo("COVID-19","You are not at risk of COVID-19")

#create a label for temperature mount to be enter
l1=Label(window,text="TEMPERATURE:",font=90)
l1.grid(row=0,column=0)
e1=Entry(window)
e1.grid(row=0,column=1)
l2=Label(window,text="COUGH:",font=90)
l2.grid(row=1,column=0)
e2=Entry(window)
e2.grid(row=1,column=1)
l3=Label(window,text="BREATHING:",font=90)
l3.grid(row=2,column=0)
e3=Entry(window)
e3.grid(row=2,column=1)

b1=Button(window,text="COVID-19",command=covid_19)
b1.grid(row=3,column=1)

window.mainloop()'''

#Write Python Program to Display First 10 Numbers Using while Loop Starting from 0
'''num=10
while num<=10:
    print(num)
num+=1'''

#Write a Program to Find the Average of n Natural Numbers Where n Is the Input from the User
'''num=int(input('enter a number'))
if num>0:
    print('number is positive')
if num<0:
    print('number is negative')'''

#Program to Find the GCD of Two Positive Numbers
'''num1=int(input('enter a number'))
num2=int(input('enter a number'))
if num1>num2:
    num1,num2=num2,num1
for i in range(1,num1+1):
    if num1%i==0 and num2%i==0:
        gcd=i
print('gcd of two numbers is:',gcd)'''

#Write Python Program to Find the Sum of Digits in a Number
'''num=int(input('enter a number'))
sum=0
while num>0:
    sum=sum+num%10
    num=num//10
print('sum of digits in a number is:',sum)'''

#Write a Program to Display the Fibonacci Sequences up to nth term Where n is Provided by the User
'''n=int(input('enter a number'))
a=0
b=1
print(a)
print(b)
for i in range(2,n):
    c=a+b
    print(c)
    a=b
    b=c'''

#Program to Repeatedly Check for the Largest Number Until the User Enters "done"
'''num=input('enter a number')
while num!='done':
    num=int(input('enter a number'))
if num>largest:
        largest=num
print('largest number is:',largest)'''

#Demonstrate for Loop Using range() Function
'''num=int(input('enter a number'))
for i in range(1,11):
    print(i)'''

#Program to Iterate through Each Character in the String Using for Loop
'''name=input('enter a name')
for i in name:
    print(i)'''


#Write a Program to Find the Sum of All Odd and even Numbers up to a Number Specified by the User.
'''num=int(input('enter a number'))
sum=0
for i in range(1,num+1):
    if i%2==0:
        sum=sum+i
print('sum of all even numbers is:',sum)'''

#Write a Program to Find the Factorial of a Number
'''num=int(input('enter a number'))
fact=1
for i in range(1,num+1):
    fact=fact*i
print('factorial of a number is:',fact)'''

#Program to Demonstrate Infinite while Loop and break
'''num=int(input('enter a number'))
while True:
    if num==10:
        break
    print(num)
    num+=1'''

#Write a Program to Check Whether a Number Is Prime or Not
'''num=int(input('enter a number'))
if num>1:
    for i in range(2,num):
        if num%i==0:
            print('number is not prime')
            break
    else:
        print('number is prime')'''

#Program to Demonstrate continue Statement
'''num=int(input('enter a number'))
for i in range(1,num+1):
    if i%2==0:
        continue
    print(i)'''

#Program to Check for ValueError Exception
'''num=int(input('enter a number'))
if num>0:
    print('number is positive')
else:
    print('number is negative')'''

#Program to Check for ZeroDivisionError Exception
'''num=int(input('enter a number'))
if num>0:
    print('number is positive')
else:
    print('number is negative')'''

#Program to Check for ZeroDivisionError Exception
'''numerator=int(input('enter a numerator'))
denominator=int(input('enter a denominator'))
if denominator==0:
    print('denominator cannot be zero')

else:
    result=numerator/denominator
    print('result is:',result)'''

#write a calculate total balance after deposit
'''current_bal=20000
deposit_amount=float(input('enter money to be deposit into account: '))
total_bal=current_bal+deposit_amount
print('total account bal:',total_bal)'''

#write a python prgrm to display balance after withdrawl an amount
'''current_bal=20000
withdrawl_amount=float(input('enter money to be withdrawl from account: '))
print('total account bal:',current_bal-withdrawl_amount)'''

#write a python program to calculate intrest monthly based on current bank balance
'''current_account_bal=10000
annual_intrest=6
monthly_rate=annual_interest/12
intrest=current_account_bal*(monthly_rate/100)
print('interest monthly:',interest)'''

#write a python program to calculate shipping cost for delivery of a product
'''weight=40
distance=100
base_shipping_cost=0.5
shipping_cost=weight*distance*base_shipping_cost
print('shipping cost:',shipping_cost)'''
