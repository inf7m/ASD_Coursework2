from data_structures.borrower_node import BorrowerNode


class BorrowerList:

    def __init__(self):

        self.head = None
        self.tail = None

    # =========================
    # ADD BORROWER
    # =========================

    def add_borrower(self, borrower):

        new_node = BorrowerNode(borrower)

        if self.head is None:

            self.head = new_node
            self.tail = new_node

        else:

            self.tail.next = new_node

            new_node.previous = self.tail

            self.tail = new_node

    # =========================
    # DISPLAY ALL BORROWERS
    # =========================

    def display_all_borrowers(self):

        current = self.head

        while current is not None:

            print(current.borrower)

            current = current.next

    # =========================
    # SEARCH BORROWER
    # =========================

    def search_borrower(self, username):

        current = self.head

        while current is not None:

            if current.borrower.username == username:

                return current.borrower

            current = current.next

        return None

    # =========================
    # REMOVE BORROWER
    # =========================

    def remove_borrower(self, username):

        current = self.head

        while current is not None:

            if current.borrower.username == username:

                # REMOVE HEAD
                if current == self.head:

                    self.head = current.next

                    if self.head is not None:

                        self.head.previous = None

                # REMOVE TAIL
                elif current == self.tail:

                    self.tail = current.previous

                    if self.tail is not None:

                        self.tail.next = None

                # REMOVE MIDDLE
                else:

                    current.previous.next = current.next

                    current.next.previous = current.previous

                return True

            current = current.next

        return False

    # =========================
    # UPDATE BORROWER
    # =========================

    def update_borrower_name(
            self,
            username,
            new_first_name,
            new_last_name):

        borrower = self.search_borrower(username)

        if borrower is not None:

            borrower.first_name = new_first_name
            borrower.last_name = new_last_name

            return True

        return False