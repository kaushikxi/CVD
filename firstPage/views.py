from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt,csrf_protect
import pandas as pd
import joblib
import pickle
import numpy as np
import json


# Create your views here.

# with open('./Trainedmodel/model_pickle','rb') as f:
#     reloadModel = pickle.load(f)

reloadModel1 = joblib.load("./Trainedmodel/LogisticRegression.pkl")
# reloadModel2 = joblib.load("./Trainedmodel/HRFLM2.pkl")
# reloadModel3 = joblib.load("./Trainedmodel/HRFLM3.pkl")
# reloadModel4 = joblib.load("./Trainedmodel/HRFLM4.pkl")
# reloadModel5 = joblib.load("./Trainedmodel/HRFLM5.pkl")



def index(request):
    return render(request,'index.html')

@csrf_exempt
def predictdisease(request):
    if request.method == "POST":
      post_data = json.loads(request.body.decode("utf-8"))
      print(post_data.get('age'))
    #   print(post_data.get('trestbps'))

      age = int(post_data.get('age'))
      trestbps = int(post_data.get("trestbps"))
      chol = int(post_data.get("chol"))
      thalch = int(post_data.get("thalch"))
      gender0 = int(post_data.get("gender0"))
      gender1 = int(post_data.get("gender1"))
      cp0 = int(post_data.get("cp0"))
      cp1 = int(post_data.get("cp1"))
      cp2 = int(post_data.get("cp2"))
      cp3 = int(post_data.get("cp3"))
      fbs0 = int(post_data.get("fbs0"))
      fbs1 = int(post_data.get("fbs1"))
      restecg0 = int(post_data.get("restecg0"))
      restecg1 = int(post_data.get("restecg1"))
      restecg2 = int(post_data.get("restecg2"))
      ca0 = int(post_data.get("ca0"))
      ca1 = int(post_data.get("ca1"))
      ca2 = int(post_data.get("ca2"))
      ca3 = int(post_data.get("ca3"))
      ca4 = int(post_data.get("ca4"))
     
      X = np.asarray([[ age, trestbps, chol, thalch, gender0, gender1, cp0, cp1, cp2, cp3, fbs0, fbs1, restecg0, restecg1, restecg2, ca0, ca1, ca2, ca3, ca4 ]])
      print(X)
      scoreval = reloadModel1.predict(X)
      return HttpResponse(scoreval, content_type='text/plain')
        


