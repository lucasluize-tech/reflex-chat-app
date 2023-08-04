<h1 text-align="center"> Chatbot App using reflex</h1>

this is a chatbot app using reflex, a python framework still in development,
it seems to be a wrapper of nextjs under the hood. Not sure if will be a good
performant stack but this is my build to test it out.

### Requirements

all you need to do is run the following command:

```bash
$ git clone https://github.com/lucasluize/reflex-chat-app.git
$ cd reflex-chat-app
$ pip install -r requirements.txt
$ reflex run --loglevel debug
```

Frontend server should be running on port 3000 and backend on port 8000.
test it out by going to http://localhost:3000 and http://localhost:8000/ping

don't forget to create a .env file with your credentials for the chatbot api.
`OPENAI_API_KEY=[YOUR_API_KEY]`

## You can check more about reflex on their docs!

https://github.com/reflex-dev/reflex
