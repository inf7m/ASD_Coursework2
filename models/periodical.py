from models.library_item import LibraryItem


class Periodical(LibraryItem):

    def __init__(
            self,
            title,
            category,
            language,
            authors,
            year_published):

        super().__init__(
            title,
            category,
            language,
            authors,
            year_published
        )

    # =========================
    # STRING DISPLAY
    # =========================

    def __str__(self):

        return (
            f"[PERIODICAL] "
            f"{super().__str__()}"
        )