list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

for x in list:
    print(x)
print("===============================")

for i in range(len(list)):
    print(list[i])

print("===============================")

for x in list:
    if x == "orange":
        break
    print(x)

