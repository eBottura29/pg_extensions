import pygame, time, math, random

pygame.init()


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        output = func(*args, **kwargs)
        end = time.time()
        print(f"Function {func.__name__} took {(end - start) * 1000:.2f} ms to execute.")
        return output

    return wrapper


def clamp(value, min_value, max_value):
    return max(min_value, min(value, max_value))


def lerp(start, end, t):
    return start + t * (end - start)


def map_value(value, start1, stop1, start2, stop2):
    return start2 + (stop2 - start2) * ((value - start1) / (stop1 - start1))


def draw_circle(surface, color, position, radius, width=0):
    pygame.draw.circle(surface, color.tup(), (int(position.x) + window.WIDTH // 2, -int(position.y) + window.HEIGHT // 2), radius, width)


def draw_rectangle(surface, color, position, size, width=0):
    pygame.draw.rect(surface, color.tup(), pygame.Rect(position.x + window.WIDTH // 2, -position.y + window.HEIGHT // 2, size.x, size.y), width)


def draw_line(surface, color, start_pos, end_pos, width=1):
    pygame.draw.line(
        surface,
        color.tup(),
        (int(start_pos.x + window.WIDTH // 2), int(-start_pos.y + window.HEIGHT // 2)),
        (int(end_pos.x + window.WIDTH // 2), int(-end_pos.y + window.HEIGHT // 2)),
        width,
    )

def draw_line(surface, color, points, width=0):
    for point in points:
        point = int(point.x + window.WIDTH // 2), int(-point.y + window.HEIGHT // 2)
        
    pygame.draw.polygon(surface, color, points, width)


def distance_between_points(p1, p2):
    return math.sqrt((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2)


def random_float(min_value=0.0, max_value=1.0):
    return random.uniform(min_value, max_value)


def sign(value):
    if value > 0:
        return 1
    elif value < 0:
        return -1
    else:
        return 0


def rect_collision(rect1_position, rect1_scale, rect2_position, rect2_scale):
    return pygame.Rect.colliderect(
        pygame.Rect(rect1_position.x, rect1_position.y, rect1_scale.x, rect1_scale.y), pygame.Rect(rect2_position.x, rect2_position.y, rect2_scale.x, rect2_scale.y)
    )


def circle_collsion(circle1_position, circle1_radius, circle2_position, circle2_radius):
    dst = circle1_position - circle2_position
    dst = dst.magnitude()

    if dst > circle1_radius + circle2_radius:
        return False

    return True

class Color:
    def __init__(self, r=0, g=0, b=0):
        self.r = r
        self.g = g
        self.b = b

    def tup(self):
        return self.r, self.g, self.b

    @staticmethod
    def random():
        return Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def blend(self, other, ratio=0.5):
        """
        Blends two colors based on a ratio.
        """
        r = int(self.r * ratio + other.r * (1 - ratio))
        g = int(self.g * ratio + other.g * (1 - ratio))
        b = int(self.b * ratio + other.b * (1 - ratio))
        return Color(r, g, b)

    def __repr__(self) -> str:
        return f"{self.r} {self.g} {self.b}"

BLACK = Color(0, 0, 0)
DGRAY = Color(64, 64, 64)
GRAY = Color(128, 128, 128)
LGRAY = Color(200, 200, 200)
WHITE = Color(255, 255, 255)
RED = Color(255, 0, 0)
GREEN = Color(0, 255, 0)
BLUE = Color(0, 0, 255)
YELLOW = Color(255, 255, 0)
CYAN = Color(0, 255, 255)
MAGENTA = Color(255, 0, 255)
PURPLE = Color(128, 0, 128)
MAGENTA = Color(128, 52, 32)

class Vector2:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def magnitude(self):
        """
        Returns the magnitude (length) of the vector.
        """
        return math.sqrt(self.x**2 + self.y**2)
    
    def sqr_magnitude(self):
        mag = self.magnitude()
        return mag * mag

    def normalize(self):
        """
        Normalizes the vector (sets its length to 1).
        """
        mag = mag = self.magnitude()
        try:
            return Vector2(self.x / mag, self.y / mag)
        except ZeroDivisionError:
            try:
                return Vector2(0, self.y / mag)
            except ZeroDivisionError:
                try:
                    return Vector2(self.x / mag, 0)
                except ZeroDivisionError:
                    return Vector2(0, 0)

    def dot(self, other):
        """
        Calculates the dot product of two vectors.
        """
        return self.x * other.x + self.y * other.y
    
    def cross(self, other):
        """
        Calculates the scalar cross product of two 2D vectors.
        Returns a scalar value representing the z-component of the 3D cross product.
        """
        return self.x * other.y - self.y * other.x

    def angle_between(self, other):
        """
        Calculates the angle between two vectors in radians.
        """
        return math.acos(self.dot(other) / (self.magnitude() * other.magnitude()))

    def rotate(self, angle):
        """
        Rotates the vector by a given angle in degrees.
        """
        rad = math.radians(angle)
        cos_theta, sin_theta = math.cos(rad), math.sin(rad)
        return Vector2(
            self.x * cos_theta - self.y * sin_theta,
            self.x * sin_theta + self.y * cos_theta,
        )

    def scale(self, factor):
        """
        Scales the vector by a factor.
        """
        return Vector2(self.x * factor, self.y * factor)

    def translate(self, dx, dy):
        """
        Translates the vector by dx and dy.
        """
        return Vector2(self.x + dx, self.y + dy)

    def __repr__(self):
        return f"Vector2({self.x}, {self.y})"

    def tup(self):
        return self.x, self.y

    # Addition
    def __add__(self, other):
        if isinstance(other, Vector2):
            return Vector2(self.x + other.x, self.y + other.y)
        elif isinstance(other, (int, float)):
            return Vector2(self.x + other, self.y + other)
        return NotImplemented

    # Subtraction
    def __sub__(self, other):
        if isinstance(other, Vector2):
            return Vector2(self.x - other.x, self.y - other.y)
        elif isinstance(other, (int, float)):
            return Vector2(self.x - other, self.y - other)
        return NotImplemented

    # Multiplication
    def __mul__(self, other):
        if isinstance(other, Vector2):
            return Vector2(self.x * other.x, self.y * other.y)
        elif isinstance(other, (int, float)):
            return Vector2(self.x * other, self.y * other)
        return NotImplemented

    # Division
    def __truediv__(self, other):
        if isinstance(other, Vector2):
            return Vector2(self.x / other.x, self.y / other.y)
        elif isinstance(other, (int, float)):
            return Vector2(self.x / other, self.y / other)
        return NotImplemented

    # Negation (unary minus)
    def __neg__(self):
        return Vector2(-self.x, -self.y)

    # Equality
    def __eq__(self, other):
        if isinstance(other, Vector2):
            return self.x == other.x and self.y == other.y
        return False


class Vector3:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def magnitude(self):
        """
        Returns the magnitude (length) of the vector.
        """
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def normalize(self):
        """
        Normalizes the vector (sets its length to 1).
        """
        mag = self.magnitude()
        return Vector3(self.x / mag, self.y / mag, self.z / mag)

    def dot(self, other):
        """
        Calculates the dot product of two vectors.
        """
        return self.x * other.x + self.y * other.y + self.z * other.z

    def angle_between(self, other):
        """
        Calculates the angle between two vectors in radians.
        """
        return math.acos(self.dot(other) / (self.magnitude() * other.magnitude()))

    def scale(self, factor):
        """
        Scales the vector by a factor.
        """
        return Vector3(self.x * factor, self.y * factor, self.z * factor)

    def translate(self, dx, dy, dz):
        """
        Translates the vector by dx, dy and dz.
        """
        return Vector3(self.x + dx, self.y + dy, self.z + dz)

    def __repr__(self):
        return f"Vector3({self.x}, {self.y}, {self.z})"

    def tup(self):
        return self.x, self.y, self.z

    # Addition
    def __add__(self, other):
        if isinstance(other, Vector3):
            return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)
        elif isinstance(other, (int, float)):
            return Vector3(self.x + other, self.y + other, self.z + other)
        return NotImplemented

    # Subtraction
    def __sub__(self, other):
        if isinstance(other, Vector3):
            return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)
        elif isinstance(other, (int, float)):
            return Vector3(self.x - other, self.y - other, self.z - other)
        return NotImplemented

    # Multiplication
    def __mul__(self, other):
        if isinstance(other, Vector3):
            return Vector3(self.x * other.x, self.y * other.y, self.z * other.z)
        elif isinstance(other, (int, float)):
            return Vector3(self.x * other, self.y * other, self.z * other)
        return NotImplemented

    # Division
    def __truediv__(self, other):
        if isinstance(other, Vector3):
            return Vector3(self.x / other.x, self.y / other.y, self.z / other.z)
        elif isinstance(other, (int, float)):
            return Vector3(self.x / other, self.y / other, self.z / other)
        return NotImplemented

    # Negation (unary minus)
    def __neg__(self):
        return Vector3(-self.x, -self.y, -self.z)

    # Equality
    def __eq__(self, other):
        if isinstance(other, Vector3):
            return self.x == other.x and self.y == other.y and self.z == other.z
        return False

def wpp(point: Vector3, focal_length) -> Vector2:
    """
    Weak Perspective Projection

    Formula:
    x_proj = (focal_length * x) / (focal_length + z)
    y_proj = (focal_length * y) / (focal_length + z)
    """

    projected = Vector2()

    projected.x = (focal_length * point.x) / (focal_length + point.z)
    projected.y = (focal_length * point.y) / (focal_length + point.z)

    return projected

def rotate_x(point: Vector3, angle: float):
    angle_rad = math.radians(angle)
    return Vector3(
        point.x,
        point.y * math.cos(angle_rad) - point.z * math.sin(angle_rad),
        point.y * math.sin(angle_rad) + point.z * math.cos(angle_rad)
    )

def rotate_y(point: Vector3, angle: float):
    angle_rad = math.radians(angle)
    return Vector3(
        point.x * math.cos(angle_rad) + point.z * math.sin(angle_rad),
        point.y,
        -point.x * math.sin(angle_rad) + point.z * math.cos(angle_rad)
    )

def rotate_z(point: Vector3, angle: float):
    angle_rad = math.radians(angle)
    return Vector3(
        point.x * math.cos(angle_rad) - point.y * math.sin(angle_rad),
        point.x * math.sin(angle_rad) + point.y * math.cos(angle_rad),
        point.z
    )


class Text:
    def __init__(self, text, font, position, anchor, color, bg_color=None, anti_aliasing=True):
        """Anchor is top left"""

        self.text = text
        self.font = font
        self.position = position
        self.anchor = anchor
        self.color = color
        self.bg_color = bg_color
        self.anti_aliasing = anti_aliasing

    center = "center"
    top_left = "topleft"
    top_right = "topright"
    bottom_left = "bottomleft"
    bottom_right = "bottomright"

    arial_32 = pygame.font.SysFont("Arial", 32)
    arial_24 = pygame.font.SysFont("Arial", 24)
    arial_16 = pygame.font.SysFont("Arial", 16)

    def render(self):
        text = self.font.render(self.text, self.anti_aliasing, self.color.tup(), self.bg_color if self.bg_color != None else None)
        text_rect = text.get_rect()

        if self.anchor == Text.center:
            text_rect.center = self.position.x // 2, self.position.y // 2
        if self.anchor == Text.top_left:
            text_rect.topleft = self.position.x // 2, self.position.y // 2
        if self.anchor == Text.top_right:
            text_rect.topright = self.position.x // 2, self.position.y // 2
        if self.anchor == Text.bottom_left:
            text_rect.bottomleft = self.position.x // 2, self.position.y // 2
        if self.anchor == Text.bottom_right:
            text_rect.bottomright = self.position.x // 2, self.position.y // 2

        window.SURFACE.blit(text, text_rect)


class Button:
    def __init__(self, position, scale, render_text, text, font, color, text_color, enable_outline, outline_color, outline_width):
        """Anchor is top left"""

        self.position = position
        self.scale = scale
        self.render_text = render_text
        self.text = text
        self.font = font
        self.color = color
        self.text_color = text_color
        self.enable_outline = enable_outline
        self.outline_color = outline_color
        self.outline_width = outline_width
        self.clicked = False
        self.clicked_this_click = False

    def render(self):
        draw_rectangle(window.SURFACE, self.color.tup(), self.position, self.scale)

        if self.enable_outline:
            draw_rectangle(window.SURFACE, self.outline_color.tup(), self.position, self.scale, self.outline_width)

        if self.render_text:
            self.text_obj = Text(self.text, self.font, self.position, Text.center, self.text_color)
            self.text_obj.render()

    def listen(self) -> tuple[bool, bool, bool]:
        """Returns tuple with three parameters:\n1. hovering (is true when mouse is above)\n2. clicking (is true while clicking)\n3. clicked (is true for one frame when clicked)"""
        cursor_pos = pygame.mouse.get_pos()

        hovering = False
        clicking = False

        if cursor_pos[0] >= self.position.x and cursor_pos[0] <= self.position.x + self.scale.x and cursor_pos[1] >= self.position.y and cursor_pos[1] <= self.position.y + self.scale.y:
            hovering = True

        if hovering:
            if pygame.mouse.get_pressed()[0]:
                clicking = True

        if self.clicked == False and clicking == True and self.clicked_this_click == False:
            self.clicked = True
            self.clicked_this_click = True
        else:
            self.clicked = False

        if clicking == False:
            self.clicked_this_click = False

        return hovering, clicking, self.clicked


class Window:
    def __init__(self, width=800, height=450, fullscreen=False, title="Game", max_fps=60, icon=None):
        self.running = True
        self.WIDTH = width
        self.HEIGHT = height
        self.SURFACE = pygame.display.set_mode((self.WIDTH, self.HEIGHT), pygame.FULLSCREEN if fullscreen else 0)
        self.delta_time = 0

        pygame.display.set_caption(title)
        if icon is not None:
            pygame.display.set_icon(icon)

        self.MAX_FPS = max_fps

        self.clock = pygame.time.Clock()


class InputManager:
    def __init__(self):
        self.keys_down = {}
        self.keys_held = {}
        self.keys_up = {}

        self.mouse_buttons_down = {}
        self.mouse_buttons_held = {}
        self.mouse_buttons_up = {}

        self.mouse_position = Vector2()
        self.mouse_motion = Vector2()

    def update(self):
        # Reset state for up and down events
        self.keys_down.clear()
        self.keys_up.clear()

        self.mouse_buttons_down.clear()
        self.mouse_buttons_up.clear()

        # Update keys
        keys = pygame.key.get_pressed()
        for key_code in range(len(keys)):
            if keys[key_code]:
                if not self.keys_held.get(key_code, False):
                    self.keys_down[key_code] = True
                self.keys_held[key_code] = True
            else:
                if self.keys_held.get(key_code, False):
                    self.keys_up[key_code] = True
                self.keys_held[key_code] = False

        # Update mouse
        mouse_buttons = pygame.mouse.get_pressed()
        for button in range(len(mouse_buttons)):
            if mouse_buttons[button]:
                if not self.mouse_buttons_held.get(button, False):
                    self.mouse_buttons_down[button] = True
                self.mouse_buttons_held[button] = True
            else:
                if self.mouse_buttons_held.get(button, False):
                    self.mouse_buttons_up[button] = True
                self.mouse_buttons_held[button] = False

        # Mouse movement
        self.mouse_position = Vector2(*pygame.mouse.get_pos())
        self.mouse_motion = Vector2(*pygame.mouse.get_rel())

    def get_key_down(self, key):
        return self.keys_down.get(key, False)

    def get_key_held(self, key):
        return self.keys_held.get(key, False)

    def get_key_up(self, key):
        return self.keys_up.get(key, False)

    def get_mouse_down(self, button):
        return self.mouse_buttons_down.get(button, False)

    def get_mouse_held(self, button):
        return self.mouse_buttons_held.get(button, False)

    def get_mouse_up(self, button):
        return self.mouse_buttons_up.get(button, False)

    def get_mouse_position(self):
        return self.mouse_position

    def get_mouse_motion(self):
        return self.mouse_motion

# Initialize InputManager GLOBALLY
input_manager = InputManager()


def run(start, update, width=800, height=450, fullscreen=False, title="Game", max_fps=60, icon=None):
    global window

    window = Window(width, height, fullscreen, title, max_fps, icon)

    start()

    get_ticks_last_frame = 0

    while window.running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                window.running = False

        # Update input states
        input_manager.update()

        update()

        window.clock.tick(window.MAX_FPS)
        t = pygame.time.get_ticks()
        window.delta_time = (t - get_ticks_last_frame) / 1000.0
        get_ticks_last_frame = t

        pygame.display.flip()

    pygame.quit()

def get_window():
    return window

def set_window(wndw):
    global window
    window = wndw
