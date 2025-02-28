company_employees = {
    "Engineering": {
        "Alice": {"age": 30, "role": "Software Engineer"},
        "Bob": {"age": 28, "role": "DevOps Engineer"}
    },
    "HR": {
        "Charlie": {"age": 35, "role": "HR Manager"}
    }
}
print(company_employees)
company_employees["Engineering"]["David"] = {"age": 27, "role": "Data Scientist"}
def count_total_employees(company_employees):
    total_employees = 0
    for department in company_employees.values():
        total_employees += len(department)
    return total_employees
print(company_employees)
print("Total employees:", count_total_employees(company_employees))
