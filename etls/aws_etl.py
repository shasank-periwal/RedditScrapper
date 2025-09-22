from utils.constants import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY
import s3fs


def connect_to_s3():
    try:
        s3 = s3fs.S3FileSystem(key=AWS_ACCESS_KEY_ID, secret=AWS_SECRET_ACCESS_KEY)
        return s3
    except Exception as e:
        print(e)

def create_bucket(s3: s3fs.S3FileSystem, bucket: str):
    try:
        if not s3.exists(bucket):
            s3.makedir(bucket)
            print('Bucket created')
        else:
            print('Bucket exists')
    except Exception as e:
        print(e)

def upload_to_s3(s3: s3fs.S3FileSystem, file_path: str, bucket: str, filename: str):
    try:
        s3.put(file_path, bucket+'/raw/'+filename)
        print('File uploaded to S3')
    except Exception as e:
        print(e)