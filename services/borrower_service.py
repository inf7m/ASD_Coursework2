class BorrowerService:

    # =========================
    # BORROW ITEM
    # =========================

    @staticmethod
    def borrow_item(borrower, item):

        return borrower.borrow_item(item)

    # =========================
    # RETURN ITEM
    # =========================

    @staticmethod
    def return_item(borrower, item_title):

        return borrower.return_item(item_title)

    # =========================
    # VIEW FINE
    # =========================

    @staticmethod
    def view_fine(borrower):

        print(f"Current Fine: ${borrower.fine}")

    # =========================
    # PAY FINE
    # =========================

    @staticmethod
    def pay_fine(borrower, amount):

        borrower.pay_fine(amount)

    # =========================
    # VIEW BORROWED ITEMS
    # =========================

    @staticmethod
    def display_borrowed_items(borrower):

        borrower.display_borrowed_items()