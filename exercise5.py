# EXERCISE -WATCH SILICON_VALLEY 
# Ask user`s name and age 
# if user`s name starts with "t" or "T" and age is above 10 then 
# print you can watch silicon valley series 
# else print sorry,you can`t watch 


name =input("Enter your name : ")
age =input("Enter your age : ")
age =int(age)
if age >=10 and (name[0]=='t' or name[0] == 'T'):
    print("you can watch silicon valley")
else:
    print("You can`t watch silicon valley")    