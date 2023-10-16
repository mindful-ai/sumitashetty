class Employee:

    # Class variables
    empCount = 0

    # Constructor and Data Intialization
    def __init__(self, n, company, salary):
        self.name = n
        self.company = company
        self.salary = salary
        self.tax = 0
        Employee.empCount += 1

    # Functions
    def printinfo(self):
        print(self.name.upper())
        print('-'*30)
        print('COMPANY    :', self.company)
        print('SALARY     :', self.salary)
        print('TAX        :', self.tax)
        

    def setsalary(self, newsalary):
        self.salary = newsalary
        self.calctax()

    def getsalary(self):
        return self.salary

    def calctax(self):
        self.tax = 0.1 * float(self.salary.split()[0])

#---------------------------------------------------------------

# CORE DEVELOPER -> Inheritance

class newemp(Employee):
    pass

#---------------------------------------------------------------

class extEmployee(Employee):

    # Class variables
    # empCount is already available here

    # Constructor and Data Initialization
    # Supposed to distribute the data between parent and child
    def __init__(self, n, age, company, salary):
        super().__init__(n, company, salary)
        self.age = age
        self.addr = ''

    # Functions

    # All functions of Employee is also available here

    # Overridden function
    def printinfo(self):
        super().printinfo()
        print('-'*30)
        print('AGE        :', self.age)
        print('ADDRESS    :', self.addr)
        print('\n\n')

    # New functions
    def setaddr(self, addr):
        self.addr = addr


#################################################################

e = newemp("Kiran", "Oracle", "1000000 INR")
print("From the app -> ", e)
e.calctax()
e.printinfo()
e.setsalary("1234560 INR")
e.printinfo()

#################################################################

emp_records = [("Anil", 40, "Oracle", "1000000 INR"), 
               ("Kiran", 35, "Oracle", "800000 INR"),
               ("Raj", 36, "Oracle", "900000 INR")]

emp_objs = []
for record in emp_records:
    emp_objs.append(extEmployee(record[0], record[1], record[2], record[3]))

for obj in emp_objs:
    obj.setaddr("Bangalore")
    obj.calctax()

for obj in emp_objs:
    obj.printinfo()


################################################################# POLYMORPHISM


print("\n\nPolymorphism Demo")

e2 = emp_objs[0]
e1 = e

#s = e1
s = e2
s.printinfo()
