from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.views import View
from django.http import JsonResponse
from .models import MasterPlanHouse
from .serializers import ActivityDateSerializer
import csv
from django.utils.encoding import smart_str
from operator import itemgetter
import pandas as pd

class ActivityDownloadcsv(View):
    """
    This view class is used to download all the activities in csv given
    filename
    """
    def get(self,request):
        response = HttpResponse(content_type='text/csv')
    	#decide the file name
        response['Content-Disposition'] = 'attachment; filename="activities.csv"'

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

class SortedActivity(View):
    """
    This view class is used to download all the sorted activities in csv given
    filename
    """
    def get(self,request):
        response = HttpResponse(content_type='text/csv')
    	#decide the file name
        response['Content-Disposition'] = 'attachment; filename="sorted_activities.csv"'

        writer = csv.writer(response, csv.excel)
        response.write(u'\ufeff'.encode('utf8'))

    	#write the headers
        writer.writerow([
            smart_str(u"Activity"),
        ])
        activity_sort_dict = {}
    	#get data from database
        master_plan_house_data = MasterPlanHouse.objects.all()
        for model_data_obj in master_plan_house_data:
            activity_sort_dict[model_data_obj.si_no] = model_data_obj.activity
        for key, value in sorted(activity_sort_dict.items(), key = itemgetter(0)):
            writer.writerow([
                smart_str(value),
            ])
        return response


class SortedMasterPlan(View):
    """
    This view class is used to download all the sorted Master Plan in csv given
    filename
    """
    def get(self,request):
        response = HttpResponse(content_type='text/csv')
    	#decide the file name
        response['Content-Disposition'] = 'attachment; filename="sorted_activities.csv"'

        writer = csv.writer(response, csv.excel)
        response.write(u'\ufeff'.encode('utf8'))

    	#write the headers
        writer.writerow([
            smart_str(u"Si No"),
            smart_str(u"Activity"),
            smart_str(u"Start Date"),
            smart_str(u"End Date"),
        ])
        si = []
        activity = []
        s_date = []
        e_date = []
    	#get data from database
        master_plan_house_data = MasterPlanHouse.objects.all()
        for model_data_obj in master_plan_house_data:
             si.append(model_data_obj.si_no)
             activity.append(model_data_obj.activity)
             s_date.append(model_data_obj.start_date)
             e_date.append(model_data_obj.end_date)

        df = pd.DataFrame({'si_no':si,'activity':activity,'s_date':s_date,
                                                          'e_date':e_date})
        df.sort_values(['s_date', 'si_no'], ascending=[True, True])
        for index, row in df.iterrows():
            writer.writerow([
                smart_str(row['si_no']),
                smart_str(row['activity']),
                smart_str(row['s_date']),
                smart_str(row['e_date']),
            ])
        return response
