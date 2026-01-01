from collections import deque
from threading import Thread
import logging
import zmq

class ZMQSubscriber:
    def __init__(self, endpoint=None):
        self.__logger = logging.getLogger(__name__)
        self.__context = zmq.Context.instance()
        self.__endpoint = endpoint

        self.__socket = None
        self.__running = False
        self.__message_queue = deque(maxlen=1)
        self.__message_count = 0

        self.__recv_thread = Thread(target=self.__receive_loop, daemon=True)

    def start(self):
        if not self.__connect():
            return False
        self.__running = True
        self.__recv_thread.start()
        self.__logger.info("Started ZMQ receive thread")
        return True

    def get_message(self):
        if self.__message_queue:
            return self.__message_queue[-1]
        
        self.__logger.debug("No messages in queue")
        return None

    def __connect(self):
        try:
            self.__socket = self.__context.socket(zmq.SUB)
            self.__socket.setsockopt(zmq.RCVHWM, 10)
            self.__socket.setsockopt(zmq.RCVTIMEO, 1000)
            self.__socket.setsockopt(zmq.SUBSCRIBE, b"")
            self.__socket.connect(self.__endpoint)

            self.__logger.info(f"Connected SUB to {self.__endpoint}")
            return True
        except Exception as e:
            self.__logger.error(f"Connect Failed: {e}")
            return False
        
    def __receive_loop(self ):
        while self.__running:
            try:
                message = self.__socket.recv_multipart()
                self.__logger.debug(f"Received message with {len(message)} parts")
                self.__message_queue.append(message)
                self.__message_count += 1
            except zmq.Again:
                self.__logger.debug("Receive timed out, retrying...")
                continue
            except Exception as e:
                self.__logger.error(f"Receive Failed: {e}")
                self.__running = False
                break