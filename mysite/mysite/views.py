from django.http import HttpResponse
 
def hello_geeks (request) :
    print(request.method)
    # This will return Hello Geeks
    # string as HttpResponse
    return HttpResponse("Hello Geeks")