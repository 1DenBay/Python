class Logitic:

    def __init__(self, company_name, foundation_year, founder_name, company_slogan, inventory_space):
        self.company_name = company_name
        self.foundation_year = foundation_year
        self.founder_name = founder_name
        self.company_slogan = company_slogan
        self.inventory_space = inventory_space

    def print_report(self): #son güncel bilgileri yazdırmak için rapor
        print(f"""The company {self.company_name} and was founded in {self.foundation_year}
        The founder of the company is {self.founder_name}
        Company slogan : {self.company_slogan}
        Inventorsy spcae of the company : {self.inventory_space}""")

    def update_inventory_space(self, new_storage_space):
        self.inventory_space = new_storage_space
        print(f"Inventory space has been changed to {self.inventory_space}!")

company_1 = Logitic("DenBay A.Ş." , 1907 , "DENİZBAYAT" , "You never will walk alone" , 9999)

Logitic.update_inventory_space(8229)

Logitic.print_report()  