import scrapy
# from walmart.items import WalmartItem
from walmart.items import WalmartItem
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from scrapy.http import HtmlResponse
from scrapy.http import TextResponse
from lxml import html
from lxml import etree
import csv
import unicodedata
from selenium.webdriver.common.by import By
import time
import json
import pprint
import scrapy
import requests
from time import sleep
import urllib
from PIL import Image



class DictUnicodeProxy(object):
    def __init__(self, d):
        self.d = d
    def __iter__(self):
        return self.d.__iter__()
    def get(self, item, default=None):
        i = self.d.get(item, default)
        if isinstance(i, unicode):
            return i.encode('utf-8')
        return i
class WalmartSpider(scrapy.Spider):
    name = "walmart"


    # def getsimpleshippingData(self):


        
    #     returnitem = []
    #     lis = self.driver.find_elements_by_xpath("//*[contains(@class, 'a-row a-spacing-mini olpOffer')]")
        
    #     for li in lis:
            
    #         eitem = {}
    #         li_price = ""
    #         li_price_info = ""
    #         li_offer_condition = ""
    #         li_seller_name = ""
    #         try:
    #             li_price = li.find_element_by_xpath(".//span[contains(@class, 'olpOfferPrice')]").text
    #         except:
    #             li_price = "null"
    #         print("\n ****** PRICE :      " + li_price)
    #         try:
    #             li_price_info = li.find_element_by_xpath(".//p[contains(@class, 'olpShippingInfo')]/text()").text
    #         except:
    #             li_price_info = "null"
    #         print("\n ****** PRICE_INFO :      " + li_price_info)
    #         try:
    #             li_offer_condition = li.find_element_by_xpath(".//div[@id='offerCondition']").text
    #         except:
    #             li_offer_condition = "null"
    #         print("\n ****** OFFER CONDITION :      " + li_offer_condition)
    #         try:
    #             li_seller_name = li.find_element_by_xpath(".//h3[contains(@class, 'olpSellerName')]/a/img").get_attribute("alt")
    #         except:
    #             try:
    #                 li_seller_name = li.find_element_by_xpath(".//h3[contains(@class, 'olpSellerName')]/img").get_attribute("alt")
    #             except:
    #                 li_seller_name = li.find_element_by_xpath(".//h3[contains(@class, 'olpSellerName')]/span/a").text.encode('utf8')

    #         if li_seller_name.find("Amazon Warehouse") !=-1 :
    #             li_seller_name = "FBA"
    #         elif li_seller_name.find("Amazon.com") !=-1 :
    #             li_seller_name = "AMZ"
    #         print("========SEller NAME:  " + li_seller_name)

    #         try:
    #             li_offer_delivery = li.find_element_by_xpath(".//span[contains(@id, 'ftm_')]").text.split('?')[0].split("Want it delivered")[1].strip()
    #         except:
    #             li_offer_delivery = "null"

    #         eitem["li_price"] = li_price
    #         eitem["li_price_info"] = li_price_info
    #         eitem["li_offer_condition"] = li_offer_condition
    #         eitem["li_seller_name"] = li_seller_name
    #         eitem["li_offer_delivery"] = li_offer_delivery

    #         print("\n\n ------------------   SELLER INFO   ------------------")
    #         print(eitem)
    #         print("\n\n ------------------   END   --------------------------")

    #         sleep(3)

    #         returnitem.append(eitem)

    #     return returnitem

    # def priceConvert(self, strval):
    #     temp = float(strval.strip().split('$')[1])
    #     return temp

    # def getCheckedLastOne(self, datalist):
    #     fbatemp = {}
    #     amztemp = {}
    #     othertemp = {}

    #     for data in datalist:
    #         if data['li_seller_name'] == "FBA":
    #             if len(fbatemp) == 0:
    #                 fbatemp = data
    #             else:
    #                 if self.priceConvert(fbatemp['li_price']) > self.priceConvert(data['li_price']):
    #                     fbatemp = data
    #         elif data['li_seller_name'] == "AMZ":
    #             if len(amztemp) == 0:
    #                 amztemp = data
    #             else:
    #                 if self.priceConvert(amztemp['li_price']) > self.priceConvert(data['li_price']):
    #                     amztemp = data
    #         else:
    #             if len(othertemp) == 0:
    #                 othertemp = data
    #                 if self.priceConvert(othertemp['li_price']) > self.priceConvert(data['li_price']):
    #                     othertemp = data


    #     if len(fbatemp) == 0:
    #         if len(amztemp) == 0:
    #             if len(othertemp) == 0:
    #                 return "null"
    #             else:
    #                 return othertemp
    #         else:
    #             return amztemp
    #     else:
    #         if len(amztemp) == 0:
    #             return fbatemp
    #         else:
    #             if self.priceConvert(fbatemp['li_price']) > self.priceConvert(amztemp['li_price']):
    #                 return amztemp
    #             else:
    #                 return fbatemp
        


    #     # if len(fbatemp) == 0:
    #     #     if len(amztemp) == 0:
    #     #         if len(othertemp) == 0:
    #     #             return "null"
    #     #         else:
    #     #             return othertemp
    #     #     else:
    #     #         if len(othertemp) == 0:
    #     #             return amztemp
    #     #         else:
    #     #             if self.priceConvert(amztemp['li_price']) > self.priceConvert(othertemp['li_price']):
    #     #                 return othertemp
    #     #             else:
    #     #                 return amztemp
    #     # else:
    #     #     if len(amztemp) == 0:
    #     #          if len(othertemp)
        

    # def getshippingData(self):
    #     shipping_datalink = self.driver.find_element_by_xpath("//div[@id='olp_feature_div']//a").get_attribute("href")
    #     print("==== SHIP LINK ==== :  " + shipping_datalink)
    #     self.driver.get(shipping_datalink)
    #     sleep(1)

    #     last_pg_flag = 0
    #     list_shipinfo = []
    #     try:
    #         if self.driver.find_element_by_xpath("//li[contains(@class, 'a-last')]/a"):
    #             last_pg_flag = 1
    #         while(last_pg_flag):

    #             list_shipinfo_page = self.getsimpleshippingData()
    #             for ea_item in list_shipinfo_page:
    #                 # print("\n\n@@@@@@@@@@@@@@@    EA_ITEM   :  \n")
    #                 # print(ea_item)
    #                 # print("\n\n @@@@@@@@@@@@@@@@@ \n\n")
    #                 list_shipinfo.append(ea_item)

    #             try:
    #                 if self.driver.find_element_by_xpath("//li[contains(@class, 'a-last')]/a"):
    #                     self.driver.find_element_by_xpath("//li[contains(@class, 'a-last')]/a").click()
    #             except:
    #                 last_pg_flag = 0
    #     except:
    #         self.getsimpleshippingData()

        
    #     # print(list_shipinfo)
    #     print("\n===================== RESULT ========================")
    #     # print(self.getCheckedLastOne(list_shipinfo))
    #     return self.getCheckedLastOne(list_shipinfo)







    def __init__(self):
        chrome_driver = "walmart/chromedriver/chromedriver.exe"
        firefox_driver = "walmart/chromedriver/geckodriver.exe"
        # options = Options()
        # options.add_argument('--headless')
        # options.add_argument('--disable-gpu')  # Last I checked this was necessary
        # self.driver = webdriver.Chrome(chrome_driver, chrome_options = options)

        self.driver = webdriver.Firefox(executable_path = firefox_driver)

        base_urls = []

        # cursor.execute("SELECT ASIN from Appliances")
        # fdata = list(cursor)
        # # fdata = cursor.fetchall()
        # i=0
        # for item in fdata:
        #     base_urls.append('https://www.amazon.com/dp/' + item[0])
        #     i+=1

        

        # self.start_urls = base_urls
        self.start_urls = [
        'https://microcel.com/brands/adonit',
        # 'https://microcel.com/brands/belkin',
        # 'https://microcel.com/brands/cmi',
        # 'https://microcel.com/brands/dji',
        # 'https://microcel.com/brands/dodow',
        # 'https://microcel.com/brands/duracell',
        # 'https://microcel.com/brands/eton',
        # 'https://microcel.com/brands/fitbitcustomer',
        # 'https://microcel.com/brands/goal-zero',
        # 'https://microcel.com/brands/holi',
        # 'https://microcel.com/brands/genius',
        # 'https://microcel.com/brands/jaybird',
        # 'https://microcel.com/brands/logitech',
        # 'https://microcel.com/brands/mili',
        # 'https://microcel.com/brands/merge-vr',
        # 'https://microcel.com/brands/mightypurse',
        # 'https://microcel.com/brands/nokia',
        # 'https://microcel.com/brands/oneadaptr',
        # 'https://microcel.com/brands/phonesuit',
        # 'https://microcel.com/brands/polk',
        # 'https://microcel.com/brands/segue',
        # 'https://microcel.com/brands/sengled',
        # 'https://microcel.com/brands/speck',
        # 'https://microcel.com/brands/sharp',
        # 'https://microcel.com/brands/toshiba',
        # 'https://microcel.com/brands/ubtech',
        # 'https://microcel.com/brands/ultimate-ears',
        # 'https://microcel.com/brands/wynd',
        # 'https://microcel.com/brands/etekcity',
        # 'https://microcel.com/brands/polaroid-original'
        ]
