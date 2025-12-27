set = {1, 2, 3, 4, 5, 5, 5, "rocky bhai"}

print(set, type(set))  # {1, 2, 3, 4, 5, 'rocky bhai'} <class 'set'>


# ADD methods adds the new data in the set at the last 
set.add(56666)
print(set, type(set)) # {1, 2, 3, 4, 5, 'rocky bhai', 56666} <class 'set'>




# 1. add()

# Set me ek element add karta hai.

s = {1, 2, 3}
s.add(4)
print(s)


# 👉 Output: {1, 2, 3, 4}

# 🔹 2. update()

# Set me multiple elements add karta hai (list, tuple, set se).

s = {1, 2}
s.update([3, 4, 5])
print(s)

# 🔹 3. remove()

# Specified element remove karta hai.
# ❌ Agar element na ho → error aata hai.

s = {1, 2, 3}
s.remove(2)

# 🔹 4. discard()

# Element remove karta hai without error.

s = {1, 2, 3}
s.discard(5)   # koi error nahi

# 🔹 5. pop()

# Set se random element remove karke return karta hai.

s = {10, 20, 30}
x = s.pop()
print(x)


# 👉 Sets unordered hote hain, isliye random element nikalta hai.

# 🔹 6. clear()

# Set ke saare elements delete karta hai.

s = {1, 2, 3}
s.clear()
print(s)


# 👉 Output: set()

# 🔹 7. union()

# Do sets ko merge karta hai (duplicates nahi aate).

a = {1, 2}
b = {2, 3}
print(a.union(b))


# 👉 {1, 2, 3}

# 🔹 8. intersection()

# Common elements return karta hai.

a = {1, 2, 3}
b = {2, 3, 4}
print(a.intersection(b))


# 👉 {2, 3}

# 🔹 9. difference()

# First set ke elements jo second me nahi hain.

a = {1, 2, 3}
b = {2, 4}
print(a.difference(b))


# 👉 {1, 3}

# 🔹 10. symmetric_difference()

# Jo elements sirf ek set me ho (common nahi).

a = {1, 2, 3}
b = {2, 3, 4}
print(a.symmetric_difference(b))


# 👉 {1, 4}

# 🔹 11. issubset()

# Check karta hai ek set dusre ka part hai ya nahi.

a = {1, 2}
b = {1, 2, 3}
print(a.issubset(b))


# 👉 True

# 🔹 12. issuperset()

# Check karta hai set dusre ko contain karta hai ya nahi.

b = {1, 2, 3}
a = {1, 2}
print(b.issuperset(a))


# 👉 True

# 🔹 13. isdisjoint()

# Check karta hai dono sets me koi common element nahi.

a = {1, 2}
b = {3, 4}
print(a.isdisjoint(b))


# 👉 True