from datetime import datetime, timedelta

from models.borrower import Borrower

from generate_data.generate_books import (
    generate_books
)

from generate_data.generate_periodicals import (
    generate_periodicals
)

from generate_data.generate_magazines import (
    generate_magazines
)

from generate_data.generate_audiobooks import (
    generate_audiobooks
)


def generate_borrowers():

    books = generate_books()

    periodicals = generate_periodicals()

    magazines = generate_magazines()

    audiobooks = generate_audiobooks()

    all_items = (
            books
            + periodicals
            + magazines
            + audiobooks
    )

    borrowers = []

    # =========================
    # BORROWER 1
    # =========================

    borrower1 = Borrower(
        "B001",
        "John",
        "Tan",
        "john",
        "123"
    )

    borrow_date_1 = (
        datetime.now() - timedelta(days=5)
    )

    due_date_1 = (
        borrow_date_1 + timedelta(days=14)
    )

    borrower1.borrowed_items.append({

        "item": all_items[0],

        "borrow_date": borrow_date_1,

        "due_date": due_date_1
    })

    borrowers.append(borrower1)

    # =========================
    # BORROWER 2
    # =========================

    borrower2 = Borrower(
        "B002",
        "Alice",
        "Lim",
        "alice",
        "123"
    )

    borrow_date_2 = (
        datetime.now() - timedelta(days=20)
    )

    due_date_2 = (
        borrow_date_2 + timedelta(days=14)
    )

    borrower2.borrowed_items.append({

        "item": all_items[5],

        "borrow_date": borrow_date_2,

        "due_date": due_date_2
    })

    borrower2.fine = 15.0

    borrowers.append(borrower2)

    # =========================
    # BORROWER 3
    # =========================

    borrower3 = Borrower(
        "B003",
        "Michael",
        "Ong",
        "michael",
        "123"
    )

    borrowers.append(borrower3)

    # =========================
    # BORROWER 4
    # =========================

    borrower4 = Borrower(
        "B004",
        "Sarah",
        "Lee",
        "sarah",
        "123"
    )

    borrowers.append(borrower4)

    # =========================
    # BORROWER 5
    # =========================

    borrower5 = Borrower(
        "B005",
        "Daniel",
        "Goh",
        "daniel",
        "123"
    )

    borrowers.append(borrower5)

    # =========================
    # BORROWER 6
    # =========================

    borrower6 = Borrower(
        "B006",
        "Emily",
        "Chua",
        "emily",
        "123"
    )

    borrowers.append(borrower6)

    # =========================
    # BORROWER 7
    # =========================

    borrower7 = Borrower(
        "B007",
        "Kevin",
        "Ng",
        "kevin",
        "123"
    )

    borrowers.append(borrower7)

    # =========================
    # BORROWER 8
    # =========================

    borrower8 = Borrower(
        "B008",
        "Sophia",
        "Tan",
        "sophia",
        "123"
    )

    borrowers.append(borrower8)

    # =========================
    # BORROWER 9
    # =========================

    borrower9 = Borrower(
        "B009",
        "Ryan",
        "Lim",
        "ryan",
        "123"
    )

    borrowers.append(borrower9)

    # =========================
    # BORROWER 10
    # =========================

    borrower10 = Borrower(
        "B010",
        "Grace",
        "Wong",
        "grace",
        "123"
    )

    borrowers.append(borrower10)

    return borrowers
