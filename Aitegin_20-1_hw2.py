class Company:

    def __init__(self, company_bank, company_name):

        self.company_bank = company_bank

        self.company_name = company_name




class Person(Company):

    def __init__(self, company_bank, company_name, first_name, last_name, salary):

        super().__init__(company_bank, company_name)

        self.first_name = first_name

        self.last_name = last_name

        self.salary = salary




    def get_salary(self):

        if self.salary <= self.company_bank:

            self.company_bank -= self.salary

            print(f"Сотрудник получил зарплату: {self.salary}$")

        else:

            print("У компании не достаточно средств!")




    def person_info(self):

        print(f"{self.first_name} {self.last_name} \nЗарплата: {self.salary}$")




aitegin = Person(100, "Marlen Company", "Aitegin", "Asanbekov", 30)




aitegin.person_info()

aitegin.get_salary()

aitegin.get_salary()

aitegin.get_salary()

aitegin.get_salary()

aitegin.get_salary()

aitegin.person_info()
