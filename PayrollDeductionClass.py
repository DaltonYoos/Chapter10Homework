class Payroll_Deduction:

    def __init__(self,description,date,charge_amount,employeeid):
        
        self.__description = description
        self.__date = date
        self.__charge_amount = charge_amount
        self.__employeeid = employeeid

    def get_description(self):
        return self.__description

    def get_date(self):
        return self.__date
    
    def get_charge_amount(self):
        return self.__charge_amount

    def get_idnumber(self):
        return self.__employeeid
