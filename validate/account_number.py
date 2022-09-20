def validate_account_number(account_num):

    acc_num = ''
    for d in account_num:
        
        if d.isdigit():
            acc_num += d

        if d == 'O' or d == 'o':
            acc_num += '0'

        elif d == 'l' or d == 'I' or d == 'i':
            acc_num += '1'

        elif d == 'T':
            acc_num += '7'

    # print(acc_num)
    return acc_num

# print(validate_account_num())