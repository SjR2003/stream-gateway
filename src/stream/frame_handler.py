import logging

from stream.zmq_subscriber import ZMQSubscriber
from schemas.stream_packet import StreamHubPacket


class FrameHandler:
    def __init__(self, endpoint: str) -> None:
        self.__logger = logging.getLogger(__name__)
        self.__subscriber = ZMQSubscriber(endpoint)

    def start(self) -> bool:
        return self.__subscriber.start()

    def get_latest_frame(self) -> StreamHubPacket:
        message = self.__subscriber.get_message()
        try:
            packet = StreamHubPacket.model_validate(message)
            return packet
        except Exception as e:
            self.__logger.error(f"No valid message received {e}")
            return None
