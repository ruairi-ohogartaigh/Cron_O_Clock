from crontab import CronTab
import getpass
import os


# Crontab time format * * * * * # minute hour day_of_month month day_of_week
#
#1. * minutes 0-59
#2. * hours 0 to 23
#3. * day_of_month 1 to 31
#4. * month 1 to 12
#5. * day_of_week 0 to 6 (Sunday to Saturday, 7 is also Sunday on some systems)



def new_cron_job(freq, img, msg, display_time):
    cron = CronTab(user=getpass.getuser())  # may need OOP cronIO class to tidy code
    dirname=os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..','..', 'AlarmWindow'))
    job = cron.new(command='python3 '+dirname+'/CronOlarm.py  --image '+img+' --message '+msg+' --displaytime '+display_time)
    job.hour.on(freq[1])  # 0-23
    job.minute.on(freq[0])  # 0-59
    if freq[4]=="weekdays": # this will need further development to allow for more options
        job.dow.on("MON","TUE","WED","THU","FRI")  # 0-6 for Sunday to Saturday
    cron.write()

    return 0

# to be removed
# if __name__ == "__main__":  # basic function tesitng 
#     new_cron_job([10,14,'*','*',"weekdays"], 'coffee.png', '\"This is a test message\"', '10')