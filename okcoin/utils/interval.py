from enum import Enum


class Interval(Enum):
    S1 = "1s"
    M1 = "60s"
    M3 = "180s"
    M5 = "300s"
    M15 = "900s"
    M30 = "1800s"
    H1 = "3600s"
    H2 = "7200s"
    H4 = "14400s"
    H6 = "21600s"
    H12 = "43200s"
    D1 = "86400s"
    W1 = "604800s"
