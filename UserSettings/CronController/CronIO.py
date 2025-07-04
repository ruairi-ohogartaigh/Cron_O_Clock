from crontab import CronTab
import getpass
import os

class CronIO():
    def __init__(self, parent, user=None, apply_new_task=None):
        if user is None:
            user = getpass.getuser()
        self.cron = user
        self.cron = CronTab(user=self.cron)
        self.parent = parent
    # cron alarm is creates a GUI alarm.
    def new_cron_alarm(self, freq, img, msg, display_time):
        cron = self.cron
        dirname = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'AlarmWindow'))
        job = cron.new(command=f'python3 {dirname}/CronOlarm.py --image {img} --message "{msg}" --displaytime {display_time}')
        job.hour.on(freq[1])    # 0-23
        job.minute.on(freq[0])  # 0-59
        job.dow.on(freq[4])
        cron.write()
        return 0

    # add user defined cron job (no-GUI)
    def add_cron_job(self, job_command, freq):
        cron = self.cron
        job = cron.new(command=job_command)
        job.hour.on(freq[1])    # 0-23
        job.minute.on(freq[0])  # 0-59
        job.dow.on(freq[4])  # e.g. "SAT", "SUN", etc.

        cron.write()
        return 0
    

    def remove_cron_job(self, job_command, freq):
        cron = self.cron
        # find the job by command and remove it
        for job in cron:
            if job.command == job_command and job.hour ==job_command:
                cron.remove(job)
                cron.write()
                return 0
        return -1


    # basic getter for cron jobs, returns strings of the jobs
    def get_cron_jobs(self):
        cron = self.cron
        cronlist = []
        for job in cron:
            cronlist.append(str(job))
        return cronlist




## function testing 
# if __name__ == "__main__":
#     cron=CronIO(user=getpass.getuser())
#     cron.new_cron_alarm(freq=(00, 11, 0, 0, ["MON", "TUE", "WED", "THU", "FRI"]), img="alarm.png", msg="Test Alarm", display_time=10)
#     jobs = cron.get_cron_jobs()
#     for job in jobs:
#         print(job)