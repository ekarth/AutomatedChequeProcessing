from google.cloud import storage
import os 
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] =  'D:\\Projects\\chequeprocessing.json'

def upload_to_bucket(blob_name, file_path):
    '''Upload file to cloud storage bucket'''

    try:
        storage_client = storage.Client()
        bucket = storage_client.get_bucket('cheque_info')
        blob = bucket.blob(blob_name)
        blob.upload_from_filename(file_path)
        return True

    except Exception as e:
        print(e)
        return False
