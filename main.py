from application.salary import calculate_salary

from db.people import get_employees

from datetime import datetime

if __name__ == '__main__':
    list_employees = get_employees()
    print(list_employees)

    salary_Ivan_Ivanov = calculate_salary(150, 180)
    print(f'Salary Ivana Ivanova = {salary_Ivan_Ivanov} rubles')
    
    print(datetime.now())

