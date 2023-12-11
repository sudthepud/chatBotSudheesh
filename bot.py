#Provided from the framework
from botbuilder.core import ActivityHandler, TurnContext
from botbuilder.schema import ChannelAccount

#Imports for date and time, and regex
from datetime import datetime
from datetime import date
import re
import requests

# This class contains all the actions called based on the intent found from the message
class TaskHandler:

    # Getting the time using datetime and printing to the user
    @staticmethod
    async def time(turn_context: TurnContext):
        # Getting the time and formatting it to a proper string
        currentTime = datetime.now()
        timeToPrint = currentTime.strftime("%H:%M")
        # Printing the time to the user
        await turn_context.send_activity("The time right now is " + timeToPrint + ".")
        await turn_context.send_activity("Please let me know if I can help you with anything else!")

    # Getting the date and time using datetime and printing to the user 
    @staticmethod
    async def date(turn_context: TurnContext):
        # Getting the date and time and formatting them into proper strings
        currentDate = datetime.now()
        dateToPrint = currentDate.strftime("%m/%d/%y")
        currentTime = datetime.now()
        timeToPrint = currentTime.strftime("%H:%M")
        # Printing the date and time
        await turn_context.send_activity("The date is " + dateToPrint + " and the time is " + timeToPrint + ".")
        await turn_context.send_activity("Please let me know if I can help you with anything else!")

    # Using an external API to get the weather in a provided city, which is extracted during evaluation of message and passed to this method, then printing the weather info to the user
    @staticmethod
    async def weatherInCity(turn_context: TurnContext, city: str):
        # API key and url, and getting the response from the API using the city extracted
        api_key = '98b708a037c544f3dcc86694bdfa74be'
        api_url = f'http://api.weatherstack.com/current?access_key={api_key}&query={city}'
        response = requests.get(api_url)
        # If the response is a valid response (200 according to the API's writeup) then continue
        if (response.status_code == 200):
            data = response.json()
            # If the data has values, continue
            if ('current' in data):
                # Getting the temperature, description, true feel, wind speed, and wind direction
                temperature = data['current']['temperature']
                weather_description = data['current']['weather_descriptions'][0]
                tempFeelsLike = data['current']['feelslike']
                windSpeed = data['current']['wind_speed']
                windDirection = data['current']['wind_dir']
                # Formating the message using the data extracted form the API
                await turn_context.send_activity("The weather in " + city + f" is: {temperature}°C with " + weather_description + f" and the feels like temperature is: {tempFeelsLike}°C.\nThe wind speed is {windSpeed} KPH going " + windDirection + ".")
                await turn_context.send_activity("Please let me know if I can help you with anything else!")
            # If the data has no values, it means the city could not be found, so ask the user to provide proper spelling, a bigger city, and reformat their message
            else:
                await turn_context.send_activity("I was unable to find information about this location, please check for proper spelling including spaces, or try a larger location.")
                await turn_context.send_activity("\nIs there anything else I can help you with?")
         # If there was an error, it means the city could not be found, so ask the user to provide proper spelling, a bigger city, and reformat their message
        else:
            await turn_context.send_activity("I was unable to find information about this location, please check for proper spelling including spaces, or try a larger location.")
            await turn_context.send_activity("Is there anything else I can help you with?")

    # Method for telling the user to format a question about the weather in a specific location a certain way so the code can read it and get the city
    @staticmethod
    async def weatherFormat(turn_context: TurnContext):
        await turn_context.send_activity("It seems like you are asking about the weather. For the weather in a specific location, please format your message as 'weather in <your_location>.")
        await turn_context.send_activity("What else can I help you with?")
    

    # Handling math using regex and eval() and printing out the value of the user's provided math expression, or a failure method that asks the user to reformat their question so the bot can handle it
    @staticmethod
    async def handle_math(turn_context: TurnContext):
        # Searching for a math equation, namely divide, add, multiply, subtract
        match = re.search(r'([\d+\-*/]+)', turn_context.activity.text, re.IGNORECASE)
        if (match):
            try:
                # If there is a match, then strip out all other characters outside of the math expression and evaluate it. This is currently not space sensitive
                result = eval(match.group(1).strip())
                # Send out the result to the UI
                await turn_context.send_activity(f"The result is: {result}")
            except Exception as e:
                # If there is an error send out a message asking for valid formating
                await turn_context.send_activity(f"Please provide a math expression with numerical values, symbols, and no spaces.")
        else:
            # If there is no match, like the user says add instead of +, it tells the user to provid a valid format
            await turn_context.send_activity("Please provide a math expression with numerical values, symbols, and no spaces.")


    # Greeting method that prints to the user a generic response and how are you doing?
    @staticmethod
    async def greeting(turn_context: TurnContext):
        await turn_context.send_activity("Hi!\nHow are you doing?")

    # Booking method that provides places where the user could book plane tickets
    @staticmethod
    async def booking(turn_context: TurnContext):
        await turn_context.send_activity("You can book a flight or plan a trip on priceline.com, trivago.com, or an airlines website.")
        await turn_context.send_activity("Is there anything else I can assist you with?")

    # Pizza method that respons saying I Like Pizza too! when the user says something generic about pizza, not related to ordering it
    @staticmethod
    async def Pizza(turn_context: TurnContext):
        await turn_context.send_activity("I like Pizza too!")
        await turn_context.send_activity("Is there anything else I can do for you?")

    # Order pizza method that suggests palces to get pizza
    @staticmethod
    async def orderPizza(turn_context: TurnContext):
        await turn_context.send_activity("You can order a pizza from popular places like dominos.com, pizzahut.com, or papajohns.com.")
        await turn_context.send_activity("Is there anything else can I help you with?")

    # Help method that says what this chatbot can help with
    @staticmethod
    async def handle_help(turn_context: TurnContext):
        await turn_context.send_activity("I can help you with simple tasks.")
        await turn_context.send_activity("What else can I help you with?")

    # Outsidescope method that says the request is outside capabilities
    @staticmethod
    async def outsideScope(turn_context: TurnContext):
        await turn_context.send_activity("I'm sorry, that request or question is outside of my capabilities.")
        await turn_context.send_activity("What else can I help you with?")
    
    # Personal method that responds with saying the chatbot doesn't have personal information and doesn't store information about the user
    @staticmethod
    async def personal(turn_context: TurnContext):
        await turn_context.send_activity("Since I am a chatbot, I don't have a location, name, age, or emotions and I do not know or store any information about you.")
        await turn_context.send_activity("What else can I help you with?")

    # Greeting method that responds to a user doing well with a good to hear message
    @staticmethod
    async def doingGood(turn_context: TurnContext):
        await turn_context.send_activity("Nice! That's great to hear.")
        await turn_context.send_activity("What can I help you with?")
    
    # Greeting method that respons to a user not doing well with a sorry to hear that method
    @staticmethod
    async def doingBad(turn_context: TurnContext):
        await turn_context.send_activity("Sorry to hear that.")
        await turn_context.send_activity("What can I help you with?")

    # General food method that provides a message about popular foods
    @staticmethod
    async def food(turn_context: TurnContext):
        await turn_context.send_activity("Some popular food choices are pizza, burgers, fries, sandwhiches, and pasta.")
        await turn_context.send_activity("What else can I help you with?")

    # Joke method that puts out a joke to the user
    @staticmethod
    async def joke(turn_context: TurnContext):
        await turn_context.send_activity("I've got a joke: why was 6 afraid of 7? Because 7 ate 9!")
        await turn_context.send_activity("Is there anything else I can help you with?")

    # Reservation method that tells the user how to make a reservation
    @staticmethod
    async def reservation(turn_context: TurnContext):
        await turn_context.send_activity("To make a reservation, you should check the establishment's website or call their number.")
        await turn_context.send_activity("What else can I help you with?")

    # Movie method that says how the user can get movie tickets
    @staticmethod
    async def movie(turn_context: TurnContext):
        await turn_context.send_activity("Movie's are great, you can search for showtimes online and buy tickets online or buy tickets at the theatre.")
        await turn_context.send_activity("Is there anything else I can help you with?")

    # Method for saying bye to the user for when the user indicates they want the conversation to end
    @staticmethod
    async def bye(turn_context: TurnContext):
        await turn_context.send_activity("It has been great chatting with you and I hope I helped, take care!")

    # Method for random keywords that results in a generic "What can I help you with?" response
    @staticmethod
    async def random(turn_context: TurnContext):
        await turn_context.send_activity("What can I help you with?")


