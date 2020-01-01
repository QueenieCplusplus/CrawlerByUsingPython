# 2020.1/1 ＡＭ11:30, by Queenie Chen 

# 表單動作是指發送對象，即目標檔案的相對路徑，非絕對路徑
# 欄位名稱為 uploadImage，欄位名稱決定了提交表單時 POST 給伺服器的參數名稱
# 請確保變數名稱與參數名稱相符。
# enctype 如選擇 plain text 則此上傳文件的功能會變成 comment 留言

# <form action="processing2.php" method="post" enctype="multipart/form-data"> 

#                                     # 倘若這邊是文件類型檔案而非text則邏輯面要post files而非data
#     Lets upload jpg, png, or gif here: <input type="file" name="uploadImage"><br>

#     <input type="submit" value="Upload File Here">

# </form>

import requests

                       # 第一個參數是檔案的相對於腳本的路徑如 ../files/poupousPicture.png
image = {'uploadImage': open('', 'rb')}

# 第一個參數為網頁的絕對路徑
rq = requests.post('', files=image)

print(rq.text)

