import time
from plyer import notification


def take_a_break():
    notification.notify(
        title='Time to take a break!',
        message='Get up, stretch, and look away from your screen for a few minutes.',
        app_name='Break Reminder',
        app_icon=None,
        timeout=10
    )


while True:
    # remind every 30 minutes
    time.sleep(30*60)
    take_a_break()
