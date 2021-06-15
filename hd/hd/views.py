import pickle
from pathlib import Path 
from django.shortcuts import redirect, render

file_dir = Path(__file__).resolve().parent.parent

def home(request):
    return render(request, 'index.html')

def cancer(request):
    return render(request, 'cancer.html')

def diabets(request):
    return render(request, 'diabets.html')

def lr_prediction(request):
    load_model = pickle.load(open(str(file_dir) + "//models/heart_final_model", 'rb'))

    age = float(request.POST['age'])
    sex = float(request.POST['sex']) 
    cp =  float(request.POST['cp'])
    trestbps = float(request.POST['trestbps'])
    chol = float(request.POST['chol'])
    fbs = float(request.POST['fbs'])
    restecg = float(request.POST['restecg'])
    thalach = float(request.POST['thalach'])
    exang = float(request.POST['exang'])
    oldpeak = float(request.POST['oldpeak'])
    slope = float(request.POST['slope'])
    ca = float(request.POST['ca'])
    thal = float(request.POST['thal']) 

    res = load_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])

    if res == 0:
        res_mes = 'Congratulations you dont have Heart Disease '
    else:
        res_mes = 'Sorry you have Heart Disease'
    return render(request, 'index.html', {'res_sms':res_mes})


def diabets_prediction(request):

    load_model = pickle.load(open(str(file_dir)+"//models/diabets_final_model", 'rb'))

    num_preg = float(request.POST['num_preg'])
    glucose_conc = float(request.POST['glucose_conc'])
    diastolic_bp = float(request.POST['diastolic_bp'])
    insulin = float(request.POST['insulin'])
    bmi = float(request.POST['bmi'])
    diab_pred = float(request.POST['diab_pred'])
    age = float(request.POST['age'])
    skin = float(request.POST['skin'])

    res = load_model.predict([[num_preg, glucose_conc, diastolic_bp, insulin, bmi, diab_pred, age, skin]])

    if res == 0:
        res_mes = 'Congratulations you dont have Diabets'
    else:
        res_mes = 'Sorry you have Diabets'

    return render(request, 'diabets.html', {'res_sms':res_mes})