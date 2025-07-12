import time
from plyer import notification

while True:
    notification.notify(
        title="Drink Water Reminder",
        message="It's time to drink some water!",
        app_name="Drink Water Reminder",
        timeout = 10  # Notification will be visible for 10 seconds
    )

    time.sleep(5)  # Wait for 5 seconds before reminding again