# HOSPITAL / CLINIC MANAGEMENT SYSTEM

---

# 1. Project Description

This project is a Python console application developed using **Object-Oriented Programming (OOP)** principles and **SQLite Database**.

The system is designed to help hospitals or clinics manage staff information, patient records, salary calculations, hospital fee calculations, and reporting activities through a Command Line Interface (CLI).

The application supports:

* Staff Management
* Patient Management
* Search and Sort Operations
* Salary Calculation
* Hospital Fee Calculation
* Statistics and Reports
* CSV Report Export
* SQLite Database Storage

---

# 2. Project Objective

The objectives of this project are:

* Practice Object-Oriented Programming concepts
* Apply Layered Architecture design
* Manage hospital staff efficiently
* Manage patient treatment records
* Calculate staff salaries automatically
* Calculate hospital fees for patients
* Generate statistical reports
* Store data permanently using SQLite

---

# 3. OOP Concepts Applied

## 3.1 Encapsulation

Private attributes are used to protect data inside classes.

Example:

```python
self.__name
self.__age
self.__base_salary
```

Access to these attributes is provided through property methods.

---

## 3.2 Inheritance

The system applies inheritance through the Staff hierarchy.

```text
Staff
├── Doctor
├── Nurse
└── AdminStaff
```

All subclasses inherit common attributes and behaviors from the Staff class.

---

## 3.3 Abstraction

The Staff class is implemented as an abstract class.

```python
class Staff(ABC):
```

Abstract methods:

```python
calculate_salary()
get_role()
```

must be implemented by all subclasses.

---

## 3.4 Polymorphism

Each staff type calculates salary differently.

```python
Doctor.calculate_salary()

Nurse.calculate_salary()

AdminStaff.calculate_salary()
```

The system can call:

```python
staff.calculate_salary()
```

without knowing the exact subclass type.

---

# 4. Technologies Used

| Component    | Purpose                   |
| ------------ | ------------------------- |
| Python 3     | Main programming language |
| SQLite       | Data storage              |
| OOP          | Software design           |
| CLI          | User interaction          |
| CSV          | Report export             |
| Git & GitHub | Version control           |

---

# 5. Project Structure

```text
Hospital-Management-System
│
├── Models
│   ├── patient.py
│   └── staff.py
│
├── Services
│   ├── database.py
│   ├── patient_service.py
│   ├── staff_service.py
│   └── report_service.py
│
├── Views
│   └── menu.py
│
├── hospital.db
├── main.py
└── README.md
```

---

# 6. Main Features

## 6.1 Staff Management

The system allows users to:

* Add staff
* View staff list
* Update staff information
* Delete staff
* Search staff
* Sort staff by salary

---

## 6.2 Patient Management

The system allows users to:

* Add patient
* View patient list
* Update patient information
* Delete patient
* Search patient
* Sort patients by hospital fee

---

## 6.3 Salary Calculation

Doctor salary:

```python
salary = base_salary + bonus
```

Nurse salary:

```python
salary = base_salary + overtime_pay
```

Admin Staff salary:

```python
salary = base_salary + allowance
```

---

## 6.4 Hospital Fee Calculation

Hospital fee is calculated using:

```python
hospital_fee =
(treatment_days * daily_fee)
+ medicine_fee
```

---

## 6.5 Search Features

Staff Search:

* Search by name
* Search by role

Patient Search:

* Search by name
* Search by disease

---

## 6.6 Sorting Features

Staff:

* Sort by total salary (descending)

Patients:

* Sort by total hospital fee (descending)

---

## 6.7 Reports & Statistics

The reporting module provides:

* Total Staff
* Total Patients
* Total Salary Expense
* Total Hospital Revenue

---

## 6.8 Export CSV Report

The system can generate:

```text
hospital_report.csv
```

The exported report contains:

* Total Staff
* Total Patients
* Total Salary Expense
* Total Hospital Revenue

---

## 6.9 Exception Handling

The application validates:

* Integer input
* Float input
* Negative values
* Invalid menu selections
* Invalid staff roles

This helps prevent invalid data from being stored in the database.

---

# 7. Database Design

## Staff Table

| Field       | Type    |
| ----------- | ------- |
| id          | INTEGER |
| name        | TEXT    |
| age         | INTEGER |
| role        | TEXT    |
| base_salary | REAL    |
| extra_value | REAL    |

---

## Patients Table

| Field          | Type    |
| -------------- | ------- |
| id             | INTEGER |
| name           | TEXT    |
| age            | INTEGER |
| disease        | TEXT    |
| treatment_days | INTEGER |
| daily_fee      | REAL    |
| medicine_fee   | REAL    |

---

# 8. System Menu

Main Menu:

```text
HOSPITAL / CLINIC MANAGEMENT SYSTEM

1. Staff Management
2. Patient Management
3. Reports
0. Exit
```

---

Staff Menu:

```text
1. Add staff
2. View staff list
3. Update staff
4. Delete staff
5. Search staff
6. Sort staff by salary
0. Back
```

---

Patient Menu:

```text
1. Add patient
2. View patient list
3. Update patient
4. Delete patient
5. Search patient
6. Sort patients by hospital fee
0. Back
```

---

Reports Menu:

```text
1. Total Staff
2. Total Patients
3. Total Salary Expense
4. Total Hospital Revenue
5. Export Report CSV
0. Back
```

---

# 9. How To Run

Step 1:

```bash
git clone https://github.com/zitcon/Hospital-management-system.git
```

Step 2:

```bash
cd Hospital-management-system
```

Step 3:

```bash
python main.py
```

---

# 10. Git Workflow

The project follows a structured Git workflow:

1. Create repository
2. Develop features
3. Commit changes
4. Push to GitHub
5. Update documentation
6. Final project submission

---

# 11. Self Assessment

| Criteria             | Status    |
| -------------------- | --------- |
| Encapsulation        | Completed |
| Inheritance          | Completed |
| Abstraction          | Completed |
| Polymorphism         | Completed |
| Layered Architecture | Completed |
| CRUD Operations      | Completed |
| Search Function      | Completed |
| Sorting Function     | Completed |
| SQLite Database      | Completed |
| Exception Handling   | Completed |
| Reports & Statistics | Completed |
| CSV Export           | Completed |
| GitHub Repository    | Completed |

---

# 12. Author

Student: Nguyễn Võ Yên Khanh

Course: Programming Methods

Project: Hospital / Clinic Management System
