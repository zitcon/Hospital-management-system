class Patient:
    def __init__(self, name, age, disease, treatment_days, daily_fee, medicine_fee):
        self.__name = name
        self.__age = age
        self.__disease = disease
        self.__treatment_days = treatment_days
        self.__daily_fee = daily_fee
        self.__medicine_fee = medicine_fee

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @property
    def disease(self):
        return self.__disease

    @property
    def treatment_days(self):
        return self.__treatment_days

    @property
    def daily_fee(self):
        return self.__daily_fee

    @property
    def medicine_fee(self):
        return self.__medicine_fee

    def calculate_hospital_fee(self):
        return self.__treatment_days * self.__daily_fee + self.__medicine_fee