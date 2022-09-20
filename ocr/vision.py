from google.cloud import vision
import pandas as pd

import os
# from langdetect import detect
# from textblob import TextBlob
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '../chequeprocessing.json'
def detect_text_in_image(img_url):
    '''Detects document features in the file located in Google Cloud Storage.'''

    client = vision.ImageAnnotatorClient()
    image = vision.Image()
    image.source.image_uri = img_url

    response = client.document_text_detection(image= image, image_context= {"language_hints": ['en']})
    text = response.full_text_annotation.text

    return str(text)
    # print(response.full_text_annotation)
    # print(df)
    # for page in response.full_text_annotation.pages:
    #     for block in page.blocks:
    #         for paragraph in block.paragraphs:
    #             for word in paragraph.words:
    #                 word_text = ''.join([symbol.text for symbol in word.symbols])
    #                 print(word_text)

# detect_text_in_image('https://storage.googleapis.com/cheque_info/account_num.jpg')
# print(detect_text_in_image('https://storage.googleapis.com/cheque_info/Cheque100828_amount_in_words.jpg'))
# print(detect_text_in_image('https://storage.googleapis.com/cheque_info/cheque_amount.jpg'))
# print(detect_text_in_image('https://storage.googleapis.com/cheque_info/1663485409197c_cheque_num.jpg'))
# print(detect_text_in_image('https://storage.googleapis.com/cheque_info/date.jpg'))
# print(detect_text_in_image('https://storage.googleapis.com/cheque_info/figure.jpg'))
