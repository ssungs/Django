import requests
import csv
import json

headers = {
    'authority': 'forum.netmarble.com',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'x-requested-with': 'XMLHttpRequest',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://forum.netmarble.com/sk2/view/17/747172',
    'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    'cookie': '_ga=GA1.2.863468984.1611797310; _gid=GA1.2.1306029175.1619066685; forumToken=CFB38FA692C814B644F470A41F6931C9F9CCC2A5DE467599CB06CB5C04BEC2A0AA27AAD9F35D5F8F0474F8B846C6ACECC33081AA4E6AEDD9B27992C98979EAFA2115DA70AE9A935E24DBBC916197FA6C92D7E871080782A13D0766DE584EB49FF48A7521A0BFF7FCF0822BF35DE186F23B864040DD2361A80D5F44FE01D9CDEBA6B00543883B4A21E58FFA301C397D6079C3C2162E4B8F06F228AC95DF1CCEC2C4F720054E0A1F71696D8D74BA289CAD02B28276CFC87532EE0591D421E9DFC8D21352AB153440707843AC00422A2A59EDFBDB4F93C69F4D9D3D1D768D61E7B36407932CBFF4FA2CE535FCDAE2D79EC8C2BC2FBEC7C2306C79B8C20E9D99BE4A5BA725ED6EEC97C731048DDF2B3200734933C33227B4CE22C13EDB30735A2581C7549189AE73BCEAC8131DC042EE3572BA671D2989FC6B48E68D77628CB084B75DC8890E8C6E5A813330747342F40FDF4DAC2F26A62CF95D2975F937091E6F4A437697D0F1C55B02EC064AC79233BC495AB2FD1851BFB4CDD01D6B6CFFF19FF802B71413AB7BCD0AE68CA881FC0BE63927E832B82F5C73B8EAA57003E540C862C797B265111CBC988B7006C39F2A73C393310268F90A9377D8568BBF4A6CED651CC08BF2943DA873765C4C1A0BE6FE61DF75D2B217F34798AB00F8BB6C4A8B12DBFA1C5778E034884E12493EC6EAAA7C29410F31C2A34FBC30B8ED2D6F4244D9EFCFBE68AA79C37D03C095E020B1E7CA0D7347A6FE925881E2F2367A532442DED975A9569232536E57CD9D132B5726F71E2BAF86A9D9DE93C417B46D07B3191286428293B42F00E8F1C434628F20AF54516DF90BDD58B11899D94341A8F370B61914AEB46F3204D1CE6EEF47CE16AFF812F5BAEB128C1BE2452992EB7480C978E7559E5E546DF52890A1ACD79CA995431480A30600BAD776336E4E8C6B5E77992447F54E773A2F5DB290C117FD6EDB2702EC4C7A0423ADB12B3C256188AF1EFD2131EDB694368915C6D0ED3538A5136B253D5A9DF32ED8473B7D5143723E65C08D48958C89FFB2B97DFC435B7E901433B03B9C2382FBC8AA000C6E884A72DCCCB89AA3BA5D4189B6F5EC05C65844F9D72560C7796391BBD7C0D4DAD5ED684B0F2AB89CBC81636F3A8DF7371CB6930CD4B6F6697CA54D44E5BC1CEE12FAB4EF30D37441F34E8584CCBF69A8568895537A7D861239FAEF6529376DB3E0F9C8789EED8C43BEF885401BBED53BD1F4FE08A9AB49EF9EECA1B9DC; _gali=contentsDetail; _dc_gtm_UA-150068984-1=1',
}

params = (
    ('menuSeq', '17'),
    ('viewFlag', 'false'),
    ('_', '1619066879170'),
)

response = requests.get('https://forum.netmarble.com/api/game/sknightsmmo/official/forum/sk2/article/747172', headers=headers, params=params)

coupon = json.loads(response.text)

text = coupon['article']['content']

text_rep = text.replace('<p>', '')
text_rep = text_rep.replace('</p>', '')
text_rep = text_rep.replace('<br>', '')
text_rep = text_rep.replace('&nbsp;', '')
text_rep = text_rep.replace('https://couponview.netmarble.com/coupon/sknightsmmo/1290', '')
text_rep = text_rep.replace(':', '')
text_rep = text_rep.replace('<strong>', '')
text_rep = text_rep.replace('</strong', '')
text_rep = text_rep.replace('#', '')
text_rep = text_rep.replace('<img alt="smiley" height="23" src="https//forum.netmarble.com/resources/_build/js/lib/ckeditor_pc/plugins/smiley/images/regular_smile.png" title="smiley" width="23">', '')
text_rep = text_rep.replace('\n', '')
text_rep = text_rep.replace('(', '- ')
text_rep = text_rep.replace(')', '\n')
text_rep = text_rep.replace('>', '\n')
text_rep = text_rep.replace(' ', '')

com = text_rep.split('\n')

remove = com.pop(-1)

result = []

for coup in com:
    if len(coup) > 10:
        result.append(coup)

complete = {}

for coupon in result:
    split = coupon.split('-')
    sp = split[0].split('.')
    complete[sp[1]] = split[1]


# user_id = input('유저번호를 입력하세요. : ')

# print('입력된 유저 번호는 {} 입니다'.format(user_id), '\n', complete)

res = []


for key,value in complete.items():
    res.append(key)


res_dict = dict(enumerate(res))

wow = {'id': '', 'code': '', 'result': 0, 'response': '', 'description': '요청 전'}

for key,value in res_dict.items():
    wow['id'] = '{}'.format((int(key)+1))
    wow['code'] = '{}'.format(value)
    print(wow)