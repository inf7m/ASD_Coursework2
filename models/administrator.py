from models.user import User


class Administrator(User):

    def __init__(
            self,
            username,
            password,
            first_name,
            last_name):

        super().__init__(
            username,
            password,
            first_name,
            last_name
        )

    # =========================
    # STRING DISPLAY
    # =========================

    def __str__(self):

        return (
            f"Administrator: "
            f"{self.first_name} "
            f"{self.last_name}"
        )