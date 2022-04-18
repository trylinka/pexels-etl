from logging import getLogger
from typing import List

import requests


# Client class to get photo data from Pexels API
class Client:
    def __init__(self, base_url: str, api_key: str):
        self.base_url = base_url
        self.api_key = api_key
        self._logger = getLogger("pexels_etl.client")

    def get_photo_resources(self, topic: str, n_records: int, batch_size: int) -> List:
        """
        Retrieve photos from Pexels API
        :param topic: selected photo topic
        :param n_records: total number of photo records
        :param batch_size: number of photos in a batch
        :return: list of photos with all data, including resources
        """

        headers = {"Authorization": self.api_key}

        # Limit of API endpoint is 80 photos at once
        if batch_size > 80:
            raise ValueError("Change batch size due to pagination limit!")

        photo_data = []
        photo_ids = set()
        page = 1
        while len(photo_data) < n_records:
            payload = {"query": topic, "page": page, "per_page": batch_size}
            response = requests.get(self.base_url, params=payload, headers=headers)

            # Stop requesting photos when getting error
            response.raise_for_status()

            photos = response.json()["photos"]
            for photo in photos:
                # Handle duplicated photos got in response
                if photo["id"] in photo_ids:
                    self._logger.warning(f"Photo id {photo['id']} is duplicated!")
                    continue
                photo_ids.add(photo["id"])
                photo_data.append(photo)

            self._logger.info(f"{len(photo_data)} photo records are downloaded.")
            page += 1

        # Get necessary number of photos to upload
        return photo_data[:n_records]
