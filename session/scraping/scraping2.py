import requests
from bs4 import BeautifulSoup

headers = {
    'authority': 'movie.naver.com',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'iframe',
    'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'referer': 'https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code=189075&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false',
    'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    'cookie': 'NRTK=ag#all_gr#1_ma#-2_si#0_en#0_sp#0; NNB=NP3GCGTIIQFGA; NID_AUT=unqu3aaSzHU/8oc8WWBzbTuVf7nKkpD0gnRSOIqrVQdG/qDCeIbqfJQBU6tsi3e+; NID_JKL=62gM4oke7tg0EvQWFq2WwFYu7/SHpM4DAXnZ/3LEXEQ=; ASID=3b088bb300000177b042837100000061; nx_ssl=2; page_uid=hciqhdp0J14ssCKHd7Kssssstio-296887; notSupportBrowserAlert=true; NM_THUMB_PROMOTION_BLOCK=Y; JSESSIONID=E9BA6937A952105E7C7806289FBB8408; csrf_token=4efbc1fe-6113-4b47-9017-6118bdf9d476; NID_SES=AAABl9YvuoRvyEfe926ZE8T0SsbpEfhKFZ2M/d/18/5o1q2kisJwkbAfTYYIITI+O66ZUkPXuIZ40MWElGgejXfVbCMra/IgRjvfsUtjsKo0l2IWLq1lrOdVcRoF9fCksgLKfcE83NOEvWFzz/JisehTvXhoAhYoxm48Litre6oeXcueZ+YU+m18I9tcZlHPbAbyvJGSVMWz2O1NkV3+a7rybUB6kir8lSBt76A+ha1kzgllencjyqoq/183q1oQOHP0uZkzPj6h+hNG47/VRXHNwGYo61YPKHrz6yjoAezNJClN17OtSxEKPmzgwAZSSi9HgLxFNQ1xh6qR4MI/Gp5iiQkzZMhf7bHc77qCtQtbSzsoHytS9eF7RuQALbPmda170oYknfhoEOe+n0R5/7S8jiiviUvc+kNK9Qwd81f/MJ/wObj8NxRVC4zVzQepQYZwvem5bvlctDr3JkeEjmCwJUAZpRSKO5HmpaI3E/Sla53qk/oAks7+t7c91Tjh//i2nKUZao4fIDsosfVx5mX5CHYSOAIczWgQGRAFItMSMlks',
}

def inputPageNum(page_num):
    if int(page_num) == 0:
        return '0보다 크게 입력하세요'

    reviews = {}
    for i in range(page_num):
        params = (
            ('code', '189075'),
            ('type', 'after'),
            ('isActualPointWriteExecute', 'false'),
            ('isMileageSubscriptionAlready', 'false'),
            ('isMileageSubscriptionReject', 'false'),
            ('page', '{}'.format(i)),
        )

        response = requests.get('https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn', headers=headers, params=params)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        li_lists = soup.select('body > div > div > div.score_result > ul > li')

        # print(li_lists)

        # solved

        count = 0
        for li in li_lists:

            filtered_ment = li.select_one('#_filtered_ment_{}'.format(count))
            coment = filtered_ment.text
            rate = li.select_one('div.star_score > em').text
            if (filtered_ment.select_one('span._unfold_ment')):
                coment = filtered_ment.select_one('span > a')['data-src']

            reviews = {
                'coment' : coment.strip(),
                'rate' : rate
            }
            count += 1
            
            # print(reviews)


        return print(reviews)


        # count = 0

        # for li in ll_lists:
        #     # ems = soup1.select('body > div > div > div.score_result > ul > li > div.star_score > em')
        #     reviews = li.select_one('body > div > div > div.score_result > ul > li > div.score_reple > p > span#_filtered_ment_{}'.format(count))
        #     if li.select_one('#_unfold_ment{}'.format(count)):
        #       print(reviews.select_one('#_unfold_ment{} > a'.format(count))['data-src'])
        #     print(reviews)
        #     count += 1

inputPageNum(int(input('Enter to page number : ')))