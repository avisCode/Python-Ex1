def func(a, b, c):
    if(a+b > c and a+c > b and c+b > a):
        return "they are correct triangle sides lengths"

    else:
        return "they are in error"


print("Welcome to the triangle sides lengths test")
print("---------------------------------------\n")
print(func(4, 3, 2))
print(func(20, 3, 2))

print("\n------------------end of the test------------------")
