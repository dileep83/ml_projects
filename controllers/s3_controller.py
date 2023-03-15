import os
import boto3
from botocore.exceptions import NoCredentialsError

class S3Controller:
    def __init__(self):
        self.s3 = boto3.client('s3', region_name=os.getenv('AWS_REGION', 'us-east-1'))
        self.bucket_name = os.getenv('S3_BUCKET_NAME')

    def upload_fileobj(self, fileobj, key_prefix):
        original_key = key_prefix + '_original.jpg'
        filtered_key = key_prefix + '_filtered.jpg'
        try:
            # Upload original image
            self.s3.upload_fileobj(fileobj, self.bucket_name, original_key)

            # Upload filtered image
            fileobj.seek(0)
            self.s3.upload_fileobj(fileobj, self.bucket_name, filtered_key)
        except NoCredentialsError:
            print('Credentials not available')

    def get_presigned_url(self, key):
        return self.s3.generate_presigned_url('get_object', Params={'Bucket': self.bucket_name})
