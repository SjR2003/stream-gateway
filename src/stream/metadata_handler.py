import logging

from src.stream.zmq_subscriber import ZMQSubscriber
from schemas.tracker_metadata import TrackerPacket


class MetadataHandler:
    def __init__(self, endpoint: str) -> None:
        self.__logger = logging.getLogger(__name__)
        self.__subscriber = ZMQSubscriber(endpoint)

    def start(self) -> bool:
        return self.__subscriber.start()

    def get_latest_metadata(self) -> TrackerPacket:
        message = self.__subscriber.get_message()
        try:
            packet = TrackerPacket.model_validate(message)
            return packet
        except Exception as e:
            self.__logger.error(f"No valid message received {e}")
            return None
