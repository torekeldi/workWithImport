from application.db.people import get_employees
from application.salary import calculate_salary
from datetime import datetime
import pyjokes

if __name__ == '__main__':
    calculate_salary()
    get_employees()
    today = datetime.now().date()
    print(today)
    print(pyjokes.get_joke())
