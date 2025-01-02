from meeting_scheduler.send_notification import NotificationSender
class SMSNotification:
    def send_notification(user_id, message):
        print(f"Push Notification for {user_id} is {message}")