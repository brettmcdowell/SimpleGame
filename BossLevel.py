import sys
import pygame
from player import Human_Player
from screen import Screen
from game import BossGame
from main import play_game


if __name__ == "__main__":
    pygame.init()

    screen = Screen(width=800, height=800)
    player = Human_Player(screen.width/2, screen.height-100)
    game = BossGame()
    play_game(screen, player, game)
