import requests

cookies = {
    'exp_prm-ab-testing-new': 'prm-ab-testing-new-keep',
    'exp_profile-ab-testing': 'profile-test-recommended',
    'CookieConsent': '{stamp:%27w5M3CdpRUiAC1cNc2x+VPXo0Tc+2UkbB+THNZXs9gA0ybrrGfaiuaA==%27%2Cnecessary:true%2Cpreferences:true%2Cstatistics:true%2Cmarketing:true%2Cmethod:%27explicit%27%2Cver:1%2Cutc:1695907919759%2Cregion:%27id%27}',
    '__cf_bm': '0H1DvxNTj34fbTVJKljXDcxQsx1XRTXvpCiYdxQUSqM-1696751789-0-AV3ouU7A74hIVs0WQjAlqJjJPET48KLBduxW2nSUM2GD+Ol3nr1oT70zrqYfxC3FXVg/K0c8iesbyu/XsJtL038=',
    'cf_clearance': 'HYyle2xbJsH5qIicLvBdx18hOqFVPoatgfmi9H4.Mlo-1696751790-0-1-accd418c.ffaccd41.de9bc44b-0.2.1696751790',
}

headers = {
    'authority': 'clutch.co',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    # 'cookie': 'exp_prm-ab-testing-new=prm-ab-testing-new-keep; exp_profile-ab-testing=profile-test-recommended; CookieConsent={stamp:%27w5M3CdpRUiAC1cNc2x+VPXo0Tc+2UkbB+THNZXs9gA0ybrrGfaiuaA==%27%2Cnecessary:true%2Cpreferences:true%2Cstatistics:true%2Cmarketing:true%2Cmethod:%27explicit%27%2Cver:1%2Cutc:1695907919759%2Cregion:%27id%27}; __cf_bm=0H1DvxNTj34fbTVJKljXDcxQsx1XRTXvpCiYdxQUSqM-1696751789-0-AV3ouU7A74hIVs0WQjAlqJjJPET48KLBduxW2nSUM2GD+Ol3nr1oT70zrqYfxC3FXVg/K0c8iesbyu/XsJtL038=; cf_clearance=HYyle2xbJsH5qIicLvBdx18hOqFVPoatgfmi9H4.Mlo-1696751790-0-1-accd418c.ffaccd41.de9bc44b-0.2.1696751790',
    'if-modified-since': 'Sun, 08 Oct 2023 08:05:39 GMT',
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
}

response = requests.get('https://clutch.co/', cookies=cookies, headers=headers)
print(response.status_code)