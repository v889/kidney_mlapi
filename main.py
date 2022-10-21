

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pickle
import json


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class model_input(BaseModel):
    sg:float
    al:float
    sc:float
    hemo:float
    pcv: float
    htn: int



# loading the saved model
model = pickle.load(open('kidney.sav', 'rb'))


@app.post('/kidney_prediction')
def diabetes_pred(input_parameters: model_input):
    input_data = input_parameters.json()
    input_dictionary = json.loads(input_data)

    sg = input_dictionary['sg']
    al= input_dictionary['al']
    sc= input_dictionary['sc']
    hemo= input_dictionary['hemo']
    pcv= input_dictionary['pcv']
    htn= input_dictionary['htn']

    input_list = [sg,al,sc,hemo,pcv,htn]

    prediction =model.predict([input_list])

    if prediction[0] == 0:
        return 'The person have kidney disease'

    else:
        return 'The person is healthy'


