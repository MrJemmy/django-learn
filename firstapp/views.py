from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import FirstModel
from .forms import firstappForm, firstappModelForm

# Create your views here.
def show_data(request, id=None):  # id must be hendeled here

    show_in_html = True
    if id is not None:
        try:
            # model_row = FirstModel.objects.filter(id=id).first()
            model_row = FirstModel.objects.get(id=id)
        except:
            model_row = None
        show_in_html = False  # when to show ???
    else:
        query_dict = request.GET

        show_mata_data = False
        if show_mata_data:  # make True When you want to see
            print("===========================================")
            print(request)  # It shows 'WAGIRequest' class and Method
            print(dir(request))  # It will show all diff and various properties  of class
            print(query_dict)  # It will show class 'QueryDict' and 'key : value' passed in urls
            print("===========================================")

        # what if search is done using ID ??? how to handle that
        query = query_dict.get("query")  # <input type="text" name="query"/> # all ways we get string so for 'int' do type conversion
        if query is not None:
            try: # try except is temp solution
                if query.isnumeric():  # we can search using ID and Title
                    id = int(query)
                    model_row = FirstModel.objects.get(id=id)
                else:
                    # Here Filters return List of Values and get return only one values
                    # model_row = FirstModel.objects.filter(title=query)
                    model_row = FirstModel.objects.get(title=query)
            except:
                model_row = None
        else:
            model_row = None

    context = {
        'model_row' : model_row,
        'show' : show_in_html
    }
    return render(request, "firstapp/detail.html", context=context) # it will combine two steps

    # both are same
    # HttpResponse(render_to_string('home-view.html', context=context))
    # render(request, 'home-view.html', context=context)

# using from django.views.decorators.csrf import csrf_exempt @decorator, we can ignore csrf_token error in post requests
@login_required  # because of this user should be login, it will redirect to Django Default login page we need to reset it in Settings.py
def create_entry(request):
    show_mata_data = False

    # this form's are build in 'forms.py' file
    form = firstappForm()  # form = firstappForm(request.POST or None) : when to use which
    modelform = firstappModelForm(request.POST or None)  # always use "request.POST or None" in ModelForm
    if show_mata_data:
        print("===========================================")
        print(dir(form))
        print("===========================================")
    context = {
        "form": form,
        "modelform": modelform
    }
    if request.method == "POST":  # if we use line 58 & 60 instead of line 57 & 59 then we do not have to check for POST method in DjangoForm & DjangoModelForm
        query_dict = request.POST
        if show_mata_data:  # make True When you want to see
            print("===========================================")
            print(request)  # It shows 'WAGIRequest' class and Method
            print(dir(request))  # It will show all diff and various properties  of class
            print(query_dict)  # It will show class 'QueryDict' and 'key : value' of POST data with csrf token
            print("===========================================")
        query_dict_keys = query_dict.keys()
        if "django_form" in query_dict_keys:
            form = firstappForm(request.POST)
            context['form'] = form  # why form is not creating duplicate problem?, instant of that help to showing error
            if form.is_valid():  # do not forget this when you didn't use "request.POST or None"
                title = form.cleaned_data.get("title")
                content = form.cleaned_data.get("content")
                FirstModel.objects.create(title=title, content=content)
        elif "html_form" in query_dict_keys:
            if_exist = FirstModel.objects.filter(title__exact=query_dict.get('title')).first()
            if if_exist is None:
                FirstModel.objects.create(title=query_dict.get('title'), content=query_dict.get('content'))
            # Here we can pass error in context.
        elif "django_model_form" in query_dict_keys:
            if modelform.is_valid():
                firstapp_obj = modelform.save()  # all below code is not needed in ModelForm's "request.POST or None" while creating form OBJ
                # below 2 line will re rander form in HTML so it get cleared with data
                modelform = firstappModelForm() # Here no need for passing data because we need Empty Form
                context['modelform'] = modelform
            # if modelform.is_valid():
            #     title = modelform.cleaned_data.get("title")
            #     content = modelform.cleaned_data.get("content")
            #     FirstModel.objects.create(title=title, content=content)
    return render(request, "firstapp/create.html", context=context)
    # Every One can create this entry but we just want to give access to only SupperUser and Admin
    # how can we do that??