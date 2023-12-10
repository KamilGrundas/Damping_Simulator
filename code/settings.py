from pygame.math import Vector2

# screen
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SIDE_MENU_WIDTH = 300
TILE_SIZE = 64

# graphics
PLAY_BUTTON = "graphics/buttons/play_button.png"
PAUSE_BUTTON = "graphics/buttons/pause_button.png"
REPLAY_BUTTON = "graphics/buttons/replay_button.png"

SILENCER_1 = "graphics/silencer.png"
SILENCER_2 = "graphics/silencer_2.png"

# Screen scale attributes
A = 0.007017543859649123
B = -3.052631578947368

C = (SCREEN_HEIGHT - 150) / 4
D = 150 - C * 150

# Language
TIME = "Czas"
START_POSITION = "Pozycja początkowa"
SPEED = "Prędkość"
SUPPRESION_LEVEL = "Tłumienie"
ELASTICITY_COEFFICIENT = "Wsp. sprężystości"
MASS = "Masa"


# sliders
SLIDER_POSITIONS = (
    (1100, 300),
    (1100, 370),
    (1100, 440),
    (1100, 510),
    (1100, 580),
    (1100, 650),
)
SLIDER_MAX = 1250
SLIDER_MIN = 1010

# overlay positions
OVERLAY_POSITIONS = {"tool": (40, SCREEN_HEIGHT - 15), "seed": (70, SCREEN_HEIGHT - 5)}

PLAYER_TOOL_OFFSET = {
    "left": Vector2(-50, 40),
    "right": Vector2(50, 40),
    "up": Vector2(0, -10),
    "down": Vector2(0, 50),
}

LAYERS = {
    "water": 0,
    "ground": 1,
    "soil": 2,
    "soil water": 3,
    "rain floor": 4,
    "house bottom": 5,
    "ground plant": 6,
    "main": 7,
    "house top": 8,
    "fruit": 9,
    "rain drops": 10,
}

APPLE_POS = {
    "Small": [(18, 17), (30, 37), (12, 50), (30, 45), (20, 30), (30, 10)],
    "Large": [(30, 24), (60, 65), (50, 50), (16, 40), (45, 50), (42, 70)],
}

GROW_SPEED = {"corn": 1, "tomato": 0.7}

SALE_PRICES = {"wood": 4, "apple": 2, "corn": 10, "tomato": 20}
PURCHASE_PRICES = {"corn": 4, "tomato": 5}
