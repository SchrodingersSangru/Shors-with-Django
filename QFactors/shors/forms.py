from django import forms

device_choices =(
    ("ibmq_qasm_simulator", "ibmq_qasm_simulator"),
    ("ibmq_bogota", "ibmq_bogota"),
    ("ibmq_manila", "ibmq_manila"),
    ("ibmq_santiago", "ibmq_santiago"),
    ("ibmq_quito", "ibmq_quito"),
)
  
  
class ChoiceForms(forms.Form):
    # API_key = forms.CharField(max_length= 200)
    Number = forms.IntegerField() #max_length = 4, required=False)
    devices = forms.ChoiceField(choices = device_choices)