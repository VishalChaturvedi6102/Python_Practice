
friends = ["apple", "orange", 5, 456.09, True, "akash", "rohan"]
print(friends)

friends.append("Rocky bhai")  # joh bhi data pass kiya hai append function woh issko concatinate kardeta hai at the end of the list
#friends.sort() # TypeError: '<' not supported between instances of 'int' and 'str'
print(friends)

#SORT function : bhai wohi random aligned data but of same dataType only unnko ascending main sort maar deta hai
list1 = [1, 78,99, 67, 45,88, 22, 11, 78, 876876327934287, 38978934263289,0]
#list1.sort() 
 
#REVERSE function : poori list ko reverse kardeta hai
list1.reverse() # [0, 38978934263289, 876876327934287, 78, 11, 22, 88, 45, 67, 99, 78, 1]
print(list1) #[0, 1, 11, 22, 45, 67, 78, 78, 88, 99, 38978934263289, 876876327934287]


#INSERT method
#(index: SupportsIndex, object: int, /) -> None
#Insert object before index.
#insert method meri list main data ko kisi particular index main insert karne ki permission deta hai mujhe
list2 = [1,2,3,7,8,9,10]
list2.insert(3, 33333)
print(list2)   # [1, 2, 3, 33333, 7, 8, 9, 10]
 
#POP method :  Will delete element at index  and return its value.  
print(list2.pop(2)) # 3
print(list2)  #[1, 2, 33333, 7, 8, 9, 10]