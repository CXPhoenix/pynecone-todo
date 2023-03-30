import pynecone as pc


def index() -> pc.Component:
    return pc.center(
        pc.vstack(
            pc.heading("TODO List", size="4xl"),
            pc.text("First project using Pynecone!",
                    padding_top="1.5rem", padding_bottom="2.5rem", font_size="2rem"),
            pc.link("ARRANGE THINGS NOW",
                    href="/todo",
                    border_radius="1rem",
                    bg="#02C874",
                    padding="1rem 1.75rem",
                    color="white",
                    _hover={"background-color": "#00EC00",
                            "transform": "scale(1.25)"},
                    )
        ),
        width="100vw",
        height="90vh",
    )
