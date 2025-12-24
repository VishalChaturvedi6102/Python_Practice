#Write a program to detect double space in a string. 


name = "Salam Rocky bhai" 
print(name.find("  "))  # returns -1   because koi bhi double space nahi hai

rame = "rehman dakait ki dii  hu maut  baadi   kaisai numa hoti    hai"
print(rame.find("  "))  # 20
print(rame.find("ait"))