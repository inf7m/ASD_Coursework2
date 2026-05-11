from services.admin_service import (
    AdminService
)


class AdminMenu:

    def __init__(
            self,
            admin,
            library_tree,
            borrower_list):

        self.admin = admin

        self.admin_service = (
            AdminService(
                library_tree,
                borrower_list
            )
        )

    def display_menu(self):

        while True:

            print("\n========== ADMIN MENU ==========")

            print("1. Display All Items")
            print("2. Search Item by Title")
            print("3. Search Item by Author")
            print("4. Add New Item")
            print("5. Remove Item")
            print("6. Display Borrowers")
            print("7. Display Borrowers With Fines")
            print("8. Display Borrowed Items")
            print("9. Logout")

            choice = input(
                "Enter your choice: "
            )

            # =========================
            # DISPLAY ALL ITEMS
            # =========================

            if choice == "1":

                items = (
                    self.admin_service
                    .display_all_items()
                )

                if len(items) == 0:

                    print("\nNo items found.")

                else:

                    for item in items:

                        print(item)
                        print("-" * 40)

            # =========================
            # SEARCH BY TITLE
            # =========================

            elif choice == "2":

                title = input(
                    "Enter title: "
                )

                item = (
                    self.admin_service
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

            elif choice == "3":

                author = input(
                    "Enter author: "
                )

                results = (
                    self.admin_service
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
            # ADD NEW ITEM
            # =========================

            elif choice == "4":

                self.admin_service.add_item()

            # =========================
            # REMOVE ITEM
            # =========================

            elif choice == "5":

                title = input(
                    "Enter title to remove: "
                )

                self.admin_service.remove_item(
                    title
                )

            # =========================
            # DISPLAY BORROWERS
            # =========================

            elif choice == "6":

                self.admin_service.display_borrowers()

            # =========================
            # DISPLAY BORROWERS
            # WITH FINES
            # =========================

            elif choice == "7":

                self.admin_service.display_borrowers_with_fines()

            # =========================
            # DISPLAY BORROWED ITEMS
            # =========================

            elif choice == "8":

                self.admin_service.display_borrowed_items()

            # =========================
            # LOGOUT
            # =========================

            elif choice == "9":

                print(
                    "\nLogging out..."
                )

                break

            else:

                print(
                    "\nInvalid choice."
                )
