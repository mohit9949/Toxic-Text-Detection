from django.shortcuts import render
from . import model_prediction
def home(request):
    return render(request,"index.html")
def result(request):
    user_text=request.GET['user_text']
    result=model_prediction.get_prediction(user_text)
    return render(request,"result.html",{'model_result':result,'utext':user_text})
