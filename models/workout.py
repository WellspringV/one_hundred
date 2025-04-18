from dataclasses import dataclass


@dataclass
class Workout:
    pull_ups: int
    squats_first: int
    push_ups: int
    squats_second: int
