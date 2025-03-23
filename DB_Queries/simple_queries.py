import os
from decimal import Decimal
from datetime import time
import datetime

from dotenv import load_dotenv
import pyodbc
import SQL_Queries
from save_JSON import JSON

# Загрузка переменных окружения
load_dotenv()
DRIVER = os.getenv("MS_SQL_DRIVER")
SERVER = os.getenv('MS_SQL_SERVER')
DATABASE = os.getenv('MS_SQL_DATABASE')
PAD_DATABASE = os.getenv('MS_PAD_DATABASE')
USER = os.getenv('MS_SQL_USER')
PASSWORD = os.getenv('MS_SQL_KEY')

# Строка подключения
connection_string = f'''DRIVER={DRIVER};
                        SERVER={SERVER};
                        DATABASE={DATABASE};
                        UID={USER};
                        PWD={PASSWORD}'''

# Подключение к базе данных
conn = pyodbc.connect(connection_string)
conn.autocommit = True
cursor = conn.cursor()
active_db_name = "Hospital"
table_name = "Doctors"
data_list = []

try:
    SQL_Query = SQL_Queries.get_data_query_exists(table_name)
    cursor.execute(fr"USE {active_db_name};")
    result = cursor.execute(SQL_Query)
except pyodbc.ProgrammingError as PEex:
    print(PEex)
except pyodbc.IntegrityError as IEex:
    print(IEex)
else:
    records = result.fetchall()
    print("Записи из базы данных:", records)
    for record in records:
        if isinstance(record.Salary, Decimal) or isinstance(record.Premium, Decimal):
            salary = float(record.Salary)
            premium = float(record.Premium)
        else:
            salary = record.Salary
            premium = record.Premium
        data_dict = {'Surname': record.Surname, 'Name': record.Name, 'Salary': salary, 'Premium': premium}
        data_list.append(data_dict)
finally:
    conn.close()

for data in data_list:
    print(data)

conn = pyodbc.connect(connection_string)
conn.autocommit = True
cursor = conn.cursor()
active_db_name = "Hospital"
table_name = "Doctors"
data_list = []

try:
    SQL_Query = SQL_Queries.get_data_query_no_exists(table_name)
    cursor.execute(fr"USE {active_db_name};")
    result = cursor.execute(SQL_Query)
except pyodbc.ProgrammingError as PEex:
    print(PEex)
except pyodbc.IntegrityError as IEex:
    print(IEex)
else:
    records = result.fetchall()
    print(records)
    for record in records:
        if isinstance(record.Salary, Decimal) or isinstance(record.Premium, Decimal):
            salary = float(record.Salary)
            premium = float(record.Premium)
        else:
            salary = record.Salary
            premium = record.Premium
        data_dict = {'Surname': record.Surname, 'Name': record.Name, 'Salary': salary, 'Premium': premium}
        data_list.append(data_dict)
finally:
    conn.close()

for data in data_list:
    print(data)
conn = pyodbc.connect(connection_string)
conn.autocommit = True
cursor = conn.cursor()
active_db_name = "Hospital"
table_name = "Doctors"
data_list = []

try:
    SQL_Query = SQL_Queries.get_data_query_some(table_name)
    cursor.execute(fr"USE {active_db_name};")
    result = cursor.execute(SQL_Query)
except pyodbc.ProgrammingError as PEex:
    print(PEex)
except pyodbc.IntegrityError as IEex:
    print(IEex)
else:
    records = result.fetchall()
    print(records)
    for record in records:
        if isinstance(record.Salary, Decimal) or isinstance(record.Premium, Decimal):
            salary = float(record.Salary)
            premium = float(record.Premium)
        else:
            salary = record.Salary
            premium = record.Premium
        data_dict = {'Surname': record.Surname, 'Name': record.Name, 'Salary': salary, 'Premium': premium}
        data_list.append(data_dict)
finally:
    conn.close()

for data in data_list:
    print(data)
conn = pyodbc.connect(connection_string)
conn.autocommit = True
cursor = conn.cursor()
active_db_name = "Hospital"
table_name = "Doctors"
data_list = []

try:
    SQL_Query = SQL_Queries.get_data_query_any(table_name)
    cursor.execute(fr"USE {active_db_name};")
    result = cursor.execute(SQL_Query)
except pyodbc.ProgrammingError as PEex:
    print(PEex)
except pyodbc.IntegrityError as IEex:
    print(IEex)
