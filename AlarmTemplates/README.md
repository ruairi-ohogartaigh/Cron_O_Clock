# AlarmTemplates
The beauty of cron is that it is system based. Once the user has configured their 
schedule and it is appended to cron, this application where the user defines the schedule can be terminated. 
When an event is trigger by cron it will call an executable from this directory.
The executable will be a simple window that notifies the user to get lunch, take a break etc.


## Alarm Template GUI
To keep in simple, I think I will call a basic script in the format `./AlarmTriggers.py -i ref_image -m display_message ... TBD`
There will be a selection of images in `ImageLibrary`, for example a cup of tea, coffee, a lunch meal. Generic stock images. 

## view lock
There could be an option to remove the `X` button from the display and have the window terminate on a time. I would either get around it with hot-key operations and or killing the process. It could be an option for a third-party though if you are using linux as a daily driver you're probably aware of at least one work-around. 