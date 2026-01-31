class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def minMeetingRooms(self, intervals: list[Interval]) -> int:
        if not intervals:
            return 0

        events = []
        for interval in intervals:
            events.append((interval.start, 1))
            events.append((interval.end, -1))

        events.sort(key=lambda x: (x[0], x[1]))

        max_rooms = 0
        current_rooms = 0
        for _, delta in events:
            current_rooms += delta
            max_rooms = max(max_rooms, current_rooms)

        return max_rooms
