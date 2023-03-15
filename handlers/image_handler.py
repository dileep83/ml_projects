import os
from io import BytesIO
import boto3
import numpy as np
import cv2
from PIL import Image
from controllers import s3_controller

class ImageHandler:
    def __init__(self):
        self.s3 = s3_controller.S3Controller()

    def read_image(self, file):
        img = Image.open(file)
        img_array = np.array(img)
        return img_array

    def apply_filter(self, img_array):
        gray = cv2.cvtColor(img_array, cv2.COLOR_BGR2GRAY)
        return cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

    def save_image(self, img_array, key_prefix):
        img = Image.fromarray(img_array)
        img_io = BytesIO()
        img.save(img_io, 'JPEG')
        img_io.seek(0)
        self.s3.upload_fileobj(img_io, key_prefix)

    def get_original_image_url(self, key):
        return self.s3.get_presigned_url(key)

    def get_filtered_image_url(self, key):
        return self.s3.get_presigned_url(key)
