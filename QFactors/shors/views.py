# Create your views here.

import numbers
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
import json

from qiskit import IBMQ
from qiskit.utils import QuantumInstance
from qiskit.algorithms import Shor
from qiskit.tools.monitor import job_monitor

from django.views import View
from shors.forms import ChoiceForms

# Create your models here.

def home(request):
    return render(request, 'home.html', {})


class FactorizationView(View):
    
    template_name = "shors/home.html"
    form_class = ChoiceForms
    
    def get(self, request, *args, **kwargs):
        form = self.form_class
        return render(request, self.template_name, {'form': form})
    
    def post(self, request, *args, **kwargs):
        
        form_data = self.form_class(request.POST)
        # form_data = request.POST
        if form_data.is_valid():
            
            form_data = form_data.cleaned_data
            # API_key = form_data['API_key']
            Number =  form_data['Number']
            device = form_data['devices']
            
            print("number to factorise is ", Number)
        
        
        # API_key = str(API_key)
        # print("API key is ", )
        API_key = (f" '{API_key}' ")
        
        print("API key is ", API_key )
        
        
        # IBMQ.enable_account(API_key)
        # IBMQ.load_account(API_key, 'https://auth.quantum-computing.ibm.com/api)
        print("Account enabled ...")
        
        # # print(API_key)
        IBMQ.enable_account('Your_API_key')
        provider = IBMQ.get_provider(hub='ibm-q')

                
        backend = provider.get_backend(device)
        print("backed is ", backend)

        factors = Shor(QuantumInstance(backend, shots=100, skip_qobj_validation=False)) #Function to run Shor's algorithm where 21 is the integer to be factored

        result_dict = factors.factor(N=Number, a=2)
        result = result_dict.factors

        # response = JsonResponse({'result': str(result)})
        # response = dict({'result': str(result)})
        print("factors of " + str(Number) + " are ", str(result ))
        # return response
        # return render(request, self.template_name, response)
    
        # render('your_template.html', {'data': json_dict}). Then you use data
        response = HttpResponse({'result': str(result)})
        # print("factors of the number", response)
        return render(request, 'shors/output.html', response)
    
    