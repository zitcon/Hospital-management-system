# Hospital / Clinic Management System

## Project Information

**Project Title:** Hospital / Clinic Management System

**Course:** Programming Methods

**Student:** Nguyễn Võ Yên Khanh

**University:** Hue University of Education

**Faculty:** Faculty of Informatics

**Programming Language:** Python

**Database:** SQLite

**Version Control:** Git & GitHub

---

# 1. Project Description

The Hospital / Clinic Management System is a Python-based application developed using Object-Oriented Programming (OOP) principles and Layered Architecture.

The system helps manage hospital staff and patients efficiently. It supports staff salary calculation, patient hospital fee calculation, CRUD operations, searching, sorting, and permanent data storage using SQLite database.

The project demonstrates the practical application of OOP concepts including Encapsulation, Inheritance, Polymorphism, and Abstraction.

---

# 2. Main Features

## Staff Management

Manage three types of staff:

* Doctor
* Nurse
* Administrative Staff

Functions:

* Add staff
* View staff list
* Update staff information
* Delete staff
* Search staff by name or role
* Sort staff by total salary

---

## Patient Management

Functions:

* Add patient
* View patient list
* Update patient information
* Delete patient
* Search patient by name or disease
* Sort patients by hospital fee

---

## Salary Calculation

The system automatically calculates staff salaries based on:

### Doctor

Total Salary = Base Salary + Bonus

### Nurse

Total Salary = Base Salary + Overtime Pay

### Administrative Staff

Total Salary = Base Salary + Allowance

---

## Hospital Fee Calculation

The system automatically calculates hospital fees:

Hospital Fee = (Treatment Days × Daily Fee) + Medicine Fee

---

# 3. Object-Oriented Programming (OOP)

This project implements all four pillars of Object-Oriented Programming.

## 3.1 Encapsulation

Sensitive attributes are declared as private attributes using double underscores (__attribute).

Examples:

* Staff name
* Staff age
* Base salary
* Patient information

Data is accessed through properties and class methods.

---

## 3.2 Inheritance

The Staff class serves as a parent class.

Child classes:

* Doctor
* Nurse
* AdminStaff

These subclasses inherit common properties and behaviors from the Staff class.

---

## 3.3 Polymorphism

Each child class overrides the salary calculation behavior.

Examples:

* Doctor calculates salary using bonus.
* Nurse calculates salary using overtime payment.
* AdminStaff calculates salary using allowance.

The same method name is used with different implementations.

---

## 3.4 Abstraction

The Staff class is implemented as an Abstract Base Class (ABC).

Abstract methods:

* calculate_salary()
* get_role()

Child classes must implement these methods.

---

# 4. Layered Architecture

The project follows a three-layer architecture.

## models/

Contains data models and OOP class definitions.

Files:

* staff.py
* patient.py

---

## services/

Contains business logic and database operations.

Files:

* database.py
* staff_service.py
* patient_service.py

---

## views/

Contains the Command Line Interface (CLI).

Files:

* menu.py

---

# 5. Project Structure

```text
Hospital_Management/
│
├── models/
│   ├── __init__.py
│   ├── staff.py
│   └── patient.py
│
├── services/
│   ├── __init__.py
│   ├── database.py
│   ├── staff_service.py
│   └── patient_service.py
│
├── views/
│   ├── __init__.py
│   └── menu.py
│
├── main.py
├── hospital.db
├── README.md
└── .gitignore
```

# 6. Database Design

The application uses SQLite for permanent data storage.

## Staff Table

Fields:

* id
* name
* age
* role
* base_salary
* extra_value

## Patients Table

Fields:

* id
* name
* age
* disease
* treatment_days
* daily_fee
* medicine_fee

Data is automatically saved in the SQLite database and remains available after restarting the application.

---

# 7. Search and Sort

## Search

Staff:

* Search by name
* Search by role

Patients:

* Search by name
* Search by disease

## Sort

Staff:

* Sort by total salary (descending)

Patients:

* Sort by hospital fee (descending)

---

# 8. Exception Handling

The system uses try-except blocks to handle invalid user input.

Examples:

* Non-numeric values entered for age
* Invalid salary values
* Invalid fee values

This prevents the application from crashing unexpectedly.

---

# 9. Technologies Used

* Python 3
* SQLite
* Object-Oriented Programming (OOP)
* Git
* GitHub
* Visual Studio Code

---

# 10. How to Run the Program

## Step 1

Open the project folder in Visual Studio Code.

## Step 2

Open Terminal.

## Step 3

Run the following command:

```bash
python main.py
```

## Step 4

Use the menu options to manage staff and patients.

---

# 11. Git & GitHub

The project uses Git for version control and GitHub for source code management.

Logical commits are created throughout the development process, including:

* Project structure creation
* SQLite implementation
* OOP model implementation
* CRUD operations
* CLI interface development
* Formatting improvements
* Documentation updates

---

# 12. Future Improvements

Possible future enhancements:

* Graphical User Interface (GUI)
* Statistical reports
* Export reports to CSV/PDF
* User authentication system
* Appointment scheduling
* Doctor-patient assignment management

---

# 13. Conclusion

This project successfully demonstrates the use of Object-Oriented Programming principles, Layered Architecture, SQLite database management, CRUD operations, searching, sorting, exception handling, and Git/GitHub workflow.

The system provides a practical solution for managing hospital staff and patients while fulfilling the academic requirements of the course.

---

**Author:** Nguyễn Võ Yên Khanh

**Faculty of Informatics – Hue University of Education**
