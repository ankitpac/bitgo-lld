class NotificationService:
    def __init__(self, notification_repository):
        self.notification_repository = notification_repository

    def create_notification(self, id, coin_type, current_price, market_trade_volume, intra_day_high, market_cap):
        new_notification = self.notification_repository.create_notification(
            id, coin_type, current_price, market_trade_volume, intra_day_high, market_cap
        )

        self.send_notification(new_notification)

        return new_notification

    def send_notification(self, notification):



    def get_all_notifications(self):
        return self.notification_repository.get_all_notifications()

    def delete_notification(self, notification_id):
        return self.notification_repository.delete_notification(notification_id)
