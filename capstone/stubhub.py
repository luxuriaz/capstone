import requests
import base64
import pprint
import datetime
from datetime import date
import sched, time



def event1():
    ## Enter user's API key, secret, and Stubhub login
    app_token = "2e55a526-a5f5-3986-a1e5-0dbbe540aee6"
    consumer_key = "Z5EPKHnk2l4Q8v8Xmr7XdzyOlCga"
    consumer_secret = "ct_vAT6fvfdOWEuWrcMNAWN0fWIa"
    stubhub_username = "zdbhxc2010@gmail.com"
    stubhub_password = "Zszdwdzh1995!"

    combo = consumer_key + ':' + consumer_secret
    basic_authorization_token = base64.b64encode(combo.encode('utf-8'))
    url = 'https://api.stubhub.com/login'
    headers = {
            'Content-Type':'application/x-www-form-urlencoded',
            'Authorization':'Basic '+(basic_authorization_token),}
    body = {
            'grant_type':'password',
            'username':stubhub_username,
            'password':stubhub_password,
            'scope':'PRODUCTION'}

    r = requests.post(url, headers=headers, data=body)

    print (r)
    print (r.text)

    token_response = r.json()
    access_token = token_response['access_token']
    user_GUID = r.headers['X-StubHub-User-GUID']


    inventory_url = 'https://api.stubhub.com/search/inventory/v2'
    eventid = '9850849'
    data = {'eventid':eventid, 'rows':200}
    headers['Authorization'] = 'Bearer ' + access_token
    headers['Accept'] = 'application/json'
    headers['Accept-Encoding'] = 'application/json'

    #inventory = requests.get(inventory_url, headers=headers, params=data)
    #inv = inventory.json()


    #info_url = 'https://api.stubhub.com/catalog/events/v2/' + eventid
    #info = requests.get(info_url, headers=headers)
    #ticket_info= info.json()


    #pprint.pprint(ticket_info)
    def get_current_lowestprice():
        inventory = requests.get(inventory_url, headers=headers, params=data)
        inv = inventory.json()
        for item in inv['listing']:
            if item['ticketSplit']=="1":
                return (item['currentPrice']['amount'])
                #with service fee

    def get_current_time_difference():
        #event_date = ticket_info['eventDateLocal']
        #event_year= event_date[0:4]
        #event_month = event_date[6:7]
        #event_day = event_date[8:10]
        #event_time = datetime(event_year,event_month,event_day)
        event_time = date(2017,5,19)
        event_start_time = "23:59:59"
        #set event start time default at 8 pm EST.
        time = datetime.datetime.now()
        year_now = time.year
        month_now = time.month
        day_now = time.day
        hour_now = time.hour
        minute_now = time.minute
        second_now = time.second
        if len(str(minute_now)) == 1:
            minute_now = "0"+str(minute_now)
            #if single digit add 0 infront
        time = date(year_now,month_now,day_now)
        #assume track in the same year
        remind_days = event_time-time
        if int(str(remind_days)[0])>0:
            print ("event happens after more than 1 day")
            freq = 3600
            remind_days = str(remind_days)
            for i in range(len(remind_days)):
                if remind_days[i] == "d":
                    remind_days = remind_days[:(i-1)]
                    break

            # if more than one day before the event start, write the price every hour
            return_statement = ("Current time: " + str(time)+" " + str(hour_now) + ":"+str(minute_now)+" Current time difference: " + str(remind_days)+" days")
            return [return_statement,freq]

        else:
            print ("event happens after less than 1 day")
            freq = 600
            remind_days = 0
            current_time_hour_minute = str(hour_now)+":"+str(minute_now)+":"+str(second_now)
            # if the event happens today, write the price every ten minutes
            time_format = '%H:%M:%S'
            time_difference = datetime.datetime.strptime(event_start_time, time_format) - datetime.datetime.strptime(current_time_hour_minute, time_format)
            print (str(time_difference))
            if str(time_difference)[0]== "-":
                print "event ended"
                exit()
            return_statement = ("Current time: " + str(time)+" " + str(hour_now) + ":"+str(minute_now)+" Current time difference: " + str(time_difference))

            return [return_statement,freq]



    def main_loop():
        sign = 0
        f = open('MartinGarrix 5-19.txt', 'a')
        current_lowestprice = get_current_lowestprice()
        [current_time_difference,freq] = get_current_time_difference()
        f.write(str(current_lowestprice)+"\n")
        f.write(current_time_difference+"\n")
        f.close()
        #print (current_lowestprice)
        print (current_time_difference+"\n")
        #print (freq)
        time.sleep(freq)





    while True:
        main_loop()

