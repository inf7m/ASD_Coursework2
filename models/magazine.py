from models.periodical import Periodical


class Magazine(Periodical):

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
            f"[MAGAZINE] "
            f"{super().__str__()}"
        )