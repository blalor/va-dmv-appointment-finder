# -*- encoding: utf-8 -*-

import requests


def retrieve_calendar(calendar_id, calendar_type, month=None):
    data = {
        "type": calendar_type,
        "calendar": calendar_id,
        "calendarID": calendar_id,
        "skip": "true",
        "options[qty]": 1,
        "options[numDays]": 5,
        "ignoreAppointment": "",
        "appointmentType": "",
    }

    if month is not None:
        # month=2021-05-15
        # month=2021-06-15
        data["month"] = month

    resp = requests.post(
        "https://vadmvappointments.as.me/schedule.php",
        params={
            "action": "showCalendar",
            "fulldate": 1,
            "owner": 19444409,
            "template": "monthly",
        },
        data=data,
        headers={
            # "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Pragma": "no-cache",
            "Accept": "*/*",
            "Accept-Language": "en-us",
            # "Accept-Encoding": "gzip, deflate, br",
            "Cache-Control": "no-cache",
            "Origin": "https://vadmvappointments.as.me",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15",
            "Referer": f"https://vadmvappointments.as.me/schedule.php?calendarID={calendar_id}",
            # "Cookie": "PHPSESSID=r6f6t6v02r8kgoeaqcspnctamo",
            "X-Requested-With": "XMLHttpRequest",
        },
    )

    resp.raise_for_status()
    return resp
