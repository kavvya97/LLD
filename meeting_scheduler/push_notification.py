from meeting_scheduler.send_notification import NotificationSender
class PushNotification(NotificationSender):
    def send_notification(self, user_id: str, message: str):
        print(f"Push Notification for {user_id} is {message}")