from flask import Blueprint, render_template, request, make_response
from handlers.image_handler import process_image

image_controller = Blueprint('image_controller', __name__)

@image_controller.route('/')
def index():
    return render_template('upload.html')

@image_controller.route('/upload', methods=['POST'])
def upload():
    # Get the uploaded image file
    image_file = request.files['image']

    # Pass the image file to the image processing handler
    filtered_image = process_image(image_file)

    # Package the filtered image as an HTTP response
    response = make_response(filtered_image.tobytes())
    response.headers.set('Content-Type', 'image/png')
    response.headers.set('Content-Disposition', 'attachment', filename='filtered_image.png')
    return response
