my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
a = -1
while a < len(my_list):
    a = a + 1
    if my_list[a] < 0:
        break
    if my_list[a] > 0:
        print(my_list[a])
        continue




