from generate_data.generate_borrowers import GenerateBorrowers
from generate_data.generate_admins import GenerateAdmins


class AuthenticationService:

    def __init__(self):

        self.borrowers = GenerateBorrowers.generate()

        self.admins = GenerateAdmins.generate()

    # =========================
    # BORROWER LOGIN
    # =========================

    def borrower_login(self, username, password):

        for borrower in self.borrowers:

            if borrower.username == username:

                if borrower.check_password(password):

                    return borrower

        return None

    # =========================
    # ADMIN LOGIN
    # =========================

    def admin_login(self, username, password):

        for admin in self.admins:

            if admin.username == username:

                if admin.check_password(password):

                    return admin

        return None