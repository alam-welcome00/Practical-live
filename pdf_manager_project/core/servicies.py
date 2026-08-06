from datetime import datetime

from db.repsitory import DocumentRepsitory
from core.model import Document
from core.fileManager import FileManager
from core.thumbnail import ThumbnailGenerator
from core.reader import ReadPdf


class DocumentService:

    def __init__(self):

        self.repo = DocumentRepsitory()
        self.file_manager = FileManager()
        self.thumbnail_generator = ThumbnailGenerator()
        self.read_image = ReadPdf()

    def upload_doc(self, uploaded_file, tags, description, lecture_date=None):

        file_path = self.file_manager.save_pdf(uploaded_file)

        thumbnail = self.thumbnail_generator.generating_thumbnail(file_path)

        total_pages = self.thumbnail_generator.total_pages(file_path)

        self.read_image.conver_to_image(file_path)

        uploaded_date = datetime.now().strftime("%Y-%m-%d")

        doc = Document(
            name=uploaded_file.name,
            path=file_path,
            thumbnail_path=thumbnail,
            tags=tags,
            description=description,
            uploaded_date=uploaded_date,
            lecture_date=str(lecture_date) if lecture_date else None,
            total_pages=total_pages
        )

        self.repo.add_document(doc)

    def search_doc(self, tags=None, date=None):

        return self.repo.search_doc(tags, date)


    def get_all_doc(self):
        return self.repo.get_all_doc()


