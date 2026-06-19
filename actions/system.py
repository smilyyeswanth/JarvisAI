import os
import socket
from datetime import datetime


def get_time():
    return datetime.now().strftime("%I:%M %p")


def get_ip():
    try:
        return socket.gethostbyname(
            socket.gethostname()
        )
    except:
        return "Unable to determine IP"


def get_battery():
    try:
        result = os.popen(
            "pmset -g batt"
        ).read()

        for line in result.split("\n"):
            if "%" in line:
                return line.strip()

        return "Battery info unavailable"

    except:
        return "Battery info unavailable"