import requests 
from bs4 import BeautifulSoup
page = requests.get('https://www.google.de/search?hl=de&source=hp&ei=eHbsX5qyCZWIU9_XtfAM&q=star+wars&oq=star+wars&gs_lcp=CgZwc3ktYWIQAzILCC4QsQMQgwEQkwIyBQguELEDMggILhCxAxCDATIICC4QsQMQgwEyCAgAELEDEIMBMgUILhCxAzIFCAAQsQMyCAguELEDEIMBMggILhCxAxCDATICCC46CwgAELEDEMcBEKMCOgIIADoICAAQxwEQowI6CAguELEDEJMCOggIABDHARCvAToOCAAQsQMQgwEQxwEQowJQ0jZY9mRg2W1oA3AAeACAAaQCiAHACZIBBTcuMy4xmAEAoAEBqgEHZ3dzLXdperABAA&sclient=psy-ab&ved=0ahUKEwiazsuV3vXtAhUVxBQKHd9rDc4Q4dUDCAk&uact=5') 
soup=BeautifulSoup(page.content, 'html.parser')

extra_bar =soup.find(id="extabar")

forecast_items = extra_bar.find(class_="LHJvCe")

results = forecast_items 

result=results.find(id="result-stats").get_text()

print(result)
