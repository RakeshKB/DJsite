"""
    Different views for handling client requests
"""
from django.http import HttpResponse
import datetime

def current_datetime(request):
    now = datetime.datetime.now().time()
    html = '<html><body> The current time is %s </body></html>' % now
    return HttpResponse(html)

def hours_ahead(request, offset):
    offset = int(offset)
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = '<html><body>In %s hours, the time will be %s </body></html>' % (offset, dt)
    return HttpResponse(html)
