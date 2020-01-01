# 2020.1/1 ＡＭ11:00, by Queenie Chen


# //表單動作是指發送對象，即目標檔案的相對路徑，非絕對路徑
# //欄位名稱為 name 和 mail，欄位名稱決定了提交表單時 POST 給伺服器的參數名稱
# //請確保變數名稱與參數名稱相符。

# <!-- <form method="post" action="processing.php">

#  Name:<input type="text" name="name"><br>

#  Mail: <input type="url" name="mail"><br>

#  <input type="submit" value="Click On Me">

# </form> -->

import requests

# 欄位名稱即參數名稱
params = {'name':'Queenie', 'mail':'queenieCplusplus@gmail.com'}

# 方法中第一個參數為絕對路徑
rq = requests.post("", data=params)

print(rq.text)
