from services.borrower_service import (
    BorrowerService
)


class BorrowerMenu:

    def __init__(
            self,
            borrower,
            library_tree):

        self.borrower = borrower

        self.borrower_service = (
            BorrowerService(
                borrower,
                library_tree
            )
        )

    def display_menu(self):

        while True:

            print("\n========== BORROWER MENU ==========")

            print("1. Borrow Item")
            print("2. Return Item")
            print("3. Search Item by Title")
            print("4. Search Item by Author")
            print("5. Display Borrowed Items")
            print("6. Check Due Dates")
            print("7. Pay Fine")
            print("8. Logout")

            choice = input(
                "Enter your choice: "
            )

            # =========================
            # BORROW ITEM
            # =========================

            if choice == "1":

                title = input(
                    "Enter item title: "
                )

                self.borrower_service.borrow_item(
                    title
                )

            # =========================
            # RETURN ITEM
            # =========================

            elif choice == "2":

                title = input(
                    "Enter item title to return: "
                )

                self.borrower_service.return_item(
                    title
                )

            # =========================
            # SEARCH BY TITLE
            # =========================

            elif choice == "3":

                title = input(
                    "Enter title: "
                )

                item = (
                    self.borrower_service
                    .search_by_title(title)
                )

                if item is not None:

                    print("\nItem Found:")
                    print(item)

                else:

                    print(
                        "\nItem not found."
                    )

            # =========================
            # SEARCH BY AUTHOR
            # =========================

            elif choice == "4":

                author = input(
                    "Enter author name: "
                )

                results = (
                    self.borrower_service
                    .search_by_author(author)
                )

                if len(results) > 0:

                    print("\nItems Found:")

                    for item in results:

                        print(item)
                        print("-" * 40)

                else:

                    print(
                        "\nNo items found."
                    )

            # =========================
            # DISPLAY BORROWED ITEMS
            # =========================

            elif choice == "5":

                if (
                        len(
                            self.borrower
                            .borrowed_items
                        )
                        ==
                        0
                ):

                    print(
                        "\nNo borrowed items."
                    )

                else:

                    print(
                        "\nBorrowed Items:"
                    )

                    for record in (
                            self.borrower
                            .borrowed_items
                    ):

                        item = record["item"]

                        print(
                            f"\nTitle: {item.title}"
                        )

                        print(
                            f"Due Date: "
                            f"{record['due_date'].strftime('%Y-%m-%d')}"
                        )

            # =========================
            # CHECK DUE DATES
            # =========================

            elif choice == "6":

                if (
                        len(
                            self.borrower
                            .borrowed_items
                        )
                        ==
                        0
                ):

                    print(
                        "\nNo borrowed items."
                    )

                else:

                    print(
                        "\nDue Dates:"
                    )

                    for record in (
                            self.borrower
                            .borrowed_items
                    ):

                        item = record["item"]

                        print(
                            f"\n{item.title}"
                        )

                        print(
                            f"Borrow Date: "
                            f"{record['borrow_date'].strftime('%Y-%m-%d')}"
                        )

                        print(
                            f"Due Date: "
                            f"{record['due_date'].strftime('%Y-%m-%d')}"
                        )

            # =========================
            # PAY FINE
            # =========================

            elif choice == "7":

                self.borrower_service.pay_fine()

            # =========================
            # LOGOUT
            # =========================

            elif choice == "8":

                print(
                    "\nLogging out..."
                )

                break

            else:

                print(
                    "\nInvalid choice."
                )
