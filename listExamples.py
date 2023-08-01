list1 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

#PRINT LIST
print(list1)
print(list2)
print(list3)

#Access List Items
print(list1[2])
print(list1[2:5])

if "apple" in list1:
  print("Yes, 'apple' is in the list1")
else:
  print("No, 'apple' is not in the list1")

#Change Item Value
list1[1] = "blackcurrant"
print(list1)

list1[1:3] = ["blackcurrant", "watermelon"]
print(list1)

# Add List Items
list1.append("Jackfruit")
print(list1)

#Remove List Items
list1.remove("Jackfruit")
print(list1)

list1.pop(1)
print(list1)

#Loop in list
for x in list1:
  print(x)

for i in range(len(list1)):
  print(list1[i])

#Sort Lists
list1.sort()
print(list1)

list1.sort(reverse=True)
print(list1)

list1.sort(reverse=False)
print(list1)