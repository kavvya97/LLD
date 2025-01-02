from typing import List
import threading

class NotificationMgr:
    def __init__(self):
        self.notification_senders_map = {}
        self.notification_mgr_instance = None
        self.mtx = threading.Lock()

    @staticmethod
    def get_notification_mgr():
        if NotificationMgr.notification_mgr_instance is None:
            with NotificationMgr.mtx:
                if NotificationMgr.notification_mgr_instance is None:
                    NotificationMgr.notification_mgr_instance = NotificationMgr()
        return NotificationMgr.notification_mgr_instance

    def add_notification_sender(self, user_id: str, notification_sender):
        self.notification_senders_map[user_id] = self.notification_senders_map.get(user_id, []) + [notification_sender]

    def remove_notification_sender(self, user_id: str, notification_sender):
        senders = self.notification_senders_map.get(user_id, [])
        if notification_sender in senders:
            senders.remove(notification_sender)

    def notify(self, user_id: str, message: str):
        senders = self.notification_senders_map.get(user_id, [])
        for sender in senders:
            sender.send_notification(user_id, message)
