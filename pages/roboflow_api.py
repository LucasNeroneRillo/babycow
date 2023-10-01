from roboflow import Roboflow
from decouple import config
import random

def predict_image(filename):
    #return True if random.getrandbits(1) == 1 else False
    rf = Roboflow(api_key=config("API_KEY"))
    project = rf.workspace().project("cow-birth-monitoe-r")
    model = project.version(2).model
    result = model.predict(filename).json()
    predictions = result["predictions"][0]["predictions"]
    giving_birth = predictions["Cow Giving Birth"]["confidence"]
    print(predictions)
    #not_giving_birth = predictions["Cow Not Giving Birth"]["confidence"]
    return giving_birth > .94
