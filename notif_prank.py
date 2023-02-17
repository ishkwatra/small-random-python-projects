import time
import random
from plyer import notification

collection1 = ["Your computer might be at risk!", "Attention!",
               "Security Alert!", "Virus Detected!", "New Threats Found!"]
collection2 = ["216 anonymous files downloaded from unkown source.", "Security patch unable to work properly, scanning failed.",
               "Windows defender update failed, your anti-virus has stopped working.", "Your privacy might be at risk, 216 ambigous files found.", "New Windows sign-in detected, password sharing in progress."]


def take_a_break(headings, text):
    notification.notify(
        title=random.choice(headings),
        message=random.choice(text),
        app_name='Windows Security',
        app_icon=r'C:\Users\hp\Downloads\Windows_Settings_app_icon.ico',
        timeout=10
    )


while True:
    time.sleep(10)
    take_a_break(collection1, collection2)
