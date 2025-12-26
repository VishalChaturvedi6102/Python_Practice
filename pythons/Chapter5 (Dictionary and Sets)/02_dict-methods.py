
money = {
    "ambani": 500,
    "elon musk": 700,
    "bill gates": 100,
    0: "rehman dakait"
}

# a.items(): Returns a list of (key,value)tuples.
print(money.items())  # dict_items([('ambani', 500), ('elon musk', 700), ('bill gates', 100), (0, 'rehman dakait')])


# a.keys(): Returns a list containing dictionary's keys.
print(money.keys()) #dict_keys(['ambani', 'elon musk', 'bill gates', 0])


 # values returns all the corresponding values in from the key: value pair
print(money.values())  # dict_values([500, 700, 100, 'rehman dakait'])


# a.get("name"): Returns the value of the specified keys (and value is returned 
# eg."harry" is returned here).   ; will return None if not found 
print(money.get("elon musk"))  # 700



# a.update({"friends":}): Updates the dictionary with supplied key-value pairs.   + it can also add new data in current dictionary
money.update({"bill gates": 40})
print(money)  # {'ambani': 500, 'elon musk': 700, 'bill gates': 40, 0: 'rehman dakait'}


# difference b/wn get v/s [] index method for featching data

print(money.get("mukesh ambani"))  # returns None

print(money["mukesh ambani"])  # returns error 
# Traceback (most recent call last):
#   File "e:\Practice\Python_Practice\pythons\Chapter5 (Dictionary and Sets)\02_dict-methods.py", line 36, in <module>
#     print(money["mukesh ambani"])
#           ~~~~~^^^^^^^^^^^^^^^^^
# KeyError: 'mukesh ambani'