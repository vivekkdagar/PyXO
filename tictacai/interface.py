#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import click

from .game import Game


@click.group()
def tictactoe():
    pass


@tictactoe.command()
def human():
    game = Game()
    game.symbols()
    game.play_game('h')


@tictactoe.command()
def ai():
    game = Game()
    game.symbols()
    game.play_game('c')


@tictactoe.command()
def scores():
    Game().score_card.display_statistics()


if __name__ == '__main__':
    tictactoe()
