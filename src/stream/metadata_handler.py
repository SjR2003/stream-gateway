import logging

from src.stream.zmq_subscriber import ZMQSubscriber

class MetadataHandler:
    def __init__(self, endpoint: str):
        self.__logger = logging.getLogger(__name__)
        self.__subscriber = ZMQSubscriber(endpoint)

    def start(self):
        return self.__subscriber.start()

    def get_latest_metadata(self):
        message = self.__subscriber.get_message()
        if message and isinstance(message, dict):
            message = message.get("metadata", None)
            return message

        self.__logger.debug("No valid message received")
        return None