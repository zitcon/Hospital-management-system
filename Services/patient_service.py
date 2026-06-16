from Models.patient import Patient
from Services.database import get_connection


class PatientService:
    def create_patient_object(self, name, age, disease, treatment_days, daily_fee, medicine_fee):
        return Patient(name, age, disease, treatment_days, daily_fee, medicine_fee)

    def add_patient(self, name, age, disease, treatment_days, daily_fee, medicine_fee):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO patients (name, age, disease, treatment_days, daily_fee, medicine_fee)
        VALUES (?, ?, ?, ?, ?, ?)
        """, (name, age, disease, treatment_days, daily_fee, medicine_fee))

        conn.commit()
        conn.close()

    def get_all_patients(self):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        SELECT id, name, age, disease, treatment_days, daily_fee, medicine_fee
        FROM patients
        """)

        rows = cursor.fetchall()
        conn.close()

        result = []
        for row in rows:
            patient_id, name, age, disease, treatment_days, daily_fee, medicine_fee = row
            patient = self.create_patient_object(
                name, age, disease, treatment_days, daily_fee, medicine_fee
            )
            total_fee = patient.calculate_hospital_fee()
            result.append((
                patient_id, name, age, disease,
                treatment_days, daily_fee, medicine_fee, total_fee
            ))

        return result

    def update_patient(self, patient_id, name, age, disease, treatment_days, daily_fee, medicine_fee):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        UPDATE patients
        SET name = ?, age = ?, disease = ?, treatment_days = ?, daily_fee = ?, medicine_fee = ?
        WHERE id = ?
        """, (name, age, disease, treatment_days, daily_fee, medicine_fee, patient_id))

        conn.commit()
        conn.close()

    def delete_patient(self, patient_id):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("DELETE FROM patients WHERE id = ?", (patient_id,))

        conn.commit()
        conn.close()

    def search_patient(self, keyword):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        SELECT id, name, age, disease, treatment_days, daily_fee, medicine_fee
        FROM patients
        WHERE name LIKE ? OR disease LIKE ?
        """, (f"%{keyword}%", f"%{keyword}%"))

        rows = cursor.fetchall()
        conn.close()

        result = []
        for row in rows:
            patient_id, name, age, disease, treatment_days, daily_fee, medicine_fee = row
            patient = self.create_patient_object(
                name, age, disease, treatment_days, daily_fee, medicine_fee
            )
            total_fee = patient.calculate_hospital_fee()
            result.append((
                patient_id, name, age, disease,
                treatment_days, daily_fee, medicine_fee, total_fee
            ))

        return result

    def sort_patients_by_fee(self):
        patient_list = self.get_all_patients()
        return sorted(patient_list, key=lambda x: x[7], reverse=True)