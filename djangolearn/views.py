""" To Render html web pages """
from django.http import HttpResponse
from firstapp.models import FirstModel
from django.template.loader import render_to_string  # , get_template

def home_view(request):
    """
    - Take request (Default Django sends request to this function)
    - Return HTML as response (Returning the Response)
    """
    model_data = FirstModel.objects.all()
    name = 'Jaimin'

    context = {
        'name' : name,
        'model_data' : model_data,
    }

    html_string = render_to_string('home-view.html', context=context)

    # other method : when we want to render same html multiple time with diff data
    # template_html = get_template('home-view.html')
    # html_string_1 = template_html.render(context=context)
    # html_string_2 = template_html.render(context=context)
    # html_string_3 = template_html.render(context=context)

    return HttpResponse(html_string)