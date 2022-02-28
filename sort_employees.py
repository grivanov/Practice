def sort_employees(employees, sort_by):
    # Write your code here.
    # sort_index = int()

    # if sort_by == "name":
    #     sort_index = 0
    # elif sort_by == "age":
    #     sort_index = 1
    # elif sort_by == "salary":
    #     sort_index = 2

    sort_options = ["name", "age", "salary"]
    sort_index = sort_options.index(sort_by)

    def sort_func(a):
        return a[sort_index]

    employees.sort(key=sort_func)
    return employees


empl = [
    ["John", 33, 65000],
    ["Sarah", 24, 75000],
    ["Josie", 29, 100000],
    ["Jason", 26, 55000],
    ["Connor", 25, 110000]
]
sort_employees(empl, "salary")
