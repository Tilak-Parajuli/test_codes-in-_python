name,age=input("Enter your name : ").split(",")
print("Hello" +name+ "your age is"+str(age)) #ugly
#string formatting
# python3
print("Hello {} your age is {}.".format(name,age))
# above python 3
print(f"Hello {name} your name is {age}")
# place holder-->>>{}
print(f"Hello everyone i`m {name}.I`m going to be successful at {age}")




