from django.db import models

# Create your models here.
from datetime import datetime 



class SC(models.Model):
    question_text=models.CharField(max_length=500) #(max_length=500) # Soru cevap
    pub_date=models.DateTimeField(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    

    answer=models.CharField(max_length=500)
    def __str__(self):
        return "{} tarihli soru: {} || Cevabi:{}".format(self.pub_date,self.question_text,self.answer)

class Urun(models.Model):
    product_name=models.CharField(max_length=20)#urun kodu RVS63 Vb.
    urun_durumu=models.BooleanField(default=1)#guncel aktif olarak support destegi var mi ?
    urun_satisi=models.BooleanField(default=1)#satis yapilabilir
    def __str__(self):
        return "{} ismi, urun durumu {}, satis durumu".format(self.product_name,self.urun_durumu,self.urun_satisi)
