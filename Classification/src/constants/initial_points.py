from .point_types import PointTypes

INITIAL_RED_POINTS = (
    PointTypes.RED,
    [
        (-4500, -4400),
        (-4100, -3000),
        (-1800, -2400),
        (-2500, -3400),
        (-2000, -1400)
    ]
)

INITIAL_GREEN_POINTS = (
    PointTypes.GREEN,
    [
        (+4500, -4400),
        (+4100, -3000),
        (+1800, -2400),
        (+2500, -3400),
        (+2000, -1400)
    ]
)

INITIAL_BLUE_POINTS = (
    PointTypes.BLUE,
    [
        (-4500, +4400),
        (-4100, +3000),
        (-1800, +2400),
        (-2500, +3400),
        (-2000, +1400)
    ]
)

INITIAL_PURPLE_POINTS = (
    PointTypes.PURPLE,
    [
        (+4500, +4400),
        (+4100, +3000),
        (+1800, +2400),
        (+2500, +3400),
        (+2000, +1400)
    ]
)

def all_initial_points() -> list:
    return [
        INITIAL_RED_POINTS, 
        INITIAL_BLUE_POINTS, 
        INITIAL_GREEN_POINTS, 
        INITIAL_PURPLE_POINTS
    ]