# while loop

# incrementing values
number = 5
while number <= 10:
    print(number)
    number += 1

# decrementing values
num= 105
while num >= 100:
    print(num)
    num -= 1

# break statement
x = 1
while x <= 5:
    print(x)
    if x == 3:
        break
    x +=1

# continue statement
count = 19
while count < 25:
    count += 1
    if count == 23:
        continue
    print(count)

# for loop
languages = ['Python', 'Java', 'kotlin']
for language in languages:
    print(language)

# range
for z in range(6):
    print(z)

# range of values
for y in range(20,31):
    print(y)

for i in range(30,41,2):
    print(i)


for letter in 'innovation':
    print(letter)