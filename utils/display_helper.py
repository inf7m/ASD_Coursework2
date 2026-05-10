class DisplayHelper:

    # =========================
    # DISPLAY HEADER
    # =========================

    @staticmethod
    def display_header(title):

        print("\n" + "=" * 50)

        print(title.center(50))

        print("=" * 50)

    # =========================
    # DISPLAY SUCCESS MESSAGE
    # =========================

    @staticmethod
    def success(message):

        print(f"\n[SUCCESS] {message}")

    # =========================
    # DISPLAY ERROR MESSAGE
    # =========================

    @staticmethod
    def error(message):

        print(f"\n[ERROR] {message}")

    # =========================
    # DISPLAY SECTION LINE
    # =========================

    @staticmethod
    def line():

        print("-" * 50)

    # =========================
    # DISPLAY SEARCH RESULTS
    # =========================

    @staticmethod
    def display_results(results):

        if results is None:

            print("No result found.")

            return

        if isinstance(results, list):

            if len(results) == 0:

                print("No results found.")

                return

            for item in results:

                print(item)

        else:

            print(results)