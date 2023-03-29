from datetime import datetime

from django.test import TestCase
from .models import Currency

# Create your tests here.

# Currently not working.
class CurrencyModelTest(TestCase):

    def test_get_old_trm_with_old_date(self):
        """
        get_old_date returns the value of the Representative Market Rate for the specified date
        """

        time1 = datetime(2022,1,1)
        time2 = '2021-01-01'

        cop = Currency.objects.get(code='COP')

        self.assertAlmostEqual(cop.get_old_trm(time1), 3981.16, 2)
        self.assertAlmostEqual(cop.get_old_trm(time2), 3432.50, 2)