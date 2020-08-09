x = object()
y = object()

z = 0
x_list = [x]*10
y_list = [y]*10
big_list = x_list + y_list
another_list = []

print("x_list contains %d objects\n" % len(x_list))
print("y_list contains %d objects\n" % len(y_list))

if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...\n")

if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!\n")

print(big_list)