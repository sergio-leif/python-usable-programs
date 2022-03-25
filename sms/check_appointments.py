#!/bin/python3

import os
from twilio.rest import Client
import urllib.request
import json
import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
import sys

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

# Phone numbers to send the notification
source_phone = sys.argv[1]
to_phone = sys.argv[2]

# URL to check
url = sys.argv[3]

desired_locations = [239, 252, 266, 240, 246, 253, 248]
# desired_locations = [292, 293, 294, 295, 296]

available = False

while available == False:
    time.sleep(5)
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)

    request = urllib.request.Request(url)

    r = urllib.request.urlopen(request).read()

    answer = r.decode('utf-8')
    little = answer.split('\n')[234].split('= ')[1].replace('[','').replace(']','').replace('\r','')
    lista = list(little.split('},'))
    for index in range(len(lista)):
        if index < len(lista)-1:
            lista[index] += '}'
        location = json.loads(lista[index])
        location_id = location['LocationId']

        if location_id in desired_locations:
            print(lista[index])
            if location['FirstOpenSlot'] != 'No Appointments Available':
                chrome_browser = webdriver.Chrome('./chromedriver')

                chrome_browser.maximize_window()
                chrome_browser.get(f'{url}/{location_id}')

                #Select timeslot
                availableButton = chrome_browser.find_element_by_class_name('availableTimeslot')
                availableButton.click()

                name_field = chrome_browser.find_element_by_id('firstName')
                name_field.send_keys('Name')

                lastname_field = chrome_browser.find_element_by_id('lastName')
                lastname_field.send_keys('Last Name')

                email_field = chrome_browser.find_element_by_id('email')
                email_field.send_keys('email@email.com')

                phone_field = chrome_browser.find_element_by_id('phone')
                phone_field.send_keys('1234567890')

                permit_field = chrome_browser.find_element_by_id('driverLicense')
                permit_field.send_keys('LICENSE_NUMBER')

                sel = Select(chrome_browser.find_element_by_id("test"))
                # sel.select_by_visible_text('CDL')
                sel.select_by_visible_text('Auto')

                receive_texts = chrome_browser.find_element_by_id('receiveTexts')
                receive_texts.click()

                checkinput = chrome_browser.find_element_by_name('Attest')
                checkinput.click()

                chrome_browser.find_element_by_class_name('g-recaptcha').click()

                print(f'[{current_time}] Run and take one appointment! {url}/{location_id}')
                message = client.messages \
                    .create(
                        body="Run and take one appointment! " + url,
                        from_=source_phone,
                        to=to_phone
                    )
                available = True
                time.sleep(30)
                break
        if index == len(lista)-1:
            print(f'[{current_time}] There are not available appointments yet')
            