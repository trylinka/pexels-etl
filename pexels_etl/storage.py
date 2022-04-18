import sqlite3

from typing import Dict


# Storage class to upload photos data. Implemented as context manager
class Storage:
    def __init__(self, database: str):
        self._database = database
        self._connection = None

    def __enter__(self):
        self._connection = sqlite3.connect(self._database)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._connection.commit()
        self._connection.close()

    def upload_photo_data(self, data: Dict) -> None:
        """
        Upload photo data in "photo" table
        :param data: dict of all available data about photo
        :return: None
        """

        # Validate database connection
        if self._connection is None:
            raise ConnectionError("Connection to database isn't established. Check database connection!")
        cursor = self._connection.cursor()

        # Insert data according to table schema
        cursor.execute("INSERT INTO photos VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);",
                       (data["id"],
                        data["width"],
                        data["height"],
                        data["url"],
                        data["photographer"],
                        data["photographer_url"],
                        data["photographer_id"],
                        data["avg_color"],
                        data["liked"],
                        data["alt"]))

    def upload_photo_sources(self, photo_id: int, size: str, url: str) -> None:
        """
        Upload detailed data about photo sizes in "photo_sources" table
        :param photo_id: photo id
        :param size: name of photo size
        :param url: url to get photo with named size
        :return: None
        """

        # Validate database connection
        if self._connection is None:
            raise ConnectionError("Connection to database isn't established. Check database connection!")
        cursor = self._connection.cursor()
        cursor.execute("INSERT INTO photo_sources (photo_id, size, url) VALUES (?, ?, ?);", (photo_id, size, url))
