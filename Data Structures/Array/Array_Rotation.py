"""
This is going to go over how to rotate an array

start with: 1234567
end with: 3456712

Things to note:
arr - you already know what this is (if not dw)
d - this is what we are gonna use as a marker for how many times you would like to rotate
n - how many elements are in your array
"""

def rotatearray(arr, d, n):
    for i in range(d):              # here you want to do a for loop going through d amount of times (set on how many times you wanna rotate)
        rotatearrayleftone(arr, n)  # next would be calling the function that would rotate the array to the left one-by-one

def rotatearrayleftone(arr, n):
    temp = arr[0]                   # you want to set the temp to arr[0] so that you keep the val
    for i in range(n-1):            # so here what you have to do is make sure to do n-1, the reason for that is because array starts at 0 not 1
        arr[i] = arr[i+1]           # you want to replace the current with the next number
    arr[n-1] = temp                 # at the end give n-1 the temp value (original start value) 


arr = [1,2,3,4,5,6,7]
print(arr)
rotatearray(arr, 2, 7)
print(arr)

arr2 = ['a','b','c','d']
print(arr2)
rotatearray(arr2, 2, 4)
print(arr2)