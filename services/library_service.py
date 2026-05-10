from data_structures.library_tree import LibraryTree

from generate_data.generate_books import GenerateBooks
from generate_data.generate_periodicals import GeneratePeriodicals
from generate_data.generate_magazines import GenerateMagazines
from generate_data.generate_audiobooks import GenerateAudioBooks


class LibraryService:

    def __init__(self):

        self.library_tree = LibraryTree()

        self.load_library_items()

    # =========================
    # LOAD DATASETS INTO BST
    # =========================

    def load_library_items(self):

        books = GenerateBooks.generate()

        periodicals = GeneratePeriodicals.generate()

        magazines = GenerateMagazines.generate()

        audiobooks = GenerateAudioBooks.generate()

        all_items = []

        all_items.extend(books)

        all_items.extend(periodicals)

        all_items.extend(magazines)

        all_items.extend(audiobooks)

        for item in all_items:

            self.library_tree.insert(item)

    # =========================
    # DISPLAY ALL ITEMS
    # =========================

    def display_all_items(self):

        self.library_tree.display_all_items()

    # =========================
    # SEARCH BY TITLE
    # =========================

    def search_by_title(self, title):

        return self.library_tree.search(title)

    # =========================
    # SEARCH BY AUTHOR
    # =========================

    def search_by_author(self, author):

        return self.library_tree.search_by_author(author)

    # =========================
    # SEARCH BY CATEGORY
    # =========================

    def search_by_category(self, category):

        return self.library_tree.search_by_category(category)

    # =========================
    # SEARCH BY LANGUAGE
    # =========================

    def search_by_language(self, language):

        return self.library_tree.search_by_language(language)

    # =========================
    # SEARCH BY YEAR
    # =========================

    def search_by_year(self, year):

        return self.library_tree.search_by_year(year)

    # =========================
    # ADD NEW ITEM
    # =========================

    def add_item(self, item):

        self.library_tree.insert(item)

        print("Item added successfully.")