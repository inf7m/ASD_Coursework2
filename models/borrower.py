from models.user import User


class Borrower(User):

    MAX_BORROW_LIMIT = 8

    def __init__(
            self,
            username,
            password,
            first_name,
            last_name,
            borrower_id):

        super().__init__(
            username,
            password,
            first_name,
            last_name
        )

        self.borrower_id = borrower_id

        self.borrowed_items = []

        self.fine = 0

    # =========================
    # BORROW ITEM
    # =========================

    def borrow_item(self, item):

        if self.fine > 0:

            print("Cannot borrow items with unpaid fine.")

            return False

        if len(self.borrowed_items) >= self.MAX_BORROW_LIMIT:

            print("Borrow limit reached.")

            return False

        self.borrowed_items.append(item)

        print(f"{item.title} borrowed successfully.")

        return True

    # =========================
    # RETURN ITEM
    # =========================

    def return_item(self, item_title):

        for item in self.borrowed_items:

            if item.title.lower() == item_title.lower():

                self.borrowed_items.remove(item)

                print(f"{item.title} returned successfully.")

                return True

        print("Item not found.")

        return False

    # =========================
    # PAY FINE
    # =========================

    def pay_fine(self, amount):

        if amount <= 0:

            print("Invalid amount.")

            return

        self.fine -= amount

        if self.fine < 0:

            self.fine = 0

        print("Fine paid successfully.")

    # =========================
    # VIEW BORROWED ITEMS
    # =========================

    def display_borrowed_items(self):

        if len(self.borrowed_items) == 0:

            print("No borrowed items.")

            return

        print("\nBorrowed Items:")

        for item in self.borrowed_items:

            print(item)

    # =========================
    # STRING DISPLAY
    # =========================

    def __str__(self):

        return (
            f"Borrower ID: {self.borrower_id} | "
            f"Name: {self.first_name} {self.last_name} | "
            f"Username: {self.username} | "
            f"Fine: ${self.fine}"
        )