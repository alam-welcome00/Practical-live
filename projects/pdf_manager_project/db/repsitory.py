from db.database import get_connection
from core.model import Document


class DocumentRepsitory:

    def add_document(self, doc: Document):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO documents(
            name,
            path,
            thumbnail_path,
            tags,
            description,
            uploaded_date,
            lecture_date,
            total_pages
        )
        VALUES(?,?,?,?,?,?,?,?)
        """,
        (
            doc.name,
            doc.path,
            doc.thumbnail_path,
            doc.tags,
            doc.description,
            doc.uploaded_date,
            doc.lecture_date,
            doc.total_pages
        ))

        conn.commit()
        conn.close()

    def search_doc(self, tags=None, date=None):

        conn = get_connection()
        cursor = conn.cursor()

        query = "SELECT * FROM documents"

        conditions = []
        params = []

        if tags:
            conditions.append("tags LIKE ?")
            params.append(f"%{tags}%")

        if date:
            conditions.append("lecture_date=?")
            params.append(date)

        if conditions:
            query += " WHERE " + " AND ".join(conditions)

        cursor.execute(query, params)

        rows = cursor.fetchall()

        conn.close()

        return [Document(*row) for row in rows]
    
    def get_all_doc(self):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM documents")
        rows =cursor.fetchall()
        conn.close()

        return[Document(*row) for row in rows]