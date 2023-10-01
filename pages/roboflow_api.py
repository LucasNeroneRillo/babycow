from roboflow import Roboflow
from decouple import config


def predict_image(filename):
    rf = Roboflow(api_key=config("API_KEY"))
    project = rf.workspace().project("cow-birth-monitoe-r")
    model = project.version(2).model
    result = model.predict(filename).json()
    return result
