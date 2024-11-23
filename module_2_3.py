
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
[n] = [0]
num = my_list[n]
while num > 0:
    print(num)
    [n] = [n + 1]
    num = my_list[n]
    if n > len(my_list):
        break
    if num == 0:
        [n] = [n + 1]
        num = my_list[n]

















