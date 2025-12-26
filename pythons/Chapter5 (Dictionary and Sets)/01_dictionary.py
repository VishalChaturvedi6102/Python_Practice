#Dictionary is a collection of keys-value pair
# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
# Dictionaries are written with curly brackets, and have keys and values:


# Dictionary items are ordered, changeable, and do not allow duplicates.
# Dictionary items are presented in key:value pairs, and can be referred to by using the key name.
# yeah nah list of key:value pairs ki tarah hai

# dict main lookup  bahut zyada fast hota hai jaise mereko  from a wide collection of data of students marks main rocky bhai ke marks deekhne hote toh yeah process bahut zyada fast hoga

#empty dict
emptydictionary = {}



marks = {
    "rocky bhai" : 100,
    "rehman dakait" : 78,
    "disaster": 23
}
print(marks, type(marks))   # {'rocky bhai': 100, 'rehman dakait': 78, 'disaster': 23} <class 'dict'>

print(marks["rehman dakait"])  # 78



'''
PROPERTIES OF PYTHON DICTION ARIES  
1. It is unordered.    : the data can be store in random order
2. It is mutable.     : is changable i.e og dict will be changes when an operation is performed on it
3. It is indexed.   
4. Cannot contain duplicate keys. 




Properties of Python Dictionaries
1. It is Unordered

Python dictionary me elements fixed sequence/order me store nahi hote (especially Python 3.6 se pehle).
Matlab keys-values random order me ho sakte hain.

Example:

data = {"name": "Vishal", "age": 22, "city": "Delhi"}


Iska output order har baar same ho yeh zaroori nahi hota.

👉 Important point:
Hum dictionary ko index number (0,1,2) se access nahi kar sakte.

2. It is Mutable

Dictionary mutable hoti hai, matlab uske andar ka data change kiya ja sakta hai bina nayi dictionary banaye.

Example:

data = {"name": "Vishal", "age": 22}
data["age"] = 23
print(data)


Output:

{'name': 'Vishal', 'age': 23}


👉 Yaha original dictionary hi update ho gayi.

3. It is Indexed (Key-based Indexing)

Dictionary keys ke through indexed hoti hai, na ki numbers ke through.

Example:

data = {"name": "Vishal", "age": 22}
print(data["name"])


Output:

Vishal


👉
❌ data[0] (galat)
✅ data["name"] (sahi)

4. Cannot Contain Duplicate Keys

Dictionary me same key ek se zyada baar nahi ho sakti.
Agar duplicate key likhi jaati hai, to last value overwrite ho jaati hai.

Example:

data = {"age": 20, "age": 25}
print(data)


Output:

{'age': 25}


👉 Yaha pe pehli "age": 20 value remove ho gayi.

Short Summary (Exam ke liye 💯)

Dictionary unordered hoti hai

Dictionary mutable hoti hai

Dictionary key-based indexing use karti hai

Dictionary duplicate keys allow nahi karti

'''