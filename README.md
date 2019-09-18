<h1 align="center">
    Discord Webhook for MapleStory Official Annocement
</h1>

<div align="center">
    自動抓官方<strong>活動公告</strong>，內容以embed格式包裝，並推播到Discord Server，每次執行前會先check for update。
</div>


## Package
- [Requests](https://2.python-requests.org/en/master/#)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
- [dhooks](https://github.com/4rqm/dhooks/)

## Usage
至Discord Server文字頻道啟用Webhook功能，
將Webhook link貼到類別初始化的參數當中。
```python
class MSWEBHOOK():
    def __init__(self):
        if MS_Official.Is_updated():
            exit()
        # Your webhook link of discord server.
        self.hook = Webhook('https://discordapp.com/api/webhooks/{id}/{token}')
        # Webhook link for testing.
        self.thook = Webhook('https://discordapp.com/api/webhooks/{id}/{token}')
```

終端機直接執行。
```commandline
python MS_Webhook
```

推播到測試的server。
```commandline
python MS_Webhook t
```