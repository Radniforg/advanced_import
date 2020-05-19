# main.py

from application import people
from datetime import datetime
from application import salary

if __name__ == '__main__':
	print(datetime.date(datetime.now()))
	print(people.get_employees())
	print(salary.calculate_salary())
