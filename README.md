# TelegramAdUnit
#### Python module for sending ads to the Telegram bot.
# Install TelegramAdUnit
#### A command to install modules for working with TelegramAdUnit.
`pip install selenium pyTelegramBotAPI`
#### Now download the tau.py file in the release. Choose the latest version.
#### After that, add the tau.py file to your bot project and add the following command in the bot code itself.
`import tau`
# Work with TelegramAdUnit
#### There are only 2 teams in tau: `google_adsense()` and `yandex_ad_network()`.
#### `google_adsense()` - sends ad units from Google AdSense.
#### `yandex_ad_network()` - sends ad units from the Yandex ad network.
#### To send ads, you need to create a dictionary with information.
#### Here is the dictionary.
```python
ad = {
        'infor_ad':{
            'bot':,
            'id_message':,
            'webdriver':,
            'url_site':,
            'id_google_adsense':,
            'id_yandex_ad_network':,
            'time_sleep':,
            'push_button':,
            'print_error':
        },
        'text_ad':{
            'text_ad':,
            'you_site':,
            'service_google':,
            'service_yandex':,
            'button_text':,
            'push_text':
        },
    }
```
#### Here is a table of what to add.
Title|What do you need
-----|----------------
infor_ad.bot|your bot
infor_ad.id_message|id message
infor_ad.webdriver|selenium web driver
infor_ad.url_site|url from your site
infor_ad.id_google_adsense|id iframe
infor_ad.id_yandex_ad_network|id div
infor_ad.time_sleep|delay to load ads
infor_ad.push_button|when you click on the link, something will happen
infor_ad.print_error|error output
text_ad|ad text
