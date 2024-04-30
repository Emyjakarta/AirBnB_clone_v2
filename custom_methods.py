#!/usr/bin/python3

"""customized module for testing."""

import sys
from uuid import UUID as uuid
from io import StringIO
from sqlalchemy import text, inspect
from random import choice


class CustomMethods:
    """customized methods that facilitate testing."""

    __random_attributes = {
        "first_name": ["Emeka", "Khalid", "Akproko", "John", "Randy"],
        "last_name": ["Ukonu", "Sinteayehu", "Doctor", "Cena", "Orton"],
        "age": [50, 100, 10, 70, 15, 80],
        "latitude": [
            -89.2712,
            -14.5592,
            36.6148,
            37.943972,
            -57.2312,
            78.5632,
            42.1231,
        ],
        "longitude": [
            -16.5512,
            36.2198,
            -279.2312,
            -54.2312,
            87.5512,
            156.1231,
        ],
    }

    @staticmethod
    def get_uuid(line: StringIO) -> uuid:
        """Returns the UUID from a string."""
        return uuid(line.getvalue().strip())

    @staticmethod
    def get_instances_count(line: StringIO) -> int:
        """Returns the integer value for the number of instances of a model."""
        return int(line.getvalue().strip())

    @staticmethod
    def get_key(model_name: str, instance_id: uuid) -> str:
        """Generates the key used in the objects dictionary for an instance."""
        return f"{model_name}.{instance_id}"

    def get_first_name(self) -> str:
        """Returns a first name."""
        return choice(self.__random_attributes["first_name"])

    def get_last_name(self) -> str:
        """Returns a first name."""
        return choice(self.__random_attributes["last_name"])

    def get_email(self, first_name: str = None, last_name: str = None) -> str:
        """Returns an email address based on random first and last names."""
        return (
            f"{first_name or self.get_first_name()}."
            f"{last_name or self.get_last_name()}@lzcorp.it".lower()
        )

    def get_random_attribute(self):
        """Generates a random key and a value corresponding to that key."""
        key = choice(list(self.__random_attributes.keys()))

        return key, choice(self.__random_attributes[key])

    @staticmethod
    def set_default_collation(
        engine=None, db=None, charset="utf8mb4", collate="utf8mb4_unicode_ci"
    ):
        """
        Sets the default collation for a given database.

        Args:
            engine (sqlalchemy.engine.Engine): The SQLAlchemy engine object.
            db (str): The name of the database.
            charset (str, optional): The character set to use. Defaults to
            "utf8mb4".
            collate (str, optional): The collation to use. Defaults to
            "utf8mb4_unicode_ci".

        Raises:
            SystemExit: If the engine or db is None.
        """
        if engine is None or db is None:
            sys.exit(1)

        with engine.connect() as connection:
            # Begin a new transaction
            with connection.begin():

                connection.execute(
                    f"ALTER DATABASE {db} "
                    f"CHARACTER SET = {charset} "
                    f"COLLATE = {collate};"
                )

                # Execute raw SQL to disable foreign key checks
                connection.execute(text("SET FOREIGN_KEY_CHECKS=0"))

                # Get table names
                insp = inspect(engine)
                table_names = insp.get_table_names()

                for table_name in table_names:
                    # Execute raw SQL to alter table character set
                    connection.execute(
                        text(
                            f"ALTER TABLE {table_name} "
                            f"CONVERT TO CHARACTER SET {charset} "
                            f"COLLATE {collate};"
                        )
                    )

                # Execute raw SQL to enable foreign key checks
                connection.execute(text("SET FOREIGN_KEY_CHECKS=1"))
