import model
import numpy as np

from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

@app.route('/test', methods=['GET'])
def getResult():
    index = 10
    predictArr = []

    inputs = np.array([[[0, 0, 0.6, 0, False, 0]],[[0, 0, 0.6, 0, False, 0]]])
    for input in inputs:
        result = model.predict(input)
        predictArr.append({'index': str(index),'predict': str(result)})

    return jsonify(predictArr)

@app.route('/predict', methods=['POST'])
def postInput():
    predictArr = []
    # 取得前端傳過來的數值
    insertValuesArr = request.get_json()
    for insertValues in insertValuesArr:
        index = insertValues['index']
        x1=insertValues['content_length']
        x2=insertValues['photos_count']
        x3=insertValues['star_gap']
        x4=insertValues['like_count']
        x5=insertValues['reply']
        x6=insertValues['reviewer_rank']

        input = np.array([[x1, x2, x3, x4, x5, x6]])
        result = model.predict(input)
        predictArr.append({'index': str(index),'predict': str(result)})

    return jsonify(predictArr)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=False)