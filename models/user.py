class User:

    def __init__(
            self,
            username,
            password,
            first_name,
            last_name):

        self.username = username

        self._password = password

        self.first_name = first_name
        self.last_name = last_name

    # =========================
    # CHECK PASSWORD
    # =========================

    def check_password(self, password):

        return self._password == password

    # =========================
    # STRING DISPLAY
    # =========================

    def __str__(self):

        return (
            f"{self.first_name} "
            f"{self.last_name} "
            f"({self.username})"
        )