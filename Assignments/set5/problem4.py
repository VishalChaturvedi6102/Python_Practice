# What will be the length of following set s: 
# s = set() 
# s.add(20) 
# s.add(20.0) 
# s.add('20') # length of s after these operations


s = set() 
s.add(20) 
s.add(20.0) 
s.add('20')

print(s) # {20, '20'}  
print(len(s))  # 2


'''🧠 Deep Explanation
Step 1: s.add(20)

Set ban gaya:

{20}

Step 2: s.add(20.0)

Python check karta hai:

20 == 20.0   # True


Aur set value-based equality (==) use karta hai, type-based nahi.

So Python bolta hai:

"Ye value pehle se set me hai"

❌ Isliye 20.0 add nahi hota

Set ab bhi:

{20}

Step 3: s.add('20')

Ab compare hota hai:

20 == '20'   # False


20 → int

'20' → string

Value bhi different, type bhi different
✔️ So ye add ho jaata hai

Final set:

{20, '20'}

📏 Length = 2 kyun?

Set me sirf unique values hote hain:

20 (int & float dono ka common value)

'20' (string)

len(s)  # 2

🔑 Important Python Rule (EXAM / INTERVIEW)

In Python:
int aur float agar numerically equal hain → set/dict me duplicate maane jaate hain

Example:

{1, 1.0}      # {1}
{2, 2.0, 2}   # {2}

❓ Phir 20.0 print kyun nahi hua?

Set me pehla added value retain hota hai

Order:

s.add(20)     # pehle
s.add(20.0)   # duplicate → ignored


Isliye output me:

20   ✔️
20.0 ❌

🧪 Proof check
20 == 20.0          # True
hash(20) == hash(20.0)  # True


👉 Set hash + equality dono use karta hai

🧠 Final Summary
Element	Added?	Reason
20	✔️	First value
20.0	❌	20 == 20.0
'20'	✔️	Different type & value

Agar chaahe to next main dict me same behavior, ya True, 1, 1.0 ka confusion bhi clear kara deta hoon 😄🔥'''


'''Bhai simple words me samjhaata hoon 👇

Code
1 == 1.0

Output
True

❓ Aisa kyu hota hai?

Python me == operator value compare karta hai, type nahi.

🔹 Step-by-step samajh

1 → integer (int)

1.0 → floating point number (float)

Internally Python kya karta hai:

Jab int aur float compare hote hain,

Python int ko float me convert kar deta hai

So comparison ban jaata hai:

1.0 == 1.0


➡️ True

🔹 Important point

Python ke liye:

1   → 1.0
2   → 2.0


Value same hai, bas type different hai.

🔹 Type check karo
type(1)    # <class 'int'>
type(1.0)  # <class 'float'>


Types alag hain, lekin value same hai.

🔹 Agar type bhi check karna ho

Use is ❌ (galat for values)
Use type() ✅

type(1) == type(1.0)


Output:

False

🔹 Summary (yaad rakhne layak)
Expression	Result	Reason
1 == 1.0	True	value same
1 is 1.0	False	type & memory different
type(1) == type(1.0)	False	int ≠ float

Agar chaahe to main == vs is, ya float precision problems bhi samjha deta hoon bhai'''