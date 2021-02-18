import sqlite3
import datetime


def insert_new_data(new_data):
    try:
        conn = sqlite3.connect("C:\Workspace\homework-redi\/homework_11")
        cursor = conn.cursor()
        print("Successfully connected to database.")
        query = "INSERT INTO Employees (emp_Id, person_Id, salary_Id, department, 'position') VALUES (?,?,?,?,?)"
        cursor.executemany(query, new_data)
        conn.commit()
        print(f"Successfully inserted {cursor.rowcount} data.")
        cursor.close()
    except sqlite3.Error:
        print("Failed to insert new data.")
    finally:
        if (conn):
            conn.close()
            print("The SQLite conn is closed.")


def read_file():
    employee_list = []
    with open('Employees.txt', 'r') as file:
        employee_list += ((each.strip("\r\n")).split(" ")
                          for each in file.readlines() if (each.strip("\r\n") != ""))
    # print(employee_list)
    """ dep_list = []
    for dep in employee_list:
        if (None, dep[-1]) not in dep_list:
            dep_list.append((None, dep[-2]))
    return dep_list """

    """ post_list = []
    for post in employee_list:
        if (None, post[-1]) not in post_list:
            post_list.append((None, post[-1]))
    return post_list """

    """ temp_list = []
    counter = 0
    for emp in employee_list:
        # temp_list.append(emp[0:4])
        if emp[-2] == 'DEV':
            emp[-2] = emp[-1] = 1
            emp.insert(0, None)
            emp.insert(1, counter + 1)
            temp_list.append(emp[0:5])
        elif emp[-2] == 'TST':
            emp[-2] = emp[-1] = 2
            emp.insert(0, None)
            emp.insert(1, counter + 1)
            temp_list.append(emp[0:5])
        else:
            emp[-2] = emp[-1] = 3
            emp.insert(0, None)
            emp.insert(1, counter + 1)
            temp_list.append(emp[0:5])
        counter += 1
    return temp_list """

    temporary_list = []
    counter = 0
    # todate = str(datetime.datetime.now().date())
    for each in employee_list:
        if 'DEV' in each:
            temporary_list.append((None, counter + 1, counter + 1, 1, 1))
        elif 'TST' in each:
            temporary_list.append((None, counter + 1, counter + 1, 2, 2))
        else:
            temporary_list.append((None, counter + 1, counter + 1, 3, 3))
        counter += 1

    return temporary_list


if __name__ == "__main__":
    list = read_file()
    # print(list)
    insert_new_data(list)
