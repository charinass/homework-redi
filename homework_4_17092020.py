# import convert_docx_to_txt as c #not used

# if (c.convert_doc_to_txt()): #this line is not useful
file = "Employees.txt"


def read_file(file):
    emp_list = []
    with open(file, "r") as file:
        for i in file.readlines():
            i = i.strip("\r\n")
            if(i != ""):
                x = tuple(i.split(" "))
                emp_list.append(x)
    return emp_list


def calc_ave_salary(emp_list):
    _sum = 0
    for i in emp_list:
        # [3] accesses salary value (sorry for magic values)
        _sum += float(i[3])
    return _sum / len(emp_list)


def get_oldest_emp(emp_list):
    _age, _name = 0, ""
    for a in emp_list:
        if(_age < int(a[1])):
            _age, _name = int(a[1]), a[0]  # tuple age and name
    return _age, _name


def get_youngest_emp(emp_list):
    _age, _name = get_oldest_emp(emp_list)
    for a in emp_list:
        if (_age > int(a[1])):
            _age, _name = int(a[1]), a[0]
    return _age, _name


def get_mng_position(emp_list):
    count = 0
    for m in emp_list:
        if (m[-1] == "MNG"):  # [-1] last tuple value is position
            count += 1
    return count


def get_proportion(emp_list):
    m = f = 0
    for p in emp_list:
        if (p[2] == 'M'):  # [2] accesses gender in tuple list
            m += 1
        elif (p[2] == 'F'):
            f += 1
    m = (m/len(emp_list)) * 100  # percent
    f = (f/len(emp_list)) * 100
    return m, f


def get_age_group(age_group, emp_list):
    count = 0
    for a in emp_list:
        if (int(a[1]) in age_group):
            count += 1
    return count


##########################just being a noob here############################


def get_name_list(emp_list):
    _names = []
    _names = [i[0] for i in emp_list]
    return _names


def get_age_list(emp_list):
    _ages = []
    _ages = [i[1] for i in emp_list]  # age
    return _ages


def get_gender_list(emp_list):
    _gender = []
    _gender = [i[2] for i in emp_list]
    return _gender


def get_sal_list(emp_list):
    _salary = []
    _salary = [float(i[3]) for i in emp_list]  # age
    return _salary


def get_pos_list(emp_list):
    _position = []
    _position = [i[-1] for i in emp_list]
    return _position

#############################################################################

### extra (but implemented with extra codes above this line ^) ###


def get_least_dept_budget(emp_list):  # 6
    _temp_dict = dict(zip(get_sal_list(emp_list), get_pos_list(emp_list)))
    _lowest = min(_temp_dict.items())
    return _lowest


def count_emp_pos(emp_list):  # 7
    _temp_list = get_pos_list(emp_list)
    _count = {}
    for i in _temp_list:
        _count[i] = _temp_list.count(i)
    return _count


def calc_best_worst(emp_list):  # 8
    _temp_dict = dict(zip(get_sal_list(emp_list), get_pos_list(emp_list)))
    _best = max(_temp_dict.items())
    _worst = min(_temp_dict.items())
    _temp_best = [round(sum(float(key)
                            for key, values in _temp_dict.items() if(values == _best[1])) / get_pos_list(emp_list).count(_best[1]), 2), _best[1]]
    _temp_worst = [round(sum(float(key) for key, values in _temp_dict.items() if(
        values == _worst[1])) / get_pos_list(emp_list).count(_worst[1]), 2), _worst[1]]
    return _temp_best, _temp_worst


def get_closest_emp_sal(emp_list):
    _min_list = []
    _smallest = None
    _salary = dict(zip(get_name_list(emp_list), get_sal_list(emp_list)))
    for key_base, value_base in _salary.items():
        for key_comp, value_comp in _salary.items():
            _diff = abs(float(value_base) - float(value_comp))
            if (_smallest == None):
                _smallest = float(value_base)
            elif(_smallest > _diff and value_base != value_comp):
                _smallest = _diff
                _min_list = [key_base, value_base, key_comp, value_comp]
    return _min_list, round(_smallest, 2)


def deduct(employee_sal, average_sal):
    '''
    I'm not sure what I was practicing here
    '''
    return abs(employee_sal - average_sal)


def calc_dep_emp_sal(emp_list, dep):
    _emp_dep_salary = list(zip(get_name_list(emp_list), get_pos_list(
        emp_list), get_sal_list(emp_list)))
    _sum = 0
    _ave = sum([float(i[2]) for i in _emp_dep_salary if i[1] == dep]
               ) / len([x for x in _emp_dep_salary if x[1] == dep])
    closest_ave = min(abs(float(sal[2]) - _ave)
                      for sal in _emp_dep_salary if sal[1] == dep)
    _name = [i for i in _emp_dep_salary if (i[1] == dep and
                                            abs(float(i[2]) - _ave) == closest_ave)]
    return _ave, _name

################################################################################


if __name__ == "__main__":
    emp_list = read_file(file)
    print(f"average salary in the company: {calc_ave_salary(emp_list):.2f}")
    print(f"name of the oldest employee: {get_oldest_emp(emp_list)}")
    print(f"name of the youngest employee: {get_youngest_emp(emp_list)}")
    print(
        f"employees occupying the MNG position: {get_mng_position(emp_list)}")
    print(
        f"male/female proportion in the company: {get_proportion(emp_list)}%")
    age_group = {"18-25": range(18, 26),
                 "26-35": range(26, 36),
                 "36-48": range(36, 49),
                 "49-60": range(49, 61),
                 "61+": range(61, 100)}
    print("for each of the following age groups: \n" +
          f"18-25: {get_age_group(age_group['18-25'], emp_list)}\n" +
          f"26-35: {get_age_group(age_group['26-35'], emp_list)}\n" +
          f"36-48: {get_age_group(age_group['36-48'], emp_list)}\n" +
          f"49-60: {get_age_group(age_group['49-60'], emp_list)}\n" +
          f"61+: {get_age_group(age_group['61+'], emp_list)}")

    ### extra here ###
    print(f"employees per department: {count_emp_pos(emp_list)}")
    print(
        f"department (position) requires the most budget: {get_least_dept_budget(emp_list)}")
    print(
        f"average between the best and worst salary for each department (position): {calc_best_worst(emp_list)}")
    print(
        f"employees with the closest salaries: {get_closest_emp_sal(emp_list)}")
    print(
        f"for each department, who is the employee with the salary closest to the average salary of that department (position)? DEV: {calc_dep_emp_sal(emp_list, 'DEV')}" +
        f"\nMNG: {calc_dep_emp_sal(emp_list, 'MNG')}" +
        f"\nTST: {calc_dep_emp_sal(emp_list, 'TST')}")
