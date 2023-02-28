array_int = [1, 2, 3, 4, 5]
new_array = []

for x in array_int:
    prd = 1
    for y in array_int:
        if x != y:
            prd *= y
    new_array.append(prd)

print(new_array)

# enumerate() is a built-in function in Python that can be used to assign an index to each element in a sequence or iterable. 
# Here's an example of how to use it:
for index, value in enumerate(array_int):
    print(index, value)
