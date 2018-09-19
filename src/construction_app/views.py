from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.views import View
from django.http import JsonResponse
from .models import MasterPlanHouse
from .serializers import ActivityDateSerializer
import csv
from django.utils.encoding import smart_str

class ActivityDownloadcsv(View):
    """
    This view class is used to download all the activities in csv filename
    """
    def get(self,request):
        response = HttpResponse(content_type='text/csv')
    	#decide the file name
        response['Content-Disposition'] = 'attachment; filename="Activities.csv"'

        writer = csv.writer(response, csv.excel)
        response.write(u'\ufeff'.encode('utf8'))

    	#write the headers
        writer.writerow([
            smart_str(u"Activity"),
        ])
    	#get data from database
        master_plan_house_data = MasterPlanHouse.objects.all()
        for model_data_obj in master_plan_house_data:
            writer.writerow([
                smart_str(model_data_obj.activity),
            ])
        return response


class ActivityDateView(View):
    """
    This view class is used to show start date and end_date of the particular
    activity
    """
    def get(self,request,activity):
        query = MasterPlanHouse.objects.filter(activity__icontains=activity).first()
        serializer = ActivityDateSerializer(query)
        return JsonResponse(serializer.data, safe=False)
