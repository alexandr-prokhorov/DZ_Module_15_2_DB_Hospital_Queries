# Запрос на информацию о врачах у которых есть обследования.

def get_data_query_exists(name):
    COMMAND = fr"""SELECT Surname, Name, Salary, Premium
                FROM {name}
                WHERE EXISTS
                (SELECT * FROM DoctorsExaminations WHERE DoctorsExaminations.DoctorId = Doctors.id);"""
    return COMMAND


# Запрос на информацию о врачах у которых обследований нет.
def get_data_query_no_exists(name):
    COMMAND = fr"""SELECT Surname, Name, Salary, Premium
                    FROM {name}
                    WHERE NOT EXISTS
                    (SELECT * FROM DoctorsExaminations WHERE DoctorsExaminations.DoctorId = Doctors.id);"""
    return COMMAND


# Запрос на информацию о врачах у которых обследования начинаются в 9:00
def get_data_query_some(name):
    COMMAND = fr"""SELECT Surname, Name, Salary, Premium
                    FROM {name}
                    WHERE id = SOME (SELECT DoctorId FROM DoctorsExaminations WHERE StartTime = '9:00');"""
    return COMMAND


# Запрос на информацию о врачах у которых обследование начинается в 17:00 и заканчивается в 17:30
def get_data_query_any(name):
    COMMAND = fr"""SELECT Surname, Name, Salary, Premium
                    FROM {name}
                    WHERE id = ANY (SELECT DoctorId FROM DoctorsExaminations WHERE StartTime = '17:00' AND EndTime = '17:30');"""
    return COMMAND

# Запрос на информацию о врачах у которых зарплата ниже среднего значения зарплаты врачей по больнице.
def get_data_query_all(name):
    COMMAND = fr"""SELECT Surname, Name, Salary
                    FROM {name}
                    WHERE Salary < ALL (SELECT AVG(Salary) FROM Doctors);"""
    return COMMAND
# Запрос на информацию у которых начало работы в 9:00 и премия больше 10000.
def get_data_query_some_all(name):
    COMMAND = fr"""SELECT Surname, Name, Salary, Premium
                FROM {name}
                WHERE id = SOME (SELECT DoctorId FROM DoctorsExaminations WHERE StartTime = '9:00')
                AND Premium > ALL
                (SELECT Premium FROM Doctors WHERE Premium = 10000);"""
    return COMMAND
# Запрос на информацию о названии отделении палат и обследований.
def get_data_query_union(name):
    COMMAND = fr"""SELECT Name AS Name_List
                    FROM Departments
                    UNION
                    SELECT NameWARD
                    FROM Wards
                    UNION
                    SELECT NameExamination
                    FROM Examinations"""
    return COMMAND
# Запрос на информацию врачей и спонсоров у которых премия либо пожертвования равны 10000
def get_data_query_union_all(name):
    COMMAND = fr"""SELECT Name + ' ' + '(D)' AS Name, Premium AS Premium_OR_Donation
                    FROM {name}
                    WHERE Premium = 10000
                    UNION ALL
                    SELECT S.NameSponsor + ' ' + '(S)' AS Name, D.Amount
                    FROM Sponsors AS S
                    JOIN Donations AS D ON S.id = D.SponsorId
                    WHERE D.Amount = 10000"""
    return COMMAND
# Запрос на информацию о врачах у которых есть обследования.
def get_data_query_inner_join(name):
    COMMAND = fr"""SELECT D.Surname, D.Name, DE.StartTime, DE.EndTime
                    FROM {name} AS D
                    INNER JOIN DoctorsExaminations AS DE ON D.id = DE.DoctorId;"""
    return COMMAND
# Запрос той же информации только с использованием LEFT JOIN.
def get_data_query_left_join(name):
    COMMAND = fr"""SELECT D.Surname, D.Name, DE.StartTime, DE.EndTime
                    FROM {name} AS D
                    LEFT JOIN DoctorsExaminations AS DE ON D.id = DE.DoctorId;"""
    return COMMAND
# Запрос той же информации только с использованием RIGHT JOIN.
def get_data_query_right_join(name):
    COMMAND = fr"""SELECT D.Surname, D.Name, DE.StartTime, DE.EndTime
                    FROM {name} AS D
                    RIGHT JOIN DoctorsExaminations AS DE ON D.id = DE.DoctorId;"""
    return COMMAND
# Запрос той же информации только с использованием FULL JOIN.
def get_data_query_full_join(name):
    COMMAND = fr"""SELECT D.Surname, D.Name, DE.StartTime, DE.EndTime
                    FROM {name} AS D
                    FULL JOIN DoctorsExaminations AS DE ON D.id = DE.DoctorId;"""
    return COMMAND
# Запрос информации людей которые сделали пожертвования.Два имени добавлены без информации для проверки.
def get_data_query_left_and_right_joins(name):
    COMMAND = fr"""SELECT S.NameSponsor, D.Amount, D.Date
                FROM Sponsors AS S
                LEFT JOIN Donations AS D ON S.id = D.SponsorId
                UNION
                SELECT S.NameSponsor, D.Amount, D.Date
                FROM Sponsors AS S
                RIGHT JOIN Donations AS D ON S.id = D.SponsorId;"""
    return COMMAND