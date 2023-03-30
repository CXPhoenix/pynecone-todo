"""Welcome to Pynecone! This file outlines the steps to create a basic app."""
import pynecone as pc
from .pages.homePage import index
from .pages.todoPage import todo
from .State import TodoState


# Add state and page to the app.
app = pc.App(state=TodoState)
app.add_page(index)
app.add_page(todo, route="/todo")
app.compile()
