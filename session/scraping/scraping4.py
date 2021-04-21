import requests
import json

headers = {
    'authority': 'www.youtube.com',
    'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
    'x-origin': 'https://www.youtube.com',
    'sec-ch-ua-mobile': '?0',
    'authorization': 'SAPISIDHASH 1618906115_0c60df35ec8e7b354ca780e787b44ec04dbb3a9d',
    'content-type': 'application/json',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
    'x-youtube-client-name': '1',
    'x-youtube-client-version': '2.20210418.07.00',
    'x-goog-authuser': '0',
    'x-goog-visitor-id': 'CgtoMXJ1N0J0aXBXOCjyl_qDBg%3D%3D',
    'accept': '*/*',
    'origin': 'https://www.youtube.com',
    'x-client-data': 'CIm2yQEIpbbJAQipncoBCJasygEI+MfKAQiU+8oBCLGaywEI5JzLAQipncsBGOCaywE=',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'same-origin',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.youtube.com/channel/UCUpJs89fSBXNolQGOYKn0YQ/videos',
    'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    'cookie': 'VISITOR_INFO1_LIVE=h1ru7BtipW8; HSID=AkpSqfqYJdxNi7fYs; SSID=AhFG6Gpy1PRFBVc-c; APISID=Lw0xPlAFqKusNk55/A6263NSj_CLVKC0dR; SAPISID=AzOZV_GhUUCEX0jl/AW8Bz5mHuoAfiSkFz; __Secure-3PAPISID=AzOZV_GhUUCEX0jl/AW8Bz5mHuoAfiSkFz; LOGIN_INFO=AFmmF2swRQIhAMK0aCd7B1l0zh0VzvOfJDoxeXGnJ54e_lD7lJMVBx2cAiAQKeY2EpAwejiFPLx5x3vM1c2L3QswawtAK1gskgH0lw:QUQ3MjNmeHdrX0NrazJMcWdDV0JFZXRMWHZVRFRWYldCdXBjR3ZGajZjWXJxdW5RcW9FMkFBZU1zN3lfelEzT2VMMlRLWngxd1NZUmVwejhCNndLTTU0enhuVDg3dzdYazQxS1dmbUk5TW40d0twc0ZFcnBPOHdJdFBMR25xWUZ6Q1daamhDeU5mYjMyOWNibUN1bzdJZGpHUmVrbzEzWWgyeUl1RGFpRURaU3p1NTlJcmFzb0w0; PREF=tz=Asia.Seoul; _gcl_au=1.1.1175808146.1611883835; SID=8AePAaXIX7vZfBBV8iv7ce0Yo3HN4oj2G8I0imCL60Delzv1M2X8SMWnHF1A2awb414LUw.; __Secure-3PSID=8AePAaXIX7vZfBBV8iv7ce0Yo3HN4oj2G8I0imCL60Delzv1hWOGlYbcV6hjFUl9RTdNdw.; YSC=D7_PPQQ6hfk; SIDCC=AJi4QfFd_-9GxzXnqx9NIL3U3Od2mSpeCvT1bOaz0zUK7HmMMXj00BZ8oSmKEw9eJ1mOF4cCaRc; __Secure-3PSIDCC=AJi4QfGvmsrSxMcX2iOSDbtn9kOSvSQZyWRZOSVw4mZK7OptME4NKqTfdDpXB65zUOJQhWp-YJI',
}

params = (
    ('key', 'AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8'),
)

data = {
  '{"context":{"client":{"hl":"ko","gl":"KR","remoteHost":"106.242.79.230","deviceMake":"","deviceModel":"","visitorData":"CgtoMXJ1N0J0aXBXOCjyl_qDBg==","userAgent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36,gzip(gfe)","clientName":"WEB","clientVersion":"2.20210418.07.00","osName":"X11","osVersion":"","originalUrl":"https://www.youtube.com/channel/UCUpJs89fSBXNolQGOYKn0YQ/videos","platform":"DESKTOP","clientFormFactor":"UNKNOWN_FORM_FACTOR","timeZone":"Asia/Seoul","browserName":"Chrome","browserVersion":"89.0.4389.114","screenWidthPoints":822,"screenHeightPoints":946,"screenPixelDensity":1,"screenDensityFloat":1,"utcOffsetMinutes":540,"userInterfaceTheme":"USER_INTERFACE_THEME_LIGHT","connectionType":"CONN_CELLULAR_4G","mainAppWebInfo":{"graftUrl":"https://www.youtube.com/channel/UCUpJs89fSBXNolQGOYKn0YQ/videos","webDisplayMode":"WEB_DISPLAY_MODE_BROWSER"}},"user":{"lockedSafetyMode":false},"request":{"useSsl":true,"internalExperimentFlags":[],"consistencyTokenJars":[]},"clientScreenNonce":"MC41MTI2NjU2NDk3MjQ0NDMx","clickTracking":{"clickTrackingParams":"CAAQhGciEwi1ruCdr4zwAhXEOioKHRvRA2Y': '"},"adSignalsInfo":{"params":[{"key":"dt","value":"1618906098868"},{"key":"flash","value":"0"},{"key":"frm","value":"0"},{"key":"u_tz","value":"540"},{"key":"u_his","value":"9"},{"key":"u_java","value":"false"},{"key":"u_h","value":"1080"},{"key":"u_w","value":"1920"},{"key":"u_ah","value":"1050"},{"key":"u_aw","value":"1920"},{"key":"u_cd","value":"24"},{"key":"u_nplug","value":"3"},{"key":"u_nmime","value":"4"},{"key":"bc","value":"31"},{"key":"bih","value":"946"},{"key":"biw","value":"806"},{"key":"brdim","value":"0,30,0,30,1920,30,1920,1050,822,946"},{"key":"vis","value":"1"},{"key":"wgl","value":"true"},{"key":"ca_type","value":"image"}],"bid":"ANyPxKorvJQiEurcY7e9I8uYw25KErXfn_cRimgEcnIBqRDqMY6OVNaGhSahwjT6KqEJfWmFCRTX"}},"continuation":"4qmFsgKPARIYVUNVcEpzODlmU0JYTm9sUUdPWUtuMFlRGkRFZ1oyYVdSbGIzTVlBeUFBTUFFNEFlb0RHME5uVGtSU1JXdFRRM2RwYW5kd2JYYzBZVFp6TkhaWlFrdEVTUSUzRCUzRJoCLGJyb3dzZS1mZWVkVUNVcEpzODlmU0JYTm9sUUdPWUtuMFlRdmlkZW9zMTAy"}'
}

response = requests.get('https://www.youtube.com/youtubei/v1/browse', headers=headers, params=params, data=data)

print(response.text)

# result_dict = json.loads(response.text)

# print(result_dict)

# products_data = result_dict['onResponseReceivedActions']['0']['onResponseReceivedActions']['continuationItems']

# result = []

# for product_data in products_data:
#         title = product_data['gridVideoRenderer']['title']['runs']['0']['text']
#         total_views = product_data['gridVideoRenderer']['viewCountText']['simpleText']
        
#         smart_farm_data = {
#             'title': title,
#             'total_view': total_views
#             }
#         # print(smart_farm_data)
#         result.append(smart_farm_data)
        

# print(result)