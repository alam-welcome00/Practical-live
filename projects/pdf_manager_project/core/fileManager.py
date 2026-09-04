from datetime import datetime
import os
PDF_STORAGE = os.path.join("storage", "pdf")

class FileManager:
    def save_pdf(self,uploaded_file):
        timestamp = datetime.now().strftime("%d%m%Y_%H%M%S")
        file_name = f"{timestamp}_{uploaded_file.name}"

        file_path = os.path.join(PDF_STORAGE, file_name)

        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())      

        return file_path