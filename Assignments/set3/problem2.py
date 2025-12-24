# Write a program to fill in a letter template given below with name and date. 
# letter = '''  
#        Dear <|Name|>, 
#        You are selected! 
#        <|Date|> 


name = input("name == ")
date = input("date == ")
print(f"Dear {name} \n You are selected ! \n {date}")

# OR

letter = '''Dear  <|Name|>,
You are a penguin!
<|Date|>'''

print(letter.replace("<|Name|>", "Rocky Bhai").replace("<|Date|>", "since 1995"))