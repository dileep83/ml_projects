from flask import Flask, request, render_template, redirect, url_for
from controllers.image_controller import ImageController

app = Flask(__name__)

image_controller = ImageController()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['image']
        image_controller.process_image(file)
        return redirect(url_for('result'))
    else:
        return render_template('index.html')

@app.route('/result')
def result():
    return render_template('result.html')

if __name__ == '__main__':
    app.run(debug=True)
