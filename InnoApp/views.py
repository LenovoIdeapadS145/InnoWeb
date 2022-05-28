from django.shortcuts import render, HttpResponse
from .models import New_Feedback, New_Model
from .forms import New_Form, New_Form1, New_Form2
import wikipedia

def Index(request):
    Output = ""
    if request.method == "POST":
        try:
            Search = request.POST["Search"]
            Output = wikipedia.summary(Search)
        except:
            wiki = New_Model.objects.all()
            for i in wiki:
                if i.Word == Search:
                    Output = i.Content
                else:
                    return HttpResponse("Please enter a valid Value")
            
        return render(request, "InnoApp/Index.html", {"Output":Output})
        
    return render(request, "InnoApp/Index.html")

def Create(request):
    if request.method == "POST":
        form = New_Form1(request.POST)
        form.save()
    form = New_Form1()
    return render(request, "InnoApp/Create.html")

def Feedback(request):
    if request.method == "POST":
        form = New_Form2(request.POST)
        form.save()
    form = New_Form2()
    return render(request, "InnoApp/Feedback.html")