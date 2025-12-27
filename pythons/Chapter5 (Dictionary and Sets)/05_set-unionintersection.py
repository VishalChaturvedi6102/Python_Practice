setA = {1, 2, 3, 4}
setB = {3, 4, 5, 6}

#  dono sets ko combine karke return kar deta + reprtative values ko sirf 1 baar printkarta hai
print(setA.union(setB))  # {1, 2, 3, 4, 5, 6}

# only common walo ko select karke return kardeta hai a
print(setA.intersection(setB))  # {3, 4}    

# - operation mere dono set main joh uncommon value hai ussko return karta hai bec common values to - hojati hai nah 
print(setA - setB)  # {1, 2}

