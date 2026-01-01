"""
Roadmap:
- Synchronizes frames with perception metadata
- Matches based on:
    - timestamp
    - frame_id
- Handles missing or delayed data gracefully
- Output is always consistent for rendering
"""

import logging

from src.stream.frame_handler import FrameHandler
from src.stream.metadata_handler import MetadataHandler

class StreamSynchronizer:
    def __init__(self, frame_endpoint: str, metadata_endpoint: str):
        self.__logger = logging.getLogger(__name__)
        self.__frame_handler = FrameHandler(frame_endpoint)
        self.__metadata_handler = MetadataHandler(metadata_endpoint)

    def start(self):
        frame_started = self.__frame_handler.start()
        metadata_started = self.__metadata_handler.start()
        return frame_started and metadata_started

    def get_synchronized_data(self):
        jpeg_bytes, stream_metadata = self.__frame_handler.get_latest_frame()
        perception_metadata = self.__metadata_handler.get_latest_metadata()

        if jpeg_bytes is None or stream_metadata is None or perception_metadata is None:
            self.__logger.debug("Incomplete data for synchronization")
            return None, None

        # Here could implement more complex synchronization logic

        return {"frame": jpeg_bytes, "metadata": perception_metadata}