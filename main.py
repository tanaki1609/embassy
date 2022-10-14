import json
import time
import datetime
import requests
from dateutil.relativedelta import relativedelta
from contants import MONTHS_BY_POSITION


def check_date(date) -> bool:
    try:
        r = requests.post(url='https://consul.mofa.go.kr/ciph/0800/selectVisitReserveCalendarYes.do',
                          data={
                              'emblCd': 'KY',
                              'visitResveBussGrpCd': 'KY0001',
                              'emblTime': f'{date.year}{date.month}'
                          },
                          headers={
                              'Accept': 'application/json, text/javascript, */*; q=0.01',
                              'Accept-Encoding': 'gzip, deflate, br',
                              'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8,ru;q=0.7',
                              'Connection': 'keep-alive',
                              'Content-Length': '52',
                              'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                              'Cookie': 'TMOSHCooKie=S+E+cJwAhsS+9bKnB81hijAJAf0bFveQ0m4fDjXUHfShZAouy64POcCbmoXBDTlz2/9E3sjUgQCOoJeuSnUi1LL7O09ib7sGBPEAAAAB; SCOUTER=z2tbdo7svf2fqv; clientid=010031612824; TMOSHCooKie=UfDLRZwsU2YtOxSnB81hijAJAf0bFhs06pOF1fUJhHl+auBsXISMJ/LRpNTWB7YvFA9MiPXrh8itF3WW6nWYMq8dB7k5bjkcYBsAAAAB; JSESSIONID=tcrBplUgImclXsIDYq+5-Yev.cip22',
                              'Host': 'consul.mofa.go.kr',
                              'Origin': 'https://consul.mofa.go.kr',
                              'Referer': 'https://consul.mofa.go.kr/ciph/0800/selectCIPH0801Deng.do',
                              'sec-ch-ua': '\".Not/A)Brand\";v=\"99\", \"Google Chrome\";v=\"103\", \"Chromium\";v=\"103\"',
                              'sec-ch-ua-mobile': '?0',
                              'sec-ch-ua-platform': '\"Linux\"',
                              'Sec-Fetch-Dest': 'empty',
                              'Sec-Fetch-Mode': 'cors',
                              'Sec-Fetch-Site': 'same-origin',
                              'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
                              'X-Requested-With': 'XMLHttpRequest'
                          })
        response = json.loads(r.content)
        data = [date['visitYn'].lower() for date in response['visitReserveCalendarYesResult']]

        if response and 'y' in data:
            message = f'Есть место {MONTHS_BY_POSITION.get(date.month)}!'
            requests.post(
                f'https://api.telegram.org/bot5430523711:AAHFQFT5_dfsZO04cmjQfQGHwMJXm3-YNoI/sendMessage?chat_id=353761483&text={message}'
            )
            return True
    except:
        pass
    return False


if __name__ == '__main__':
    now = datetime.datetime.now()
    next_ = datetime.datetime.today() + relativedelta(months=1)

    a = time.perf_counter()
    check_date(now)
    check_date(next_)
    b = time.perf_counter()

    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)
    print(str(b - a) + "_stop")