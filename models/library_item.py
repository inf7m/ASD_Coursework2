class LibraryItem:

    def __init__(
            self,
            title,
            category,
            language,
            authors,
            year_published):

        self.title = title

        self.category = category

        self.language = language

        self.authors = authors

        self.year_published = year_published

    # =========================
    # STRING DISPLAY
    # =========================

    def __str__(self):

        return (
            f"Title: {self.title} | "
            f"Category: {self.category} | "
            f"Language: {self.language} | "
            f"Authors: {', '.join(self.authors)} | "
            f"Year: {self.year_published}"
        )