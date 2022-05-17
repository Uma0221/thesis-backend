import pickle

with open('./model/model.pickle', 'rb') as f:
    readModel = pickle.load(f)


def predict(input):
    pred = readModel.predict(input)[0]
    return pred
