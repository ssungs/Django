import requests
from bs4 import BeautifulSoup

import json
import csv


headers = {
    'authority': 'search.shopping.naver.com',
    'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
    'accept': 'application/json, text/plain, */*',
    'urlprefix': '/api',
    'sec-ch-ua-mobile': '?0',
    'logic': 'PART',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://search.shopping.naver.com/search/all?frm=NVSHATC&origQuery=%ED%82%A4%EB%B3%B4%EB%93%9C&pagingIndex=1&pagingSize=20&productSet=total&query=%ED%82%A4%EB%B3%B4%EB%93%9C&sort=rel&timestamp=&viewType=list',
    'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    'cookie': 'NRTK=ag#all_gr#1_ma#-2_si#0_en#0_sp#0; NNB=NP3GCGTIIQFGA; NID_AUT=unqu3aaSzHU/8oc8WWBzbTuVf7nKkpD0gnRSOIqrVQdG/qDCeIbqfJQBU6tsi3e+; NID_JKL=62gM4oke7tg0EvQWFq2WwFYu7/SHpM4DAXnZ/3LEXEQ=; AD_SHP_BID=1; ASID=3b088bb300000177b042837100000061; nx_ssl=2; JSESSIONID=5E8143E632FBA8218D41186D9B2D1140; page_uid=hcHkhwprvmZssTWZU30ssssssSK-056632; spage_uid=hcHkhwprvmZssTWZU30ssssssSK-056632; NID_SES=AAABjCko+pqSq2vVMEg6h3EzzXvQwxcVcyg6qEfC+x/t9In3TItrv+zfWQYBCUt6xHPuf8FMrb1iF/aS9zK+Po1be9FXiGX4aE6sDKbNz2AlCEpGDoqtwTK1YhiAJwjLPW532/xNrdshVa+fyyyC58muvEcVEILMrf/BAXZ27Xr5pKNP3q3khyjv5SxlLa7T4EJ3KBa9jQCURd3XfH6ktQOC/c/TKY0ht28K1jh3ZV24AxctlAxmrioE+6X2ZiZK39DenjNEy5G6i6FGipkXXpvkecFX2uxw/KDVI5UwPd+Grx5AgXG5Qd7J1T4uFfczdUYEPUglChL12cgLCvVhj5dF2VDoQLB8aU9cuTOmUPmeQxWMWI6P95idLsBMH++2YOFLKVqRbAqe3FI9G22dPx3WuwV0AHarmTavECKuMr4Ya4I7sb9juwq/7ZEmDJrhLZ4908ic0WVZ4EYfPSsnTzqQMH6/XIEjGILZmX7r6fLM6uE6pYjF9wtTf+1sa4HmpFKAS1e3LXRNsk3zHWAc5NjLOZk=; BMR=',
}

result = []

for i in range(1, 10 + 1):
    params = (
        ('sort', 'rel'),
        ('pagingIndex', '{}'.format(i)),
        ('pagingSize', '20'),
        ('viewType', 'list'),
        ('productSet', 'total'),
        ('frm', 'NVSHATC'),
        ('query', '키보드'),
        ('origQuery', '키보드'),
    )


    response = requests.get('https://search.shopping.naver.com/search/all', headers=headers, params=params)

    result_dict = json.loads(response.text)

    products_data = result_dict['shoppingResult']['products']

 

    for product_data in products_data:
        product = product_data['productTitle']
        price = product_data['price']
        reviews = product_data['reviewCount']
        keep_cnt = product_data['keepCnt']
        image = product_data['imageUrl']
        smart_farm_data = {
            'product': product,
            'price': '최저: {}'.format(price),
            'review': reviews,
            'keep': keep_cnt,
            'image': image,
            'page': i
            }
        # print(smart_farm_data)
        result.append(smart_farm_data)
        
    

with open('filepath.csv', 'w', newline='', encoding='EUC-KR') as f:
    fields = ["product", "price", "review", "keep", 'image', 'page']
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()
    writer.writerows(result)
    
    
# json_dump_file = json.dumps(result, ensure_ascii = False)

# print(result)
# print(json_dump_file)

# my_dict = ast.literal_eval(json_dump_file)



# with open('filepath.csv', 'w', newline='', encoding='utf-8') as f:
#     fields = ["product", "price", "review", "keep"]
#     writer = csv.writer(f)
#     writer.writerow(fields)
#     writer.writerows(result)