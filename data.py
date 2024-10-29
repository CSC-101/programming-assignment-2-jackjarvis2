import math
from typing import List


# Representation of a two-dimensional point.
class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return 'Point({}, {})'.format(self.x, self.y)

    def __eq__(self, other) -> bool:
        return (other is self or
                type(other) == Point and
                math.isclose(self.x, other.x) and
                math.isclose(self.y, other.y))


# Representation of a duration as minutes and seconds.
class Duration:
    def __init__(self, minutes: int, seconds: int):
        self.minutes = minutes
        self.seconds = seconds

    def __repr__(self) -> str:
        return 'Duration({}, {})'.format(self.minutes, self.seconds)

    def __eq__(self, other) -> bool:
        return (other is self or
                type(other) == Duration and
                self.minutes == other.minutes and
                self.seconds == other.seconds)

    def __lt__(self, other):
        return (self.minutes, self.seconds) < (other.minutes, other.seconds)


# Representation of a song.
class Song:
    def __init__(self, artist: str, title: str, duration: Duration):
        self.artist = artist
        self.title = title
        self.duration = duration

    def __repr__(self):
        return "Song('{}', '{}', {})".format(self.artist, self.title, self.duration)

    def __eq__(self, other):
        return (self is other or
                type(other) == Song and
                self.artist == other.artist and
                self.title == other.title and
                self.duration == other.duration)


# Representation of an axis-aligned rectangle.
class Rectangle:
    def __init__(self, top_left: Point, bottom_right: Point):
        self.top_left = top_left
        self.bottom_right = bottom_right

    def __repr__(self) -> str:
        return 'Rectangle({}, {})'.format(self.top_left, self.bottom_right)

    def __eq__(self, other) -> bool:
        return (other is self or
                type(other) == Rectangle and
                self.top_left == other.top_left and
                self.bottom_right == other.bottom_right)
