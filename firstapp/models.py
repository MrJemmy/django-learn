from django.db import models
from django.urls import reverse
from django.db.models.signals import pre_save, post_save  # Diff type of signals are there in Django Learn more.
from firstapp.othermodels.testmodel import SecondModel
from .utils import slugify_instance_title

# Create your models here.
# ALTER TABLE firstapp_firstmodel
# MODIFY COLUMN slug VARCHAR(255) COLLATE utf8mb4_bin;
class FirstModel(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    publish = models.DateField(null=True, blank=True) # Default IS : auto_now_add=False auto_now=False
    # null=True : DB will Accept Null value
    # blank=True : in Django-model-form it will accept as Blank fild
    # so Django migration will not as for default values
    created_at = models.DateTimeField(auto_now_add=True) # Update when data is added
    updated_at = models.DateTimeField(auto_now=True) # Update when any changes are made.
    # adding abow fild require default value : Django also ask 2 options when we migrate
    # 1. While Doing Migrations it will ask to set default
    # 2. We have to specify Default value in fild while creating migrations.
    slug = models.SlugField(null=True, blank=True)

    # def save(self, *args, **kwargs):  # force_insert=False, force_update=False, using=None, update_fields=None -> Learn More
        # if self.slug is None:
        #     # only slugify when slug is None
        #     self.slug = slugify(self.title)
        # super().save(*args, **kwargs)
        # we avoid to use self.save(), it will crate infinite self loop if we have now used proper conditions.

    def get_absolute_url(self):
        # This is use of URLs Reverse :- it is 'name' param which we are give  in urls.py to PATH
        # with help of this we can se this to anywhere in project
        # return f'{/user/{self.slug}/}'
        return reverse("user-slug", kwargs={'slug': self.slug})  # kwargs are directly map with dynamic_url

def firstmodel_pre_save(sender, instance, *args, **kwargs):
    print('pre_save')  # print(args, kwargs) : to get more info
    print(sender,',' ,instance)
    if instance.slug is None:
        # only slugify when slug is None
        instance = slugify_instance_title(instance)
pre_save.connect(firstmodel_pre_save, sender=FirstModel)  # There is also decorator do same thing.
# when ever any FirstModel's Data will be saved before that 'firstmodel_pre_save' will run.

def firstmodel_post_save(sender, instance, created, *args, **kwargs):
    print('post_save')  # print(args, kwargs) : to get more info
    print(sender, ',', instance)
    if created:
        print('actual created slug value :', instance.slug)
        instance = slugify_instance_title(instance)
        instance.save()  # here also infinite loop can be created if we do not have flag like created
post_save.connect(firstmodel_post_save, sender=FirstModel)  # There is also decorator do same thing.
# when ever any FirstModel's Data will be saved after that 'firstmodel_post_save' will run.

# pre_save and post_save calls each other, so it will be in loops try to use care fully
# try to avoid instance.save() in post_save

# # ================================================================================================================ # #
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

# # ================================================================================================================ # #
# After "python manage.py shell"
# from AppName.models import ModelName

# single_value = ModelName.object.get(id=1) # it returns only one value
    # it gives an error when data is not exist of more then one vales are there.
# list_values = ModelName.object.filter(name='jaimin') # it returns only one value
    # it did not give an error
    # __iexact
    # ModelName.object.filter(name__iexact='jaimin')  # 'i' will make it case-insensitive
    # __exact
    # ModelName.object.filter(name__exact='jaimin')  # it find exact results
    # __icontains
    # it contains jaimin in any name with case-insensitive
    # __contains
    # it contains jaimin in any name with case sensitive

# use qs.count() insted of len(qs) which is much faster