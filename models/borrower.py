from models.user import User


class Borrower(User):

    def __init__(
            self,
            account_number,
            first_name,
            last_name,
            username,
            password):

        super().__init__(
            first_name,
            last_name,
            username,
            password
        )

        self.account_number = (
            account_number
        )

        # =========================
        # STORES:
        # {
        #   "item": item_object,
        #   "borrow_date": datetime,
        #   "due_date": datetime
        # }
        # =========================

        self.borrowed_items = []

        # =========================
        # BORROWER FINE
        # =========================

        self.fine = 0

    def __str__(self):

        return (
            f"Account Number: "
            f"{self.account_number}\n"
            f"Name: "
            f"{self.first_name} "
            f"{self.last_name}\n"
            f"Username: "
            f"{self.username}\n"
            f"Fine: "
            f"${self.fine}"
        )
