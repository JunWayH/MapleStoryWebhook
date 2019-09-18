import requests
from bs4 import BeautifulSoup

HOST_URL = 'https://tw.beanfun.com/maplestory/'

def Is_updated():
    print('Checking for update....')
    r = requests.get('https://tw.beanfun.com/maplestory/BullentinList.aspx?cate=71')
    soup = BeautifulSoup(r.text, 'html.parser')
    r.close()
    newest_date = ''
    for ele in soup.select("td[height='21']"):
        if ele['width'] == '70':
            newest_date = ele.text
            break
    
    with open('newdate', 'r+') as f:
        if f.readline() == newest_date:
            print('Already updated..')
            return True
        else:
            print('need updating....')
            f.seek(0)
            f.truncate()
            f.write(newest_date)
            return False

def get_official_announcement():
    print('Getting offical announcement..')
    r = requests.get('https://tw.beanfun.com/maplestory/BullentinList.aspx?cate=71')
    soup = BeautifulSoup(r.text, "html.parser")
    r.close()
    anno_dict = {}
    for i in soup.select('.maple01 a'):
        temp_url = i['href']
        if 'BullentinDetail' in temp_url:
            temp_url = HOST_URL + temp_url
        elif 'EventAD' in temp_url:
            mimage = get_main_image(temp_url)
        anno_dict[i.text] = temp_url
    del anno_dict['全部']
    return anno_dict, mimage

def get_main_image(inputurl):
    tr = requests.get(inputurl)
    tsoup = BeautifulSoup(tr.text, "html.parser")
    timage = tsoup.select('.header img')[0]['src']
    return timage

if __name__ == "__main__":
    get_official_announcement()