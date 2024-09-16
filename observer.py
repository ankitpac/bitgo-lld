from abc import ABC, abstractmethod

class Observer(ABC):

    @abstractmethod
    def send_notification(self):
        pass