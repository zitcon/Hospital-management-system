from services.database import get_connection


class StaffService:
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
        SELECT id, name, age, role, base_salary, extra_value,
        base_salary + extra_value AS total_salary
        FROM staff
        """)

        result = cursor.fetchall()
        conn.close()
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
        SELECT id, name, age, role, base_salary, extra_value,
        base_salary + extra_value AS total_salary
        FROM staff
        WHERE name LIKE ? OR role LIKE ?
        """, (f"%{keyword}%", f"%{keyword}%"))

        result = cursor.fetchall()
        conn.close()
        return result

    def sort_staff_by_salary(self):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        SELECT id, name, age, role, base_salary, extra_value,
        base_salary + extra_value AS total_salary
        FROM staff
        ORDER BY total_salary DESC
        """)

        result = cursor.fetchall()
        conn.close()
        return result