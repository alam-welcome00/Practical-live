# upload documents
# -->uploaded_file, tags, description, date
# -->uploaded_file -->.pdf
# -->uploaded_file -->folder with the same name as pdf --> extract all image
# -->uploaded_file--> Total number of pages
# -->uploaded_file-->date time

from db.repsitory import DocumentRepsitory
from datetime import datetime
import os
from core.fileManager import FileManager
from core.thumbnail import ThumbnailGenerator
PDF_STORAGE = os.path.join("storage", "pdf")

class DocumentService:
    def __init__(self):
        self.repo = DocumentRepsitory()
        self.file_manager = FileManager()
        self.thumbnail_generator = ThumbnailGenerator()
    def upload_doc(self, uploaded_file, tags, description, lecture_Date=None):

        doc = []
        file_path = self.file_manager.save_pdf(uploaded_file)

        # 2.GENERATED THUMBNAIL
        thumbnail = self.thumbnail_generator.generating_thumbnail(file_path)
        # 3.GET TOTAL PAGE
        total_page = self.thumbnail_generator.total_pages(file_path)
        # 4.CONVERT PAGES

        # 5.CREATE REQUIRED VARIABLE ->UPLOADED DATE
        # 6.SAVE TO DB
        # self.repo.add_document(doc)