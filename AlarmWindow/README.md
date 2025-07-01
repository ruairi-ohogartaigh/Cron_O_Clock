# AlarmTemplates
The beauty of cron is that it is system based. Once the user has configured their 
schedule and it is appended to cron, the application in *UserSettings* where the user defines the schedule can be terminated. 
When an event is trigger by cron it will call an executable from this directory.
The executable is a simple window that notifies the user to get lunch, take a break etc.
From the directory of this README.md, simply call the command below to see a sample for a coffee break.  

```
python3 ./CronOlarm.py --image coffee.png --message "Time for vitamin C!" --displaytime 5
```
## Alarm template call
As can be seen, this command takes three arguments:
- An image from the *Imglib* folder using the flag `-i` or `--image`
- The message for the user and a display time using the flag `-m` or `--message`
- The desired time the image will display for in seconds. the flags are `-t` and `--displaytime` 

There is a small selection of images in `ImageLibrary`, for example a cup of tea, coffee. I intend to allow users add to the library of images through the UI when setting a schedule.


## view lock
There could be an option to remove the `X` button from the display and have the window terminate on a time. I would either get around it with hot-key operations and or killing the process. It could be an option for a third-party though if you are using linux as a daily driver you're probably aware of at least one work-around. 

## User config side
I think there are a few thinks to be added to the User config GUI. The display time should be able to be set for 10 or 30 minutes for break times and lunch. This can be set of te config side by formatting.

For messages, there could be addition for basic templates.

## further development of the AlarmWindow
There could be another argument added to the CLI to allow uses automate tasks too. This might be the next change I make to this folder. For now, I think it is developed enough for development on the other project components.