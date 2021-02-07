from django.db import models
# Create your models here.


class EV(models.Model):
    site_name = models.CharField(max_length=100)
    url = models.URLField('Site URL')

    def __str__(self):
        return "이름 : "+self.site_name+", 주소 : "+self.url

class EVUserRegister(models.Model):
    user_id = models.CharField(max_length=50)
    user_pwd = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50)

    def __str__(self):
        return self.user_id + " , " + self.user_pwd + " , " + self.user_name
