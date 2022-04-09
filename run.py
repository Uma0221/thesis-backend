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

    insertValuesArr = np.array([[0, 0, 0, 0.6, 0, False, 0],[-1,4,2],[1, 0, 0, 0.6, 0, False, 0],[],[2,3],[10],[-2],[3,5,4,0,2,3,9,1,8]])
    for insertValues in insertValuesArr:
        if(len(insertValues)>0 and insertValues[0]>=0 and insertValues[0]<=9):
            if(len(insertValues)!=7):
                index = insertValues[0]
                result = -1

            else:
                index = insertValues[0]
                x1=insertValues[1]
                x2=insertValues[2]
                x3=insertValues[3]
                x4=insertValues[4]
                x5=insertValues[5]
                x6=insertValues[6]

                input = np.array([[x1, x2, x3, x4, x5, x6]])
                result = model.predict(input)
        
            predictArr.append({'index': str(index),'predict': str(result)})

    return jsonify(predictArr)

@app.route('/predict', methods=['POST'])
def postInput():
    predictArr = []
    # 取得前端傳過來的數值
    insertValuesArr = request.get_json()
    for insertValues in insertValuesArr:
        if(len(insertValues)>0 and insertValues[0]>=0 and insertValues[0]<=9):
            if(len(insertValues)!=7):
                index = insertValues['index']
                result = -1
            else:
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