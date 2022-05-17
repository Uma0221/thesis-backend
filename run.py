import model
import numpy as np

from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

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
            elif(insertValues['photos_count'] > 0):
                index = insertValues['index']
                result = 7
            else:
                index = insertValues['index']
                content_length = np.log2(insertValues['content_length']+1)/10
                star = (insertValues["star"]-1)/4
                month = insertValues["month"]/11
                month_rate = insertValues['month_rate']
                like_count = np.log2(insertValues["like_count"]+1)/5
                reviewer_rank = insertValues["reviewer_rank"]/10
                content_compare = abs(insertValues["content_positive"]-insertValues["content_negative"])

                input = np.array([[content_length, star, month, month_rate, like_count, reviewer_rank, content_compare]])
                result = model.predict(input)

            predictArr.append({'index': str(index), 'predict': str(result)})

    return jsonify(predictArr)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=False)
