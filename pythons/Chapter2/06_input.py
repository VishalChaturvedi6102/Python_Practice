# for taking input from the users
# we use input function

# a = input("Bhai ek no. enter kar for a: ")
# b = input("Bhai ek no. enter kar for b: ")
# print("Number hai :",a)   
# print("Number hai :",b) 
# print("SUM is ", a + b)   

# yaha per nah sum main concatenation ho raha hai 
# Bhai ek no. enter kar for a: 1
# Bhai ek no. enter kar for b: 2
# Number hai : 1
# Number hai : 2
# SUM is  12


# reason yaha per humara i/p as string store ho raha hai so to avoid it we declare type before the input function that we want 
a = int(input("Bhai ek no. enter kar for a: "))
b = int(input("Bhai ek no. enter kar for b: "))
print("Number hai :",a)   
print("Number hai :",b) 
print("SUM is ", a + b) 
# yeah sahi answer dega  
# Bhai ek no. enter kar for a: 1
# Bhai ek no. enter kar for b: 3
# Number hai : 1
# Number hai : 3
# SUM is  4