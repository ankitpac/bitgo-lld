from notification.notification.notification import Notification
from notification.notification.notification_status import NotificationStatus


class NotificationRepository:
    def __init__(self):
        self.notifications = []

    def create_notification(self, id, coin_type, current_price, market_trade_volume, intra_day_high, market_cap):
        new_notification = Notification(
            id, coin_type, current_price, market_trade_volume, intra_day_high, market_cap, NotificationStatus.CREATED.value
        )
        self.notifications.append(new_notification)
        return new_notification

    def get_all_notifications(self):
        return self.notifications

    def delete_notification(self, notification_id):
        for notification in self.notifications:
            if notification.id == notification_id:
                del notification[notification_id]
