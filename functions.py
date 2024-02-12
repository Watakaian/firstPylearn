# inbuilt function
y = max(67, 56, 34, 23, 89)
print(y)
x = min(67, 56, 34, 23, 89)
print(x)
z = pow(2, 3)
print(z)


# user defined functions
def name():
    print("Wataka")


name()  # calling a function

# parameters and argument
def students(names, course ,age):
       print(names,course,age)
students("Martin", "MIT", 18)
students('Wataka','Cybersecurity',18)

def employees(fullName, ID_no, salary,position,age):
    return (fullName,ID_no,salary,position,age)
print(employees('Wataka Ian',1234,'202000','Manager',27))
print(employees('Munyendo Ian',1234,'202000','CTO',27))
print(employees('Hussein Ian',1234,'202000','CFO',27))
print(employees('Arnold Ian',1234,'202000','CEO',27))
print(employees('John Ian',1234,'202000','ADMN',27))




