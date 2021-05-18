#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 18 17:32:39 2021

@author: Bea Jimenez <bea.jimenez@alumni.ie.edu>
"""

"""
Rock, Paper, Scissors
=====================

At each turn, the player is asked to pick either Rock, Paper, or Scissors.
The program also randomly picks one of these options.
When both the player and the computer pick the same choice, there is no winner.
If they pick different choices, the winner is based on the following:

Scissors win over Paper
Paper wins over Rock
Rock wins over Scissors

"""

import random

picks = ("rock", "paper", "scissors")

comp_pick = random.choice(picks)
human_pick = input("pick one of rock, paper, scissors. Press q to quit\n").lower()

scores = {"comp": 0, "human": 0}

while human_pick != "q":
    if comp_pick == human_pick:
        print("Deuce. Status:", scores)
    else:
        if comp_pick == "rock":
            if human_pick == "scissors":
                scores["comp"] = scores["comp"] + 1
                print("Computer wins. Status:", scores)
            else:
                scores["human"] = scores["human"] + 1
                print("Human wins. Status:", scores)
        elif comp_pick == "paper":
            if human_pick == "scissors":
                scores["human"] = scores["human"] + 1
                print("Human wins. Status:", scores)
            else:
                scores["comp"] = scores["comp"] + 1
                print("Computer wins. Status:", scores)
        else:
            if human_pick == "rock":
                scores["human"] = scores["human"] + 1
                print("Human wins. Status:", scores)
            else:
                scores["comp"] = scores["comp"] + 1
                print("Computer wins. Status:", scores)

    comp_pick = random.choice(picks)
    human_pick = input("pick one of rock, paper, scissors. Press q to quit\n").lower()

print("Thanks for playing. Final score:", scores)
