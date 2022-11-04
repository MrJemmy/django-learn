from django.shortcuts import render
from .models import FirstModel
from django.contrib.auth.decorators import login_required

# Create your views here.
def show_data(request, id=None): # id must be hendeled here

    show_in_html = True
    if id is not None:
        try:
            model_row = FirstModel.objects.get(id=id)
        except:
            model_row = None
        show_in_html = False  # when to show ???
    else:
        query_dict = request.GET

        show_mata_data = False
        if show_mata_data: # make True When you want to see
            print("===========================================")
            print(request) # It shows 'WAGIRequest' class and Method
            print(dir(request)) # It will show all diff and various properties  of class
            print(query_dict) # It will show class 'QueryDict' and 'key : value' passed in urls
            print("===========================================")

        # what if search is done using ID ??? how to handle that
        query = query_dict.get("query") # <input type="text" name="query"/> # all ways we get string so for 'int' do type conversion
        if query is not None:
            try: # try except is temp solution
                if query.isnumeric(): # we can search using ID and Title
                    id = int(query)
                    model_row = FirstModel.objects.get(id=id)
                else:
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
@login_required # because of this user should be login, it will redirect to Django Default login page we need to reset it in Settings.py
def create_entry(request):
    if request.method == "POST":
        query_dict = request.POST

        show_mata_data = False
        if show_mata_data:  # make True When you want to see
            print("===========================================")
            print(request)  # It shows 'WAGIRequest' class and Method
            print(dir(request))  # It will show all diff and various properties  of class
            print(query_dict)  # It will show class 'QueryDict' and 'key : value' of POST data with csrf token
            print("===========================================")

        FirstModel.objects.create(title=query_dict.get('title'),content=query_dict.get('content'))
    context = {}
    return render(request, "firstapp/create.html", context=context)
    # Every One can create this entry but we just want to give access to only SupperUser and Admin