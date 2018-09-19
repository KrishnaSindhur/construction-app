from django.test import TestCase
from .models import MasterPlanHouse

class MasterPlanHouseTestCase(TestCase):
    """
    Simple unit test to check start date and end date of models
    """
    def setUp(self):
         MasterPlanHouse.objects.create(si_no= '1.6', activity= 'Building well', \
                                        start_date= '2018-09-06', end_date= '2018-12-06')
         MasterPlanHouse.objects.create(si_no= '1.7', activity= 'Building gates', \
                                        start_date= '2018-10-06', end_date= '2018-11-06')

    def test_MasterPlanHouse_model(self):
        building_well_data = MasterPlanHouse.objects.get(activity='Building well')
        building_gate_data = MasterPlanHouse.objects.get(activity='Building gates')
        self.assertEqual(building_well_data.start_date, '2018-09-06')
        self.assertEqual(building_well_data.end_date, '2018-12-06')
        self.assertEqual(building_gate_data.start_date, '2018-10-06')
        self.assertEqual(building_gate_data.end_date, '2018-11-06')
