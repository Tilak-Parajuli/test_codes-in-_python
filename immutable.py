# strings are immutable in python
# in ruby strings are mutable
# e.g.
string ="string"
print(string[1]) #printing the first character
# string[1] ='T' error #in string characters can`t be changed
print(string.replace('t','T')) #replacing characters in string
print(string) #it is not changed i.e.original string can`t be changed

# but you can store in new variable
# for e.g
new_string =string.replace("t","T")
print(new_string)
