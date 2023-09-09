from django.db import models
from django.db.models import Q
# we can perform and( Q(condition)  & Q(condition) ), or( Q(condition) | Q(condition) ), negation( ~Q(condition) )
# Create your models here.

class FirstModelQuerySet(models.QuerySet):
    def search(self, query=None):
        if query is None or query == '':
            return self.none() # [] it will return empty list
        lookups = Q(title__icontains=query) | Q(content__icontains=query)
        if query.isnumeric():  # we can search using ID and Title
            id = int(query)
            lookups = lookups | Q(id=id)
            data_list = self.filter(lookups)
        else:
            data_list = self.filter(lookups)
        return data_list

class FirstModelManager(models.Manager): # , models.QuerySet):
    # over writing method Here
    def get_queryset(self):
        return FirstModelQuerySet(self.model, using=self._db)
        # return models.QuerySet(self.model, using=self._db)  # Dose this will work test that also

    def search(self, query=None):
        return self.get_queryset().search(query)

class FirstModel(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=120)
    content = models.TextField()
    publish = models.DateField(null=True, blank=True) # Default IS : auto_now_add=False auto_now=False
    # null=True : DB will Accept Null value
    # blank=True : in Django-model-form it will accept as Blank fild
    # so Django migration will not as for default values
    created = models.DateTimeField(auto_now_add=True) # Update when data is added
    updated = models.DateTimeField(auto_now=True) # Update when any changes are made.
    # adding abow fild require default value : Django also ask 2 options when we migrate
    # 1. While Doing Migrations it will ask to set default
    # 2. We have to specify Default value in fild while creating migrations.
    slug = models.SlugField(null=True, blank=True)

    objects = FirstModelManager()
    """
        # we can rename ModelManager Name
        # we can have multiple ModelManager for one model
        # Here we have inherited Model.QuerySet so all methods of QuerySet all will we will get
    """

    def query_set_methods(self):
        get_single_value = FirstModel.objects.get(id=1)  # error if not exist , it returns object not query set
        get_list_values = FirstModel.objects.filter(title='Hello World')  # did not give an error , it returns Query Set
        get_exclude_list_values = FirstModel.objects.exclude(title='Hello World')  # did not give an error
        get_ordered_list_values = FirstModel.objects.exclude(title='Hello World').order_by('title')
        """
            # order_by('title') : Ascending order
            # order_by('-title') : Descending order
            # order_by('?') : Random order
            # order in A to Z, a to z 
        """
        get_reversed_list_values = FirstModel.objects.filter(title__icontains='hello').order_by('id').reverse()  # only work well with order_by query set values
        get_selected_columns_dict_values = FirstModel.objects.filter(title='Hello World').values('title', 'content')  # it returns rows in Dict Formate
        # get_distinct_list_values : find example
        get_selected_columns_list_values = FirstModel.objects.filter(title='Hello World').values_list('title', 'content', named=False, flat=False)  # it will return tuple
        """
            # named == True :  it will return tuple of row with name to each column 
        """


        db_select_get_values = FirstModel.objects.using('default')  # if we have mulitple db connected and from which db we want to get values.
        get_distinct_date = FirstModel.objects.dates('created', 'year', order='DESC')  # default is order='ASC'
        """
            # it will return dates only, and work only for DateFiled 
            # year : list of (years, 1, 1)
            # months : list of combination of (years, month, 1) 
            # week : list of combination of (years, month, date)  # all dates will be monday
            # day : list of combination of (years, month, date) 
        """
        get_distinct_datetime = FirstModel.objects.datetimes('created', 'year', order='DESC', tzinfo=None)  # default is order='ASC'
        """
            # it will return dates only, and work only for DateFiled 
            # year : list of (years, 1, 1)
            # months : list of combination of (years, month, 1) 
            # week : list of combination of (years, month, date)  # all dates will be monday
            # day : list of combination of (years, month, date) 
            
            # tzinfo : None Then django will use current time zone  ???
        """
        get_empty_query_set = FirstModel.objects.none()


        qs1 = FirstModel.objects.filter(title='Hello World').values_list('title', 'content', named=True)
        qs2 = FirstModel.objects.filter(title='jaimin').values_list('title', 'content', named=True)
        # Union
        get_distinct_union_values = qs1.union(qs2)
        get_all_union_values = qs1.union(qs2, all=True)

        # intersection
        get_intersection_values = qs1.intersection(qs2)  # values witch are common in both query

        # difference
        get_qs1_diff = qs1.difference(qs2) # qs1.values - qs2.values
        get_qs2_diff = qs2.difference(qs1) # qs2.values - qs1.values

        """
            # if we will take id in values_list('id', 'title', named=True)
            # then title are same but id are not same then also it will not consider as Union duplicate, 
            intersected value, difference in qs
        """

    def query_set_not_seen_methods(self):
        """
        below methods are used in query optimization in djagno
        """
        select_related(*fields)
        difer(*fields)
        only(*fields)
        prefetch_related(*lookups)
        extra(select=None, where=None, params=None, tables=None, order_by=None, select_params=None)
        select_for_update(nowait=False, skip_locked=False, of=())
        raw(raw_query, params=None, translation=None)
        annotate(*args, **kwargs)

    def other_query_set_methods(self):
        get_first_row = FirstModel.objects.filter(title='Hello World').first()
        get_last_row = FirstModel.objects.filter(title='Hello World').last()
        get_latest_row = FirstModel.objects.latest('created')  # based on date
        get_earliest_row = FirstModel.objects.earliest('created')  # based on date

    def crud_query_set_metods(self):
        fm = FirstModel(title='New Jaimin', content='new life of jaimin')
        fm.save()  # this helps when before adding data in db we have some changes to made

        fm = FirstModel.objects.create(title='New Jaimin', content='new life of jaimin')
        # it will directly create entry in database

        fm, created = FirstModel.objects.get_or_create(title='New Jaimin', content='new life of jaimin')
        # created 1st time then flag 'created' will return True, otherwise false
        # fm will return data

        fm = FirstModel.objects.filter(id=14).update(title="Jaimin's Birthday")
        # fm return number of rows are updated

        fm, created = FirstModel.objects.update_or_create(title='New Jaimin', content='new life of jaimin',
                                                          defaults={'title':'New Jaimin'})
        # if title New Jaimin will be there it will not update tile but will update content otherwise, create new row
        # always give require values in defaults or in parameters

        # BULK CREATE
        objs = [
            FirstModel(title='first', content='first content'),
            FirstModel(title='second', content='second content'),
            FirstModel(title='third', content='third content'),
        ]
        bulk_create_fm = FirstModel.objects.bulk_create(objs, batch_size=None, ignore_conflicts=False)
        """
            # save() method and pre_save and post_save signals will not call
            # dose not work with 1. child model (inheritance model) 2. many to many relation 
        """

        # BULK UPDATE
        qs = FirstModel.objects.filter(title='jaimin')
        qs.title = 'MrJemmy'
        bulk_update_fm = FirstModel.objects.bulk_update(qs, ['title'], batch_size=None)
        """
            # can not update primary key
            # save() method and pre_save and post_save signals will not call
            # updating large number of columns in large number of row generate BIG query, avoid setting 'batch_size'
            # if duplicates are there only 1st one will be updated 
        """

        # BULK GET
        id_list = [1, 3, 5]
        bulk_get_fm = FirstModel.objects.in_bulk(id_list, field_name='pk') # Default value field_name='pk'
        bulk_get_fm = FirstModel.objects.in_bulk([])  # will return empty DICT
        bulk_get_fm = FirstModel.objects.in_bulk()  # will return all value in dict form
        """
            bulk_get_fm = {
                1 : QueryObject<1>,
                2 : QueryObject<2>,
                3 : QueryObject<3>
            }
            # to access data "bulk_get_fm[0].title"
            
            # only works with PK or uniq column find more about that.
        """

        # DELETE
        delete_data = FirstModel.objects.filter(title='Hello World').delete()
        # it will delete in bulk and single both way

        # count
        qs = FirstModel.objects.filter(title='Hello World')
        data_count = qs.count()

        # explain(format=None, **options) : how query will execute, this detail may help improve query performance.
        qs = FirstModel.objects.filter(title='Hello World').explain()

    def other_not_seen_query_set_methods(self):
        aggregate(*args, **kwargs)
        as_manager()
        iterator(chunk_size=2000)

    def aggregate_in_query_set(self):
        from django.db.models.aggregates import Avg, Sum, Min, Max, Count, StdDev, Variance
        opration_result = FirstModel.objects.all().aggregate(Max('FieldName') - Min(FieldName))  # we can perfrom oprations like this here
        # check out "django model aggregate" documentation
        # ADVANCE : StdDev, Variance and found others

    def fild_lookups_methods(self):
        get_less_then_list_values = FirstModel.objects.filter(id__lt=10)
        get_less_then_or_equal_to_list_values = FirstModel.objects.filter(id__lte=10)
        get_greater_then_list_values = FirstModel.objects.filter(id__gt=10)
        get_greater_then_or_equal_to_list_values = FirstModel.objects.filter(id__gte=10)

        get_case_sensitive_start_with_list_value = FirstModel.objects.filter(title__startswith='Hello')
        get_case_insensitive_start_with_list_value = FirstModel.objects.filter(title__istartswith='Hello')
        get_case_sensitive_ends_with_list_value = FirstModel.objects.filter(title__endswith='World')
        get_case_insensitive_end_with_list_value = FirstModel.objects.filter(title__iendswith='World')

        get_case_insensitive_list_values = FirstModel.objects.filter(title__iexact='Hello World')
        get_case_sensitive_list_values = FirstModel.objects.filter(title__exact='Hello World')
        get_case_insensitive_contains_list_values = FirstModel.objects.filter(title__icontains='hello')
        get_case_sensitive_contains_list_values = FirstModel.objects.filter(title__contains='hello')

        get_using_in_list_values = FirstModel.objects.filter(title__in=['hello', 'jaimin', 'world'])

        get_in_range_list_values = FirstModel.objects.filter(created__range=('2022-04-01','2023-03-31')) # works with only DateTimeField only TEST it
        get_in_range_list_values = FirstModel.objects.filter(id__range=(10,14)) # also char can be used

        get_using_date_list_values = FirstModel.objects.filter(created__date=date('2023-03-31'))
        get_using_date_list_values = FirstModel.objects.filter(created__date__gt=date('2023-03-31')) # we can use gt, gte, lt, lte

        get_using_year_list_values = FirstModel.objects.filter(created__year=2023)
        get_using_year_list_values = FirstModel.objects.filter(created__year__gte=2022)  # we can use gt, gte, lt, lte
        """
            from datetime import date, time
            # __month, __day, __week, __week_day, __quarter, __time, __hour, __minute, __second
            # __week : passing week number (1-52 or 53) according to ISO-8601
            # __week_day : passing day number (1[sunday] - 7[saturday])
            # __quarter : quarter number (1 to 4)
            # __time : passing in time(6,00) methods    time(6,00) == 6:00:00 o'clock
            
            -> __month, __day, __week, __week_day __quarter works on both DateField and DateTimeField
            -> __time, __hour, __minute, __second works on only DateTimeField
        """

        get_null_list_values = FirstModel.objects.filter(publish__isnull=True)

        """
            FIND more
            # regex 
            # iregex
        """



