name,char=input("Enter your name and one character\t:\t").split(",")
print(f"HELLO {name}!!.\n char={char}")
print(f"length = {len(name)}") #length of name
print(f"char count ={(name.count(char))}")#case sensative
print(f"char count ={name.lower().count(char.lower())}")


# name.strip().lower().count()
# char.strip().lower()
#name.strip().lower().count(char.strip().lower())
print(f"Character Count ={name.strip().lower().count(char.strip().lower())}")
