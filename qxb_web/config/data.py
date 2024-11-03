"""
此文件用来存放测试数据
"""

SIT_URL = ''

UAT_URL = ''

PRD_URL = 'https://www.qixin.com/api/search/advanced'

# ================================================cookie===============================================================

SIT_COOKIE = ''

UAT_COOKIE = ''

PRD_COOKIE = {
    'Cookie': 'aliyungf_tc=3cab73cf0d1528b00fb0ef547bc21d31c8fb83676ee766d0a7c4107b4b7d7d3e; web-canary=never;'
              ' Hm_lvt_52d64b8d3f6d42a2e416d59635df3f71=1729949892; '
              'HMACCOUNT=5052568F7ABA7226; flogger_fpid=4f506787d46b929efc2a243bc502a5bd; '
              'fid=6522f1453ebbdcc31fad4db579c0f2db; acw_tc=ac11000117305327598935764e0c715704c75a5578b5dd4571079f1eb32d67;'
              ' adv-banner_visible=%5B%5D; pdid=s%3AZM3AmXf9jyUTbDeRGzCqxEtcQZeEXPe8.ElZXnxIJsyYxCO6NG728NGEWZSIri0WrJfFAwOg5FMM; '
              'Hm_lpvt_52d64b8d3f6d42a2e416d59635df3f71=1730532792'
}

headers = {
    'Content-Type': 'application/json;charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest'
}

# =================================================入参================================================================

# 关键词
key_word = {"key": "哈哈", "page": 1}

# 搜索范围-企业名称
scope_name = {"scope": [1], "key": "哈哈", "page": 1}
