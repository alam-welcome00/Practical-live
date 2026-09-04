import os
import pymupdf
THUMBNAIL_DIR = os.path.join("storage", "thumbnails")

class ThumbnailGenerator:

    def generating_thumbnail(self, pdf_path):
        os.makedirs(THUMBNAIL_DIR, exist_ok=True)

        doc = pymupdf.open(pdf_path)
        page = doc.load_page(0)
        pix = page.get_pixmap()

        base_name = os.path.basename(pdf_path).replace(".pdf", ".png")
        thumb_path = os.path.join(THUMBNAIL_DIR, base_name)

        pix.save(thumb_path)
        doc.close()

        return thumb_path

    def total_pages(self,pdf_path):
        doc = pymupdf.open(pdf_path)
        self.total_pages = len(doc)
        return self.total_pages