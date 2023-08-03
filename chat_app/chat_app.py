"""Welcome to Reflex! This file outlines the steps to create a basic app."""
from rxconfig import config

import reflex as rx
from chat_app import style
from chat_app.state import State


def index() -> rx.Component:
    return rx.container(chat(), action_bar(), margin_y="2em")


def question_answer(question: str, answer: str) -> rx.Component:
    return rx.container(
        rx.box(
            rx.text(question, style=style.question_style),
            text_align="right",
        ),
        rx.box(
            rx.text(answer, style=style.answer_style),
            text_align="left",
        ),
        overflow="hidden",
    )


def chat() -> rx.Component:
    return rx.box(
        rx.foreach(
            State.chat_history,
            lambda messages: question_answer(messages[0], messages[1]),
        )
    )


def action_bar() -> rx.Component:
    return rx.hstack(
        rx.input(
            placeholder="Ask a question",
            on_blur=State.set_question,
            style=style.input_style,
        ),
        rx.button(
            "Ask",
            on_click=State.answer,
            style=style.button_style,
        ),
        flex_direction="row",
        justify_content="space-between",
    )


# Add state and page to the app.
app = rx.App()
app.add_page(index, route="/")
app.compile()
