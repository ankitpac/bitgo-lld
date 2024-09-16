from notification.notification.observer import Observer


class BTCObserver(Observer):
    def __init__(self, users):
        self.users = users