# This class handles getting the intent from the user input and calling the appropriate action based on that intent
class MyBot(ActivityHandler):
    async def on_message_activity(self, turn_context: TurnContext):
        # Getting the intent, or subject that we are focused on handling, using the extract_intent method
        intent = self.extract_intent(turn_context.activity.text.lower())

        # Calling the appropriate TaskHandler method based on the intent provided by the extract intent method
        if (intent == "booking"):
            await TaskHandler.booking(turn_context)
        elif (intent == "Pizza"):
            await TaskHandler.Pizza(turn_context)
        elif (intent == "orderPizza"):
            await TaskHandler.orderPizza(turn_context)
        elif (intent == "math"):
            await TaskHandler.handle_math(turn_context)
        elif (intent == "reservation"):
            await TaskHandler.reservation(turn_context)
        elif (intent == "movie"):
            await TaskHandler.movie(turn_context)
        elif (intent == "help"):
            await TaskHandler.handle_help(turn_context)
        elif (intent == "greeting"):
            await TaskHandler.greeting(turn_context)
        elif (intent == "outsideScope"):
            await TaskHandler.outsideScope(turn_context)
        elif (intent == "personal"):
            await TaskHandler.personal(turn_context)
        elif (intent == "doingGood"):
            await TaskHandler.doingGood(turn_context)
        elif (intent == "doingBad"):
            await TaskHandler.doingBad(turn_context)
        elif (intent == "time"):
            await TaskHandler.time(turn_context)
        elif (intent == "date"):
            await TaskHandler.date(turn_context)
        elif (intent == "food"):
            await TaskHandler.food(turn_context)
        elif (intent == "joke"):
            await TaskHandler.joke(turn_context)
        elif (intent == "random"):
            await TaskHandler.random(turn_context)
        elif (intent == "bye"):
            await TaskHandler.bye(turn_context)
        elif (intent == "weatherFormat"):
            await TaskHandler.weatherFormat(turn_context)
        elif ("weatherInCity|" in intent):
            # Extracting the city found in the message using the | character to pass to the TaskHandler method 
            city = re.sub(r'^weatherInCity\|', '', intent)
            await TaskHandler.weatherInCity(turn_context, city)
        else:
            # This else statement is the final fallback that will reply to the user with message not supported yet
            await turn_context.send_activity("I'm sorry, your message subject may not be supported yet, or please try to rephrase your message.")

    # This method evaluates the user provided message and provides an intent, or subject, that is used to act on the message, based on keywords and phrases
    def extract_intent(self, message: str) -> str:

        # Pizza related chats get caught here, and are further evaluated for ordering pizza
        if ("pizza" in message):
            # If the message is also order related then say the intent is orderPizza
            if (any(word in message for word in ["order", "get", "want", "buy"])):
                return "orderPizza"
                # If not order related return general Pizza intent
            else:
                return "Pizza"
        
        # Weather related chats get caught here
        elif (any(word in message for word in ["weather", "temperature", "cold", "hot"])):
            # If the user also has the words "weather in", then get the city following the in and rend it to the weatherInCity function
            if "weather in" in message:
                # Using regex to get the city name and isolating it by removing everything before the weather in and any punctiation after the city
                city_extracted = re.sub(r'.*weather in', '', message, flags=re.IGNORECASE)
                city = re.sub(r'[^\w\s]', '', city_extracted).strip()
                # weatherInCity along with the city we extracted, using the | to seperate the city later
                return ("weatherInCity|" + city)
            # Else, send a message to show the user the correct format for getting the weather
            else:
                return "weatherFormat"

        # Catching anything related to plane tickets
        elif (any(word in message for word in ["flight", "plane", "trip", "airport", "book", "ticket"])):
            return "booking"
        # Catching math related messages
        elif (any(word in message for word in ["math", "add", "divide", "multiply", "subtract", "product", "sum", "+", "/", "-", "*"])):
            return "math"
        # Catching general food related messages
        elif (any(word in message for word in ["food", "hungry", "eat", "consume", "munch", "bite", "grub"])):
            return "food"
        # Catching time related messages
        elif (any(word in message for word in ["clock", "time", "hour", "seconds", "minutes"])):
            return "time"
        # Catching date related messages
        elif (any(word in message for word in ["date", "day", "year", "month"])):
            return "date"
        # Catching joke related messages
        elif (any(word in message for word in ["joke", "funny", "laugh", "giggle"])):
            return "joke"
        # Catching messages related to the user doing well
        elif (any(word in message for word in ["good", "alright", "great", "awesome", "fantastic", "superb", "phenomenal", "happy"])):
            return "doingGood"
        # Catching messages related to the user not doing well
        elif (any(word in message for word in ["terrible", "bad", "horrible", "sad", "cry", "hurt", "pain"])):
            return "doingBad"
        # Catching reservation related messages
        elif (any(word in message for word in ["reserve", "restaurant", "reservation"])):
            return "reservation"
        # Catching movie related messages
        elif (any(word in message for word in ["cinema", "movie", "theatre", "film"])):
            return "movie"
        # Catching messages related to the user leaving or saying bye signifying they want the chat to end
        elif (any(word in message for word in ["bye", "see you", "cya", "take care", "later", "farewell", "peace", "no", "leave", "exit", "end", "stop", "done", "finish", "last", "gone"])):
            return "bye"

        # If none of the situations above are met, then this will return a not supported message
        elif (any(word in message for word in ["can you", "what is", "will you", "do you", "how can", "please do", "do this", "order", "this", "do", "can", "will", "want", "buy", "?", "give"])):
            return "outsideScope"
        
        # Personal questions will get caught here
        elif (any(word in message for word in ["where are", "age", "old", "name", "you"])):
            return "personal"

        # Basic greeting words, but is last because "hi" is in "this", and what's up could be used elsewhere
        elif (any(word in message for word in ["hello", "hi", "hey", "what's up", "howdie", "yo"])):
            return "greeting"

        # Random words that may come up and are not caught by any other intents, in that case just ask if theres anything to help with
        elif (any(word in message for word in ["yes", "nice", "maybe", "ok", "okay", "lol", "cool", "sick", "yeah", "nah", "of", "course", "so"])):
            return "random"

        # Help
        elif ("help" in message):
            return "help"

        # If not caught by other intents and by the outside scope intent, then say the message type is not supported
        else:
            return "unknown"

    # Code provided by microsoft framework
    async def on_members_added_activity(
        self,
        members_added: ChannelAccount,
        turn_context: TurnContext
    ):
        for member_added in members_added:
            if member_added.id != turn_context.activity.recipient.id:
                await turn_context.send_activity("Welcome to the chatbot. I can help with simple tasks.")