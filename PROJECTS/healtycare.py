class HealthInsurance: #şirket bilgileri

    def __init__(self, company_name, foundation_year, founder_name, company_slogan, num_of_employees, num_of_clients): #parametre tanımları
        self.company_name = company_name
        self.foundation_year = foundation_year
        self.founder_name = founder_name
        self.company_slogan = company_slogan
        self.num_of_employees = num_of_employees
        self.num_of_clients = num_of_clients

    def print_report(self): #son güncel bilgileri yazdırmak için rapor
        print(f"""The company {self.company_name} was founded in {self.foundation_year}
        The founder of the company is {self.founder_name}
        Company slogan : {self.company_slogan}
        Num of emplooyes : {self.num_of_employees}
        Num of clients : {self.num_of_clients}""")

    def sup_health_insurance(self, age, chronic_disease, income): #sigortadan yararlanma şartları
        if age >= 60 and chronic_disease == True and income < 6000 :
            print("We are Sorry , You are not eligible for supplemental healt insurance")
        
        elif age < 60 and income >= 6000 or chronic_disease == False:
            print("Congratulations! You can get supplemental healt insurance ")
    
    def update_num_clients(self, new_number): #güncel müşteri sayısı
        self.num_of_clients = new_number
        print(f"Number of clients has been changed to {self.num_of_clients}")
    
company_1 = HealthInsurance("Medipol" , 2002 , "DenBay" , "We can keep alive you" , 2 , 1907)

company_1.sup_health_insurance(45 , False , 7800)
company_1.sup_health_insurance(65,False,8900)

company_1.update_num_clients(1908)

company_1.print_report()