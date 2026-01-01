import logging

from stream.zmq_subscriber import ZMQSubscriber

class FrameHandler:
    def __init__(self, endpoint: str):
        self.__logger = logging.getLogger(__name__)
        self.__subscriber = ZMQSubscriber(endpoint)

    def start(self):
        return self.__subscriber.start()

    def get_latest_frame(self):
        message = self.__subscriber.get_message()
        if message and isinstance(message, dict):
            metadata = message.get("metadata", None)
            jpeg_bytes = message.get("jpeg_bytes", None)
            return jpeg_bytes, metadata

        self.__logger.debug("No valid message received")
        return None, None