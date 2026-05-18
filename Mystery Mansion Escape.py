import flet as ft
import random

def main(page: ft.Page):
    page.title = "Mystery Mansion Escape"
    page.window.width = 1000
    page.window.height = 700
    page.bgcolor = "#8b80dc"

    rooms = [
        "Library",
        "Kitchen",
        "Basement",
        "Ballroom",
        "Garden",
    ]

    players = ["Player 1", "Player 2"]

    player_position = {
        "Player 1": 0,
        "Player 2": 0
    }

    current_player = 0

    criminals = ["Butler", "Chef", "Garderner"]
    weapons = ["Knife", "Poison", "Candlestick"]
    mystery = {
        "criminal": random.choice(criminals),
        "weapon": random.choice(weapons),
        "room": random.choice(rooms)
    }

    title = ft.Text(
        "Mystery Mansion Escape",
        size = 34,
        weight = "bold"
    )

    game_log = ft.Text(
        value = "Press Start Game",
        size = 20,
        color = "darkblue"
    )

    turn_text = ft.Text(
        value = f"Current Turn: {players[current_player]}",
        size = 20,
    )

    room_text = ft.Text(
        value = "Current Room: Library",
        size = 20
    )

    dice_text = ft.Text(
        value = "Dice Roll:", 
        size = 20
    )

    def start_game(e):
        game_log.value = "Game Started"
        update_display()

    def roll_dice():
        return random.randint(1, 6)
    
    def move_player(steps):
        player = players[current_player]
        player_position[player] += steps
        player_position[player] = (
            player_position[player] % len(rooms)
        )
      

    def switch_turn():
        nonlocal current_player

        if current_player == 0:
            current_player = 1
        else: 
            current_player = 0

    def check_win():
        player = players[current_player]
        current_room = rooms[player_position[player]]

        if current_room == mystery["room"]:
            game_log.value = (
                f"{player} discovered an important clue in the "
                f"{current_room}"
            )
    def update_display():
        player = players[current_player]
        current_room = rooms[player_position[player]]
        turn_text.value = f"Current Turn: {player}"
        room_text.value = f"{player} is in {current_room}"
        page.update
    
    def roll_button_click(e):

        try:
            player = players[current_player]
            dice = roll_dice()
            dice_text.value = f"Dice Roll: {dice}"
            move_player(dice)
            current_room = rooms[player_position[player]]
            game_log.value = (
                f"{player} rolled a {dice}"
                f" and moved to the {current_room}"
            )
            check_win()
            switch_turn()
            update_display()

        except Exception as error:
            game_log.value = f"Error: {error}"
            page.update()

    start_button = ft.ElevatedButton(
        "Start Game",
        on_click = start_game,
        width = 200
    )

    roll_button = ft.ElevatedButton(

        "Roll Dice",
        on_click = roll_button_click,
        width = 200
    )

    page.add(
        ft.Column(
            controls = [
                title,
                turn_text,
                room_text,
                dice_text,
                ft.Row(
                    controls = [
                        start_button,
                        roll_button
                    ],
                    alignment = ft.MainAxisAlignment.CENTER
                ),
                game_log
            ],
            spacing = 19,
            horizontal_alignment = ft.CrossAxisAlignment.CENTER
        )
    )
ft.run(main)


