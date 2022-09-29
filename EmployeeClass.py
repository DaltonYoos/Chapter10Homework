class Employee:

    def __init__(self, name, IDNumber,department,job_title,mnthly_sal):

        self.__name = name
        self.__IDNumber = IDNumber
        self.__department = department
        self.__job_title =job_title
        self.__mnthly_sal = mnthly_sal

    def get_name(self):
        return self.__name

    def get_ID(self):
        return self.__IDNumber

    def get_department(self):
        return self.__department

    def get_job(self):
        return self.__job_title

    def months_salary(self):
        return self.__mnthly_sal