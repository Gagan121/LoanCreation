import datetime as dt

class Data:
    def __init__(self, **kwargs):
        self._loanAmount = kwargs['loanAmount']
        self._numberOfMonths = kwargs['numberOfMonths']
        self._apr = kwargs['apr']
        self._lendingDate = kwargs['lendingDate']
        self._repaymentDay = kwargs['repaymentDay']

    def loanAmount(self, la = None):
        if la: self._loanAmount = la
        return self._loanAmount

    def numberOfMonths(self, nom = None):
        if nom: self._numberOfMonths = nom
        return self._numberOfMonths

    def apr(self, apr_ = None):
        if apr_: self._apr = apr_
        return self._apr

    def lendingDate(self, ld = None):
        if ld: self._lendingDate = ld
        return self._lendingDate

    def repaymentDay(self, rd = None):
        if rd: self._repaymentDay = rd
        return self._repaymentDay

    def annualRepaymentAmount(self, ara = None):
        if ara: self._annualRepaymentAmount = ara
        return self._annualRepaymentAmount

    def paymentDates(self, pd = None):
        if pd: self._paymentDates = pd
        return self._paymentDates


class DataTest:

    def generateTestValues(self):
        loanAmount = 100
        numberOfMonths = 10
        apr = 6
        lendingDate = dt.date(2001, 1, 1)
        repaymentDay = 2

        data = Data(loanAmount=loanAmount, numberOfMonths=numberOfMonths, apr=apr, lendingDate=lendingDate,repaymentDay=repaymentDay)

        paymentDates = [dt.date(2001, 2, 2), dt.date(2001, 3, 2), dt.date(2001, 4, 2),dt.date(2001, 5, 2), dt.date(2001, 6, 2), dt.date(2001, 7, 2),dt.date(2001, 8, 2), dt.date(2001, 9, 2), dt.date(2001, 10, 2),dt.date(2001, 11, 2)]
        annualRepaymentAmount = 10.6
        data.paymentDates(paymentDates)
        data.annualRepaymentAmount(annualRepaymentAmount)
        return data


    def generateTestValuesWithOutListOfDatesAndRepaymentDay(self):
        loanAmount = 100
        numberOfMonths = 10
        apr = 6
        lendingDate = dt.date(2001, 1, 1)
        repaymentDay = 2

        return Data(loanAmount=loanAmount, numberOfMonths=numberOfMonths, apr=apr, lendingDate=lendingDate,repaymentDay=repaymentDay)