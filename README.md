# Food Chatbot

A Django-based chatbot web application that uses OpenAI's GPT models to interact with users about their favorite foods, simulates conversations between AI agents, and provides a REST API for querying vegetarian users. The project is containerized with Docker and designed for deployment on Azure App Service.

This is a project done for the application process of the company Elephants in the Room.

## Structure

The project runs on a docker with a PostgreSQL database both deployed in Azure.
Enter this URL to access the REST framework interface's root:
```bash
https://food-chatbot-app.azurewebsites.net/
```
From here you can access three paths:

### 1: API
Here you have the api for the databases with their CRUD operations:
```bash
https://food-chatbot-app.azurewebsites.net/api/
```
Although for security reasons only List and Retrieve are avaliable so: 
```bash
https://food-chatbot-app.azurewebsites.net/api/users/
https://food-chatbot-app.azurewebsites.net/api/users/{id}
```

And there's also the requested endpoint to retrieve the vegetarian users.
This function is protected with BasicAuth so credentials are needed to access.
```bash
https://food-chatbot-app.azurewebsites.net/api/users/vegetarians
```

### 2: ADMIN
The basic admin page (also needs credentials):
```bash
https://food-chatbot-app.azurewebsites.net/admin/
```

### 3: CHAT
This is a bonus implementation that I decided to add.
```bash
https://food-chatbot-app.azurewebsites.net/chat/
```
This path leads to a chat interface to of a MVP. What it does is it uses the Chatgpt A as an interviewer (same as with the 100 bot interactions) but in this case it asks you your 3 favourite foods and from that it gives you a recommendation from a db of restaurants that it has.

Te business idea with this would be for example presenting this interface as a free app for people while selling the user preference data to restaurants. With this the users would be abled to decide which restaurants to go to according to their preferences while on the other hand the restaurants would know the food preferences from the public and modify their menus accordingly.

To make the interface I used a CDN to make a simple and easy interface as the main focus of the project was the backend.

### MANAGEMENT COMMANDS
I made some management commands, for example simulate_chats.py to make the 100 conversations between Chatgpt A and Chatgpt B:
```bash
python manage.py simulate_chats
```
Or once deployed:
```bash
docker exec -it myproject_container python manage.py simulate_chats
```
And also a script to generate restaurants (by default 20)
```bash
python manage.py create_restaurants
```
Both scripts can create a custom ammount by using the --count arg:
```bash
python manage.py create_restaurants --count 10
```

### SERVICES
In services there's the two Chatgpt A/B classes and the parser (food_parser).
Chatgpt B instead of choosing random foods first chooses a personality and after that it decides what favourite foods it has. This had to be done because otherwise almost all the agents decided the same foods, repeating Sushi or Pizza in almost all the answers, so I made this to get more variety.

food_parser is the function that parses your answer and returns the 3 item list and the is_vegetarian boolean.

### AUTHENTICATION
The instructions asked specifically to add authentication to the API endpoint for the vegetarian_list, so I made only this API endpoint private. This way everyone can access the main one with all the users but only authorized users can access the vegetarian list.