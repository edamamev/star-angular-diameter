import math

# Angular Diameter Functions
## The following functions assume the star_distance is much
## greater than the star_diameter. This often occurs in space
## cos space is big
def angular_diameter_degrees(star_diameter, star_distance):
    """
    Returns the Star's Angular Diameter in Degrees.
    Both the Stars Diameter and Distance must be in the same unit.
    """
    return get_degrees_from_radians(star_diameter / star_distance)
    pass


def angular_diameter_radians(star_diameter, star_distance):
    """
    Returns the Star's Angular Diameter in Radians.
    Both the Stars Diameter and Distance must be in the same unit.
    """
    return star_diameter / star_distance


def angular_diameter_arc_minutes(star_diameter, star_distance):
    """
    Returns the Star's Angular Diameter in Arc Minutes.
    Both the Stars Diameter and Distance must be in the same unit.
    """
    return get_arc_minutes_from_radians(star_diameter / star_distance)


def angular_diameter_arc_seconds(star_diameter, star_distance):
    """
    Returns the Star's Angular Diameter in Arc Seconds.
    Both the Stars Diameter and Distance must be in the same unit.
    """
    return get_arc_seconds_from_radians(star_diameter / star_distance)


def angular_diameter_milliarc_seconds(star_diameter, star_distance):
    """
    Returns the Star's Angular Diameter in Milliarc Seconds.
    Both the Stars Diameter and Distance must be in the same unit.
    """
    return get_milliarc_seconds_from_radians(star_diameter / star_distance)


## The below function doesn't assume the star_distance is much
## greater than the star_diameter.

def angular_diameter_radians_object(object_diameter, object_distance):
    """
    Returns the Object's Angular Diameter in Radians.
    Both the Object's Diameter and Distance must be in the same unit.
    """
    return 2 * math.atan(object_diameter / object_distance)


def angular_diameter_degrees_object(object_diameter, object_distance):
    """
    Returns the Object's Angular Diameter in Degrees.
    Both the Object's Diameter and Distance must be in the same unit.
    """
    return get_degrees_from_radians(\
        angular_diameter_radians_object(object_diameter, object_distance)\
    )


def angular_diameter_arc_minutes_object(object_diameter, object_distance):
    """
    Returns the Object's Angular Diameter in Arc Minutes.
    Both the Object's Diameter and Distance must be in the same unit.
    """
    return get_arc_minutes_from_radians(\
        angular_diameter_radians_object(object_diameter, object_distance)\
    )


def angular_diameter_arc_seconds_object(object_diameter, object_distance):
    """
    Returns the Object's Angular Diameter in Arc Seconds.
    Both the Object's Diameter and Distance must be in the same unit.
    """
    return get_arc_seconds_from_radians(\
        angular_diameter_radians_object(object_diameter, object_distance)\
    )


def angular_diameter_milliarc_seconds_object(object_diameter, object_distance):
    """
    Returns the Object's Angular Diameter in Milliarc Seconds.
    Both the Object's Diameter and Distance must be in the same unit.
    """
    return get_milliarc_seconds_from_radians(\
        angular_diameter_radians_object(object_diameter, object_distance)\
    )


# Unit Conversion Functions

def get_arc_minutes_from_radians(radians: float):
    """
    Converts Radians into Arc Minutes.
    """
    return radians * math.pi / 10800


def get_arc_minutes_from_degrees(degrees: float):
    """
    Converts Degrees into Arc Minutes.
    """
    return degrees * 60


def get_arc_seconds_from_radians(radians: float):
    """
    Conerts Radians to Arc Seconds.
    """
    return radians * (math.pi / 648000)


def get_arc_seconds_from_degrees(degrees: float):
    """
    Converts Degrees to Arc Seconds.
    """
    return get_arc_minutes_from_degrees(degrees) * 60


def get_milliarc_seconds_from_arc_seconds(arcseconds: float):
    """
    Converts Arc Seconds to Milliarc Seconds
    """
    return arcseconds * 1000


def get_milliarc_seconds_from_radians(radians: float):
    """
    Converts Radians to Milliarc Seconds
    """
    return get_arc_seconds_from_radians(radians) * 1000


def get_radians_from_degrees(degrees: float):
    """
    Converts Degrees to Radians
    """
    return degrees * (math.pi / 180)


def get_degrees_from_radians(radians: float):
    """
    Converts Radians to Degrees
    """
    return radians * (180 / math.pi)
