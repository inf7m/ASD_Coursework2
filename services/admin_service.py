from data_structures.borrower_list import BorrowerList

from generate_data.generate_borrowers import GenerateBorrowers


class AdminService:

    def __init__(self):

        self.borrower_list = BorrowerList()

        self.load_borrowers()

    # =========================
    # LOAD BORROWERS INTO DLL
    # =========================

    def load_borrowers(self):

        borrowers = GenerateBorrowers.generate()

        for borrower in borrowers:

            self.borrower_list.add_borrower(borrower)

    # =========================
    # DISPLAY ALL BORROWERS
    # =========================

    def display_all_borrowers(self):

        self.borrower_list.display_all_borrowers()

    # =========================
    # SEARCH BORROWER
    # =========================

    def search_borrower(self, username):

        return self.borrower_list.search_borrower(username)

    # =========================
    # REMOVE BORROWER
    # =========================

    def remove_borrower(self, username):

        success = self.borrower_list.remove_borrower(username)

        if success:

            print("Borrower removed successfully.")

        else:

            print("Borrower not found.")

    # =========================
    # UPDATE BORROWER
    # =========================

    def update_borrower(
            self,
            username,
            new_first_name,
            new_last_name):

        success = self.borrower_list.update_borrower_name(
            username,
            new_first_name,
            new_last_name
        )

        if success:

            print("Borrower updated successfully.")

        else:

            print("Borrower not found.")