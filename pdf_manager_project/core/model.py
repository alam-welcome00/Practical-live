class Document:
    def __init__(
        self,
        id=None,
        name=None,
        path=None,
        thumbnail_path=None,
        tags=None,
        description=None,
        uploaded_date=None,
        lecture_date=None,
        total_pages=None
    ):
        self.id = id
        self.name = name
        self.path = path
        self.thumbnail_path = thumbnail_path
        self.tags = tags
        self.description = description
        self.uploaded_date = uploaded_date
        self.lecture_date = lecture_date
        self.total_pages = total_pages