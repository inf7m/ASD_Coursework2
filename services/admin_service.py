from models.book import Book
from models.periodical import Periodical
from models.magazine import Magazine
from models.audio_book import AudioBook


class AdminService:

    def __init__(
            self,
            library_tree,
            borrower_list):

        self.library_tree = (
            library_tree
        )

        self.borrower_list = (
            borrower_list
        )

    # =========================
    # DISPLAY ALL ITEMS
    # =========================

    def display_all_items(self):

        return (
            self.library_tree
            .display_all_items()
        )

    # =========================
    # SEARCH BY TITLE
    # =========================

    def search_by_title(
            self,
            title):

        return (
            self.library_tree
            .search_by_title(title)
        )

    # =========================
    # SEARCH BY AUTHOR
    # =========================

    def search_by_author(
            self,
            author):

        return (
            self.library_tree
            .search_by_author(author)
        )

    # =========================
    # ADD NEW ITEM
    # =========================

    def add_item(self):

        print("\nSelect Item Type:")
        print("1. Book")
        print("2. Periodical")
        print("3. Magazine")
        print("4. Audio Book")

        choice = input(
            "Enter choice: "
        )

        title = input("Title: ")
        category = input("Category: ")
        language = input("Language: ")

        authors_input = input(
            "Authors (comma separated): "
        )

        authors = [
            author.strip()
            for author in authors_input.split(",")
        ]

        year_published = int(
            input("Year Published: ")
        )

        # =========================
        # BOOK
        # =========================

        if choice == "1":

            isbn = input("ISBN: ")

            item = Book(
                title,
                category,
                language,
                authors,
                isbn,
                year_published
            )

        # =========================
        # PERIODICAL
        # =========================

        elif choice == "2":

            item = Periodical(
                title,
                category,
                language,
                authors,
                year_published
            )

        # =========================
        # MAGAZINE
        # =========================

        elif choice == "3":

            item = Magazine(
                title,
                category,
                language,
                authors,
                year_published
            )

        # =========================
        # AUDIO BOOK
        # =========================

        elif choice == "4":

            isbn = input("ISBN: ")

            audio_format = input(
                "Audio Format: "
            )

            item = AudioBook(
                title,
                category,
                language,
                authors,
                isbn,
                audio_format,
                year_published
            )

        else:

            print("\nInvalid choice.")

            return

        self.library_tree.insert(item)

        print(
            "\nItem added successfully."
        )

    # =========================
    # REMOVE ITEM
    # =========================

    def remove_item(
            self,
            title):

        item = (
            self.library_tree
            .search_by_title(title)
        )

        if item is None:

            print("\nItem not found.")

            return

        self.library_tree.remove(title)

        print(
            f"\n'{title}' removed successfully."
        )

    # =========================
    # DISPLAY BORROWERS
    # =========================

    def display_borrowers(self):

        current = (
            self.borrower_list.head
        )

        while current is not None:

            print(current.borrower)

            print("-" * 40)

            current = current.next

    # =========================
    # DISPLAY BORROWERS
    # WITH FINES
    # =========================

    def display_borrowers_with_fines(self):

        current = (
            self.borrower_list.head
        )

        found = False

        while current is not None:

            borrower = current.borrower

            if borrower.fine > 0:

                print(borrower)

                print("-" * 40)

                found = True

            current = current.next

        if not found:

            print(
                "\nNo borrowers with fines."
            )

    # =========================
    # DISPLAY BORROWED ITEMS
    # =========================

    def display_borrowed_items(self):

        current = (
            self.borrower_list.head
        )

        while current is not None:

            borrower = current.borrower

            print(
                f"\nBorrower: "
                f"{borrower.first_name} "
                f"{borrower.last_name}"
            )

            if (
                    len(
                        borrower.borrowed_items
                    )
                    ==
                    0
            ):

                print(
                    "No borrowed items."
                )

            else:

                for record in (
                        borrower.borrowed_items
                ):

                    item = record["item"]

                    print(
                        f"- {item.title}"
                    )

                    print(
                        f"  Due Date: "
                        f"{record['due_date'].strftime('%Y-%m-%d')}"
                    )

            print("-" * 40)

            current = current.next
