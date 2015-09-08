#this file is used for compute datetime1 sub datetime2
#!/usr/bin/python
import sys,time

def dateinput():
    date = raw_input('please input the first date:')
    return date

def datetrans(tdate):
    #spdate = tdate.replace('/','-')
    try:
        datesec = time.strptime(tdate,'%Y-%m-%d')
    except ValueError:
        print '%s is not a reightful date format!'%tdate
        sys.exit(1)
    return time.mktime(datesec)

def daysdiff(date1,date2):
    d1 = datetrans(date1)
    d2 = datetrans(date2)
    daysec = 24 * 60 * 60
    return int((d1 -d2)/daysec)

#date1 = dateinput()
#date2 = dateinput()

#date1sec = datetrans(date1)
#date2sec = datetrans(date2)

#print 'The number of days between two dates is:',daysdiff(date1sec,date2sec)
                           
