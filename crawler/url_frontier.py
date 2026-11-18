from queue import Queue
from urllib.parse import urlparse


class UrlFrontier:
    def __init__(self, queue: Queue):
        self.__queue = queue
        self.__seen = set()

    def __is_valid_url(self, url: str) -> bool:
        try:
            parsed = urlparse(url)
            return all([parsed.scheme in ("http", "https"), parsed.netloc])
        except Exception:
            return False

    def add(self, url: str) -> bool:
        if not self.__is_valid_url(url) or url in self.__seen:
            return False
        
        self.__seen.add(url)
        self.__queue.put(url)
        return True

    def get(self) -> str | None:
        if not self.__queue.empty():
            return self.__queue.get()
