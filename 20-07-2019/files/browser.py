import webbrowser
import time

url = 'http://www.mattcole.us/'
url2 = 'http://facebook.com/'
url3 = 'https://gab.ai/home'
url4 = 'https://duckduckgo.com/'

chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

webbrowser.get(chrome_path).open(url)
time.sleep(20)
webbrowser.get(chrome_path).open_new_tab(url2)
time.sleep(20)
webbrowser.get(chrome_path).open_new_tab(url3)
time.sleep(20)
webbrowser.get(chrome_path).open_new_tab(url4)

