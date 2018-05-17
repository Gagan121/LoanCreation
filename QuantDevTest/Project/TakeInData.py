import datetime
import unittest
from decimal import *

class TakeInData:

    # all the functions are trapped in a while loop until they are break when a valid response is entered

    def takeInputDate(self, anotherPrompt= None):
        while(True):
            try:
                date = input('please enter the {} in the format YYYY-MM-DD with dashes: '.format(anotherPrompt))
                return datetime.datetime.strptime(date, '%Y-%m-%d')
            except ValueError:
                print('incorrect date format entered please try again')


    # setting the day for 1-28 as feb only has 28 days thus to reduce the confusion
    def takeInputForDay(self, anotherPrompt = None):
        while (True):
            repaymentDay = self.takeInput(anotherPrompt, int)
            if (0 < repaymentDay < 29):
                return repaymentDay
            print('please enter a valid date between 1 - 28')



    #  compares input and checks if can be parse into the desired data type
    def takeInput(self,prompt = None, type = None):
        intInput = None
        responseIsValid = True
        while(responseIsValid):
            try:
                # a custom casting it here type has a data type passed through it
                intInput = type( input(prompt+" ") )
                if isinstance(intInput,type):
                    responseIsValid = False
            except:
                print(f'incorrect type of data enter please try again.')

        return intInput


class DataValidationTest(unittest.TestCase):
    _takeInData = TakeInData()
    def testTakeInput(self):
        self.assertTrue(self._takeInData.takeInput("Enter a Integer value", int))
        self.assertTrue(self._takeInData.takeInput("Enter a Decimal value", Decimal))

    def testTakeInputForDay(self):
        self.assertTrue(self._takeInData.takeInputForDay("Enter a number between 1 - 28: "))

    def testInputDate(self):
        self.assertTrue(self._takeInData.takeInputDate("test"))
