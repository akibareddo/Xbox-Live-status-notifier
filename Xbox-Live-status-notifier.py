from bs4 import BeautifulSoup
from email.mime.text import MIMEText
import urllib2
import smtplib
import time
import sys

def email1():
    gmail_user = "USER"
    gmail_pwd = "PASS"
    FROM = "EMAIL"
    #Change the TO line to the emails you want alerts sent to,
    #Separated by a comma ONLY. THIS MEANS YOU MATT.
    TO = "INSERT EMAILS HERE"
    SUBJECT = "Xbox Live services are experiencing issues."
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
        print 'Successfully sent the email.'
    except:
        print "Failed to send email."


def email2():
    gmail_user = "USER"
    gmail_pwd = "PASS"
    FROM = "EMAIL"
    #Change the TO line to the emails you want alerts sent to,
    #Separated by a comma ONLY. THIS MEANS YOU MATT.
    TO = "ENTER EMAILS HERE"
    SUBJECT = "Xbox Live services are back up."
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
        print 'Successfully sent the email.'
    except:
        print "Failed to send email."

#This happens if stuff is bad.
def activetestbad():
    global meowtest
    if meowtest == True:
        email1()
        meowtest = False
    if active != x:
        print "Holy meow everything's broken\r",
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
x = str('<img alt="" aria-label="" class="p-b-md p-r-md" src="/Content/Images/LiveStatus/active_icon.png" title=""/>')

while 1:
    #This is where the magic happens. We get the input from
    #the website, which we then analyze and test.
    currenttime = time.strftime("%c")
    starttime = time.time()
    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    try:
        r = opener.open("http://support.xbox.com/en-US/xbox-live-status").read()
    except urllib2.URLError:
        print "Unable to reach website. https://support.xbox.com/en-US/xbox-live-status may not be up, or there may be a problem with the script."
        time.sleep(20)
        sys.exit()
    soup = BeautifulSoup(r)
    endtime = time.time()
    elapsed = (endtime - starttime)/3600
    elapsedtext = "%.3f" % elapsed
    active = str(soup.find("img", class_="p-b-md p-r-md"))
    print "Analyzing...Beep boop meow...\r",
    time.sleep(5)
    if active == x:
        activetestok()
    else:
        errordesc = str(soup.find("div", class_="content xl-col-14-24 xl-col-24-offset-5 xl-right-offset l-col-13-24 l-col-24-offset-5 m-col-16-24 m-col-24-offset-6 s-col-21-24 xs-col-21-24 p-l-md l-right-offset"))
        try:
            p_tag = str(soup.p.extract())
        except (NameError, TypeError, AttributeError):
            print "Something went wrong with analyzing the output"
            time.sleep(20)
            sys.exit
        f = p_tag[23:-4]
        if  'span' not in f:
            activetestbad()
