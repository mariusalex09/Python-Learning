from re import X


given = [100, 200, 300, 400, 500]
print(given)
expected = list(reversed(given))
print(given)
print(expected)

x = [10]
y = x
y.append(2)
print(x, y)

given1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]

expected1 = [elem for elem in given1 if elem != ""]
print(expected1)

given2 = [5, 10, 15, 20, 25, 50, 20]
for index, val in enumerate(given2):
    if val == 20:
        given2[index] = 200
        break
print(given2)

given3 = [5, 20, 15, 20, 25, 50, 20]
expected3 = [elem for elem in given3 if elem != 20]
print(expected3)

list1 = ["M", "na", "i", "Ri"]
list2 = ["y", "me", "s", "ck"]
expected4 = ["".join(elem) for elem in zip(list1, list2)]

print(expected4)

