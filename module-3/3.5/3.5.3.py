from typing import Union, List


class TrackLine:

    def __init__(self, to_x: Union[int, float], to_y: Union[int, float], max_speed: int = 0):
        self.to_x = to_x
        self.to_y = to_y
        self.max_speed = max_speed


class Track:

    def __init__(self, start_x: Union[int, float] = 0, start_y: Union[int, float] = 0):
        self.start_x = start_x
        self.start_y = start_y
        self._tracks: List[TrackLine] = []

    def add_track(self, tr: TrackLine):
        self._tracks.append(tr)

    def get_tracks(self):
        return tuple(self._tracks)

    def __eq__(self, other: 'Track'):
        return True if self.get_length() == other.get_length() else False

    def __gt__(self, other: 'Track'):
        return True if self.get_length() > other.get_length() else False

    @staticmethod
    def get_dist(line_1: TrackLine, line_2: TrackLine):
        return ((line_2.to_x - line_1.to_x) ** 2 + (line_2.to_y - line_1.to_y) ** 2) ** 0.5

    def get_length(self):
        prev_track_line = TrackLine(self.start_x, self.start_y)

        result_dist = 0
        for track_line in self._tracks:
            result_dist += self.get_dist(prev_track_line, track_line)
            prev_track_line = track_line

        return result_dist

    def __len__(self):
        return int(self.get_length())


track1, track2 = Track(), Track(0, 1)
track1.add_track(TrackLine(2, 4, 100))
track1.add_track(TrackLine(5, -4, 100))
track2.add_track(TrackLine(3, 2, 90))
track2.add_track(TrackLine(10, 8, 90))
res_eq = track1 == track2
print(res_eq)
