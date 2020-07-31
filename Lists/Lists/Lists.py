#declarations
numbers = []
strings = []


#initialization
names = ["John", "Eric", "Jessica"]
numbers.append(1)
numbers.append(2)
numbers.append(3)
strings.append("hello")
strings.append("world")
second_name = names[1]
secnumbers = numbers[0]


#Outputs
for x in numbers:
    print(x)
for y in strings:
    print(y)
print("The second name on the names list is %s" % second_name)

#alignment decides where the loop covers
for x in numbers:
    print(x)
    for y in strings:
        print(y)

print("The second number set has %d" % secnumbers)