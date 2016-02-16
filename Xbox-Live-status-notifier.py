from bs4 import BeautifulSoup
from email.mime.text import MIMEText
import urllib2
import smtplib
import time
 
##Functions that decide what happens when things are working and when things aren't.
##activetestpos() is called when there is a confirmed outage. The system will not alert again for half an hour by default.
##activetestneg() is called when there is no outage. You will see "This will show up if everything is right" every 30 seconds.
def ActivePos():
    print "This will show up if everything is wrong."
 
    def email():
            GmailUser = "INSERT BOT EMAIL HERE"
            GmailPwd = "INSERT BOT PASSWORD HERE"
            FROM = "Whoever you want here"
            TO = "Email group here (for multiple emails separate via comma and follow instructions below)"
            SUBJECT = "Xbox Live is experiencing problems."
            TEXT = "If you are seeing this, Xbox Live is currently experiencing problems.\nThis can be for any number of reasons, please review for more info \n http://support.xbox.com/en-US/xbox-live-status\nAlert emails will be suppressed for 30 minutes following this one."
 
            #Prepare actual message
            message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
            """ % (FROM, "".join(TO), SUBJECT, TEXT)
            #If you are including multiple emails, use this line instead of the above:
            #""" % (FROM, ", ".join(TO), SUBJECT, TEXT)
            try:
                server = smtplib.SMTP("smtp.gmail.com", 587)
                server.ehlo()
                server.starttls()
                server.login(GmailUser, GmailPwd)
                server.sendmail(FROM, TO, message)
                server.close()
                print 'Successfully sent alert email, waiting 30 minutes before polling again.'
            except:
                print "Failed to send email"
    email()
    #Adjust time.sleep() according to how often you want emails
    time.sleep(1800)
           
 
def ActiveNeg():
    print "This will show up if everything is alright."
    #Adjust time.sleep() for how often you want the website to be polled
    time.sleep(30)
   
 
x = str('[<div class="statusText">' '\\n' '<span class="">Xbox Live service is active.</span>' '\\n' '<span>See details &gt;</span>' '\\n' '</div>]')
while 1:
    #This is the beginning of the log parsing.
    #Beautiful Soup analyzes the web page and parses out anything with <div> and matches "statusText".
    #Luckily for us, there is only one of those on the page.
    r = urllib2.urlopen("http://support.xbox.com/en-US/xbox-live-status").read()
    soup = BeautifulSoup(r)
    active = str(soup.find_all("div", class_='statusText'))
    #Testing active against x (doesn't match "Xbox Live service is active" exactly) will process functions accordingly
    if active == x:
        ActiveNeg()
    if active != x:
        ActivePos()
    ##To continue the script running forever and ever and ever
