# Write a program to accept marks of 6 students and display them in a sorted  manner

marks = ()

m1 = (input("enter marks = "))
marks.append(m1)
m2 = (input("enter marks = "))
marks.append(m2)
m3 = (input("enter marks = "))
marks.append(m3)
m4 = (input("enter marks = "))
marks.append(m4)
m5 = (input("enter marks = "))
marks.append(m5)
m6 = (input("enter marks = "))
marks.append(m6)

sortedMarks = marks.sort()
print(sortedMarks)