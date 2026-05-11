from datetime import datetime, timedelta


class BorrowerService:

    def __init__(
            self,
            borrower,
            library_tree):

        self.borrower = borrower

        self.library_tree = (
            library_tree
        )

    # =========================
    # BORROW ITEM
    # =========================

    def borrow_item(
            self,
            title):

        # CHECK FINE

        if self.borrower.fine > 0:

            print(
                "\nYou cannot borrow items "
                "until your fine is paid."
            )

            return

        # CHECK BORROW LIMIT

        if (
                len(
                    self.borrower
                    .borrowed_items
                )
                >=
                8
        ):

            print(
                "\nBorrow limit reached "
                "(Maximum 8 items)."
            )

            return

        # SEARCH ITEM

        item = (
            self.library_tree
            .search_by_title(title)
        )

        if item is None:

            print("\nItem not found.")

            return

        # CHECK DUPLICATE BORROW

        for record in (
                self.borrower
                .borrowed_items
        ):

            borrowed_item = (
                record["item"]
            )

            if (
                    borrowed_item.title.lower()
                    ==
                    item.title.lower()
            ):

                print(
                    "\nItem already borrowed."
                )

                return

        # CREATE DATES

        borrow_date = datetime.now()

        due_date = (
            borrow_date
            +
            timedelta(days=14)
        )

        # STORE RECORD

        self.borrower.borrowed_items.append({

            "item": item,

            "borrow_date": borrow_date,

            "due_date": due_date
        })

        print(
            f"\n'{item.title}' borrowed successfully."
        )

        print(
            f"Due Date: "
            f"{due_date.strftime('%Y-%m-%d')}"
        )

    # =========================
    # RETURN ITEM
    # =========================

    def return_item(
            self,
            title):

        for record in (
                self.borrower
                .borrowed_items
        ):

            item = record["item"]

            if (
                    item.title.lower()
                    ==
                    title.lower()
            ):

                self.borrower.borrowed_items.remove(
                    record
                )

                print(
                    f"\n'{item.title}' returned successfully."
                )

                return

        print(
            "\nBorrowed item not found."
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
    # PAY FINE
    # =========================

    def pay_fine(self):

        if self.borrower.fine <= 0:

            print(
                "\nNo outstanding fine."
            )

            return

        print(
            f"\nOutstanding Fine: "
            f"${self.borrower.fine}"
        )

        confirm = input(
            "Pay fine now? (y/n): "
        )

        if confirm.lower() == "y":

            self.borrower.fine = 0

            print(
                "\nFine paid successfully."
            )

        else:

            print(
                "\nPayment cancelled."
            )
