# Cron_O_Clock
Cron_O_Clock is a GUI for scheduling User interface notifications. At present it is a combination of two modules:
- AlarmWindow - GUI widows called by cron
- UserSettings  - User interface Crontab scheduler


## UserSettings
This is the folder containing the main project GUI. The folder has two sub-directories, "CronController" where the cron commands are placed, and "CronControlWindows", where the GUI frontend is located. For more information, read the README.md in this subdirectory.

## AlarmWindow 
This folder holds basic scripts that can be called from the CLI. 
These scripts will be triggered by cronjobs configured in the UI. 
The only script available at present is a basic notification screen that contains a message and background image.
View the README.md in this subdirectory for more information.


## Why 
There are probably multiple examples of this kind of app available in several locations on the internet.
I'm not as familiar with Cron as I would like to be, I think this project could be a good exercise in familiarizing myself with cron scheduling. 
