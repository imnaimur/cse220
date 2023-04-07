# task1 a
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(4))

# task1 b
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1)+ fibonacci(n-2)
    
print(fibonacci(6))

# task1 c
def print_array(arr, n):
    if n == 0:
        return
    else:
        print_array(arr, n-1)
        print(arr[n-1],end=" ")
my_array = [1, 2, 3, 4, 5]
print_array(my_array, len(my_array)) # prints 1 2 3 4 5
print()

def powerN(b, n):
    if n == 0:
        return 1
    else:
        return b * powerN(b, n-1)


print(powerN(3, 3))


def binary(n):
    st = ""
    if n != 0:
        rem = n%2
        st += str(rem)
        binary(n//2)
        print(rem,end = "")

binary(10)
print()

#medium
def hocBuilder(n):
    if n == 1:
        return 8
    else:
        return 5+hocBuilder(n-1)
    
print(hocBuilder(1))