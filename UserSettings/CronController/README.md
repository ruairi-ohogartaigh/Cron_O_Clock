# CronController
This is the folder where cron jobs set by the user in the user settings UI will appended to crontab.

## Current state
I have a single function created and confirmed its operations with the AlarmWindow
* Viewing the crontab, initial thoughts of needing a csv log have changes, `grep` and `rm`  may be a simple option for removing jobs in the schedule. 

## Further work
On reviewing the function, There might be a valid argument in building it into a class structure. At present, the crontab user is defined every time the function is called. It should be moved into a bigger scope for better code structure. 
