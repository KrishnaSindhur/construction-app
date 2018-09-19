from django.db import models

class MasterPlanHouse(models.Model):
     """
     This is model for the Master Plan House has attributes or columns like
     SI NO, Activity, Start Date and End Date
     """
     si_no = models.CharField(max_length=256,primary_key=True)
     activity = models.CharField(max_length=256)
     start_date = models.CharField(max_length=256)
     end_date = models.CharField(max_length=256)


     def __str__(self):
         return "{}-{}-{}-{}".format(self.si_no, self.activity, self.start_date, self.end_date)
