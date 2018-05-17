from decimal import *
from Project.TakeInData import TakeInData
from Project.ProduceOutput import ProduceOutput
from Project.Processing import Processing
from Project.Data import *

class mainController():

    def producingOutput(self,data):
        pO = ProduceOutput()
        pO.printOut(data)

    def gatheringInput(self):
        getData = TakeInData()
        # enter values
        loanAmount = getData.takeInput("Please enter loan amount:", int)
        numberOfMonths = getData.takeInput("Please enter the number of months the loan is for:", int)
        apr = getData.takeInput("Please enter the APR:", Decimal)
        lendingDate = getData.takeInputDate("issue date")

        repaymentDay = getData.takeInputForDay("Please enter the day of the month for repayments:")
        data = Data(loanAmount=loanAmount, numberOfMonths=numberOfMonths, apr=apr, lendingDate=lendingDate,
                    repaymentDay=repaymentDay)
        return data


    def processDetails(self,data):
        p = Processing()
        return p.process(data)





def main():
    # MVC model

    control = mainController()
    # gather data
    data = control.gatheringInput()
    # process data
    data = control.processDetails(data)
    # print out data
    control.producingOutput(data)


if __name__ == '__main__': main()