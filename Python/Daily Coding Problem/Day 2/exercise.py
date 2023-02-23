array_int = [1, 2, 3, 4, 5]
new_array = []

for x in array_int:
    prd = 1
    for y in array_int:
        if x != y:
            prd *= y
    new_array.append(prd)

print(new_array)
