import pynecone as pc
from ..State import TodoState


def alertModel() -> pc.Component:
    return pc.alert_dialog(
        pc.alert_dialog_overlay(
            pc.alert_dialog_content(
                pc.alert_dialog_header("Warning"),
                pc.alert_dialog_body(
                    TodoState.modelText
                ),
                pc.alert_dialog_footer(
                    pc.button(
                        "Close",
                        on_click=TodoState.closeModel,
                    )
                ),
            )
        ),
        is_open=TodoState.modelShow,
    )


def todoPageHeader() -> pc.Component:
    return pc.heading(
        "TODO SYSTEM",
        text_align="center"
    )


def todoSetterForm() -> pc.Component:
    return pc.flex(
        pc.text_area(
            value=TodoState.newTodoText,
            on_change=TodoState.set_newTodoText,
            placeholder="Your todo..."
        ),
        pc.hstack(
            pc.vstack(
                pc.text("Expired Date:", width="100%"),
                pc.input(
                    value=TodoState.newTodoExpiredDate,
                    type_="date",
                    on_change=TodoState.set_newTodoExpiredDate
                ),
                width="100%"
            ),
            pc.vstack(
                pc.text("Expired Time:", width="100%"),
                pc.input(
                    value=TodoState.newTodoExpiredTime,
                    type_="time",
                    on_change=TodoState.set_newTodoExpiredTime
                ),
                width="100%"
            )
        ),
        pc.button(
            "add todo item!",
            bg="#005757",
            color="white",
            _hover={},
            on_click=TodoState.addItem
        ),
        width="100%",
        justify="center",
        flex_direction="column",
        padding="0rem 0.75rem",
        gap="0.75rem"
    )


def todoContent(text) -> pc.Component:
    return pc.text(
        text,
        font_size="1.5rem",
        line_height="2rem",
        width="100%"
    )


def todoExpiredTime(timeString) -> pc.Component:
    return pc.text(
        timeString,
        font_size="0.875rem",
        line_height="1.25rem",
        width="100%"
    )


def todoDoneBtn(item) -> pc.Component:
    return pc.button(
        "done.",
        border_radius="0.5rem",
        bg="rgb(220, 38, 38)",
        color="white",
        _hover={
            "color": "rgb(38, 38, 38)",
            "bg": "rgb(209, 213, 219)"
        },
        on_click=TodoState.removeItem(item)
    )


def todoBox(todoData: pc.Var) -> pc.Component:
    return pc.box(
        pc.flex(
            todoContent(todoData.text),
            pc.flex(
                todoDoneBtn(todoData),
                justify="end",
                width="100%"
            ),
            todoExpiredTime(todoData.expiredTime),
            padding="1rem 1.5rem",
            flex_direction="column",
            gap="0.75rem"
        ),
        width="100%",
        border_width="2px",
        border_radius="0.5rem",
        border_color=todoData.borderColor
    )


def todo() -> pc.Component:
    return pc.flex(
        todoPageHeader(),
        todoSetterForm(),
        pc.foreach(TodoState.showTodos, todoBox),
        alertModel(),
        width=["100%", "100%", "90%", "75%", "75%"],
        margin="0 auto",
        flex_direction="column",
        justify="center",
        padding=["1rem 0.25rem", "1.5rem ",
                 "2rem 4rem", "2rem 4rem", "2rem 4rem"],
        gap="3rem"
    )
