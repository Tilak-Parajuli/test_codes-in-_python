# if elif if statement 
# show ticket pricing 
# 1 to 3 (free) 
# 4 to 10 (150)
# 11 to 60 (250)
# above 60 (200)

age =input("Enter your age :")
age = int(age)
if age==0 or age<0:
    print("You can`t watch series")
elif 0<age<=3:
    print("The Ticket is free.")
elif 3<age<=10:
    print("The Ticket fee is 150")
elif 10<age<=60:
    print("The Ticket fee is 250")
else:
    print("The Ticket fee is 200")            
