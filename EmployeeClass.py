class Employee:

    def __init__(self, name, idnum,department,job_title,month_pay):

        self.__name = name
        self.__idnum = idnum
        self.__department = department
        self.__job_title =job_title
        self.__month_pay = month_pay

    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__idnum

    def get_department(self):
        return self.__department

    def get_job(self):
        return self.__job_title

    def get_months_pay(self):
        return self.__month_pay