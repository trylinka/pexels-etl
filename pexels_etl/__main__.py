from logging import getLogger

from pexels_etl import config
from pexels_etl.client import Client
from pexels_etl.storage import Storage

logger = getLogger("pexels_etl")

if __name__ == "__main__":
    logger.info("Get data from Pexels API...")
    client = Client(base_url=config.BASE_URL, api_key=config.API_KEY)
    photos_data = client.get_photo_resources(topic=config.PHOTOS_TOPIC, n_records=config.N_RECORDS,
                                             batch_size=config.BATCH_SIZE)

    logger.info("Upload photo data to database...")
    with Storage(database=config.SQLITE_DB) as storage:
        for idx, photo_data in enumerate(photos_data):
            storage.upload_photo_data(data=photo_data)
            photo_sources = photo_data["src"]
            for size, url in photo_sources.items():
                storage.upload_photo_sources(photo_id=photo_data["id"], size=size, url=url)
            # Reduce amount of logs in console
            if idx % 100 == 0:
                logger.info(f"Uploaded {idx} / {len(photos_data)} photo records to database.")

    logger.info("Done!")
