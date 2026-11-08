"""
All Pygame drawing and rendering functions.
Surfaces and fonts are passed as parameters — no globals imported.
================================================================================
YOUR NAME  : ___________________________
STUDENT ID : ___________________________
================================================================================
Implement drawWorm() and drawApple() below (Tasks 8 and 9).
All other functions are provided — do NOT modify them.

All drawing functions receive DISPLAYSURF and BASICFONT as parameters.
Do NOT import or use global variables from wormy.py.
================================================================================
"""

import pygame
from constants import (
    CELLSIZE, WINDOWWIDTH, WINDOWHEIGHT,
    WHITE, BLACK, RED, APPLE_SHINE, LEAF_GREEN,
    GREEN, DARKGREEN, HEADGREEN, DARKGRAY,
    UP, DOWN, LEFT, RIGHT, HEAD,
)


# ─────────────────────────────────────────────────────────────────────────────
# TASK 8 — drawWorm()                                                 [15 pts]
# ─────────────────────────────────────────────────────────────────────────────
def drawWorm(DISPLAYSURF, wormCoords, direction=RIGHT):
    """
    Draw the worm on DISPLAYSURF.

    Each segment occupies one grid cell (CELLSIZE x CELLSIZE pixels).
    The pixel top-left corner of cell (col, row) is:
        px = col * CELLSIZE
        py = row * CELLSIZE

    MINIMUM requirement for full credit:
        - Each segment: dark-green outer rectangle + green inner rectangle.
          Suggested sizes:
            outer rect: (px+1, py+1, CELLSIZE-2, CELLSIZE-2)
            inner rect: (px+4, py+4, CELLSIZE-8, CELLSIZE-8)

    BONUS (+5 extra credit):
        - Rounded corners: use border_radius in pygame.draw.rect()
        - Head brighter than body (use HEADGREEN for segment at index HEAD)
        - Two eyes on the head with pupils facing the direction of travel

    Args:
        DISPLAYSURF  : Active pygame display surface.
        wormCoords (list): Current worm segments; index 0 is the head.
        direction  (str):  Current movement direction (for eye orientation).
    """
    for index, coord in enumerate(wormCoords):
        px = coord['x'] * CELLSIZE
        py = coord['y'] * CELLSIZE

        outer_rect = pygame.Rect(px + 1, py + 1, CELLSIZE - 2, CELLSIZE - 2)
        inner_rect = pygame.Rect(px + 4, py + 4, CELLSIZE - 8, CELLSIZE - 8)

        if index == HEAD:
            # Head rendering with HEADGREEN and rounded corners
            pygame.draw.rect(DISPLAYSURF, DARKGREEN, outer_rect, border_radius=6)
            pygame.draw.rect(DISPLAYSURF, HEADGREEN, inner_rect, border_radius=4)

            # Directional eyes
            eye_radius = 3
            pupil_radius = 1

            if direction == UP:
                eye1 = (px + 6, py + 6)
                eye2 = (px + CELLSIZE - 7, py + 6)
                pupil1 = (px + 6, py + 5)
                pupil2 = (px + CELLSIZE - 7, py + 5)
            elif direction == DOWN:
                eye1 = (px + 6, py + CELLSIZE - 7)
                eye2 = (px + CELLSIZE - 7, py + CELLSIZE - 7)
                pupil1 = (px + 6, py + CELLSIZE - 6)
                pupil2 = (px + CELLSIZE - 7, py + CELLSIZE - 6)
            elif direction == LEFT:
                eye1 = (px + 6, py + 6)
                eye2 = (px + 6, py + CELLSIZE - 7)
                pupil1 = (px + 5, py + 6)
                pupil2 = (px + 5, py + CELLSIZE - 7)
            else:  # RIGHT
                eye1 = (px + CELLSIZE - 7, py + 6)
                eye2 = (px + CELLSIZE - 7, py + CELLSIZE - 7)
                pupil1 = (px + CELLSIZE - 6, py + 6)
                pupil2 = (px + CELLSIZE - 6, py + CELLSIZE - 7)

            # Draw whites of eyes
            pygame.draw.circle(DISPLAYSURF, WHITE, eye1, eye_radius)
            pygame.draw.circle(DISPLAYSURF, WHITE, eye2, eye_radius)
            # Draw pupils
            pygame.draw.circle(DISPLAYSURF, BLACK, pupil1, pupil_radius)
            pygame.draw.circle(DISPLAYSURF, BLACK, pupil2, pupil_radius)
        else:
            # Body segments
            pygame.draw.rect(DISPLAYSURF, DARKGREEN, outer_rect, border_radius=4)
            pygame.draw.rect(DISPLAYSURF, GREEN, inner_rect, border_radius=3)


# ─────────────────────────────────────────────────────────────────────────────
# TASK 9 — drawApple()                                                [15 pts]
# ─────────────────────────────────────────────────────────────────────────────
def drawApple(DISPLAYSURF, coord):
    """
    Draw the apple on DISPLAYSURF at the given grid coordinate.

    The pixel top-left corner of cell (col, row) is:
        px = coord['x'] * CELLSIZE
        py = coord['y'] * CELLSIZE

    MINIMUM requirement for full credit:
        - A filled RED rectangle covering the cell:
            pygame.draw.rect(DISPLAYSURF, RED, pygame.Rect(px, py, CELLSIZE, CELLSIZE))

    BONUS (+5 extra credit):
        - Circular apple body using pygame.draw.circle()
        - Darker lower ellipse for depth shading
        - Small LEAF_GREEN rectangle at the top as a stem/leaf
        - Small APPLE_SHINE circle for a specular highlight

    Args:
        DISPLAYSURF  : Active pygame display surface.
        coord (dict): {'x': int, 'y': int} grid position of the apple.
    """
    # TODO: implement this function
    pass


# ─────────────────────────────────────────────────────────────────────────────
# PROVIDED functions — Do NOT modify anything below this line.
# ─────────────────────────────────────────────────────────────────────────────

def drawGrid(DISPLAYSURF):
    """Draw subtle dark-gray grid lines across the entire window."""
    for x in range(0, WINDOWWIDTH, CELLSIZE):
        pygame.draw.line(DISPLAYSURF, DARKGRAY, (x, 0), (x, WINDOWHEIGHT))
    for y in range(0, WINDOWHEIGHT, CELLSIZE):
        pygame.draw.line(DISPLAYSURF, DARKGRAY, (0, y), (WINDOWWIDTH, y))


def drawScore(DISPLAYSURF, BASICFONT, score):
    """Render the current score in the top-right corner."""
    surf = BASICFONT.render('Score: %s' % score, True, WHITE)
    rect = surf.get_rect()
    rect.topleft = (WINDOWWIDTH - 120, 10)
    DISPLAYSURF.blit(surf, rect)


def drawPressKeyMsg(DISPLAYSURF, BASICFONT):
    """Render a 'Press a key to play.' hint in the bottom-right corner."""
    surf = BASICFONT.render('Press a key to play.', True, DARKGRAY)
    rect = surf.get_rect()
    rect.topleft = (WINDOWWIDTH - 200, WINDOWHEIGHT - 30)
    DISPLAYSURF.blit(surf, rect)