###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################

def event2():
    ## Enter user's API key, secret, and Stubhub login
    app_token = "2e55a526-a5f5-3986-a1e5-0dbbe540aee6"
    consumer_key = "Z5EPKHnk2l4Q8v8Xmr7XdzyOlCga"
    consumer_secret = "ct_vAT6fvfdOWEuWrcMNAWN0fWIa"
    stubhub_username = "zdbhxc2010@gmail.com"
    stubhub_password = "Zszdwdzh1995!"

    combo = consumer_key + ':' + consumer_secret
    basic_authorization_token = base64.b64encode(combo.encode('utf-8'))
    url = 'https://api.stubhub.com/login'
    headers = {
            'Content-Type':'application/x-www-form-urlencoded',
            'Authorization':'Basic '+(basic_authorization_token),}
    body = {
            'grant_type':'password',
            'username':stubhub_username,
            'password':stubhub_password,
            'scope':'PRODUCTION'}

    r = requests.post(url, headers=headers, data=body)

    print (r)
    print (r.text)

    token_response = r.json()
    access_token = token_response['access_token']
    user_GUID = r.headers['X-StubHub-User-GUID']


    inventory_url = 'https://api.stubhub.com/search/inventory/v2'
    eventid = '9745451'
    data = {'eventid':eventid, 'rows':200}
    headers['Authorization'] = 'Bearer ' + access_token
    headers['Accept'] = 'application/json'
    headers['Accept-Encoding'] = 'application/json'

    #inventory = requests.get(inventory_url, headers=headers, params=data)
    #inv = inventory.json()


    #info_url = 'https://api.stubhub.com/catalog/events/v2/' + eventid
    #info = requests.get(info_url, headers=headers)
    #ticket_info= info.json()


    #pprint.pprint(ticket_info)
    def get_current_lowestprice():
        inventory = requests.get(inventory_url, headers=headers, params=data)
        inv = inventory.json()
        for item in inv['listing']:
            if item['ticketSplit']=="1":
                return (item['currentPrice']['amount'])
                #with service fee

    def get_current_time_difference():
        #event_date = ticket_info['eventDateLocal']
        #event_year= event_date[0:4]
        #event_month = event_date[6:7]
        #event_day = event_date[8:10]
        #event_time = datetime(event_year,event_month,event_day)
        event_time = date(2017,4,29)
        event_start_time = "24:00:00"
        #set event start time default at 8 pm EST.
        time = datetime.datetime.now()
        year_now = time.year
        month_now = time.month
        day_now = time.day
        hour_now = time.hour
        minute_now = time.minute
        second_now = time.second
        if len(str(minute_now)) == 1:
            minute_now = "0"+str(minute_now)
            #if single digit add 0 infront
        time = date(year_now,month_now,day_now)
        #assume track in the same year
        remind_days = event_time-time
        if int(str(remind_days)[0])>0:
            print ("event happens after more than 1 day")
            freq = 2
            remind_days = str(remind_days)
            for i in range(len(remind_days)):
                if remind_days[i] == "d":
                    remind_days = remind_days[:(i-1)]
                    break

            # if more than one day before the event start, write the price every hour
            return_statement = ("Current time: " + str(time)+" " + str(hour_now) + ":"+str(minute_now)+" Current time difference: " + str(remind_days)+" days")
            return [return_statement,freq]

        else:
            print ("event happens after less than 1 day")
            freq = 1
            remind_days = 0
            current_time_hour_minute = str(hour_now)+":"+str(minute_now)+":"+str(second_now)
            # if the event happens today, write the price every ten minutes
            time_format = '%H:%M:%S'
            time_difference = datetime.datetime.strptime(event_start_time, time_format) - datetime.datetime.strptime(current_time_hour_minute, time_format)
            print (str(time_difference))
            if str(time_difference)[0]== "-":
                print "event ended"
                exit()
            return_statement = ("Current time: " + str(time)+" " + str(hour_now) + ":"+str(minute_now)+" Current time difference: " + str(time_difference))

            return [return_statement,freq]



    def main_loop():
        sign = 0
        f = open('deadmau5 4-28.txt', 'a')
        current_lowestprice = get_current_lowestprice()
        [current_time_difference,freq] = get_current_time_difference()
        f.write(str(current_lowestprice)+"\n")
        f.write(current_time_difference+"\n")
        f.close()
        #print (current_lowestprice)
        print (current_time_difference+"\n")
        #print (freq)
        time.sleep(freq)





    while True:
        main_loop()



event1()
event2()
