#2020, 1/1, 13:00, by Queenie Chen

# 登入架構設計如下：
# login Page 會是登入頁面首頁
# 處理 cookie的頁面是 cookies/welcom
# 使用者第一次登入會使用 post 方法，將登入資訊寫入表單儲存於伺服器專門處理 cookie 的頁面回傳 cookie
# 接著能用 get 方法，並夾帶 cookie
# 連結到 profile

import requests
paramsToGetCookie = {'username': 'Queen', 'password': '000000000'}
rq = requests.post('http://pythonscraping.com/pages/cookies/welcome.php', paramsToGetCookie)

print('cookies is set to:')
print(rq.cookies.get_dict())
print('after login, and cookie processing phase, we can reach to Profile now!')

rq = requests.get('http://pythonscraping.com/pages/cookies/profile.php', cookies=rq.cookies)
print(rq.text)