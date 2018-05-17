from Project.Data import DataTest
import unittest
from Project.Main import mainController

class mainTest(unittest.TestCase):

    def testingMain(self):
        control = mainController()
        data = DataTest().generateTestValuesWithOutListOfDatesAndRepaymentDay()
        data = control.processDetails(data)
        self.assertFalse(control.producingOutput(data))