import data
from typing import List, Optional
from data import Point, Rectangle, Song, Duration
# Write your functions for each part in the space below.

# Part 1
def create_rectangle(p1: Point, p2: Point) -> Rectangle:
    """Create a rectangle from two points.

    Purpose:
        To create a rectangle based on two given points, identifying the top-left and bottom-right corners.

    Input:
        p1 (Point): First corner point.
        p2 (Point): Second corner point.

    Output:
        Rectangle: A rectangle defined by the top-left and bottom-right points.
    """
    top_left_x = min(p1.x, p2.x)
    top_left_y = max(p1.y, p2.y)
    bottom_right_x = max(p1.x, p2.x)
    bottom_right_y = min(p1.y, p2.y)
    return Rectangle(Point(top_left_x, top_left_y), Point(bottom_right_x, bottom_right_y))

#part 2
def shorter_duration_than(d1: Duration, d2: Duration) -> bool:
    """Check if the first duration is shorter than the second.

    Purpose:
        To compare two durations to determine if the first is shorter than the second.

    Input:
        d1 (Duration): First duration.
        d2 (Duration): Second duration.

    Output:
        bool: True if d1 is shorter than d2, False otherwise.
    """
    if d1.minutes < d2.minutes:
        return True
    elif d1.minutes == d2.minutes:
        return d1.seconds < d2.seconds
    else:
        return False


#part 3
def song_shorter_than(songs: List[Song], max_duration: Duration) -> List[Song]:
    """
    Purpose:
    Filter a list of songs to return only those that are shorter than a given maximum duration.

    Input:
    - songs: A list of Song objects, each containing an artist, title, and Duration.
    - max_duration: A Duration object representing the upper bound on the length of songs to be included.

    Output:
    - A list of Song objects from the input list where each song's duration is less than max_duration.

    Representation:
    - Song: Represents a song with an artist name (str), title (str), and duration (Duration).
    - Duration: Represents a duration with minutes (int) and seconds (int), where duration comparison
      is done by first comparing minutes, then seconds.
    """
    return [song for song in songs if song.duration < max_duration]

#part 4
def running_time(songs: List[Song], playlist: List[int]) -> Duration:
    """Calculate the total running time of a playlist.

    Purpose:
        To calculate the total duration of a playlist specified by a list of song indices.

    Input:
        songs (List[Song]): List of songs.
        playlist (List[int]): List of song indices.

    Output:
        Duration: Total duration of the playlist.
    """
    total_minutes = 0
    total_seconds = 0
    for index in playlist:
        if 0 <= index < len(songs):
            total_minutes += songs[index].duration.minutes
            total_seconds += songs[index].duration.seconds
    total_minutes += total_seconds // 60
    total_seconds = total_seconds % 60

    return Duration(total_minutes, total_seconds)


#part5
def validate_route(city_links: List[List[str]], route: List[str]) -> bool:
    """Validate a travel route based on city links.

    Purpose:
        To determine if a specified route between cities is valid based on available links.

    Input:
        city_links (List[List[str]]): Links between cities.
        route (List[str]): A list of cities representing the route.

    Output:
        bool: True if the route is valid, False otherwise.
    """
    if len(route) <= 1:
        return True

    for i in range(len(route) - 1):
        if [route[i], route[i + 1]] not in city_links and [route[i + 1], route[i]] not in city_links:
            return False

    return True

# part 6
def longest_repetition(nums: List[int]) -> Optional[int]:
    """Find the starting index of the longest contiguous repetition of a number.

    Purpose:
        To identify the index at which the longest contiguous repetition of a single number starts.

    Input:
        nums (List[int]): A list of integers.

    Output:
        Optional[int]: Starting index of the longest repetition or None if empty.
    """
    if not nums:
        return None

    max_length = 1
    current_length = 1
    start_index = 0
    max_start_index = 0

    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            current_length += 1
        else:
            if current_length > max_length:
                max_length = current_length
                max_start_index = start_index
            current_length = 1
            start_index = i

    if current_length > max_length:
        max_start_index = start_index

    return max_start_index

