# chatBotSudheesh
ChatBot coded in Python, is able to tell the weather, do simple math, and respond to simple tasks or questions for the kata challenge. It relies on the Microsoft bot framework for functionality using app.py and configy.py.

The bot is able to find the weather in user-specified locations, do basic math, and respond to simple questions and tasks - like the ones specified in the writeup.
Originally, my kata was the weather application that got information about the weather given a location from a user. However, I decided to attempt integrating this functionality into a chatbot, and thus use an external API to get the weather when a user asks for the weather in a named location in the chatbot.

The bot.py is the file containing the bot's logic and was coded in Python by me, Sudheesh Dabbara, and relies on the Microsoft bot framework, which provides Microsoft's app.py and config.py files

To run the chatbot, the Microsoft bot framework emulator is required. To run the bot, download the files into a directory, navigate into the directory, and run python app.py, then go to the emulator, click open bot, then enter http://localhost:3978/api/messages as the bot URL, and then click connect.

