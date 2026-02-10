import dash
from dash import html, dcc, Input, Output, State
import dash_bootstrap_components as dbc

from config import client, MODEL, messages

# =====================
# App initialization
# =====================
app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.VAPOR],
)
app.title = "GenBot – Génération IA"

# =====================
# Styles
# =====================
CHAT_CONTAINER_STYLE = {
    "height": "65vh",
    "overflowY": "auto",
    "padding": "15px",
    "backgroundColor": "#f6f2ff",
    "borderRadius": "12px",
}

USER_BUBBLE = {
    "backgroundColor": "#6f42c1",
    "color": "white",
    "padding": "10px 14px",
    "borderRadius": "15px",
    "maxWidth": "75%",
    "marginLeft": "auto",
}

BOT_BUBBLE = {
    "backgroundColor": "white",
    "color": "#3d246c",
    "padding": "10px 14px",
    "borderRadius": "15px",
    "maxWidth": "75%",
    "border": "1px solid #e0d7f5",
}

# =====================
# Layout
# =====================
app.layout = dbc.Container(
    fluid=True,
    children=[
        dbc.Row(
            dbc.Col(
                html.H2(
                    "💜 GenBot – Génération IA",
                    className="text-center my-4",
                    style={"color": "#5a2d82"},
                )
            )
        ),
        dbc.Row(
            dbc.Col(
                html.Div(
                    id="chat-window",
                    style=CHAT_CONTAINER_STYLE,
                )
            )
        ),
        dbc.Row(
            [
                dbc.Col(
                    dcc.Input(
                        id="user-input",
                        type="text",
                        placeholder="Posez votre question à Génération IA...",
                        className="form-control",
                    ),
                    width=10,
                ),
                dbc.Col(
                    dbc.Button(
                        "Envoyer",
                        id="send-button",
                        color="primary",
                        className="w-100",
                    ),
                    width=2,
                ),
            ],
            className="mt-3",
        ),
    ],
)


# =====================
# Callback
# =====================
@app.callback(
    Output("chat-window", "children"),
    Input("send-button", "n_clicks"),
    State("user-input", "value"),
    State("chat-window", "children"),
    prevent_initial_call=True,
)
def update_chat(n_clicks, user_input, chat_history):
    if not user_input:
        return chat_history

    if chat_history is None:
        chat_history = []

    # User message
    chat_history.append(
        html.Div(
            user_input,
            style=USER_BUBBLE,
            className="mb-2",
        )
    )

    messages.append({"role": "user", "content": user_input})

    response = client.chat.complete(
        model=MODEL,
        messages=messages,
    )

    bot_reply = response.choices[0].message.content
    messages.append({"role": "assistant", "content": bot_reply})

    # Bot message
    chat_history.append(
        html.Div(
            bot_reply,
            style=BOT_BUBBLE,
            className="mb-3",
        )
    )

    return chat_history


# =====================
# Run server
# =====================
if __name__ == "__main__":
    app.run(debug=True)
