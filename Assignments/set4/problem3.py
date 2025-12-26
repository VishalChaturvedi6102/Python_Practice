#Check that a tuple type cannot be changed in python. 

tuple = (1, False, "rocky bhai")

tuple[2] = "rehman dakait"
print(tuple)


# Traceback (most recent call last):
#   File "e:\Practice\Python_Practice\Assignments\set4\problem3.py", line 5, in <module>
#     tuple[2] = "rehman dakait"
#     ~~~~~^^^
# TypeError: 'tuple' object does not support item assignment

#  because tuple is immutable