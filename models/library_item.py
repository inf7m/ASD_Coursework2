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

        # =========================
        # AUTHORS STORED AS A LIST
        # =========================

        self.authors = authors

        self.year_published = (
            year_published
        )

    def __str__(self):

        authors_text = ", ".join(
            self.authors
        )

        return (
            f"Title: {self.title}\n"
            f"Category: {self.category}\n"
            f"Language: {self.language}\n"
            f"Authors: {authors_text}\n"
            f"Year Published: "
            f"{self.year_published}"
        )