# //span[contains(@id, 'ftm_')]
        #https://www.amazon.com/dp/B0149KS94U
        #https://www.amazon.com/dp/B00TIXMN14

        # yield Request(parse=parse_basic, headers=headers)
        # parse(response = requests.get(url, headers=headers))
        # ,'https://www.amazon.com/dp/B00AREGVUM'


    def start_requests(self):

        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        for b_url in self.start_urls:
            yield scrapy.Request(b_url, headers=headers, callback=self.parse_basic, dont_filter=True)


    def parse_basic(self, response):

        


        # sleep(1)
        # self.driver.get(response.url)
        # sleep(5)
        # target_address = self.driver.find_element_by_xpath("//span[@id='glow-ingress-line2']").text.encode('utf8')
        # print("\n\nTARGET: =====  " + target_address)

        # if target_address.find('Champlain 12919‌') == -1:
        #     # To set some thing.
        #     self.driver.find_element_by_xpath("//a[contains(@class, 'nav-a nav-a-2 a-popover-trigger a-declarative')]").click()
        #     sleep(5)
        #     self.driver.find_element_by_xpath("//input[contains(@id, 'GLUXZipUpdateInput')]").send_keys("12919")
        #     sleep(3)
        #     self.driver.find_element_by_id("GLUXZipUpdate").click()
        #     sleep(1)
        #     self.driver.find_element_by_name("glowDoneButton").click()
        # else:
        #     print("\nAlready Set! ======  " + self.driver.find_element_by_id('glow-ingress-line2').text.encode('utf8'))

        # with open('result/data.csv', 'wb') as csvfile:
        #     # fieldnames = ["PartNum", "Url", "Title", "Manufacturer", "WalmartNum", "Description", "ListPrice", "SalePrice", "ImageURL", "ImageFile", "Quantity", "Depth", "Height", "Weight", "Width", "Catagory", "SpecialType", "shippingType"]
        #     fieldnames = ["Title","Description","SKU", "Barcode", "Brand", "MSRP", "Cost", "image_urls"]
        #     writer = csv.DictWriter(csvfile, fieldnames=fieldnames, lineterminator='\n')
        #     writer.writeheader()

        print("-------------------------------start------------------------\n")

        detail_array = []
        tlis = []
        imglist = []
        # item = []
        self.driver.get(response.url)


        detail_array = self.driver.find_elements_by_xpath("//div[contains(@class, 'itemListing ng-scope')]/div[contains(@class, 'itemIdentification')]/div[contains(@class, 'itemPicture')]/a")

        for mli in detail_array:
            tlis.append(str(mli.get_attribute("href")))

        for li in tlis:
            time.sleep(0.5)
            self.driver.get(li)

            # print("\n\nTitle:  " + self.driver.find_element_by_xpath("//div[contains(@class, 'itemPictureDescription')]").text )
            # print("\nSKU:  " + self.driver.find_element_by_xpath("//div[contains(@class, 'value')][1]").text )
            # print("\nBarcode:  " + self.driver.find_element_by_xpath("//div[contains(@class, 'value')][2]").text )

            sku = self.driver.find_element_by_xpath("//div[contains(@class, 'value')][1]").text

            imglist = self.driver.find_elements_by_xpath("//div[contains(@class, 'itemImageViews')]//img")
            d_imglist = []
            for imgli in imglist:
                d_imglist.append('https://microcel.com' + str(imgli.get_attribute("src")))
            
            

            # print("\nTitle:  " + self.driver.find_element_by_xpath("//div[contains(@class, 'itemPictureDescription')]").text )
            
            try:
                Title = self.driver.find_element_by_xpath("//div[contains(@class, 'itemPictureDescription')]").text
                pass
            except Exception as e:
                Title = ''
                pass

            try:
                Description = self.driver.find_element_by_xpath("//div[contains(@class, 'xpditem-desc')]").text.encode('utf-8')
                pass
            except Exception as e:
                Description = ''
                pass

            try:
                SKU = self.driver.find_element_by_xpath("//div[contains(@class, 'value')][1]").text
                pass
            except Exception as e:
                SKU = ''
                pass

            try:
                Barcode = self.driver.find_element_by_xpath("//div[contains(@class, 'value')][2]").text
                pass
            except Exception as e:
                Barcode = ''
                pass
            
            try:
                Brand = self.driver.find_element_by_xpath("//div[contains(@class, 'value')][2]").text
                pass
            except Exception as e:
                Brand = ''
                pass

            try:
                MSRP = self.driver.find_element_by_xpath("//div[contains(@class, 'value')][2]").text
                pass
            except Exception as e:
                MSRP = ''
                pass

            try:
                Cost = self.driver.find_element_by_xpath("//div[contains(@class, 'yourPrice')]/div[contains(@class, 'x')]").text.split('Price:')[1]
                pass
            except Exception as e:
                Cost = ''
                pass

            yield WalmartItem(Title=Title, Description=Description, SKU=SKU, Barcode=Barcode, Brand=Brand, MSRP=MSRP, Cost=Cost, image_urls=[d_imglist[0]])

                # writer.writerow(DictUnicodeProxy(item))
                # exit()
        # csvfile.close()
        
        exit()
        print("--------------------------------end-------------------------\n")
        self.driver.close()





    
    # def parseItem(self):
    #     items = []
    #     tlis = []
    #     #each trip div has desribed two trip legs, we have to create 2 elements for each div
    #     with open('result/data.csv', 'wb') as csvfile:
    #         # fieldnames = ["PartNum", "Url", "Title", "Manufacturer", "WalmartNum", "Description", "ListPrice", "SalePrice", "ImageURL", "ImageFile", "Quantity", "Depth", "Height", "Weight", "Width", "Catagory", "SpecialType", "shippingType"]
    #         fieldnames = ["Handle","Title","Body","Price", "ImgUrl"]
    #         writer = csv.DictWriter(csvfile, fieldnames=fieldnames, lineterminator='\n')
    #         writer.writeheader()
    #         sIndex = 0
    #         # lis = self.driver.find_elements_by_xpath('//div[@id="product-loop"]/div')
    #         lis = self.driver.find_elements_by_xpath("//div[contains(@id, 'product-loop')]/div[contains(@class, 'product-index')]/a")
    #         for mli in lis:
    #             tlis.append(str(mli.get_attribute("href")))

    #         for li in tlis:
    #             # print("\nNNNNNNNNNNNNNNNNN")
    #             # print(i)
    #             # print("\nMMMMMMMMMMMMMMMMM")
    #             time.sleep(0.5)
                
                
    #             self.driver.get(li)
    #             item = WalmartItem()
    #             # print("\nNNNNNNNNNNNNNNNNN")
    #             # print(item['Name'])
    #             # print("\nNNNNNNNNNNNNNNNNN")
    #             # try:
    #             #     item['Name'] = (self.driver.find_elements_by_xpath("//div[@id='product-description']/h2"))[0].text
    #             #     pass
    #             # except Exception as e:
    #             #     item['Name'] = ""
    #             #     pass
    #             try:
    #                 item['Price'] = (self.driver.find_elements_by_xpath("//span[contains(@class, 'product-price')]"))[0].text
    #                 pass
    #             except Exception as e:
    #                 item['Price'] = ""
    #                 pass
    #             try:
    #                 item['Title'] = (self.driver.find_elements_by_xpath("//div[@id='product-description']/h1"))[0].text
    #                 pass
    #             except Exception as e:
    #                 item['Title'] = ""
    #                 pass
                
    #             try:
    #                 item['Body'] = str((self.driver.find_elements_by_xpath("//div[contains(@class, 'rte')]"))[0].get_attribute('innerHTML').encode('utf-8'))
    #                 # print("\n AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
    #                 # print(item['Body'])
    #                 # print("\nBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB")
    #                 pass
    #             except Exception as e:
    #                 item['Body'] = ""
    #                 pass

    #             try:
    #                 item['ImgUrl'] = (self.driver.find_elements_by_xpath("//div[@id='product-photos']/div/img"))[0].get_attribute("src")
    #                 # print("\n AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
    #                 # print(item['ImgUrl'])
    #                 # print("\nBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB")
    #                 pass
    #             except Exception as e:
    #                 item['ImgUrl'] = ""
    #                 pass
                
    #             try:
    #                 item['Handle'] = li.split("/")[-1]
    #                 pass
    #             except Exception as e:
    #                 item['Handle'] = ""
    #                 pass
                
                
                

                # try:
                #     imgUrl = (li.find_elements_by_xpath(".//img[contains(@class,'Tile-img')]"))[0].get_attribute("src")
                #     pass
                # except Exception as e:
                #     imgUrl = ""
                #     pass
                # try:
                #     salePrice = (li.find_elements_by_xpath(".//span[@class='price-characteristic']"))[0].text+"."+(li.find_elements_by_xpath(".//span[@class='price-mantissa']"))[0].text
                #     pass
                # except Exception as e:
                #     salePrice = ""
                #     pass
                # try:
                #     listPrice = (li.find_elements_by_xpath(".//span[@class='price-characteristic']"))[1].text+"."+(li.find_elements_by_xpath(".//span[@class='price-mantissa']"))[1].text
                #     pass
                # except Exception as e:
                #     listPrice = ""
                #     pass
                # try:
                #     shippingType = (li.find_elements_by_xpath(".//div[@data-tl-id='shipping-message-tile-shippingMessage']"))[0].text
                #     pass
                # except Exception as e:
                #     shippingType = ""
                #     pass
                # try:
                #     (li.find_elements_by_xpath(".//a[@class='product-title-link line-clamp line-clamp-2']"))[0].click()
                #     pass
                # except Exception as e:
                #     pass

                # try:
                #     item['Manufacturer'] = self.driver.find_elements_by_xpath(".//a[@class='prod-brandName']/span[@itemprop='brand']")[0].text
                #     pass
                # except Exception as e:
                #     item['Manufacturer'] = ""
                #     pass

                # try:
                #     item['WalmartNum'] = self.driver.find_elements_by_xpath(".//div[contains(@class,'display-inline-block wm-item-number')]")[0].get_attribute("aria-label")
                #     item['WalmartNum'] = item['WalmartNum'][15:]
                #     pass
                # except Exception as e:
                #     item['WalmartNum'] = ""
                #     pass
                # try:
                #     item['Description'] = self.driver.find_elements_by_xpath(".//div[@data-tl-id='AboutThis-ShortDescription']")[0].text
                #     pass
                # except Exception as e:
                #     item['Description'] = ""
                #     pass
                # try:
                #     item['ListPrice'] = listPrice
                #     pass
                # except Exception as e:
                #     item['ListPrice'] = ""
                #     pass
                # try:
                #     item['SalePrice'] = salePrice
                #     pass
                # except Exception as e:
                #     item['SalePrice'] = ""
                #     pass
                # try:
                #     item['ImageURL'] = self.driver.find_elements_by_xpath("//img[contains(@class,'prod-hero-image-image')]")[0].get_attribute("src")
                #     pass
                # except Exception as e:
                #     item['ImageURL'] = ""
                #     pass
                # try:
                #     imgfile = self.driver.find_elements_by_xpath("//img[contains(@class,'prod-hero-image-image')]")[0].get_attribute("src")
                #     sPos = imgfile.find("?")
                #     item['ImageFile'] = imgfile[33:sPos]
                #     pass
                # except Exception as e:
                #     item['ImageFile'] = ""
                #     pass
                # try:
                #     item['Quantity'] = self.driver.find_elements_by_xpath('//*[@id="quantity"]/option')[-1].text
                #     pass
                # except Exception as e:
                #     item['Quantity'] = ""
                #     pass

                # try:
                #     (self.driver.find_elements_by_xpath("//span[contains(text(), 'Specifications')]"))[0].click()
                #     pass
                # except Exception as e:
                #     pass

                # try:
                #     spec_div = self.driver.find_elements_by_xpath('//div[@class="Specifications"]')[0]
                #     pass
                # except Exception as e:
                #     pass
                # #temp_div = spec_div.find_elements_by_xpath("//th[contains(text(), 'Display Technology')]")[0].find_elements_by_xpath("//following-sibling::td")[0].find_elements_by_xpath("//div")[0].text
                # """depth = spec_div.find_elements_by_xpath("//th[contains(text(), 'Assembled Product Weight') and (@class='display-name')]/following-sibling::td/div")[0].text
                # print("--------------------------------test----------------------------------\n")
                # print("----------------"+depth.encode('utf-8'))
                # print("---------------------------------end----------------------------------\n")"""
                # try:
                #     depth = spec_div.find_elements_by_xpath("//th[contains(text(), 'Depth (with stand)') and (@class='display-name')]/following-sibling::td/div")[0].text
                #     item['Depth'] = depth.encode('utf-8')
                #     pass
                # except Exception as e:
                #     pass

                # try:
                #     depth = spec_div.find_elements_by_xpath("//th[contains(text(), 'Manufacturer Part Number') and (@class='display-name')]/following-sibling::td/div")[0].text
                #     item['PartNum'] = depth.encode('utf-8')
                #     pass
                # except Exception as e:
                #     pass

                # try:
                #     height = spec_div.find_elements_by_xpath("//th[contains(text(), 'Height (with stand)') and (@class='display-name')]/following-sibling::td/div")[0].text
                #     item['Height'] = height.encode('utf-8')
                #     pass
                # except Exception as e:
                #     pass

                # try:
                #     weight = spec_div.find_elements_by_xpath("//th[contains(text(), 'Assembled Product Weight') and (@class='display-name')]/following-sibling::td/div")[0].text
                #     item['Weight'] = weight.encode('utf-8')
                #     pass
                # except Exception as e:
                #     pass

                # try:
                #     width = spec_div.find_elements_by_xpath("//th[contains(text(), 'Width (with stand)') and (@class='display-name')]/following-sibling::td/div")[0].text
                #     item['Width'] = width.encode('utf-8')
                #     pass
                # except Exception as e:
                #     pass

                # try:
                #     category_ol = self.driver.find_elements_by_xpath('//ol[@class="breadcrumb-list "]/li/a')
                #     catagory = ""
                #     for ol_li in category_ol:
                #         catagory = catagory + ol_li.text+" / "#(ol_li.find_elements_by_xpath("//a[@itemprop='item']"))[0].text+" / "
                #     catagory = catagory[:-3]
                #     pass
                # except Exception as e:
                #     catagory = ""
                #     pass

                # item['Catagory'] = catagory
                # item['SpecialType'] = specialType
                # if shippingType== "2-day shipping":
                #     shippingType = "Free Shipping"
                # item['shippingType'] = shippingType

                # # self.driver.back()
                # writer.writerow(DictUnicodeProxy(item))

                # # items.append(item)
                # sIndex+=1
                # print("CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC")
                # print(str(sIndex))
                # print("DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD")
                # if sIndex == 24:
                #     break
                # if sIndex%40==0:
                #     sPage = sIndex/40+1
                #     self.driver.get("https://www.walmart.com/browse/3944/?cat_id=3944&facet=condition%3ANew%7C%7Cretailer%3AWalmart.com%7C%7Cspecial_offers%3AAs+Advertised%7C%7Cspecial_offers%3AClearance%7C%7Cspecial_offers%3ANew%7C%7Cspecial_offers%3AReduced+Price%7C%7Cspecial_offers%3ARollback%7C%7Cspecial_offers%3ASpecial+Buy%7C%7Ccondition%3ARefurbished&grid=true&max_price=150&min_price=50&page="+str(sPage)+"&sort=best_seller&stores=-1#searchProductResult")
                    
            # csvfile.close()
        # return items

# disconnect from server
# db.close()