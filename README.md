# Welcome
Hello, continuing on from [my previous discord repo](https://github.com/yfp-c/Discord-bot-on-RasPi-zero-2-w-discontinued) I have moved my python discord bot to an oracle cloud server, where it is hosted FREE 24/7 and due to the modular design of my bot, it will always be up regardless if I add, remove or update any features.

![image](https://user-images.githubusercontent.com/98178943/208892337-989e4974-c2c2-4d86-8444-1865cece1741.png)

This bot has been a great learning experience for me, as someone who is very new to tech. I've had to incorporate/use powershell, python, cloud servers, bash and most recently I've implemented an SQLite database with full discord python interaction. 

### Key features (and more still to be added soon)
- SQLite database to store values (discord id/username and other values which will increment)
- Implemented public APIs which can be interacted with users (e.g. retrieve quotes)
- Scraped [large web content using powershell](https://github.com/yfp-c/Powershell-Fun-/blob/main/Web%20scraping/Scrape_fortunecookie_quotes.ps1) and implemented it into a cog
- Scan for specific words, responding in return
- Scan for specific user, responding in return with cooldown so user is not spammed whenever they send a message in channel
- Send message at certain time every day or on a certain day of the week (e.g. send a weekly message to remind colleagues to fill in timesheets!)
- Made use of the 'buttons' feature in discord.py and combined it with public apis
- Notify users of command cooldown to prevent spam and duration of cooldown.

# Adding discord bot to Oracle cloud server
- Sign up to https://cloud.oracle.com/, you may need to enter contact and card details
- To choose the always free setting, make sure you choose these features: 
![image](https://user-images.githubusercontent.com/98178943/208894510-024c69d0-0544-4231-a667-f8aae901d4af.png)
- Depending on the image (ideally choose an Ubuntu one like Canonical Ubuntu 20.04) you will need to set up the environment.

#### Setting up bot on ubuntu server
- login and enter the following:
```
sudo apt-get update -y && sudo apt-get upgrade -y
sudo apt-get install screen
sudo apt-get install python3
pip install discord
pip install discord.py
```
#### Script to run bot in detached screen mode
```
#!/bin/bash
screen -d -m -S discordbot python3 /home/pi/discordbot.py
# starts bot in screen mode, gives it a name and detaches
```
#### Starting
- Copy of the contents of your (or my) bot in and start it by executing the main python file.

#### Quality of life improvements for the user
- To make it easier for myself when adding, removing, updating features on the bot, and rather than entering the terminal and typing lots of commands. I have found it easier to use SSH software which makes managing my bot an ease. 
- I use bitvise to manage mine and a tutorial for adding your oracle cloud server to bitvise can be found here.. https://www.youtube.com/watch?v=90JbCrB3m3I

## Future plans
- To continue adding new features where I will have to learn and understand new concepts and technologies (such as the sqlite database)
- CI/CD pipeline which I have attempted successfully here: https://github.com/yfp-c/CICD-with-discord-bot-and-concourse-on-oracle 
- Containerize discord bot for others to use (for this I'll need to do a major cleanup)
