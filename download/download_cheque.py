from google.cloud import storage
import os 

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]='D:\\Projects\\chequeprocessing.json'

def download_file_from_bucket(blob_name, file_path):
    '''Download a file from google cloud storage bucket'''

    try:
        storage_client = storage.Client()
        bucket = storage_client.get_bucket('cheque_info')
        blob = bucket.blob(blob_name)
        with open(file_path, 'wb') as f:
            storage_client.download_blob_to_file(blob, f)
        return True

    except Exception as e:
        # print(e)
        return False
