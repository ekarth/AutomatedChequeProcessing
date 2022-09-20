import string 
def validate_amount_words(text):
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = text.replace("and", "")
    text = text.replace("only", "")
    text = text.replace("thous", "thousand")
    words = [word.lower() for word in text.split()]

    i = 0
    while i < len(words):
        if words[i] == 'rupees':
            break
        i += 1

    i += 1
    j = i 
    while j < len(words):
        if len(words[j]) <= 2:
            break
        j += 1
    
    amount_in_words = words[i: j]
    amount_in_words = " ".join(amount_in_words)
    # print(amount_in_words)
    return amount_in_words

# print(validate_amount_words('(M)/CTS-2010 Rupees Acounty Two lash Twenty three, and only and only only thousand S T U V S D de ple del d TER'))