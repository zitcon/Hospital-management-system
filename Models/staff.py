from abc import ABC, abstractmethod


class Staff(ABC):
    def __init__(self, name, age, base_salary):
        self.__name = name
        self.__age = age
        self.__base_salary = base_salary

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @property
    def base_salary(self):
        return self.__base_salary

    @abstractmethod
    def calculate_salary(self):
        pass

    @abstractmethod
    def get_role(self):
        pass


class Doctor(Staff):
    def __init__(self, name, age, base_salary, bonus):
        super().__init__(name, age, base_salary)
        self.__bonus = bonus

    def calculate_salary(self):
        return self.base_salary + self.__bonus

    def get_role(self):
        return "Doctor"


class Nurse(Staff):
    def __init__(self, name, age, base_salary, overtime_pay):
        super().__init__(name, age, base_salary)
        self.__overtime_pay = overtime_pay

    def calculate_salary(self):
        return self.base_salary + self.__overtime_pay

    def get_role(self):
        return "Nurse"


class AdminStaff(Staff):
    def __init__(self, name, age, base_salary, allowance):
        super().__init__(name, age, base_salary)
        self.__allowance = allowance

    def calculate_salary(self):
        return self.base_salary + self.__allowance

    def get_role(self):
        return "AdminStaff"