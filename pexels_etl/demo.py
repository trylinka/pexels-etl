import sqlite3
from logging import getLogger

from pexels_etl import config

logger = getLogger("pexels_etl.demo")


def show_demo(database: str) -> None:
    """
    Run example queries to show results from tables
    :param database: database name
    :return: none
    """
    logger.info("Run demo queries...")

    connection = sqlite3.connect(database)
    cursor = connection.cursor()

    # Check top 5 photographers from "photo" table
    cursor.execute("""
    SELECT photographer 
    FROM (SELECT photographer, 
          count(id) 
          FROM photos 
          GROUP BY photographer 
          ORDER BY 2 DESC) 
    limit 5;
    """)
    logger.info(f"5 top photographers: {[ph[0] for ph in cursor.fetchall()]}")

    # Get total amount of liked photos
    cursor.execute("""
    SELECT count(liked) AS liked_photos 
    FROM photos
    WHERE liked = 1; 
    """)
    for row in cursor:
        logger.info(f"Amount of liked photos: {row[0]}")

    # Get average width and height of all photos
    cursor.execute("""
    SELECT avg(width) AS avg_photo_width, 
           avg(height) AS avg_photo_height 
    FROM photos;
    """)
    for row in cursor:
        logger.info(f"Average width and height of photos: {', '.join(str(value) for value in row)}")


if __name__ == '__main__':
    show_demo(database=config.SQLITE_DB)
