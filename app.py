from flask import Flask, request
from flask_restful import Api
from download import download_cheque
from upload import upload_details
from ocr import vision
from validate import account_number, amount_figure, amount_words, amount, cheque_date, cheque_number, correct_words
import preprocessing
# import vision
import time 
import  json
import os

app = Flask(__name__)
api = Api(app)


keyList = ['issue_date', 'account_number', 'cheque_number', 'amount_figure', 'amount_in_words',  'is_valid']
result = dict.fromkeys(keyList, None)
result['is_valid'] = True

@app.route('/', methods=['GET', 'POST'])
def get():

    file_name = request.args.get("cheque")

    folder_path = os.path.join(os.getcwd(), 'download')
    download_path = os.path.join(folder_path, file_name)
    is_downloaded = download_cheque.download_file_from_bucket(file_name, download_path)
    # print("download: ", is_downloaded)

    preprocessing.extract_cheque_features(download_path)

    upload_path = os.path.join(os.getcwd(), 'upload')
    features = ["_date.jpg", "_account_num.jpg", "_cheque_num.jpg", "_figure.jpg", "_amount_in_words.jpg", "_sign.jpg"]
    
    for feature in features:
        feature_file_name = file_name.split('.')[0] + feature
        is_uploaded = upload_details.upload_to_bucket(feature_file_name, os.path.join(upload_path, feature_file_name))
        # if is_uploaded:
        #     print("uploaded: ", feature_file_name)

    bucket_url = 'https://storage.googleapis.com/cheque_info'
    for feature, field in zip(features[:-1], keyList[:-1]):
        text = vision.detect_text_in_image(bucket_url + '/' + file_name.split('.')[0] + feature)

        if field == 'issue_date':
            result['is_valid'], result[field] = cheque_date.validate_check_date(text)
        
        elif field == 'account_number':
            result[field] = account_number.validate_account_number(text)
        
        elif field == 'cheque_number':
            result[field] = cheque_number.validate_cheque_number(text)

        elif field == 'amount_figure':
            result[field] = amount_figure.validate_cheque_amount(text)
        
        elif field == 'amount_in_words':
            result[field] = amount_words.validate_amount_words(text)
            result[field] = correct_words.update_amount(result[field])
        
    result['is_valid'] = amount.validate_amount_fig_amount_words(result['amount_figure'], result['amount_in_words'])
    ans = json.dumps(result)

    return ans

if __name__ == "__main__":
    app.run(port= 5000, debug= True)