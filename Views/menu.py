from services.staff_service import StaffService
from services.patient_service import PatientService

staff_service = StaffService()
patient_service = PatientService()


def input_int(message):
    while True:
        try:
            value = int(input(message))
            if value < 0:
                print("Value cannot be negative.")
            else:
                return value
        except ValueError:
            print("Please enter a valid integer.")


def input_float(message):
    while True:
        try:
            value = float(input(message))
            if value < 0:
                print("Value cannot be negative.")
            else:
                return value
        except ValueError:
            print("Please enter a valid number.")


def display_staff(staff_list):
    print("\nID | Name | Age | Role | Base Salary | Extra | Total Salary")
    print("-" * 75)

    for staff in staff_list:
        print(f"{staff[0]} | {staff[1]} | {staff[2]} | {staff[3]} | {staff[4]} | {staff[5]} | {staff[6]}")


def display_patients(patient_list):
    print("\nID | Name | Age | Disease | Days | Daily Fee | Medicine Fee | Total Fee")
    print("-" * 90)

    for patient in patient_list:
        print(f"{patient[0]} | {patient[1]} | {patient[2]} | {patient[3]} | {patient[4]} | {patient[5]} | {patient[6]} | {patient[7]}")


def staff_menu():
    while True:
        print("\n===== STAFF MANAGEMENT =====")
        print("1. Add staff")
        print("2. View staff list")
        print("3. Update staff")
        print("4. Delete staff")
        print("5. Search staff")
        print("6. Sort staff by salary")
        print("0. Back")

        choice = input("Choose: ")

        if choice == "1":
            name = input("Name: ")
            age = input_int("Age: ")
            role = input("Role Doctor/Nurse/AdminStaff: ")
            base_salary = input_float("Base salary: ")
            extra_value = input_float("Bonus/Overtime/Allowance: ")

            staff_service.add_staff(name, age, role, base_salary, extra_value)
            print("Staff added successfully.")

        elif choice == "2":
            display_staff(staff_service.get_all_staff())

        elif choice == "3":
            staff_id = input_int("Enter staff ID: ")
            name = input("New name: ")
            age = input_int("New age: ")
            role = input("New role Doctor/Nurse/AdminStaff: ")
            base_salary = input_float("New base salary: ")
            extra_value = input_float("New bonus/overtime/allowance: ")

            staff_service.update_staff(staff_id, name, age, role, base_salary, extra_value)
            print("Staff updated successfully.")

        elif choice == "4":
            staff_id = input_int("Enter staff ID: ")
            staff_service.delete_staff(staff_id)
            print("Staff deleted successfully.")

        elif choice == "5":
            keyword = input("Enter name or role: ")
            display_staff(staff_service.search_staff(keyword))

        elif choice == "6":
            display_staff(staff_service.sort_staff_by_salary())

        elif choice == "0":
            break

        else:
            print("Invalid choice.")


def patient_menu():
    while True:
        print("\n===== PATIENT MANAGEMENT =====")
        print("1. Add patient")
        print("2. View patient list")
        print("3. Update patient")
        print("4. Delete patient")
        print("5. Search patient")
        print("6. Sort patients by hospital fee")
        print("0. Back")

        choice = input("Choose: ")

        if choice == "1":
            name = input("Name: ")
            age = input_int("Age: ")
            disease = input("Disease: ")
            treatment_days = input_int("Treatment days: ")
            daily_fee = input_float("Daily fee: ")
            medicine_fee = input_float("Medicine fee: ")

            patient_service.add_patient(name, age, disease, treatment_days, daily_fee, medicine_fee)
            print("Patient added successfully.")

        elif choice == "2":
            display_patients(patient_service.get_all_patients())

        elif choice == "3":
            patient_id = input_int("Enter patient ID: ")
            name = input("New name: ")
            age = input_int("New age: ")
            disease = input("New disease: ")
            treatment_days = input_int("New treatment days: ")
            daily_fee = input_float("New daily fee: ")
            medicine_fee = input_float("New medicine fee: ")

            patient_service.update_patient(
                patient_id, name, age, disease, treatment_days, daily_fee, medicine_fee
            )
            print("Patient updated successfully.")

        elif choice == "4":
            patient_id = input_int("Enter patient ID: ")
            patient_service.delete_patient(patient_id)
            print("Patient deleted successfully.")

        elif choice == "5":
            keyword = input("Enter name or disease: ")
            display_patients(patient_service.search_patient(keyword))

        elif choice == "6":
            display_patients(patient_service.sort_patients_by_fee())

        elif choice == "0":
            break

        else:
            print("Invalid choice.")


def main_menu():
    while True:
        print("\n========== HOSPITAL / CLINIC MANAGEMENT SYSTEM ==========")
        print("1. Staff Management")
        print("2. Patient Management")
        print("0. Exit")

        choice = input("Choose: ")

        if choice == "1":
            staff_menu()
        elif choice == "2":
            patient_menu()
        elif choice == "0":
            print("Program ended.")
            break
        else:
            print("Invalid choice.")