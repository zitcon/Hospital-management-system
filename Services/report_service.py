import csv

from Services.staff_service import StaffService
from Services.patient_service import PatientService


class ReportService:
    def __init__(self):
        self.staff_service = StaffService()
        self.patient_service = PatientService()

    def total_staff(self):
        return len(self.staff_service.get_all_staff())

    def total_patients(self):
        return len(self.patient_service.get_all_patients())

    def total_salary_expense(self):
        staff_list = self.staff_service.get_all_staff()
        return sum(staff[6] for staff in staff_list)

    def total_hospital_revenue(self):
        patient_list = self.patient_service.get_all_patients()
        return sum(patient[7] for patient in patient_list)

    def export_report_csv(self):
        with open("hospital_report.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)

            writer.writerow(["Hospital Report"])

            writer.writerow(["Total Staff", self.total_staff()])
            writer.writerow(["Total Patients", self.total_patients()])
            writer.writerow(["Total Salary Expense", self.total_salary_expense()])
            writer.writerow(["Total Hospital Revenue", self.total_hospital_revenue()])

        return "hospital_report.csv"