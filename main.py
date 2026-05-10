from menus.main_menu import MainMenu
from menus.borrower_menu import BorrowerMenu
from menus.admin_menu import AdminMenu

from services.authentication_service import AuthenticationService
from services.library_service import LibraryService
from services.borrower_service import BorrowerService
from services.admin_service import AdminService

from utils.input_helper import InputHelper
from utils.display_helper import DisplayHelper

from models.book import Book
from models.periodical import Periodical
from models.magazine import Magazine
from models.audiobook import AudioBook


class SOLASystem:

    def __init__(self):

        self.authentication_service = AuthenticationService()

        self.library_service = LibraryService()

        self.admin_service = AdminService()

    # =====================================
    # START SYSTEM
    # =====================================

    def run(self):

        while True:

            MainMenu.display()

            choice = InputHelper.get_integer(
                "Enter your choice: "
            )

            # =====================================
            # BORROWER LOGIN
            # =====================================

            if choice == 1:

                self.borrower_login_menu()

            # =====================================
            # ADMIN LOGIN
            # =====================================

            elif choice == 2:

                self.admin_login_menu()

            # =====================================
            # EXIT
            # =====================================

            elif choice == 3:

                print("Thank you for using SOLA.")

                break

            else:

                print("Invalid option.")

    # =====================================
    # BORROWER LOGIN MENU
    # =====================================

    def borrower_login_menu(self):

        DisplayHelper.display_header(
            "BORROWER LOGIN"
        )

        username = InputHelper.get_string(
            "Username: "
        )

        password = InputHelper.get_string(
            "Password: "
        )

        borrower = (
            self.authentication_service
            .borrower_login(
                username,
                password
            )
        )

        if borrower is not None:

            DisplayHelper.success(
                "Login successful."
            )

            self.borrower_menu(borrower)

        else:

            DisplayHelper.error(
                "Invalid username or password."
            )

    # =====================================
    # ADMIN LOGIN MENU
    # =====================================

    def admin_login_menu(self):

        DisplayHelper.display_header(
            "ADMIN LOGIN"
        )

        username = InputHelper.get_string(
            "Username: "
        )

        password = InputHelper.get_string(
            "Password: "
        )

        admin = (
            self.authentication_service
            .admin_login(
                username,
                password
            )
        )

        if admin is not None:

            DisplayHelper.success(
                "Login successful."
            )

            self.admin_menu()

        else:

            DisplayHelper.error(
                "Invalid username or password."
            )

    # =====================================
    # BORROWER MENU
    # =====================================

    def borrower_menu(self, borrower):

        while True:

            BorrowerMenu.display()

            choice = InputHelper.get_integer(
                "Enter your choice: "
            )

            # SEARCH BY TITLE

            if choice == 1:

                title = InputHelper.get_string(
                    "Enter title: "
                )

                result = (
                    self.library_service
                    .search_by_title(title)
                )

                DisplayHelper.display_results(result)

            # SEARCH BY AUTHOR

            elif choice == 2:

                author = InputHelper.get_string(
                    "Enter author: "
                )

                results = (
                    self.library_service
                    .search_by_author(author)
                )

                DisplayHelper.display_results(results)

            # SEARCH BY CATEGORY

            elif choice == 3:

                category = InputHelper.get_string(
                    "Enter category: "
                )

                results = (
                    self.library_service
                    .search_by_category(category)
                )

                DisplayHelper.display_results(results)

            # SEARCH BY LANGUAGE

            elif choice == 4:

                language = InputHelper.get_string(
                    "Enter language: "
                )

                results = (
                    self.library_service
                    .search_by_language(language)
                )

                DisplayHelper.display_results(results)

            # SEARCH BY YEAR

            elif choice == 5:

                year = InputHelper.get_integer(
                    "Enter year: "
                )

                results = (
                    self.library_service
                    .search_by_year(year)
                )

                DisplayHelper.display_results(results)

            # BORROW ITEM

            elif choice == 6:

                title = InputHelper.get_string(
                    "Enter title to borrow: "
                )

                item = (
                    self.library_service
                    .search_by_title(title)
                )

                if item is not None:

                    BorrowerService.borrow_item(
                        borrower,
                        item
                    )

                else:

                    DisplayHelper.error(
                        "Item not found."
                    )

            # RETURN ITEM

            elif choice == 7:

                title = InputHelper.get_string(
                    "Enter title to return: "
                )

                BorrowerService.return_item(
                    borrower,
                    title
                )

            # VIEW BORROWED ITEMS

            elif choice == 8:

                BorrowerService.display_borrowed_items(
                    borrower
                )

            # CHECK DUE DATE

            elif choice == 9:

                print(
                    "Due dates feature demo placeholder."
                )

            # VIEW FINE

            elif choice == 10:

                BorrowerService.view_fine(
                    borrower
                )

            # PAY FINE

            elif choice == 11:

                amount = InputHelper.get_float(
                    "Enter payment amount: "
                )

                BorrowerService.pay_fine(
                    borrower,
                    amount
                )

            # LOGOUT

            elif choice == 12:

                print("Logging out...")

                break

            else:

                print("Invalid option.")

    # =====================================
    # ADMIN MENU
    # =====================================

    def admin_menu(self):

        while True:

            AdminMenu.display()

            choice = InputHelper.get_integer(
                "Enter your choice: "
            )

            # DISPLAY ALL ITEMS

            if choice == 1:

                self.library_service.display_all_items()

            # ADD BOOK

            elif choice == 2:

                self.add_book()

            # ADD PERIODICAL

            elif choice == 3:

                self.add_periodical()

            # ADD MAGAZINE

            elif choice == 4:

                self.add_magazine()

            # ADD AUDIO BOOK

            elif choice == 5:

                self.add_audiobook()

            # SEARCH BORROWER

            elif choice == 6:

                username = InputHelper.get_string(
                    "Enter borrower username: "
                )

                borrower = (
                    self.admin_service
                    .search_borrower(username)
                )

                DisplayHelper.display_results(
                    borrower
                )

            # DISPLAY ALL BORROWERS

            elif choice == 7:

                self.admin_service.display_all_borrowers()

            # REMOVE BORROWER

            elif choice == 8:

                username = InputHelper.get_string(
                    "Enter borrower username: "
                )

                self.admin_service.remove_borrower(
                    username
                )

            # UPDATE BORROWER

            elif choice == 9:

                username = InputHelper.get_string(
                    "Enter borrower username: "
                )

                new_first_name = (
                    InputHelper.get_string(
                        "New first name: "
                    )
                )

                new_last_name = (
                    InputHelper.get_string(
                        "New last name: "
                    )
                )

                self.admin_service.update_borrower(
                    username,
                    new_first_name,
                    new_last_name
                )

            # LOGOUT

            elif choice == 10:

                print("Logging out...")

                break

            else:

                print("Invalid option.")

    # =====================================
    # ADD BOOK
    # =====================================

    def add_book(self):

        title = InputHelper.get_string(
            "Title: "
        )

        category = InputHelper.get_string(
            "Category: "
        )

        language = InputHelper.get_string(
            "Language: "
        )

        author = InputHelper.get_string(
            "Author: "
        )

        year = InputHelper.get_integer(
            "Year Published: "
        )

        isbn = InputHelper.get_string(
            "ISBN: "
        )

        book = Book(
            title,
            category,
            language,
            [author],
            year,
            isbn
        )

        self.library_service.add_item(book)

    # =====================================
    # ADD PERIODICAL
    # =====================================

    def add_periodical(self):

        title = InputHelper.get_string(
            "Title: "
        )

        category = InputHelper.get_string(
            "Category: "
        )

        language = InputHelper.get_string(
            "Language: "
        )

        author = InputHelper.get_string(
            "Author: "
        )

        year = InputHelper.get_integer(
            "Year Published: "
        )

        periodical = Periodical(
            title,
            category,
            language,
            [author],
            year
        )

        self.library_service.add_item(
            periodical
        )

    # =====================================
    # ADD MAGAZINE
    # =====================================

    def add_magazine(self):

        title = InputHelper.get_string(
            "Title: "
        )

        category = InputHelper.get_string(
            "Category: "
        )

        language = InputHelper.get_string(
            "Language: "
        )

        author = InputHelper.get_string(
            "Author: "
        )

        year = InputHelper.get_integer(
            "Year Published: "
        )

        magazine = Magazine(
            title,
            category,
            language,
            [author],
            year
        )

        self.library_service.add_item(
            magazine
        )

    # =====================================
    # ADD AUDIO BOOK
    # =====================================

    def add_audiobook(self):

        title = InputHelper.get_string(
            "Title: "
        )

        category = InputHelper.get_string(
            "Category: "
        )

        language = InputHelper.get_string(
            "Language: "
        )

        author = InputHelper.get_string(
            "Author: "
        )

        year = InputHelper.get_integer(
            "Year Published: "
        )

        audio_id = InputHelper.get_string(
            "Audio ID: "
        )

        audio_format = InputHelper.get_string(
            "Audio Format: "
        )

        audiobook = AudioBook(
            title,
            category,
            language,
            [author],
            year,
            audio_id,
            audio_format
        )

        self.library_service.add_item(
            audiobook
        )


# =====================================
# START APPLICATION
# =====================================

if __name__ == "__main__":

    system = SOLASystem()

    system.run()