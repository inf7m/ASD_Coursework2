from models.library_item import LibraryItem


class Book(LibraryItem):

    def __init__(
            self,
            title,
            category,
            language,
            authors,
            year_published,
            isbn):

        super().__init__(
            title,
            category,
            language,
            authors,
            year_published
        )

        self.isbn = isbn

    # =========================
    # STRING DISPLAY
    # =========================

    def __str__(self):

        return (
            f"[BOOK] "
            f"{super().__str__()} | "
            f"ISBN: {self.isbn}"
        )