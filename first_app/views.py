from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic, Webpage, AccessRecord

# Create your views here.
def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records':webpages_list}
    return render(request,'index.html',context=date_dict)

def index_old(request):
    return HttpResponse("My first App. Go to '/first_app/' to check user records.")