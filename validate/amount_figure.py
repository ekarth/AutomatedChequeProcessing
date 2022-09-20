def validate_cheque_amount(amount_fig):

    amount = ''
    for d in amount_fig:
        
        if d.isdigit():
            amount += d

        if d == 'O' or d == 'o':
            amount += '0'

        elif d == 'l' or d == 'I' or d == 'i':
            amount += '1'

        elif d == 'T':
            amount += '7'

    # print(amount)
    return int(amount)

# print(validate_cheque_amount('125,00,12/-'))

