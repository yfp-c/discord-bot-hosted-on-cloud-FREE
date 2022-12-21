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