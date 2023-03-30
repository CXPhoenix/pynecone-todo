from typing import Union
from datetime import datetime
from zoneinfo import ZoneInfo
from pydantic import BaseModel
import pynecone as pc

taipeiZone = ZoneInfo("Asia/Taipei")


def setBorderColor(expiredTime: str) -> str:
    if expiredTime == "":
        return "rgb(16, 185, 129)"
    now = datetime.now(tz=taipeiZone)
    dateExpiredTime = datetime.fromisoformat(
        expiredTime).replace(tzinfo=taipeiZone)
    if dateExpiredTime < now:
        return "rgb(234, 88, 12)"
    if (dateExpiredTime - now).seconds < (2*24*60*60):
        return "rgb(202, 138, 4)"
    return "rgb(16, 185, 129)"


class ModelState(pc.State):
    show: bool = False

    def change(self):
        self.show = not self.show


class TodoItem(BaseModel):
    text: str
    expiredTime: Union[str, None] = None
    borderColor: str = "rgb(16, 185, 129)"


class TodoState(pc.State):
    borderColor: str = "rgb(16, 185, 129)"

    todos: list[TodoItem] = [
        TodoItem(**{
            "text": "test1",
            "expiredTime": "2023-04-11T10:30:00",
        }),
        TodoItem(**{
            "text": "test2",
            "expiredTime": "2023-05-12T10:30:00",
        }),
        TodoItem(**{
            "text": "test3",
            "expiredTime": "2023-07-08T09:00:00",
        })
    ]

    showTodos: list[TodoItem] = todos[::-1]

    newTodoText: str = ""
    newTodoExpiredDate: str = ""
    newTodoExpiredTime: str = ""

    modelShow: bool = False
    modelText: str = ""

    def closeModel(self):
        self.modelShow = False

    def addItem(self):
        if self.newTodoText == "":
            self.modelText = "You should write the todo."
            self.modelShow = True
            return
        if self.newTodoExpiredDate != "" and self.newTodoExpiredTime == "":
            self.modelText = "You should set a expired time."
            self.modelShow = True
            return
        if self.newTodoExpiredDate == "" and self.newTodoExpiredTime != "":
            self.modelText = "You should set a expired date."
            self.modelShow = True
            return
        if self.newTodoExpiredDate != "" and self.newTodoExpiredTime != "":
            expiredTime = self.newTodoExpiredDate + "T" + self.newTodoExpiredTime + ":00"  # noqa: E501
        else:
            expiredTime = ""
        newTodoItem = TodoItem(**{
            "text": self.newTodoText,
            "expiredTime": expiredTime,
            "borderColor": setBorderColor(expiredTime)
        })
        self.todos.append(newTodoItem)
        self.showTodos = self.todos[::-1]
        self.newTodoText = ""
        self.newTodoExpiredDate = ""
        self.newTodoExpiredTime = ""

    def removeItem(self, item: dict):
        self.todos.remove(TodoItem(**item))
        self.showTodos = self.todos[::-1]

    pass
