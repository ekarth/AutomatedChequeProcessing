update_words = {
    'lakhs': 'lakh',
    'lashs': 'lakh',
    'lash': 'lakh',
    'lack': 'lakh',
    'lacks': 'lakh',
    'lac': 'lakh',
    'tounty': 'twenty',
    'acounty': 'twenty',
    'twety': 'twenty'
}

def update_amount(amount):
    words = amount.split()
    updated_amount = ""
    for word in words:
        if word in update_words.keys():
            updated_amount += (update_words[word] + " ")
        else:
            updated_amount += (word + " ")

    return updated_amount.strip()
