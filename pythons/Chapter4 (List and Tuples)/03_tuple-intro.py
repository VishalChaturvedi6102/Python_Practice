# Tuples are used to store multiple items in a single variable.
# Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.
# A tuple is a collection which is ordered and unchangeable.
# Tuples are written with round brackets.

# tuple bbhi same as list hai only difference
'''
tuple immutable hai just like string i.e upon any change / operation on tuple return main ek new tuple create hoga 
uss mai  asn. hoga 
() to store data
'''

tuple = (1, 2, 3 ,4 , 5)
print(tuple)

# EMPTY TUPLE kaise banai
emptyTuple = ()
print(type(emptyTuple))  #<class 'tuple'>

#TUPLE WITH ONLY 1 VALUE
onevaluetuple = (1,)
print(type(onevaluetuple))  #<class 'tuple'>
''' agar onevaluetuple = (1) aise likha nah yaar then py issko <int > samjha gaa'''

tpp = (1, 2, 3, 4, "Kachua", "bachua", False)
#tpp[0] = "room"  #Traceback (most recent call last):
#   File "e:\Practice\Python_Practice\pythons\Chapter4 (List and Tuples)\03_tuple-intro.py", line 26, in <module>
#     tpp[0] = "room"
#     ~~~^^^
# TypeError: 'tuple' object does not support item assignment

# cause tuple just like string immutable hai nah bhai i.e why hum log o.g tuple main kuch  changes wagera naghi kar sakte hai 



