import cv2 as cv
import numpy as np

def drawInfos(frame, markerCorner, markerId):
    corners = markerCorner.reshape((4, 2))
    (topLeft, topRight, botRight, botLeft) = corners
    
    # convert each of the (x, y) pairs to int
    topRight = (int(topRight[0]), int(topRight[1]))
    topLeft = (int(topLeft[0]), int(topLeft[1]))
    botRight = (int(botRight[0]), int(botRight[1]))
    botLeft = (int(botLeft[0]), int(botLeft[1]))
    
    # draw axes (z missing as of now)
    axisX = np.subtract(botRight, botLeft)
    axisY = np.subtract(topLeft, botLeft)
    
    cv.arrowedLine(frame,
        botLeft,
        np.add(botLeft, axisY),
        (255, 175, 5),
        3
    )
    cv.arrowedLine(frame,
        botLeft,
        np.add(botLeft, axisX),
        (100, 5, 255),
        3
    )
    
    # draw marker IDs
    cv.putText(frame, str(markerId),
        (topLeft[0], topLeft[1] - 15),
        cv.FONT_HERSHEY_SIMPLEX,
        1.25, (0, 0, 255), 3
    )
    
    return frame