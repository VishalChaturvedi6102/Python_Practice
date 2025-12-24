# string is squence of characters enclosed in ""
# string is datatype
# string is immutable

name = "goodkiller"
# to find the length of the string
print(len(name))  #10


#slicing
nameslice = name[0:3]
print(nameslice)  # goo
character1 = name[0] #g
character1 = name[1] #o
character1 = name[-1] #r
print(character1)


# -ve slicing : hum nah -ve slicing main  apne -ve indexes ko corresponding +ve indexes ke according set kar sakte hai                 h  a   r  r  y    len(harry) =5
#    +ve indexes => 0  1   2  3  4 
#    -ve indexes => -5 -4 -3 -2 -1

str = "harry"

print(str[-4:-1])  #arr
print(str[1:4])   # arr

print(str[:4])  # [0:4]
print(str[1:])   # [1:length /5]