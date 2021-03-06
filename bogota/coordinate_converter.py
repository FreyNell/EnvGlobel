
import math as m

LATITUDE_CENTER = 4.6528093
LONGITUDE_CENTER = -74.0863529
IMAGE_HEIGHT = 2000
IMAGE_WIDTH = 2000
PIXELS_PER_DEGREE = 5830


def convertToPixels(latitude, longitude):
    y = (LATITUDE_CENTER - latitude) * PIXELS_PER_DEGREE + IMAGE_HEIGHT/2
    x = (longitude - LONGITUDE_CENTER) * PIXELS_PER_DEGREE + IMAGE_WIDTH/2
    return round(y), round(x)
