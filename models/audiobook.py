from models.library_item import LibraryItem


class AudioBook(LibraryItem):

    def __init__(
            self,
            title,
            category,
            language,
            authors,
            year_published,
            audio_id,
            audio_format):

        super().__init__(
            title,
            category,
            language,
            authors,
            year_published
        )

        self.audio_id = audio_id

        self.audio_format = audio_format

    # =========================
    # STRING DISPLAY
    # =========================

    def __str__(self):

        return (
            f"[AUDIO BOOK] "
            f"{super().__str__()} | "
            f"Audio ID: {self.audio_id} | "
            f"Format: {self.audio_format}"
        )