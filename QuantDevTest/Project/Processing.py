import unittest
from Project.ProduceOutput import ProduceOutput
from Project.Data import *


class Processing:
    def process(self, data):
        #                                     loan * (1+apr)% / term
        annualRepaymentAmount = (data.loanAmount() * (1 + (data.apr() / 100))) / data.numberOfMonths()

        # you start paying the month after you get your loan thus the plus  1 on the month
        newPaymentDate = dt.date(data.lendingDate().year, (data.lendingDate().month) + 1, data.repaymentDay())

        # comprehension generating payment dates for list
        paymentDates = [self.getDates(newPaymentDate, x) for x in range(data.numberOfMonths())]

        # storing data value back into data object
        data.annualRepaymentAmount(annualRepaymentAmount)
        data.paymentDates(paymentDates)

        return data


    def getDates(self,date, months):
        # reduce months by 1 as it goes from 0-11 not 1-12
        month = (date.month -1) + months
        # add the year after dividing month by 12 and dropping the decimal
        year = date.year + (month // 12)
        # need to plus one as the it goes from 0 - 11 = 12 values
        month = (month % 12) + 1

        return dt.date(year,month,date.day)



class ProcessingTest(unittest.TestCase):

    _processing = Processing()

    def testGetDate(self):
        date = self._processing.getDates(dt.date(2001, 2, 1), 1)
        self.assertEqual(date, dt.date(2001, 3, 1))

    def testProcess(self):
        data = DataTest().generateTestValuesWithOutListOfDatesAndRepaymentDay()
        dataValid = DataTest().generateTestValues()
        tempData = self._processing.process(data)
        output = ProduceOutput()

        self.assertEqual(output.printOut(tempData), output.printOut(dataValid))

