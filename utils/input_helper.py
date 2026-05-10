class InputHelper:

    # =========================
    # GET INTEGER INPUT
    # =========================

    @staticmethod
    def get_integer(message):

        while True:

            try:

                value = int(input(message))

                return value

            except ValueError:

                print("Invalid integer input.")

    # =========================
    # GET FLOAT INPUT
    # =========================

    @staticmethod
    def get_float(message):

        while True:

            try:

                value = float(input(message))

                return value

            except ValueError:

                print("Invalid number input.")

    # =========================
    # GET NON-EMPTY STRING
    # =========================

    @staticmethod
    def get_string(message):

        while True:

            value = input(message).strip()

            if value != "":

                return value

            print("Input cannot be empty.")