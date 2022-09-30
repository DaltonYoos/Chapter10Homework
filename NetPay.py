import EmployeeClass as ec
import PayrollDeductionClass as pdc

def main():

    employee_info = ec.Employee('Jimmy Smith', 58475, 'Information Systems', 'Developer', 6800.00)

    transaction1 = pdc.Payroll_Deduction('Food Court', '8/14/2022', 22.50, 39119)
    transaction2 = pdc.Payroll_Deduction('Gift Contribution', '8/12/2022', 25.00, 58475)
    transaction3 = pdc.Payroll_Deduction('Food Court', '8/17/2022', 15.25, 21547)
    transaction4 = pdc.Payroll_Deduction('Vending Machines', '8/22/2022', 3.00, 58475)
    transaction5 = pdc.Payroll_Deduction('Vending Machines', '8/5/2022', 2.75, 58475)

    net_income = employee_info.get_months_pay()
    
    employee_transactions = [transaction1, transaction2, transaction3, transaction4, transaction5]

    for transactions in employee_transactions: 
            if pdc.Payroll_Deduction.get_idnumber(transactions) == employee_info.get_id():
                net_income = net_income - pdc.Payroll_Deduction.get_chargeamnt(transactions)


    print('*** Employee Pay ***')
    print('Name:', ec.Employee.get_name(employee_info))
    print('ID Number:', ec.Employee.get_id(employee_info))
    print('Department:', ec.Employee.get_department(employee_info))
    print('Gross Pay: $', ec.Employee.get_months_pay(employee_info))
    print('Net Pay: $', net_income)


main()