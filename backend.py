from datetime import datetime
from time import strftime, strptime


def refresh_progress(deadline):
    current_date = strftime("%Y/%m/%d")
    start = datetime.strptime(current_date, "%Y/%m/%d")
    end = datetime.strptime(deadline, "%Y/%m/%d")
    delta = (end - start)
    return delta.days * 24
