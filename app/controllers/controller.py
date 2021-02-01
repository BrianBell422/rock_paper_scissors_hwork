from flask import render_template, request, redirect
from app import app
from app.models.games import Game
from app.models.players import Player


# @app.route("/welcome")
# def index():
#     return 'Welcome to Rock, Paper, Scissors: The Browser Game'


# @app.route("/<choice1>/<choice2>")
# def rps(choice1, choice2):
#     player_1 = Player("James", choice1)
#     player_2 = Player("Andrew", choice2)
#     game = Game()
#     winner = game.play(player_1, player_2)
#     if winner:
#      return f"The Winner is {winner.name} with {winner.choice} "
#     else:
#         return "None"


@app.route("/")
def welcome():
    return render_template("welcome.html", title="Welcome")

@app.route("/play")
def index():
    return render_template("index.html", title="Play the Game")

@app.route("/play", methods=["POST"])
def rps():
    player_1_name = request.form["player_1_name"]
    player_2_name = request.form["player_2_name"]
    player_1_choice = request.form["choice_1"]
    player_2_choice = request.form["choice_2"]
    player_1 = Player(player_1_name, player_1_choice)
    player_2 = Player(player_2_name, player_2_choice)
    game = Game()
    winner = game.play(player_1, player_2)
    if winner:
        return render_template("index.html", title="Play the Game", result=f"The Winner is {winner.name} with {winner.choice} ")
    else:
        return render_template("index.html", title="Play the Game", result="Draw")