else:
    records = result.fetchall()
    print(records)
    for record in records:
        if isinstance(record.Salary, Decimal) or isinstance(record.Premium, Decimal):
            salary = float(record.Salary)
            premium = float(record.Premium)
        else:
            salary = record.Salary
            premium = record.Premium
        data_dict = {'Surname': record.Surname, 'Name': record.Name, 'Salary': salary, 'Premium': premium}
        data_list.append(data_dict)
finally:
    conn.close()

for data in data_list:
    print(data)
conn = pyodbc.connect(connection_string)
conn.autocommit = True
cursor = conn.cursor()
active_db_name = "Hospital"
table_name = "Doctors"
data_list = []

try:
    SQL_Query = SQL_Queries.get_data_query_all(table_name)
    cursor.execute(fr"USE {active_db_name};")
    result = cursor.execute(SQL_Query)
except pyodbc.ProgrammingError as PEex:
    print(PEex)
except pyodbc.IntegrityError as IEex:
    print(IEex)
else:
    records = result.fetchall()
    print(records)
    for record in records:
        if isinstance(record.Salary, Decimal):
            salary = float(record.Salary)
        else:
            salary = record.Salary
        data_dict = {'Surname': record.Surname, 'Name': record.Name, 'Salary': salary}
        data_list.append(data_dict)
finally:
    conn.close()

for data in data_list:
    print(data)
conn = pyodbc.connect(connection_string)
conn.autocommit = True
cursor = conn.cursor()
active_db_name = "Hospital"
table_name = "Doctors"
data_list = []

try:
    SQL_Query = SQL_Queries.get_data_query_some_all(table_name)
    cursor.execute(fr"USE {active_db_name};")
    result = cursor.execute(SQL_Query)
except pyodbc.ProgrammingError as PEex:
    print(PEex)
except pyodbc.IntegrityError as IEex:
    print(IEex)
else:
    records = result.fetchall()
    print(records)
    for record in records:
        if isinstance(record.Salary, Decimal) or isinstance(record.Premium, Decimal):
            salary = float(record.Salary)
            premium = float(record.Premium)
        else:
            salary = record.Salary
            premium = record.Premium
        data_dict = {'Surname': record.Surname, 'Name': record.Name, 'Salary': salary, 'Premium': premium}
        data_list.append(data_dict)
finally:
    conn.close()

for data in data_list:
    print(data)

conn = pyodbc.connect(connection_string)
conn.autocommit = True
cursor = conn.cursor()
active_db_name = "Hospital"
table_name = "Departments"
data_list = []

try:
    SQL_Query = SQL_Queries.get_data_query_union(table_name)
    cursor.execute(fr"USE {active_db_name};")
    result = cursor.execute(SQL_Query)
except pyodbc.ProgrammingError as PEex:
    print(PEex)
except pyodbc.IntegrityError as IEex:
    print(IEex)
else:
    records = result.fetchall()
    print(records)
    for record in records:
        data_dict = {'Name': record.Name_List}
        data_list.append(data_dict)
finally:
    conn.close()
for data in data_list:
    print(data)

conn = pyodbc.connect(connection_string)
conn.autocommit = True
cursor = conn.cursor()
active_db_name = "Hospital"
table_name = "Doctors"
data_list = []

try:
    SQL_Query = SQL_Queries.get_data_query_union_all(table_name)
    cursor.execute(fr"USE {active_db_name};")
    result = cursor.execute(SQL_Query)
except pyodbc.ProgrammingError as PEex:
    print(PEex)
except pyodbc.IntegrityError as IEex:
    print(IEex)
else:
    records = result.fetchall()
    print(records)
    for record in records:
        if isinstance(record.Premium_OR_Donation, Decimal):
            premium = float(record.Premium_OR_Donation)
        else:
            premium = record.Premium_OR_Donation
        data_dict = {'Name': record.Name, 'Premium_OR_Donation': premium}
        data_list.append(data_dict)
finally:
    conn.close()
for data in data_list:
    print(data)

conn = pyodbc.connect(connection_string)
conn.autocommit = True
cursor = conn.cursor()
active_db_name = "Hospital"
table_name = "Doctors"
data_list = []

try:
    SQL_Query = SQL_Queries.get_data_query_inner_join(table_name)
    cursor.execute(fr"USE {active_db_name};")
    result = cursor.execute(SQL_Query)
except pyodbc.ProgrammingError as PEex:
    print(PEex)
except pyodbc.IntegrityError as IEex:
    print(IEex)
else:
    records = result.fetchall()
    print(records)
    for record in records:
        if isinstance(record.StartTime, time) or isinstance(record.EndTime, time):
            startDate = record.StartTime.strftime('%H:%M')
            endDate = record.EndTime.strftime('%H:%M')
        else:
            startDate = record.StartTime
            endDate = record.EndTime
        data_dict = {'Surname': record.Surname, 'Name': record.Name, 'StartTime': startDate,
                     'EndTime': endDate}
        data_list.append(data_dict)
