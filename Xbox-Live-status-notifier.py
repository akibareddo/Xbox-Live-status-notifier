from bs4 import BeautifulSoup
from email.mime.text import MIMEText
import urllib2
import smtplib
import time
import sys

def emailstart():
    gmail_user = "BOTEMAIL@gmail.com"
    gmail_pwd = "SUPER SECRET PASSWORD"
    FROM = "THE COOLEST BOT EVER"
    #Change the TO line to the emails you want alerts sent to,
    #Separated by a comma ONLY.
    TO = "Bane@TDKR.com","CIA@TDKR.com","DrPavel@TDKR.com"
    SUBJECT = "Xbox Live services are limited as of " + currenttime
    TEXT = "As of " + currenttime + ", Xbox Live is currently experiencing problems affecting " + f + "." + "\nThis can be for any number of reasons, please review for more info \n http://support.xbox.com/en-US/xbox-live-status"

    #Prepare actual message
    message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, "".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        print 'Successfully sent email for beginning of outage at ' + currenttime
    except:
        print 'Failed to send email for beginning of outage at ' + currenttime

def emailend():
#Just did it again for posterity, not really necessary
    gmail_user = "BOTEMAIL@gmail.com"
    gmail_pwd = "SUPER SECRET PASSWORD"
    FROM = "THE COOLEST BOT EVER"
    #Change the TO line to the emails you want alerts sent to,
    #Separated by a comma ONLY.
    TO = "Bane@TDKR.com","CIA@TDKR.com","DrPavel@TDKR.com"
    TEXT = "Xbox Live has now resumed its normal status as of " + currenttime + ". Total downtime is " + elapsedtext + " hours."

    #Prepare actual message
    message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, "".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        print 'Successfully sent email for end of outage at ' + currenttime
    except:
        print 'Failed to send email at ' + currenttime

#This happens if stuff is bad.
def activetestbad():
    global meowtest
    if meowtest == True:
       email1()
       meowtest = False
    if active != x:
        print "Holy meow everything's broken\r",
       #This bot is a cat, did I forget to mention that? I love you Miss Fortune
        time.sleep(5)

#This happens if stuff is good.    
def activetestok():
    global meowtest
    if meowtest == False:
        email2()
        meowtest = True
        print "Normality has mew-sumed, meow\r"
    else:
        print "Everything's just purrfect :3\r",
        time.sleep(5)

#These lines are used as variables. Meowcount is used
#since it's a global variable with a very unique name 
#(it has to be global for the script to work)
meowtest = True
x = str('<h3 class="servicename m-t-n ">Xbox Live Core Services</h3>')

while 1:
    #This is where the magic happens. We get the input from
    #the website, which we then analyze and test.
    currenttime = time.strftime("%c")
    starttime = time.time()
    try:
        r = urllib2.urlopen("http://support.xbox.com/en-US/xbox-live-status").read()
    except urllib2.URLError:
        print "Unable to reach website. http://support.xbox.com/en-US/xbox-live-status may not be up, or there may be a problem with the script."
        time.sleep(20)
        sys.exit()
    soup = BeautifulSoup(r)
    print "Analyzing...Beep boop meow...\r",
    time.sleep(5)
    endtime = time.time()
    elapsed = (endtime - starttime)/3600
    elapsedtext = "%.10f" % elapsed
    active = str(soup.find("h3", class_="servicename m-t-n "))
    if active == x:
        activetestok()
    else:
        errordesc = str(soup.find("div", class_="content xl-col-14-24 xl-col-24-offset-5 xl-right-offset l-col-13-24 l-col-24-offset-5 m-col-16-24 m-col-24-offset-6 s-col-21-24 xs-col-21-24 p-l-md l-right-offset"))
        try:
            p_tag = str(soup.p.extract())
        except (NameError, TypeError, AttributeError):
            print "Something went wrong with analyzing the output."
            time.sleep(20)
            sys.exit
        f = p_tag[23:-4]
        activetestbad()
