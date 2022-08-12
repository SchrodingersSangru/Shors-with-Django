# Create your views here.

import numbers
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
import json
import time as time

from qiskit import IBMQ
from qiskit.utils import QuantumInstance
from qiskit.algorithms import Shor
from qiskit.tools.monitor import job_monitor

from django.views import View
from .models import FactorModel
from shors.forms import FactorForm

import environ

env = environ.Env(
    # set casting, default value
    DEBUG=( bool , False)
)

environ.Env.read_env()

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/


# SECURITY WARNING: keep the secret key used in production secret!


# Create your models here.


class FactorizationView(View):
    
    template_name = "shors/home.html"
    form_class = FactorForm
    
    def get(self, request, *args, **kwargs):
        form = self.form_class
        return render(request, self.template_name, {'form': form})
    
    def post(self, request, *args, **kwargs):
        
        form = self.form_class(request.POST)
        # form_data = request.POST
        if form.is_valid():
            
            form_data = form.cleaned_data
            # API_key = form_data['API_key']
            Number =  form_data['Number']
            device = form_data['devices']
            # form.save()
            print("number to factorise is ", Number)
        
        
        
        # API_key = (f" '{API_key}' ")
        # API_key.value_to_string
        # print("API key is ", API_key )
        
    
        print("Account enabled ...")
        API_key = 'ee0757e41299179fb8fd3aab7236e79a12eda6a41c2e860c72fcb9a16274068b3f7c86a6b03428677bd874cfd2a41d90794800294648da41d0141a24dce55ce8'
        # API_key = env('API_key')
        # # print(API_key)
        IBMQ.enable_account(API_key)
        provider = IBMQ.get_provider(hub='ibm-q')

                
        backend = provider.get_backend(device)
        print("backend is ", backend)
        t1 = time.time()
        factors = Shor(QuantumInstance(backend, shots=100, skip_qobj_validation=False)) #Function to run Shor's algorithm where 21 is the integer to be factored
        
        result_dict = factors.factor(N=Number, a=2)
        result = result_dict.factors
        t2 = time.time()
        tot_time = t2-t1
        
        print("total time taken to factorize " + str(Number) + " is  in Seconds ", tot_time)

        response = JsonResponse({'result': str(result)})
        # response = dict({'result': str(result)})
        save_data = FactorModel.objects.create(Number = Number, time=tot_time)
        # print("save data ", save_data)
        # form.save(save_data)
        
        
        # output = {'response': str(result), 'time': tot_time}
        print("factors of " + str(Number) + " are ", str(result))
        return response
    
        # return HttpResponse( json.dumps( output ) )
        # return render(request, self.template_name, response)
    
        # render('your_template.html', {'data': json_dict}). Then you use data
        # response = HttpResponse({'result': str(result)})
        # print("factors of the number", response)
        # return render(request, 'shors/output.html', response)
    
