import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title="ALERT!!",
            message="take a break for 20 minute",
            timeout=20          #how long pop up will show for
        )
        time.sleep(100)
