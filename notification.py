from notification_status import NotificationStatus


class Notification:
    def __int__(self, id, coin_type, current_price, market_trade_volume, intra_day_high, market_cap, status):
        self.id = id
        self.coin_type = coin_type
        self.current_price = current_price
        self.market_trade_volume = market_trade_volume
        self.intra_day_high = intra_day_high
        self.market_cap = market_cap
        self.status = status