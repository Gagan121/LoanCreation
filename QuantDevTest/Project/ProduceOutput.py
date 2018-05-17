from Project.Data import DataTest
import unittest

class ProduceOutput:

    def printOut(self,data=None):
        print('\n --------------------------------------------------------------------')
        print(f'Total loan amount taken out : £{data.loanAmount()}')
        print(f'The loan has been set to be taken out for {data.numberOfMonths()} Months')
        print(f'The APR for this loan is {data.apr()}%')
        print(f'The date when this loan was given was {data.lendingDate().strftime("%Y-%m-%d")}')
        print(f'The repayment day has been set to the: {data.repaymentDay()} of every Month')
        print(f'The amount to repay every month is £{data.annualRepaymentAmount()} including interest')
        self.printOutList(data.paymentDates())

    def printOutList(self,list):
        for item in list:
            print(f'The repayment date is {item}')

    @staticmethod
    def printOutStrError(content):
        print(content)


class ProduceOutputTest(unittest.TestCase):
    _output = ProduceOutput()

    def testPrintOutputStrError(self):
        self.assertFalse(ProduceOutput.printOutStrError("test"))

    def testPrintOutput(self):
        dataTest = DataTest()
        data = dataTest.generateTestValues()
        self.assertFalse(self._output.printOut(data))




