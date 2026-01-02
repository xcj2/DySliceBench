#!/usr/bin/env python
# -*- coding: utf-8 -*-

POSITIONS = ["top", "south", "east", "west", "north", "bottom"]


class Dice(object):

    def __init__(self, initial_faces):
        self.faces = {p: initial_faces[i] for i, p in enumerate(POSITIONS)}
        self.store_previous_faces()

    def store_previous_faces(self):
        self.previous_faces = self.faces.copy()

    def change_face(self, after, before):
        self.faces[after] = self.previous_faces[before]

    def change_faces(self, rotation):
        self.change_face(rotation[0], rotation[1])
        self.change_face(rotation[1], rotation[2])
        self.change_face(rotation[2], rotation[3])
        self.change_face(rotation[3], rotation[0])

    def roll(self, direction):
        self.store_previous_faces()
        if direction == "E":
            self.change_faces(["top", "west", "bottom", "east"])
        elif direction == "N":
            self.change_faces(["top", "south", "bottom", "north"])
        elif direction == "S":
            self.change_faces(["top", "north", "bottom", "south"])
        elif direction == "W":
            self.change_faces(["top", "east", "bottom", "west"])

    def rolls(self, directions):
        for d in directions:
            self.roll(d)

    def show_top(self):
        return self.faces["top"]


def main():
    dice = Dice(input().split())
    dice.rolls(input())
    print(dice.show_top())

if __name__ == "__main__":
    main()