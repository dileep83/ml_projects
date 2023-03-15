from handlers.image_handler import ImageHandler
import os

class ImageController:
    def __init__(self):
        self.image_handler = ImageHandler()

    def process_image(self, file):
        img_array = self.image_handler.read_image(file)
        filtered_img_array = self.image_handler.apply_filter(img_array)
        filename = file.filename
        key_prefix = os.path.splitext(filename)[0]
        self.image_handler.save_image(img_array, key_prefix + '_original.jpg')
        self.image_handler.save_image(filtered_img_array, key_prefix + '_filtered.jpg')

    def get_original_image_url(self, key):
        return self.image_handler.get_original_image_url(key)

    def get_filtered_image_url(self, key):
        return self.image_handler.get_filtered_image_url(key)
