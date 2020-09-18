from flask import Flask, request, render_template, url_for, jsonify
from image_processor import ImageProcessor
from digit_predictor import DigitPredictor

app = Flask(__name__)

arr = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def get_image():
    global arr
    ImgP = ImageProcessor()
    try:
        req = request.data
    except:
        print("Error occured! Couldn't get image data")
    
    ImgP.imageGenerator(req)
    arr = ImgP.imageProcessor()
    DigP = DigitPredictor()
    result_digit = DigP.digitPredict(arr)
    return jsonify(data = result_digit)

if __name__ == "__main__":
    app.run(debug = True)