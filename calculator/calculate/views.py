from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    result = ''
    if request.POST :
        txt_field = request.POST.get('display','')
        operation = request.POST.get('operation')
        if operation == '=':
            try:
                result = eval(txt_field)
            except:
                result = 'Error'
        elif operation == 'clear':
            result = ' '
        elif operation == 'del':
            result=txt_field[:-1]
        else :
            result = txt_field+operation
        
    return render(request,'calc.html',{'result':result})