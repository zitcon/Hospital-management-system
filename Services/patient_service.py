from services.database import get_connection


class PatientService:
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
        SELECT id, name, age, disease, treatment_days, daily_fee, medicine_fee,
        treatment_days * daily_fee + medicine_fee AS total_fee
        FROM patients
        """)

        result = cursor.fetchall()
        conn.close()
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
        SELECT id, name, age, disease, treatment_days, daily_fee, medicine_fee,
        treatment_days * daily_fee + medicine_fee AS total_fee
        FROM patients
        WHERE name LIKE ? OR disease LIKE ?
        """, (f"%{keyword}%", f"%{keyword}%"))

        result = cursor.fetchall()
        conn.close()
        return result

    def sort_patients_by_fee(self):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        SELECT id, name, age, disease, treatment_days, daily_fee, medicine_fee,
        treatment_days * daily_fee + medicine_fee AS total_fee
        FROM patients
        ORDER BY total_fee DESC
        """)

        result = cursor.fetchall()
        conn.close()
        return result