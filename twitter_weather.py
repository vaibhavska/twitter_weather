from selenium import webdriver
import re
import numpy
import time
browser=webdriver.Chrome()
# OPening part for loging into TWITTER
browser.get("https://twitter.com/login?lang=en-gb")#for opening the login page of twitter
a=browser.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/fieldset/div[1]/input')#for finding the useranme box
a.send_keys("")#your oen email id here
a=browser.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/fieldset/div[2]/input')#for finding the password box
a.send_keys("")#your password here
a=browser.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/div[2]/button')#for the submit button
a.submit()
#now we are logged into twitter
for i in range(1,10):
    print(i);
    
while True:
    time.sleep(10)
    value=browser.find_elements_by_xpath('.//span[@class = "count-inner"]')#for finding the number of notifications
    b=value[0].text
    print("---->",b,"type",type(b),"type value",type(value))
    lenvalue=0
    for i in value:
    	lenvalue=lenvalue+1
    if lenvalue>0 and b!='':#control will enter the loop only if the there are any notifications
        bmw=b
        print(value[0].text," notification found")
        bmw=int(bmw)
        print(bmw)
        browser.get("https://twitter.com/i/notifications")#for the notifications page
        list_handle=[]
        a=browser.find_elements_by_class_name("TweetTextSize")
        list=[]
        elem = browser.find_elements_by_css_selector("span.username.u-dir")#for the user handles
        j=0
        for i in elem:
            if(i.text!=''):
                j=j+1
                if(j>0):
                    list_handle.append(i.text)
        for i in range(0,bmw):
            print(list_handle)
        for i in range(0,bmw):
            print(a[i].text)
            z=str(a[i].text)
            postalregex = re.compile(r'(\d){6}')
            po=postalregex.search(z)
            postal=po.group()
            list.append(postal)
        for i in range(0,bmw):
            print(i)
            browser.get("https://www.google.com")
            sub=browser.find_element_by_id("lst-ib")
            sub.send_keys(list[i]," WEATHER")
            sub.submit()
            time.sleep(3)
            sub=browser.find_elements_by_id("wob_gsvg")
            temp=(sub[0].text)[0:2]
            sub=browser.find_element_by_id("wob_dc")
            kind=sub.text
            sub=browser.find_elements_by_id("wob_pp")
            pp=sub[0].text
            sub=browser.find_elements_by_id("wob_hm")
            humidity=sub[0].text
            sub=browser.find_elements_by_id("wob_ws")
            ws=sub[0].text
            message="Looks like its ",temp,"ºC out there with ",kind," conditions\nPrecipitation:",pp,"\nHumidity:",humidity,"\nWind Speed:",ws," ",time.strftime("%H:%M:%S"),"at ",list[i]
            browser.get("https://twitter.com/login?lang=en-gb")
            a=browser.find_element_by_id("global-new-tweet-button")
            a.click()
            a=browser.find_element_by_id("tweet-box-global")
            a.clear()
            a.send_keys(message," ",list_handle[i])
            elem = browser.find_elements_by_css_selector("span.button-text.tweeting-text")

            elem[1].click()

