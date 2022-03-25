# coding:utf-8
from urllib.parse import unquote
import requests
from lxml import etree
import re
import copy
from redis import Redis

link = 'https://s.taobao.com/search?ie=utf8&initiative_id=staobaoz_20220326&stats_click=search_radio_all%3A1&js=1&imgfile=&q=%E4%B9%90%E9%AB%98&suggest=0_1&_input_charset=utf-8&wq=legao&suggest_query=legao&source=suggest'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.46',
    'referer': 'https://s.taobao.com/search?ie=utf8&initiative_id=staobaoz_20220326&stats_click=search_radio_all%3A1&js=1&imgfile=&q=%E4%B9%90%E9%AB%98&suggest=0_1&_input_charset=utf-8&wq=legao&suggest_query=legao&source=suggest',
    'cookie': 'cna=VxSdGq5W9WECAXPNciF8oBw6; lgc=bzzzz_kaba; tracknick=bzzzz_kaba; enc=pI80SsyGaXghBvrT9b%2FiXoJMBsdVdQYHPxwce1lUj9%2F5fwIGH7%2F3hZOvz5eIFDSDCbdZCtknqc5OQnwbPG3dpQ%3D%3D; thw=cn; sgcookie=E100RTx%2B39fPnBdzkimf3cFg7O3eIcCh%2BwJjRxP1j0W4I3XrH%2FMRU29CuJJpHzdmosKRhbUlbM4u2jUWzWETd8A9C%2FtcrDWJdz4YSJvSuVgusebL390zhmyQ%2FdnzCjPKpyzW; uc3=id2=UojcjU6y2%2BVQSw%3D%3D&lg2=WqG3DMC9VAQiUQ%3D%3D&nk2=AR7rEKars5hk%2Fw%3D%3D&vt3=F8dCvConqKrxwZvQzf4%3D; uc4=id4=0%40UOBYxUZKAx73vNpi6CS1hl6uJSD4&nk4=0%40A7NLpSHVvfKW3Z7DjMYJ63kLDrpD; _cc_=URm48syIZQ%3D%3D; _m_h5_tk=eafef614954e34957560c3104b0d2a36_1648233451136; _m_h5_tk_enc=f40f3d2f1e7951f04a98385a9c508573; mt=ci=-1_0; cookie2=279fb819b7de90c53c103591eee7b675; uc1=cookie14=UoewCLNQ6ITIZA%3D%3D; t=1c8d579fff35a4cdc555b38dcfcc7e32; _tb_token_=3778166e58fbe; alitrackid=www.taobao.com; lastalitrackid=www.taobao.com; xlly_s=1; JSESSIONID=93D6C167FF6F243147372B9F10A12E0B; tfstk=cqdFB0qWYXhEmn1SH61rAVqvbkfdZ68Hr57fKp3UzB3ZIiBhixZRShu17aaaq9f..; l=eBO0BG2uLPsVidgLBOfZnurza77TKIRfguPzaNbMiOCPO7Cp54MVW60BEcY9CnGVHsA9R3-3_v0_BnD9Vyh4pYD4L3k_J_qI3dC..; isg=BAYG7A_umCymvUxo4_CZ88uBV_yIZ0ohjg6Ck_AvvykE86cNWPeGMAlByy8_20I5; x5sec=7b227365617263686170703b32223a223739326639313738323633623336326364656564306434646664313632363733434b485639354547454a2f7638637a493461434768514561444445354f4459794e4463334f5441374d5367434d4b6546677037382f2f2f2f2f77453d227d',
    }
response = requests.get(url = link, headers = headers).text
with open('./file.html','w',encoding = 'utf-8') as f:
    f.write(response)
f.close()
    