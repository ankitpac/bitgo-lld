from enum import Enum


class NotificationStatus(Enum):
    CREATED = 'CREATED'
    SENT = 'SENT'
    FAILED = 'FAILED'
    OUTSTANDING = 'OUTSTANDING'
