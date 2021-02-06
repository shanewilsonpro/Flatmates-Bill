from flat import Bill, Flatmate
from reports import PdfReport

amount = float(input("Hey, enter the bill amount: "))
period = input("What is the bill period? (E.g. December 2020) ")

flatmate1_name = input("What is your name? ")
days_in_house1 = int(input(f"How many days did {flatmate1_name} stay in the house during the bill period? "))

flatmate2_name = input("What is the name of other flatmate? ")
days_in_house2 = int(input(f"How many days did {flatmate2_name} stay in the house during the bill period? "))

the_bill = Bill(amount, period)
flatmate1 = Flatmate(flatmate1_name, days_in_house1)
flatmate2 = Flatmate(flatmate2_name, days_in_house2)

print(f"{flatmate1_name} pays: ", flatmate1.pays(the_bill, flatmate2))
print(f"{flatmate2_name} pays: ", flatmate2.pays(the_bill, flatmate1))

pdf_report = PdfReport(filename=f"{the_bill.period}.pdf")
pdf_report.generate(flatmate1, flatmate2, the_bill)