import json, logging

def read_json(file_path):
    with open(file_path) as file:
        json_file = json.load(file)
    return json_file


def parse_cookies(cookies):
    group_value = ''
    access_token = ''
    refresh_token = ''
    user_id = ''
    cf_bm = ''

    if cookies:
        with open(cookies) as file:
            json_raw = json.loads(file.read())
            for item in json_raw:
                if item['name'] == '__Secure-ab-group':
                    group_value = item['value']
                elif item['name'] == '__Secure-access-token':
                    access_token = item['value']
                elif item['name'] == '__Secure-refresh-token':
                    refresh_token = item['value']
                elif item['name'] == '__Secure-user-id':
                    user_id = item['value']
                elif item['name'] == '__cf_bm':
                    cf_bm = item['value']
            return group_value, access_token, refresh_token, user_id, cf_bm
    else:
        logging.warning('Куки не найдены!')


def generate_headers(company_id, group_value, access_token, refresh_token, user_id, cf_bm):
    headers = {
        'authority': 'seller.ozon.ru',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'ru',
        'content-type': 'application/json',
        'cookie': f'__Secure-ab-group={group_value}; __Secure-access-token={access_token}; __Secure-refresh-token={refresh_token}; __Secure-user-id={user_id}; __cf_bm={cf_bm}; __Secure-ab-group={group_value}; __Secure-access-token={access_token}; __Secure-refresh-token={refresh_token}; __Secure-user-id={user_id}; __cf_bm={cf_bm}',
        'origin': 'https://seller.ozon.ru',
        'referer': 'https://seller.ozon.ru/app/reviews',
        'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        # 'sentry-trace': 'd22f8266447d41a8ac67b2d6279b9d2d-938428fd81d1024b-0',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
        'x-o3-company-id': company_id,
        'x-o3-language': 'ru'
    }

    return headers