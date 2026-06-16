from Models.staff import Doctor, Nurse, AdminStaff
from Services.database import get_connection


class StaffService:
    def create_staff_object(self, name, age, role, base_salary, extra_value):
        if role == "Doctor":
            return Doctor(name, age, base_salary, extra_value)
        elif role == "Nurse":
            return Nurse(name, age, base_salary, extra_value)
        elif role == "AdminStaff":
            return AdminStaff(name, age, base_salary, extra_value)
        else:
            raise ValueError("Invalid staff role")

    def add_staff(self, name, age, role, base_salary, extra_value):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO staff (name, age, role, base_salary, extra_value)
        VALUES (?, ?, ?, ?, ?)
        """, (name, age, role, base_salary, extra_value))

        conn.commit()
        conn.close()

    def get_all_staff(self):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        SELECT id, name, age, role, base_salary, extra_value
        FROM staff
        """)

        rows = cursor.fetchall()
        conn.close()

        result = []
        for row in rows:
            staff_id, name, age, role, base_salary, extra_value = row
            staff = self.create_staff_object(name, age, role, base_salary, extra_value)
            total_salary = staff.calculate_salary()
            result.append((staff_id, name, age, role, base_salary, extra_value, total_salary))

        return result

    def update_staff(self, staff_id, name, age, role, base_salary, extra_value):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        UPDATE staff
        SET name = ?, age = ?, role = ?, base_salary = ?, extra_value = ?
        WHERE id = ?
        """, (name, age, role, base_salary, extra_value, staff_id))

        conn.commit()
        conn.close()

    def delete_staff(self, staff_id):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("DELETE FROM staff WHERE id = ?", (staff_id,))

        conn.commit()
        conn.close()

    def search_staff(self, keyword):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        SELECT id, name, age, role, base_salary, extra_value
        FROM staff
        WHERE name LIKE ? OR role LIKE ?
        """, (f"%{keyword}%", f"%{keyword}%"))

        rows = cursor.fetchall()
        conn.close()

        result = []
        for row in rows:
            staff_id, name, age, role, base_salary, extra_value = row
            staff = self.create_staff_object(name, age, role, base_salary, extra_value)
            total_salary = staff.calculate_salary()
            result.append((staff_id, name, age, role, base_salary, extra_value, total_salary))

        return result

    def sort_staff_by_salary(self):
        staff_list = self.get_all_staff()
        return sorted(staff_list, key=lambda x: x[6], reverse=True)