from db.database import get_connection
from datetime import datetime

class Analytics_service:
    def record_page_visit(self,document_id,page_number):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO page_visites (document_id, page_number, time_stamp)
            VALUES (?,?,?)
                """,(document_id,page_number,datetime.now().isoformat()))

        conn.commit()
        conn.close()

    def get_unique_page_count(self, document_id):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT COUNT(DISTINCT page_number)
            FROM page_visites
            WHERE document_id = ?
        """, (document_id,))

        result = cursor.fetchone()

        conn.close()

        return result[0] if result else 0

    def record_app_visit(self, event_type):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO app_visits (event_type, time_stamp)
        VALUES (?,?)
""", (event_type, datetime.now().isoformat()))

        conn.commit()
        conn.close()


    def get_app_visit(self):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT event_type, count(*)
            from app_visits
            GROUP BY event_type        
""")
        data = cursor.fetchall()
        conn.close()

        return data


    def reset_analytics(self):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("DELETE from page_visites")
        cursor.execute("DELETE from app_visits")

        conn.commit()
        conn.close()     