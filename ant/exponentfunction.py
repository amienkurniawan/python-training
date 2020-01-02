def raise_to_number(base_num,pow_num):
    result = 1
    for index in range(pow_num) :
        result = result * base_num
    return result
print(raise_to_number(3,2))