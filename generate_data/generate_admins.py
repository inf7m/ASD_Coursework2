from models.administrator import Administrator


class GenerateAdmins:

    @staticmethod
    def generate():

        return [

            Administrator(
                "admin",
                "admin123",
                "System",
                "Admin"
            ),

            Administrator(
                "librarian",
                "lib123",
                "Library",
                "Manager"
            )
        ]