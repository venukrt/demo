
import os,sys,json,re
import datetime, time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

msg = MIMEMultipart()


list=[]
dict={}
dict1={}
dict2={}
dict3={}

def sendmail():
    password = "venugopal06"
    msg['From'] = "venucs44@gmail.com"
    msg['To'] = "venugopal.ise@gmail.com"
    msg['Subject'] = "Testing"
    
    # add in the message body
    message="Hi testing mail"
    msg.attach(MIMEText(message, 'plain'))
 
    #create server
    server = smtplib.SMTP('smtp.gmail.com: 587')
 
    server.starttls()
 
    # Login Credentials for sending the mail
    server.login(msg['From'], password)
 
 
    # send the message via the server.
    server.sendmail(msg['From'], msg['To'], msg.as_string())
 
    server.quit()
 
    print "successfully sent email to %s:" % (msg['To'])

def licetest():
    with open("test.json") as f:
        for line in f:
            line=line.strip()
            list.append(line)
            #print list
        return list


def getexprirydate1(test):
    for item in test:
        if "expiry" in item and "_id" in item and "customerId" in item:
            cname=item.split("customerId")
            cnametest= cname[1].split("productClassName")
            cn=(''.join(cnametest[0]))
            cname1=(cn.split('"'))
            #print cname1[2]
            cid=item.split("_id")
            cid= cid[1].split("customerId")
            cid=(''.join(cid[0]))
            cid=(cid.split('"'))
            #print cid[2]
            expdate=item.split("expiry")
            expdate=(''.join(expdate[1]))
            expdate=(expdate.split('"'))
            #print expdate[2]
            dict[cid[2]]=(cname1[2],expdate[2])
            #print dict
    return dict

def convertdatetoseconds(dict):
    for key in dict:        
        date1=dict[key][1].split('-')
        #print date1
        year=int(date1[2])
        month=int(date1[1])
        date=int(date1[0])
        #print year , month , date
        t = datetime.datetime(year,month,date,0, 0)
        sec= time.mktime(t.timetuple())
        dict1[key]=(dict[key][0],sec)
        #print dict1
    return dict1

def comparedate(dict1):
    today=datetime.date.today().strftime("%d-%m-%y")
    todaydate=today.split('-')
    year=int(todaydate[2])
    mnth=int(todaydate[1])
    curdate=int(todaydate[0])
    t = datetime.datetime(year,mnth,curdate,0, 0)
    curdatesec= time.mktime(t.timetuple())
    for key in dict1:
        #print dict1[key]
        result=dict1[key][1]-curdatesec
        #print result
        dict2[key]=(dict1[key][0],result)
    return dict2

def convertsecondstodays(dict2):

    for key in dict2:
        #secs=dict2[key]
        days = dict2[key][1]//86400
        hours = (dict2[key][1] - days*86400)//3600
        minutes = (dict2[key][1] - days*86400 - hours*3600)//60
        seconds = dict2[key][1] - days*86400 - hours*3600 - minutes*60
        result = ("{}".format(days))
        dict3[key]=(dict2[key][0],result)
        #if int(15)=result:
        #    print ""
    return dict3

def checkdays(dict3):
    for key in dict3:
        print "test",(dict3[key][1])
        if "15.0" ==(dict3[key][1]):
            print "expiry date is going to be expire ",dict3[key][1],dict3[key][0],dict3[key]
            message="expiry date is going to be expire ",dict3[key][1],dict3[key][0],dict3[key]
            #sendmail(message)
        elif "7" ==(dict3[key][1]):
            print "expiry date is going to be expire ",dict3[key][1],dict3[key][0],dict3[key]
            message="expiry date is going to be expire ",dict3[key][1],dict3[key][0],dict3[key]
            #sendmail(message)
        else:
            print "no expiration date"
            message="no expiration date"
            #sendmail(message)
    
def main():
    
    test=licetest()
    dict=getexprirydate1(test)
    #print dict
    dict1=convertdatetoseconds(dict)
    #print dict1
    print "------------------------days------------------------------------------"
    dict2=comparedate(dict1)
    #print dict2
    dict3=convertsecondstodays(dict2)
    #print dict3
    checkdays(dict3)

if __name__=='__main__':
    main()
