from fpdf import FPDF

class Bill:
    """
    Object contains data about bill such as total
    amount and period of bill
    """
    def __init__(self, amount, period):
        self.amount = amount
        self.period = period

class Flatmate:
    """
    creates a flatmate person who lives in the flat
    and pays a share of the bill
    """
    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, flatmate2):
        weight = self.days_in_house / (self.days_in_house + flatmate2.days_in_house)
        to_pay = bill.amount * weight
        return to_pay

class PdfReport:
    """
    creates a PDF file that contains data about flatmates such as their names
    their due amount and the period of time
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        flatmate1_pay = str(round(flatmate1.pays(bill, flatmate2), 2))
        flatmate2_pay = str(round(flatmate2.pays(bill, flatmate1), 2))

        pdf = FPDF(orientation="P", unit="pt", format="A4")
        pdf.add_page()

        # add icon
        pdf.image("house-icon.png", w=30, h=30)

        # insert title
        pdf.set_font(family="Times", size=24, style="B")
        pdf.cell(w=0, h=80, txt="Flatmates Bill", border=0, align="C", ln=1)

        # insert period label and value
        pdf.set_font(family="Times", size=14, style="B")
        pdf.cell(w=100, h=40, txt="Period: ", border=0)
        pdf.cell(w=150, h=40, txt=bill.period, border=0, ln=1)

        # insert name and due amount of first flatmate
        pdf.set_font(family="Times", size=12)
        pdf.cell(w=100, h=25, txt=flatmate1.name, border=0)
        pdf.cell(w=150, h=25, txt=flatmate1_pay, border=0, ln=1)

        # insert name and due amount of second flatmate
        pdf.cell(w=100, h=25, txt=flatmate2.name, border=0)
        pdf.cell(w=150, h=25, txt=flatmate2_pay, border=0, ln=1)

        pdf.output(self.filename)

the_bill = Bill(amount = 120, period = "May 2021")
shane = Flatmate(name="Shane", days_in_house=20)
jerry = Flatmate(name="Jerry", days_in_house=25)

print("Shane pays: ", shane.pays(bill=the_bill, flatmate2=jerry))
print("Jerry pays: ", jerry.pays(bill=the_bill, flatmate2=shane))

pdf_report = PdfReport(filename="Report1.pdf")
pdf_report.generate(flatmate1=shane, flatmate2=jerry, bill=the_bill)