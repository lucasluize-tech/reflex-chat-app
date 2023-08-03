import reflex as rx
import os


class ChatappConfig(rx.Config):
    pass


config = ChatappConfig(
    app_name="chat_app",
    db_url="postgresql://lucasluize@localhost:5432/relfex-chat-app",
    env=rx.Env.DEV,
    env_path=os.path.join(os.getcwd(), ".env"),
    tailwind={
        "theme": {
            "extend": {},
        },
        "plugins": [],
    },
)
