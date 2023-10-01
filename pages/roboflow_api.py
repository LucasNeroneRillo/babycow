from roboflow import Roboflow
from decouple import config

rf = Roboflow(api_key=config("API_KEY"))
project = rf.workspace().project("cow-birth-monitoe-r")
model = project.version(2).model

# infer on a local image
# print(model.predict("giving_birth.jpeg").json())
# print(model.predict("not_giving_birth.jpeg").json())