"""
    ## Model Inheritance ##
        # Abstract Base Class
        # Multi-table Inheritance
        # Proxy Models
"""

# Abstract Base Class
class CommonColumns(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    deleted = models.DateTimeField()
    class Meta:
        abstract = True  # TABLE will not be created for this MODEL

class Model1(CommonColumns):
    name = models.CharField(max_length=200)
    updated = None # this columns will not be created
    deleted = models.DateField() # we can overwrite columns

    # this model will inherit all columns of abstract class
    """
        # meta class also will be inherited 
        # but Django will Make abstract False for us
        # other then that other meta values will remain same
    """

# Multi-table Inheritance
class MyTableOne(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    deleted = models.DateTimeField()

class Modle2(MyTableOne):
    name = models.CharField(max_length=200)

    """
        # one to one relation will be form between them
        # Inserted data in MyTableOne also will be visible in Modle2 and vice versa also True
        # USING Modle2 we can access MyTableOne also 
    """


# Proxy Models
class ProxyFirstModel(FirstModel):
    class Meta:
        proxy = True
        ordering = ['title']
    """
        # this Model is same as FirstModel, TABLE will not be created for this model
        # we can have diff manger for This MODEL 
        # we can make few changes in Proxy model Behaviour 
        # also methods can be diff for Proxy Model
        # it can be created using only 'single Non Abstract model', can not use multiple Non Abstract model.
        # proxy can have can be made using Multiple Abstract model class 
        # we can integrate other proxy model that shared common Non Abstract model
    """
    def proxyMethod(self):
        return self.title


## ONE-to-ONE relationship
"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, parent_link=False, **optional)  # parent_link=False : Default
        # we can make user OneToOneField filed as primary_key=True
        # parent_link = True : with this in child all the columns will be inherited, may now visible in table 
        # limit_choices_to = {'column_name' : True}   : if column_name has value True then only it can make relation
        # related_name ? , related_query_name ?, to_field ?, swappable ?, db_constraint ? ,
        
    ## on_delete
        CASCADE : also delete child if parent get deleted 
        PROTECT : try to delete parent and still child is exist it will throw an error 
        SET_NULL : parent get deleted child will set NULL in reference 
        SET_DEFAULT : parent get deleted child will set DEFAULT value in reference
        SET() : parent get deleted, we can set value in child using SET()
        DO_NOTHING : parent get deleted, in child everything will remain same
        
    ## reverse_relation using post_delete signal
        from .models import ModelName
        from django.db.models.signals import post_delete
        from django.dispatch import receiver
        @receiver(post_delete, sender=ModelName)
        def delete_related_user(sender, instance, **kwargs):
            instance.user.delete()
            # we can here perform other operations also 
            
            
        -> go in apps.py file in APP to config signal 
        class AppnameConfig(AppConfig):
            name = 'Appname'
            def ready(self):
                import Appname.signal_file
        -> go in __init__.py file in APP and set variable 
            default_app_config = 'Appname.apps.AppnameConfig'  # AppnameConfig class name in apps.py
        
"""

## ONE-to-MANY relationship
"""
    user = models.ForeignKey(User, on_delete=models.SET_NULL)
        # limit_choices_to = {'column_name' : True}   : if column_name has value True then only it can make relation
        # related_name ? , related_query_name ?, to_field ?, swappable ?, db_constraint ? ,
        
    ## reverse_relation using post_delete signal can be implemented 
"""

## MANY-to-MANY relationship
"""
    user = models.ManyToMany(User) # on_delete=models.PROTECT
        # related_name ? , related_query_name ?,
        
        -> one extra table will be created with name model2_user
        -> to get one to many users
        def all_users(self):
            return ','.join([str(user) for user in self.user.all()])
            # here user will be object of UserModel and str will return username fild
            # for other model we will have to overwrite to_string method 
            # we can use 'all_users' as column name
            # like this method also can be writen in User Model
            
        -> for ADV thing search in documentation.
"""
