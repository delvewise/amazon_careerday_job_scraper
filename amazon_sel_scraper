# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 18:31:05 2021

@author: nickd
"""
import math
import csv
from time import sleep
from parsel import Selector
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

def amazon_scrap():
    sleep(1.5)
    profiles = driver.find_elements_by_xpath('.//*[@class="job-link"]')
    profiles = [profile.get_attribute('href') for profile in profiles]

    for profile in profiles:
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[1])
        driver.get(profile)
        sleep(2.5)

        sel = Selector(text=driver.page_source)

        job_location= None
        job_team= None
        job_type= None
        job_id= None
        job_title= None
        job_division= None
        job_description= None
        job_qualifications= None
        try:
            job_id = sel.xpath('//*[@class="info"]/div/p/text()').extract_first().split(' | ')[0]
        except NoSuchElementException:
            job_id= None
            pass
        except TypeError:
            job_id=None
            pass            
        except UnicodeEncodeError:
            print('job id fail')
            job_id=None
            pass
        except UnboundLocalError:
            job_id= None
            pass
        try:
            job_title = sel.xpath('//*[@class="info"]/h1/text()').extract()
        except NoSuchElementException:
            job_title= None
            pass
        except TypeError:
            job_title=None
            pass
        except UnicodeEncodeError:
            job_title=None
            pass
        except UnboundLocalError:
            job_title= None
            pass
        try:
            job_division = sel.xpath('//*[@class="info"]/div/p/text()').extract_first().split(' | ')[1]
        except NoSuchElementException:
            job_division= None
            pass
        except TypeError:
            job_division=None
            pass
        except UnicodeEncodeError:
            job_division=None
            pass
        except UnboundLocalError:
            job_division= None
            pass
        sleep(0.5)
        try:
            job_description = sel.xpath('//*[@class="section description"]/p/text()').extract()
        except NoSuchElementException:
            job_description= None
            pass
        except TypeError:
            job_description=None
            pass
        except UnicodeEncodeError:
            job_description=None
            pass
        except UnboundLocalError:
            job_description = None
            pass
        try:
            job_qualifications = sel.xpath('//*[@class="section"]/p/text()').extract()
        except NoSuchElementException:
            job_qualifications= None
            pass
        except TypeError:
            job_qualifications=None
            pass
        except UnicodeEncodeError:
            job_qualifications=None
            pass
        except UnboundLocalError:
            job_qualifications= None
            pass
        try:
            job_location = [sel.xpath('//*[@class= "association-content"]/a/text()').extract_first()]
        except NoSuchElementException:
            job_location= None
            job_team= None
            job_type= None
            pass
        except TypeError:
            job_location= None
            job_team= None
            job_type= None
            pass
        except UnicodeEncodeError:
            job_location= None
            job_team= None
            job_type= None
            pass
        except UnboundLocalError:
            job_location= None
            job_team= None
            job_type= None
            pass
        sleep(0.3)
        try:

            if len( sel.xpath('//*[@class= "association-content"]/a').extract()) == 2:
                job_type= sel.xpath('//*[@class= "association-content"]/a/text()').extract()[1]
                job_team=None
            if len( sel.xpath('//*[@class= "association-content"]/a').extract()) == 3:
                job_type= sel.xpath('//*[@class= "association-content"]/a/@href').extract()[2]
                job_team= sel.xpath('//*[@class= "association-content"]/a/@href').extract()[1]
            if len(sel.xpath('//*[@class= "association-content"]/a').extract()) == 4:
                job_location.append(sel.xpath('//*[@class= "association-content"]/a/text()').extract()[1])
                job_type= sel.xpath('//*[@class= "association-content"]/a/@href').extract()[3]
                job_team = sel.xpath('//*[@class= "association-content"]/a/@href').extract()[2]
        except NoSuchElementException:
            job_team= None
            job_type= None
            pass
        except TypeError:
            job_team= None
            job_type= None
            pass
        except UnicodeEncodeError:
            print('side bar fail')
            job_team= None
            job_type= None
            pass            
        except UnboundLocalError:
            job_team= None
            job_type= None
            pass

        writer.writerow([job_id, job_title, job_division, job_description, job_qualifications, job_location, job_team, job_type])
        driver.close()

        driver.switch_to.window(driver.window_handles[0])

##WRTIES
#if have parameter page
# writer = csv.writer(open(parameters.result_file, 'w'))
result_file = '215_2021BA_AMZ_jobs.csv'
writer = csv.writer(open(result_file, 'w'))
writer.writerow(['job_id', 'job_title', 'job_division', 'job_description', 'job_qualifications', 'job_location', 'job_team', 'job_type'])

driver = webdriver.Chrome('C://Users/nickd/OneDrive//Desktop/delve/chromedriver')
driver.maximize_window()
sleep(0.5)


#driver.get('')
driver.get('https://www.amazon.jobs/en/search?offset=0&result_limit=10&sort=relevant&cities[]=Seattle%2C%20Washington%2C%20USA&cities[]=Bellevue%2C%20Washington%2C%20USA&distanceType=Mi&radius=24km&latitude=&longitude=&loc_group_id=&loc_query=&base_query=analyst&city=&country=&region=&county=&query_options=&')
sleep(2.3)
rg= driver.find_element_by_xpath('.//*[@class="col-sm-6 job-count-info"]')
#get post total
rg= int(rg.text[17:-5])
print(rg)
rg= rg/10
print('before rounding', rg)
rg= math.ceil(rg)
i=0
for i in range(rg):
    i= i+1
    try:
        sleep(2)
        amazon_scrap()
        print("Nice Job Nick", i)
    except NoSuchElementException:
        print('failed on listing page', i)
        driver.switch_to.window(driver.window_handles[0])
        pass
    except UnicodeEncodeError:
        print('failed on listing page', i)
        driver.switch_to.window(driver.window_handles[0])
        pass

    try:
        driver.find_element_by_xpath('.//*[@class="btn circle right"]').click()
    except NoSuchElementException:
        print('Abrupt End BUT we did it')
        driver.quit()
        break

print('we did it')
driver.quit()
