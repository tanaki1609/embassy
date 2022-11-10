import json
import time
import datetime

import requests
from dateutil.relativedelta import relativedelta
from contants import MONTHS_BY_POSITION, HEADERS, BASE_URL


def check_date(date) -> bool:
    try:
        r = requests.post(url=f'{BASE_URL}/ciph/0800/selectVisitReserveCalendarYes.do',
                          data={
                              'emblCd': 'KY',
                              'visitResveBussGrpCd': 'KY0001',
                              'emblTime': f'{date.year}{date.month}'
                          },
                          headers=HEADERS)
        response = json.loads(r.content)

        data = [
            v['visitYn'].lower()
            for v in response['visitReserveCalendarYesResult'] if int(v['visitDe'][6:8]) >= date.day
        ]
        if response and 'y' in data:
            message = f'Есть место {MONTHS_BY_POSITION.get(date.month)}!'
            requests.post(
                f'https://api.telegram.org/bot5430523711:AAHFQFT5_dfsZO04cmjQfQGHwMJXm3-YNoI/sendMessage?chat_id=5472619858&text={message}'
            )
            return True
    except:
        pass
    return False


if __name__ == '__main__':
    now = datetime.datetime.now()
    next_ = datetime.datetime.today() + relativedelta(months=1)

    a = time.perf_counter()
    have_now = check_date(now)
    have_next = check_date(next_)
    b = time.perf_counter()

    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)
    print(str(b - a) + "_stop")
