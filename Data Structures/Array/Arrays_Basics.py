"""
This is gonna be a quick refresher on arrays, don't worry if you get lost I am as lost as you are LOL
for reference I am just writing down what I get from: https://www.geeksforgeeks.org/array-python-set-1-introduction-functions/ 

So let's start with what we now about arrays:
- can only manipulate specific data type values
- if there needs to be more room what happens is that it doubles and then you add the extras into it (def a better way to explin this)
"""

# Operations on Array
"""
- 'b' = | signed char | int | 1 byte (minimum) |
- 'B' = | unsigned char | int | 1 |
- 'u' = | Py_UNICODE | unicode character | 2 |
- 'h' = | signed short | int | 2 |
- 'H' = | unsigned short | int | 2 |
- 'i' = | singed int | int | 2 |
- 'I' = | unsigned int | int | 2 |
- 'l' = | signed long | int | 4 |
- 'L' = | unsigned long | int | 4 |
- 'q' = | signed long long | int | 8 |
- 'Q' = | unsigned long long | int | 8 |
- 'f' = | float | float | 4 |
- 'd' = | double | float | 8 |
"""

# Append
"""
This function adds a value mentioned in its arguement to the end of the array
"""
test_array = []
test_array.append(1)
test_array.append(2)
test_array.append(3)
print(test_array)


# Insert
"""
two parameters 
    - what you want to add
    - what position to add it into
"""
test_array.insert(0,0)
print(test_array)

# Pop
"""
removes the element at the position inside the arguement
"""
test_array.pop(0)
print(test_array)

# Remove
"""
Removes the first element found in the array that matches the element in the argument
"""
test_array.remove(3)
print(test_array)

# Index
"""
returns the index of the element that you are looking for (first occurence)
"""
print(test_array.index(1))

# Reverse
test_array.reverse()
print(test_array)