import num2words
import re 

def compare(str1, str2):

    if str1  == str2:
        return True
    else:
        return False

def validate_amount_fig_amount_words(amount, legal_amount_words):
    
    amount_in_words = num2words.num2words(amount, lang= 'en_IN')
    amount_in_words = re.sub('[^a-zA-Z0-9]+\s*', ' ', amount_in_words)
    amount_in_words = amount_in_words.strip()
    return compare(amount_in_words, legal_amount_words)

# print(validate_amount_fig_amount_words(2223000, 'acounty two lash twenty three thousand'))
