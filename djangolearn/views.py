""" To Render html web pages """
from django.http import HttpResponse

def home_view(request):
    """
    - Take request (Default Django sends request to this function)
    - Return HTML as response (Returning the Response)
    """

    name = "Jaimin"
    html_string = f"""
        <h1 style="text-align:center"> Hello {name}! </h1>
        <h2 align="center"> How are you? </h2>
    """

    return HttpResponse(html_string)