finally:
    conn.close()
for data in data_list:
    print(data)

conn = pyodbc.connect(connection_string)
conn.autocommit = True
cursor = conn.cursor()
active_db_name = "Hospital"
table_name = "Doctors"
data_list = []

try:
    SQL_Query = SQL_Queries.get_data_query_left_join(table_name)
    cursor.execute(fr"USE {active_db_name};")
    result = cursor.execute(SQL_Query)
except pyodbc.ProgrammingError as PEex:
    print(PEex)
except pyodbc.IntegrityError as IEex:
    print(IEex)
else:
    records = result.fetchall()
    print(records)
    for record in records:
        if isinstance(record.StartTime, time) or isinstance(record.EndTime, time):
            startDate = record.StartTime.strftime('%H:%M')
            endDate = record.EndTime.strftime('%H:%M')
        else:
            startDate = record.StartTime
            endDate = record.EndTime
        data_dict = {'Surname': record.Surname, 'Name': record.Name, 'StartTime': startDate,
                     'EndTime': endDate}
        data_list.append(data_dict)
finally:
    conn.close()
for data in data_list:
    print(data)

conn = pyodbc.connect(connection_string)
conn.autocommit = True
cursor = conn.cursor()
active_db_name = "Hospital"
table_name = "Doctors"
data_list = []

try:
    SQL_Query = SQL_Queries.get_data_query_right_join(table_name)
    cursor.execute(fr"USE {active_db_name};")
    result = cursor.execute(SQL_Query)
except pyodbc.ProgrammingError as PEex:
    print(PEex)
except pyodbc.IntegrityError as IEex:
    print(IEex)
else:
    records = result.fetchall()
    print(records)
    for record in records:
        if isinstance(record.StartTime, time) or isinstance(record.EndTime, time):
            startDate = record.StartTime.strftime('%H:%M')
            endDate = record.EndTime.strftime('%H:%M')
        else:
            startDate = record.StartTime
            endDate = record.EndTime
        data_dict = {'Surname': record.Surname, 'Name': record.Name, 'StartTime': startDate,
                     'EndTime': endDate}
        data_list.append(data_dict)
finally:
    conn.close()
for data in data_list:
    print(data)

conn = pyodbc.connect(connection_string)
conn.autocommit = True
cursor = conn.cursor()
active_db_name = "Hospital"
table_name = "Doctors"
data_list = []

try:
    SQL_Query = SQL_Queries.get_data_query_full_join(table_name)
    cursor.execute(fr"USE {active_db_name};")
    result = cursor.execute(SQL_Query)
except pyodbc.ProgrammingError as PEex:
    print(PEex)
except pyodbc.IntegrityError as IEex:
    print(IEex)
else:
    records = result.fetchall()
    print(records)
    for record in records:
        if isinstance(record.StartTime, time) or isinstance(record.EndTime, time):
            startDate = record.StartTime.strftime('%H:%M')
            endDate = record.EndTime.strftime('%H:%M')
        else:
            startDate = record.StartTime
            endDate = record.EndTime
        data_dict = {'Surname': record.Surname, 'Name': record.Name, 'StartTime': startDate,
                     'EndTime': endDate}
        data_list.append(data_dict)
finally:
    conn.close()
for data in data_list:
    print(data)

conn = pyodbc.connect(connection_string)
conn.autocommit = True
cursor = conn.cursor()
active_db_name = "Hospital"
table_name = "Doctors"
data_list = []

try:
    SQL_Query = SQL_Queries.get_data_query_left_and_right_joins(table_name)
    cursor.execute(fr"USE {active_db_name};")
    result = cursor.execute(SQL_Query)
except pyodbc.ProgrammingError as PEex:
    print(PEex)
except pyodbc.IntegrityError as IEex:
    print(IEex)
else:
    records = result.fetchall()
    print(records)
    for record in records:
        if isinstance(record.Amount, Decimal):
            amount = float(record.Amount)
        else:
            amount = record.Amount
        if isinstance(record.Date, datetime.date):
            date = record.Date.strftime('%Y-%m-%d')
        else:
            date = record.Date
        data_dict = {'NameSponsor': record.NameSponsor, 'Amount': amount, 'Date': date}
        data_list.append(data_dict)
finally:
    conn.close()
for data in data_list:
    print(data)

# if __name__ == '__main__':
#     JSON.save_json('Query_LEFT_and_RIGHT_JOIN', data_list)