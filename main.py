from game import Game

if __name__ == "__main__":
    game = Game()

    while True:
        if game.home_page:
            game.display_home_page()
        elif game.game_page:
            game.display_game_page()
        elif game.final_page:
            game.display_final_page()
        else:
            break
