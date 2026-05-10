from data_structures.tree_node import TreeNode


class LibraryTree:

    def __init__(self):

        self.root = None

    # =========================
    # INSERT
    # =========================

    def insert(self, item):

        if self.root is None:

            self.root = TreeNode(item)

        else:

            self._insert(self.root, item)

    def _insert(self, current_node, item):

        if item.title.lower() < current_node.item.title.lower():

            if current_node.left is None:

                current_node.left = TreeNode(item)

            else:

                self._insert(current_node.left, item)

        else:

            if current_node.right is None:

                current_node.right = TreeNode(item)

            else:

                self._insert(current_node.right, item)

    # =========================
    # SEARCH
    # =========================

    def search(self, title):

        return self._search(self.root, title)

    def _search(self, current_node, title):

        if current_node is None:

            return None

        if current_node.item.title.lower() == title.lower():

            return current_node.item

        if title.lower() < current_node.item.title.lower():

            return self._search(current_node.left, title)

        return self._search(current_node.right, title)

    # =========================
    # DISPLAY ALL ITEMS
    # =========================

    def display_all_items(self):

        self._inorder_traversal(self.root)

    def _inorder_traversal(self, current_node):

        if current_node is not None:

            self._inorder_traversal(current_node.left)

            print(current_node.item)

            self._inorder_traversal(current_node.right)

    # =========================
    # SEARCH BY AUTHOR
    # =========================

    def search_by_author(self, author_name):

        results = []

        self._search_author_recursive(
            self.root,
            author_name,
            results
        )

        return results

    def _search_author_recursive(
            self,
            current_node,
            author_name,
            results):

        if current_node is not None:

            self._search_author_recursive(
                current_node.left,
                author_name,
                results
            )

            for author in current_node.item.authors:

                if author_name.lower() in author.lower():

                    results.append(current_node.item)

            self._search_author_recursive(
                current_node.right,
                author_name,
                results
            )

    # =========================
    # SEARCH BY CATEGORY
    # =========================

    def search_by_category(self, category):

        results = []

        self._search_category_recursive(
            self.root,
            category,
            results
        )

        return results

    def _search_category_recursive(
            self,
            current_node,
            category,
            results):

        if current_node is not None:

            self._search_category_recursive(
                current_node.left,
                category,
                results
            )

            if current_node.item.category.lower() == category.lower():

                results.append(current_node.item)

            self._search_category_recursive(
                current_node.right,
                category,
                results
            )

    # =========================
    # SEARCH BY LANGUAGE
    # =========================

    def search_by_language(self, language):

        results = []

        self._search_language_recursive(
            self.root,
            language,
            results
        )

        return results

    def _search_language_recursive(
            self,
            current_node,
            language,
            results):

        if current_node is not None:

            self._search_language_recursive(
                current_node.left,
                language,
                results
            )

            if current_node.item.language.lower() == language.lower():

                results.append(current_node.item)

            self._search_language_recursive(
                current_node.right,
                language,
                results
            )

    # =========================
    # SEARCH BY YEAR
    # =========================

    def search_by_year(self, year):

        results = []

        self._search_year_recursive(
            self.root,
            year,
            results
        )

        return results

    def _search_year_recursive(
            self,
            current_node,
            year,
            results):

        if current_node is not None:

            self._search_year_recursive(
                current_node.left,
                year,
                results
            )

            if current_node.item.year_published == year:

                results.append(current_node.item)

            self._search_year_recursive(
                current_node.right,
                year,
                results
            )