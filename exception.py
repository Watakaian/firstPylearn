# exception = errors
try:
    print(x)
except:
    print("An error occurred")
finally:
    print("success")

num1 = 20
num2 = 0
try:
    print(num1/num2)
except:
    print("An zero division error occurred")

# user-defined functions
try:
    def multiply(num3, num4):
        print(num3*num4)
except:
    print("An error occurred")
finally:
    print("success")
multiply(6, 5)
