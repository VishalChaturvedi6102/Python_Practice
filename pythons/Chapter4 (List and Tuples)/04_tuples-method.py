tuple = (1, 45, 435, 567, False, 89, "kachua",
         "random")
print(tuple)
#count method mera ek counter hai 
no = tuple.count(45)
print(no)  # 1 i.e one 1 occurence of 45 is there in my tuple

i = tuple.index(False) # 4 the index
print(i)

# joh mera index method hai nah woh mere finding number ki index ki first occurence ko find karke stop hojata hai agar ussko woh particular data jiss index per mil jata hai woh ussko return kardeta hai bus aage check bhi nahi karta 

# LENGTH : returns the total length of the tuple
print(len(tuple)) #8