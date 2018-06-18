from urllib import parse

base_url = 'http://sou.zhaopin.com/jobs/searchresult.ashx?'

# 封装请求地址
def reqUrl(jl, kw, p=1):
    params = {
        'jl': jl,  # 工作地址
        'kw': kw,  # 职位名称
        'p': p,  # 页码
    }
    params = parse.urlencode(params)
    start_url = base_url + params
    return start_url


# 配置请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:60.0) Gecko/20100101 Firefox/60.0',
}

# 配置数据库（mysql）
DATABASE = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'password': '',
    'db': 'zhilian',
    'charset': 'utf8'
}