import requests

cookies = {
    'shortlist_prompts': 'true',
    'exp_prm-ab-testing-new': 'prm-ab-testing-new-keep',
    'exp_profile-ab-testing': 'profile-test-recommended',
    'CookieConsent': '{stamp:%27w5M3CdpRUiAC1cNc2x+VPXo0Tc+2UkbB+THNZXs9gA0ybrrGfaiuaA==%27%2Cnecessary:true%2Cpreferences:true%2Cstatistics:true%2Cmarketing:true%2Cmethod:%27explicit%27%2Cver:1%2Cutc:1695907919759%2Cregion:%27id%27}',
    'cf_clearance': '6cdd0KJUpfod1JhManrX6vHwqLgH6GETLxK.hp3P834-1696471989-0-1-c1860a0.cdd47483.ece37d89-0.2.1696471989',
    '__cf_bm': 'Q8AWn0YA.g0a3WUDnqlmj1G7pXzL4c5R8RZC5zrGe0E-1696473456-0-AXOC0NvSohiu++Icerpcr3RM6CEBSZcFdUxhTU+9xWDKXeRMykaeIjiYgXWVxaUw49lfbzaiqa6nRnCC+FMVgaI=',
}

headers = {
    'authority': 'clutch.co',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    # 'cookie': 'shortlist_prompts=true; exp_prm-ab-testing-new=prm-ab-testing-new-keep; exp_profile-ab-testing=profile-test-recommended; CookieConsent={stamp:%27w5M3CdpRUiAC1cNc2x+VPXo0Tc+2UkbB+THNZXs9gA0ybrrGfaiuaA==%27%2Cnecessary:true%2Cpreferences:true%2Cstatistics:true%2Cmarketing:true%2Cmethod:%27explicit%27%2Cver:1%2Cutc:1695907919759%2Cregion:%27id%27}; cf_clearance=6cdd0KJUpfod1JhManrX6vHwqLgH6GETLxK.hp3P834-1696471989-0-1-c1860a0.cdd47483.ece37d89-0.2.1696471989; __cf_bm=Q8AWn0YA.g0a3WUDnqlmj1G7pXzL4c5R8RZC5zrGe0E-1696473456-0-AXOC0NvSohiu++Icerpcr3RM6CEBSZcFdUxhTU+9xWDKXeRMykaeIjiYgXWVxaUw49lfbzaiqa6nRnCC+FMVgaI=',
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
}

params = {
    'reviews': '10',
}


response = requests.get('https://clutch.co/agencies/design', params=params, cookies=cookies, headers=headers)

print(response.status_code)