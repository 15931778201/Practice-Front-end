import time
import pyquery
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait

chromedriver_path=r'/Users/wushaoxia/Downloads/chromedriver'
driver = webdriver.Chrome(executable_path=chromedriver_path)
wait = WebDriverWait(driver, 10)

driver.implicitly_wait(10)

driver.set_window_size(1280,800)

def index_page(page):
    """
    抓取索引页
    :param page: 页码
    """
    print('正在爬取第', str(page), '页数据')
    try:
        url = 'https://search.jd.com/Search?keyword=iPhone&ev=exbrand_Apple'
        driver.get(url)
        if page > 1:
            input = driver.find_element_by_xpath('//*[@id="J_bottomPage"]/span[2]/input')
            button = driver.find_element_by_xpath('//*[@id="J_bottomPage"]/span[2]/a')
            input.clear()
            input.send_keys(page)
            button.click()
        get_products()
    except TimeoutException:
        index_page(page)
        
def get_products():
    """
    提取商品数据
    """
    js = '''
    timer = setInterval(function(){
       var scrollTop=document.documentElement.scrollTop||document.body.scrollTop;
       var ispeed=Math.floor(document.body.scrollHeight / 100);
       if(scrollTop > document.body.scrollHeight * 90 / 100){
           clearInterval(timer);
       }
       console.log('scrollTop:'+scrollTop)
       console.log('scrollHeight:'+document.body.scrollHeight)
       window.scrollTo(0, scrollTop+ispeed)
    }, 20)
    '''
    driver.execute_script(js)
    time.sleep(2.5)
    html = driver.page_source
    doc = pyquery(html)
    items = doc('#J_goodsList .gl-item .gl-i-wrap').items()
    i = 0
    for item in items:
        insert_data = {
            'image': item.find('.p-img a img').attr('src'),
            'price': item.find('.p-price i').text(),
            'name': item.find('.p-name em').text(),
            'commit': item.find('.p-commit a').text(),
            'shop': item.find('.p-shop a').text(),
            'icons': item.find('.p-icons .goods-icons').text()
        }
        i += 1
        print('当前第', str(i), '条数据，内容为：' , insert_data)
