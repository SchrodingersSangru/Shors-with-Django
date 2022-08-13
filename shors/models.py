from datetime import datetime
from django.db import models
import datetime
# Create your models here.
class FactorModel(models.Model):
    ## took the number as a input to the fields
    
    Number = models.IntegerField()
    
    ## device choices
    device_choices =(
    ("ibmq_qasm_simulator", "ibmq_qasm_simulator"),
    ("ibmq_16_melbourne", "ibmq_16_melbourne"),
    ("ibmq_vigo", "ibmq_vigo"),
    ("ibmq_santiago", "ibmq_santiago"),
    ("ibmq_armonk", "ibmq_armonk"),
)
    
    
  
    devices = models.CharField(choices = device_choices, default = 'ibmq_qasm_simulator', max_length= 50)
    time = models.CharField(max_length= 50)
    created_at = models.DateTimeField(default= datetime.datetime.now)
    

    # def save(self, *args, **kwargs):
    #     self.computed = self.time
    #     super(FactorModel, self).save(*args, **kwargs)
    
    
    class Meta:
        db_table = "Shors_data"