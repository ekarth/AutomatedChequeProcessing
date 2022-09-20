def validate_cheque_number(chq_num):

    cheque_num = ''
    for d in chq_num:
        
        if d.isdigit():
            cheque_num += d

        if d == 'O' or d == 'o':
            cheque_num += '0'

        elif d == 'l' or d == 'I' or d == 'i':
            cheque_num += '1'

        elif d == 'T':
            cheque_num += '7'

    return int(cheque_num[1: 7])

# print(validate_cheque_number('182 8001.'))