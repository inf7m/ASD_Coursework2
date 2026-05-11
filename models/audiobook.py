from models.library_item import (
    LibraryItem
)


class AudioBook(LibraryItem):

    def __init__(
            self,
            title,
            category,
            language,
            authors,
            isbn,
            audio_format,
            year_published):

        super().__init__(
            title,
            category,
            language,
            authors,
            year_published
        )

        self.isbn = isbn

        # =========================
        # AUDIO FORMAT
        # Example:
        # mp3, au, wav
        # =========================

        self.audio_format = (
            audio_format
        )

    def __str__(self):

        return (
            super().__str__()
            +
            f"\nISBN: {self.isbn}"
            +
            f"\nAudio Format: "
            f"{self.audio_format}"
        )
