from django.shortcuts import render,redirect
import pyttsx3
# Create your views here.
from django.shortcuts import render,HttpResponse
from translate import Translator
# Create your views here.
  
def home(request):
    if request.method == "POST":
        text = request.POST["translate"]
        language = request.POST["language"]
        translator= Translator(to_lang=language)
        translation = translator.translate(text)
        return HttpResponse(translation)
    return render(request,"call.html")

def some(request):
    value= request.GET["inp"]
    obj=pyttsx3.init()
    obj.say(value)
    obj.runAndWait()
    return redirect('/')