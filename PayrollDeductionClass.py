class Payroll_Deduction:

    def __init__(self,description,date,charge_amount,IDNumber):
        
        self.__description = description
        self.__date = date
        self.__charge_amount = charge_amount
        self.__IDNumber = IDNumber

    def get_description(self):
        return self.__description

    def get_date(self):
        return self.__date
    
    def get_chargeamnt(self):
        return self.__charge_amount

    def get_IDNum(self):
        return self.__IDNumber
