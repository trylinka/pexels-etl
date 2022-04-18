import sqlite3
from logging import getLogger

from pexels_etl import config

logger = getLogger("pexels_etl.setup_db")


def setup_database(database: str) -> None:
    """
    Setup database for ETL pipeline
    :param database: database name
    :return: None
    """

    logger.info("Initialize database...")

    with open(config.DDL_TABLES, "r") as sql_file, sqlite3.connect(database) as connection:
        sql_script = sql_file.read()
        cursor = connection.cursor()
        cursor.executescript(sql_script)

    logger.info("Database is setup!")


if __name__ == '__main__':
    setup_database(database=config.SQLITE_DB)
