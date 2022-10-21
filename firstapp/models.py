from django.db import models
from firstapp.othermodels.testmodel import SecondModel

# Create your models here.
class FirstModel(models.Model):
    title = models.TextField()
    content = models.TextField()

# After "python manage.py shell"
# from AppName.models import ModelName

# ========== To Assign Data In Table ========== #
# obj1 = ModelName.object.create(var1="value1",var2="value2")
# obj1.save()

# obj2 = ModelName()
# obj2.var1 = 'value1'
# obj2.var2 = 'value2'
# obj2.save()

# ========== To Access Data To use ========== #
# obj3 = ModelName.object.get(id=1)
# data1 = obj3.var1
# data2 = obj3.var2
# ========== To Update Data To use ========== #
# obj3 = ModelName.object.get(pk=1)  where pk == primary key
# obj3.var1 = 'newValue1'
# obj3.var2 = 'newValue2'
