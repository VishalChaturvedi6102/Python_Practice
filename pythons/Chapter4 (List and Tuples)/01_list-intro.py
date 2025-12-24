# lists are containers to store a set of values of any data type. 
# list main differnt/ heterogenous type ke dataTypes bhi daal sakt hu
# mere list is mutable unlike strings  matlab agar mere apne list main koi bhi changes kiye toh wala mere o.g list main impact hoga unlike strings jiss main ek poori new string hii create ho jaati hai 

#in list indexing also styarts from 0

friends = ["apple", "orrange", 5, 345.09897, False, "Rocky bhai", "Rajat Dalal"]

print(friends[0])  # apple  mere 0th index per apple hai yaha per normal array ki tarah indexing hoti hai

friends[0] = "grapes"
print(friends[0]) # grapes
print(friends)  #  ['grapes', 'orrange', 5, 345.09897, False, 'Rocky bhai', 'Rajat Dalal']   mere og list main changes ho gaye 

#list slicing *same as string
print(friends[1:4])  # ['orrange', 5, 345.09897]
