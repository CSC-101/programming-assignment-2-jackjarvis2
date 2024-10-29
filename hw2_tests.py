
import unittest
from data import Point, Song, Duration
from hw2 import create_rectangle, shorter_duration_than,song_shorter_than,  running_time, validate_route, longest_repetition

# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_create_rectangle1(self):
        p1 = Point(2, 2)
        p2 = Point(10, 10)
        result = create_rectangle(p1, p2)
        self.assertEqual(result.top_left, Point(2, 10))
        self.assertEqual(result.bottom_right, Point(10, 2))

    def test_create_rectangle2(self):
        p1 = Point(10, 10)
        p2 = Point(2, 2)
        result = create_rectangle(p1, p2)
        self.assertEqual(result.top_left, Point(2, 10))
        self.assertEqual(result.bottom_right, Point(10, 2))

    # Part 2
    def test_shorter_duration1(self):
        d1 = Duration(2, 30)
        d2 = Duration(3, 0)
        self.assertTrue(shorter_duration_than(d1, d2))

    def test_shorter_duration2(self):
        d1 = Duration(3, 0)
        d2 = Duration(2, 30)
        self.assertFalse(shorter_duration_than(d1, d2))

    # Part 3
    def setUp(self):
        self.songs = [
            Song("Artist A", "Song A", Duration(3, 30)),
            Song("Artist B", "Song B", Duration(4, 15)),
            Song("Artist C", "Song C", Duration(2, 45)),
            Song("Artist D", "Song D", Duration(5, 0))
        ]

    def test_song_shorter_than(self):
        max_duration = Duration(4, 0)
        expected = [
            Song("Artist A", "Song A", Duration(3, 30)),
            Song("Artist C", "Song C", Duration(2, 45))
        ]
        result = song_shorter_than(self.songs, max_duration)
        self.assertEqual(result, expected)

    def test_all_songs_shorter_than(self):
        max_duration = Duration(6, 0)
        expected = self.songs
        result = song_shorter_than(self.songs, max_duration)
        self.assertEqual(result, expected)
    # Part 4
    def setUp(self):
        self.songs = [
            Song("Artist A", "Song A", Duration(3, 30)),
            Song("Artist B", "Song B", Duration(4, 15)),
            Song("Artist C", "Song C", Duration(2, 45))
        ]

    def test_running_time(self):
        playlist = [0, 1]
        expected = Duration(7, 45)
        result = running_time(self.songs, playlist)
        self.assertEqual(result, expected)

    def test_empty_playlist(self):
        playlist = []
        expected = Duration(0, 0)
        result = running_time(self.songs, playlist)
        self.assertEqual(result, expected)

    # Part 5
    def test_validate_route(self):
        city_links = [
            ['A', 'B'],
            ['B', 'C'],
            ['C', 'D']
        ]
        route = ['A', 'B', 'C']
        self.assertTrue(validate_route(city_links, route))

    def test_invalid_route(self):
        city_links = [
            ['A', 'B'],
            ['B', 'C']
        ]
        route = ['A', 'C']
        self.assertFalse(validate_route(city_links, route))

    # Part 6
    def test_longest_repetition(self):
        nums = [1, 1, 2, 2, 1, 1, 1, 3]
        result = longest_repetition(nums)
        self.assertEqual(result, 4)

    def test_empty_list(self):
        nums = []
        result = longest_repetition(nums)
        self.assertIsNone(result)




if __name__ == '__main__':
    unittest.main()
