the_list = [10, 15, 3, 8]
k = 17


def check_sum(a_list, num):
    for x in range(len(a_list)-2):
        for y in range(x, len(a_list)):
            if a_list[x]+a_list[y] == num:
                return True
    return False


print(check_sum(the_list, k))

