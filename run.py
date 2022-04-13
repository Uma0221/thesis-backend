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
    predictArr = []

    insertValuesArr = np.array([
        [0, 0, 0, 0.33, 0.33, 0.08, 0.6, 0, False, 0],
        [-1, 4, 2],
        [1.4, 2, 5, 0.33, 0.33, 4, 0.24, 1, True, 5],
        [2, 0, 0, 0.33, 0.33, 0.6, 0.03, 0, False, 0],
        ["test"],
        [3, 3],
        [10],
        [-2],
        [4, 5, 4, 0.33, 0.33, 0, 0.4, 2, True, 8]
    ])
    for insertValues in insertValuesArr:
        if(len(insertValues) > 0):
            if(len(insertValues) != 10):
                index = insertValues[0]
                result = -1

            else:
                index = insertValues[0]
                content_length = insertValues[1]
                photos_count = insertValues[2]
                content_positive = insertValues[3]
                content_negative = insertValues[4]
                star_gap = insertValues[5]
                month_rate = insertValues[6]
                like_count = insertValues[7]
                reply = insertValues[8]
                reviewer_rank = insertValues[9]

                input = np.array([[content_length, photos_count, content_positive,
                                 content_negative, star_gap, month_rate, like_count, reply, reviewer_rank]])
                result = model.predict(input)

            predictArr.append({'index': str(index), 'predict': str(result)})

    return jsonify(predictArr)


@app.route('/predict', methods=['POST'])
def postInput():
    predictArr = []
    # 取得前端傳過來的數值
    insertValuesArr = request.get_json()
    for insertValues in insertValuesArr:
        if(len(insertValues) > 0):
            if(len(insertValues) != 10):
                index = insertValues['index']
                result = -1
            else:
                index = insertValues['index']
                content_length = insertValues['content_length']
                photos_count = insertValues['photos_count']
                content_positive = insertValues['content_positive']
                content_negative = insertValues['content_negative']
                star_gap = insertValues['star_gap']
                month_rate = insertValues['month_rate']
                like_count = insertValues['like_count']
                reply = insertValues['reply']
                reviewer_rank = insertValues['reviewer_rank']

                input = np.array([[content_length, photos_count, content_positive,
                                 content_negative, star_gap, month_rate, like_count, reply, reviewer_rank]])
                result = model.predict(input)

            predictArr.append({'index': str(index), 'predict': str(result)})

    return jsonify(predictArr)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=False)
