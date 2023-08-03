import reflex as rx
import os


class ChatappConfig(rx.Config):
    pass


config = ChatappConfig(
    app_name="chat_app",
    api_url="http://localhost:8000",
    env=rx.Env.DEV,
    env_path=os.path.join(os.getcwd(), ".env"),
    tailwind={
        "theme": {
            "extend": {},
        },
        "plugins": [],
    },
)
