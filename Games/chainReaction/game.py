import pygame
import math
import random
import sys
import os
import wave
import struct
import urllib.request
from collections import deque
import numpy as np

# --- Game Configuration ---
# Get screen size and maximize grid
pygame.init()
info = pygame.display.Info()
AVAILABLE_WIDTH = info.current_w
AVAILABLE_HEIGHT = info.current_h

# Calculate optimal grid size to fill screen
UI_HEIGHT = 160
GRID_WIDTH = 10  # More columns for wider screens
GRID_HEIGHT = 12  # More rows for taller screens
CELL_SIZE = min((AVAILABLE_WIDTH) // GRID_WIDTH, (AVAILABLE_HEIGHT - UI_HEIGHT) // GRID_HEIGHT)
SCREEN_WIDTH = GRID_WIDTH * CELL_SIZE
SCREEN_HEIGHT = GRID_HEIGHT * CELL_SIZE + UI_HEIGHT
FPS = 60

# --- Modern Gradient Colors & Theme ---
COLOR = {
    "BLACK": (0, 0, 0),
    "WHITE": (255, 255, 255),
    "BACKGROUND": (10, 12, 25),  # Deep blue-black
    "BACKGROUND_GRADIENT_TOP": (20, 25, 45),  # Lighter blue
    "BACKGROUND_GRADIENT_BOTTOM": (5, 8, 15),  # Darker blue-black
    "GRID": (60, 70, 90),
    "GRID_DARK": (25, 30, 45),
    "UI_BACKGROUND": (12, 15, 28),
    "UI_GRADIENT_TOP": (25, 30, 50),
    "UI_GRADIENT_BOTTOM": (10, 12, 22),
    "BUTTON": (45, 55, 80),
    "BUTTON_HOVER": (70, 85, 120),
    "ACCENT": (100, 120, 200),  # Bright blue accent
}

PLAYER_COLORS = [
    (239, 83, 80),    # 1: Red
    (3, 169, 244),     # 2: Light Blue
    (139, 195, 74),   # 3: Light Green
    (255, 238, 88),   # 4: Yellow
    (255, 112, 67),   # 5: Deep Orange
    (171, 71, 188),    # 6: Purple
    (38, 198, 218),    # 7: Cyan
    (255, 183, 77),   # 8: Amber
]

# --- Animation & Effect Parameters ---
PULSATE_SPEED = 0.05
ORB_TRAVEL_SPEED = 300
PLACE_ANIM_DURATION = 0.25 # seconds
EXPLOSION_DELAY = 0.15  # Delay between explosions
SHAKE_INTENSITY = 4
SHAKE_DURATION = 0.15

# --- Inline asset generation (single-file) ---
def _generate_sine_wave(frequency, duration, sample_rate=44100, amplitude=0.3):
    t = np.linspace(0, duration, int(sample_rate * duration))
    return amplitude * np.sin(2 * np.pi * frequency * t)

def _apply_envelope(wave_data, attack=0.01, decay=0.1, sustain=0.7, release=0.2):
    length = len(wave_data)
    envelope = np.ones(length)
    attack_samples = max(1, int(length * attack))
    decay_samples = max(1, int(length * decay))
    release_samples = max(1, int(length * release))
    envelope[:attack_samples] = np.linspace(0, 1, attack_samples)
    decay_end = min(length, attack_samples + decay_samples)
    envelope[attack_samples:decay_end] = np.linspace(1, sustain, decay_end - attack_samples)
    envelope[-release_samples:] = np.linspace(sustain, 0, release_samples)
    return wave_data * envelope

def _save_wav(filename, wave_data, sample_rate=44100):
    wave_data = np.clip(wave_data, -1, 1)
    wave_int16 = (wave_data * 32767).astype(np.int16)
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with wave.open(filename, 'w') as wav_file:
        wav_file.setnchannels(1)
        wav_file.setsampwidth(2)
        wav_file.setframerate(sample_rate)
        wav_file.writeframes(wave_int16.tobytes())

def _gen_place_sound(path):
    sr = 44100
    duration = 0.1
    w1 = _generate_sine_wave(800, duration, sr, 0.2)
    w2 = _generate_sine_wave(1200, duration, sr, 0.15)
    mixed = _apply_envelope(w1 + w2, attack=0.01, decay=0.3, sustain=0.3, release=0.4)
    _save_wav(path, mixed, sr)

def _gen_explode_sound(path):
    sr = 44100
    duration = 0.3
    t = np.linspace(0, duration, int(sr * duration))
    freq = 100 + (40 - 100) * (t / duration)
    w1 = 0.4 * np.sin(2 * np.pi * freq * t)
    noise = np.random.normal(0, 0.15, len(t))
    w2 = _generate_sine_wave(2000, duration, sr, 0.1)
    mixed = _apply_envelope(w1 + noise * 0.5 + w2 * 0.3, attack=0.001, decay=0.2, sustain=0.4, release=0.4)
    _save_wav(path, mixed, sr)

def _gen_win_sound(path):
    sr = 44100
    duration = 1.0
    notes = [523, 659, 784, 1047]
    per = duration / len(notes)
    full = np.array([], dtype=np.float32)
    for n in notes:
        w = _generate_sine_wave(n, per, sr, 0.25)
        w = _apply_envelope(w, attack=0.05, decay=0.2, sustain=0.7, release=0.3)
        full = np.concatenate([full, w])
    _save_wav(path, full, sr)

def _gen_music(path):
    sr = 44100
    duration = 30
    chords = [
        [262, 330, 392],
        [220, 262, 330],
        [175, 220, 262],
        [196, 247, 294],
    ]
    per = duration / len(chords)
    full = np.array([], dtype=np.float32)
    for chord in chords:
        chord_wave = np.zeros(int(sr * per), dtype=np.float32)
        for f in chord:
            chord_wave += _generate_sine_wave(f, per, sr, 0.08)
        chord_wave = _apply_envelope(chord_wave, attack=0.1, decay=0.2, sustain=0.6, release=0.5)
        full = np.concatenate([full, chord_wave])
    _save_wav(path, full, sr)

def _maybe_download_font():
    # Optional: try to fetch a font; game has system-font fallback if this fails
    try:
        url = "https://github.com/google/fonts/raw/main/ofl/orbitron/Orbitron%5Bwght%5D.ttf"
        dest = os.path.join('assets', 'GameFont.ttf')
        if not os.path.exists(dest):
            urllib.request.urlopen(url)  # quick connectivity check
            urllib.request.urlretrieve(url, dest)
    except Exception:
        pass

def ensure_assets():
    os.makedirs('assets', exist_ok=True)
    # We'll generate WAV files; loader already falls back to WAV if OGG missing
    required = {
        'place': os.path.join('assets', 'place.wav'),
        'explode': os.path.join('assets', 'explode.wav'),
        'win': os.path.join('assets', 'win.wav'),
        'music': os.path.join('assets', 'music.wav'),
    }
    if not os.path.exists(required['place']):
        _gen_place_sound(required['place'])
    if not os.path.exists(required['explode']):
        _gen_explode_sound(required['explode'])
    if not os.path.exists(required['win']):
        _gen_win_sound(required['win'])
    if not os.path.exists(required['music']):
        _gen_music(required['music'])
    _maybe_download_font()

class Particle:
    """Visual particle effect for explosions"""
    def __init__(self, pos, color):
        self.pos = pygame.Vector2(pos)
        angle = random.uniform(0, 2 * math.pi)
        speed = random.uniform(100, 250)
        self.vel = pygame.Vector2(math.cos(angle) * speed, math.sin(angle) * speed)
        self.color = color
        self.lifetime = random.uniform(0.4, 0.8)
        self.age = 0
        self.size = random.randint(4, 8)
    
    def update(self, dt):
        self.age += dt
        self.pos += self.vel * dt
        self.vel *= 0.92  # Friction
        return self.age < self.lifetime
    
    def draw(self, screen):
        alpha = 1 - (self.age / self.lifetime)
        size = int(self.size * alpha)
        if size > 0:
            # Particle with glow
            glow_color = tuple(int(c * alpha * 0.5) for c in self.color)
            main_color = tuple(int(c * alpha) for c in self.color)
            
            # Outer glow
            if size > 2:
                pygame.draw.circle(screen, glow_color, (int(self.pos.x), int(self.pos.y)), size + 2)
            
            # Main particle
            pygame.draw.circle(screen, main_color, (int(self.pos.x), int(self.pos.y)), size)

class Button:
    """A clickable UI button with hover effects."""
    def __init__(self, rect, text, text_color=COLOR["WHITE"]):
        self.rect = pygame.Rect(rect)
        self.text = text
        self.text_color = text_color
        self.font = pygame.font.Font(FONT_PATH, 32)
        self.base_color = COLOR["BUTTON"]
        self.hover_color = COLOR["BUTTON_HOVER"]
        self.is_hovered = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            was_hovered = self.is_hovered
            self.is_hovered = self.rect.collidepoint(event.pos)
            # Could add hover sound here if desired
        if event.type == pygame.MOUSEBUTTONDOWN and self.is_hovered:
            return True
        return False

    def draw(self, screen):
        color = self.hover_color if self.is_hovered else self.base_color
        
        # Add glow effect when hovered
        if self.is_hovered:
            glow_rect = self.rect.inflate(8, 8)
            glow_color = tuple(min(c + 30, 255) for c in color)
            pygame.draw.rect(screen, glow_color, glow_rect, border_radius=14)
        
        pygame.draw.rect(screen, color, self.rect, border_radius=12)
        pygame.draw.rect(screen, COLOR["GRID"], self.rect, 2, border_radius=12)
        
        text_surf = self.font.render(self.text, True, self.text_color)
        text_rect = text_surf.get_rect(center=self.rect.center)
        screen.blit(text_surf, text_rect)

class Cell:
    """Represents a grid cell, handling its own state and drawing."""
    def __init__(self, row, col):
        self.row, self.col = row, col
        self.orbs, self.owner = 0, None
        self.rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        
        # Calculate critical mass
        is_corner = (row in (0, GRID_HEIGHT - 1)) and (col in (0, GRID_WIDTH - 1))
        is_edge = not is_corner and (row in (0, GRID_HEIGHT - 1) or col in (0, GRID_WIDTH - 1))
        base_critical = 2 if is_corner else (3 if is_edge else 4)
        self.critical_mass = min(base_critical, 3)
        
        # For placement animation
        self.scale = 0
        self.is_placing = False
        self.rotation = random.uniform(0, 2 * math.pi)
        self.rotation_speed = random.uniform(0.8, 1.2)

    def start_placement(self):
        self.is_placing = True
        self.scale = 0

    def update(self, dt):
        if self.is_placing:
            self.scale += dt / PLACE_ANIM_DURATION
            if self.scale >= 1:
                self.scale = 1
                self.is_placing = False

        if self.orbs > 1:
            self.rotation += self.rotation_speed * dt * math.pi
            self.rotation %= (2 * math.pi)

    def draw(self, screen):
        # Draw cell background - simple solid color for performance
        pygame.draw.rect(screen, COLOR["GRID_DARK"], self.rect)
        
        if self.owner is not None:
            color = PLAYER_COLORS[self.owner]
            center = self.rect.center
            
            # Pulsating effect for critical cells
            pulse = 0
            if self.orbs == self.critical_mass - 1:
                pulse = math.sin(pygame.time.get_ticks() * PULSATE_SPEED) * 2
            
            base_radius = 14
            animate_scale = (self.scale if self.is_placing else 1)

            if self.orbs == 1:
                radius = max(6, int((base_radius + pulse) * animate_scale))
                pos = (int(center[0]), int(center[1]))
                pygame.draw.circle(screen, (20, 20, 30), (pos[0] + 1, pos[1] + 2), radius + 1)
                pygame.draw.circle(screen, color, pos, radius)
                highlight_pos = (pos[0] - int(radius * 0.25), pos[1] - int(radius * 0.25))
                highlight_color = tuple(min(255, int(c * 1.3)) for c in color)
                pygame.draw.circle(screen, highlight_color, highlight_pos, max(3, int(radius * 0.3)))
            else:
                orbit_radius = 16 if self.orbs >= 3 else 12
                orbit_radius += pulse * 0.5
                orbit_radius *= animate_scale
                orb_data = []
                for idx in range(self.orbs):
                    angle = self.rotation + (2 * math.pi * idx) / self.orbs
                    depth = (math.sin(angle) + 1) * 0.5
                    x = center[0] + math.cos(angle) * orbit_radius
                    y = center[1] + math.sin(angle) * orbit_radius * 0.45
                    scale = 0.8 + depth * 0.35
                    orb_data.append({
                        "pos": (x, y),
                        "depth": depth,
                        "scale": scale
                    })

                orb_data.sort(key=lambda item: item["depth"])

                glow_surface = pygame.Surface((CELL_SIZE, CELL_SIZE), pygame.SRCALPHA)
                pygame.draw.circle(glow_surface, (*color, 45), (CELL_SIZE // 2, CELL_SIZE // 2), CELL_SIZE // 2 - 4)
                screen.blit(glow_surface, (self.rect.left, self.rect.top))

                for item in orb_data:
                    pos = (int(item["pos"][0]), int(item["pos"][1]))
                    radius = max(5, int(base_radius * item["scale"]))
                    shadow_offset = 2 - item["depth"]
                    shadow_pos = (pos[0] + int(shadow_offset), pos[1] + int(shadow_offset * 1.5))
                    pygame.draw.circle(screen, (25, 25, 40), shadow_pos, radius + 1)

                    shade_factor = 0.75 + item["depth"] * 0.4
                    shaded_color = tuple(min(255, int(c * shade_factor)) for c in color)
                    pygame.draw.circle(screen, shaded_color, pos, radius)

                    highlight_offset = (math.cos(self.rotation + item["depth"]) * radius * 0.25,
                                        math.sin(self.rotation + item["depth"]) * radius * 0.25)
                    highlight_pos = (pos[0] - int(highlight_offset[0]), pos[1] - int(highlight_offset[1]))
                    highlight_color = tuple(min(255, int(c * 1.35)) for c in color)
                    pygame.draw.circle(screen, highlight_color, highlight_pos, max(3, int(radius * 0.3)))

class AnimatedOrb:
    """An orb that visually travels between cells."""
    def __init__(self, start_cell, end_cell, player_id):
        self.start = pygame.Vector2(start_cell.rect.center)
        self.end = pygame.Vector2(end_cell.rect.center)
        self.pos = self.start.copy()
        self.target_cell = end_cell
        self.player_id = player_id
        dist = self.start.distance_to(self.end)
        self.dir = (self.end - self.start).normalize() if dist > 0 else pygame.Vector2()
        self.progress = 0  # Animation progress 0 to 1

    def update(self, dt):
        # Smooth acceleration/deceleration
        self.progress += dt * (1 / 0.3)  # 0.3 seconds travel time
        if self.progress > 1:
            self.progress = 1
        
        # Ease-in-out interpolation for smooth movement
        t = self.progress
        ease = t * t * (3 - 2 * t)  # Smoothstep function
        
        self.pos = self.start + (self.end - self.start) * ease
        return self.progress >= 1

    def draw(self, screen):
        color = PLAYER_COLORS[self.player_id]
        radius = 14

        pos = (int(self.pos.x), int(self.pos.y))

        # Simple animated orb - clean circle
        shadow_pos = (pos[0] + 1, pos[1] + 2)
        shadow_color = (20, 20, 30, 180)
        pygame.draw.circle(screen, shadow_color, shadow_pos, radius + 1)

        # Main solid circle
        pygame.draw.circle(screen, color, pos, radius)

        # Small highlight
        highlight_pos = (pos[0] - int(radius * 0.25), pos[1] - int(radius * 0.25))
        highlight_color = tuple(min(255, int(c * 1.3)) for c in color)
        pygame.draw.circle(screen, highlight_color, highlight_pos, max(3, int(radius * 0.3)))

class Game:
    """Main class to manage game states, logic, and rendering."""
    def __init__(self):
        # Ensure assets exist when running as a single file
        try:
            ensure_assets()
        except Exception as e:
            print(f"Asset preparation warning: {e}")
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Chain Reaction - Modern Edition")
        self.clock = pygame.time.Clock()
        self.load_assets()
        self.game_state = "menu"
        self.num_players = 0
        # Create gradient background surface
        self.background_gradient = self.create_gradient_surface(SCREEN_WIDTH, SCREEN_HEIGHT,
            COLOR["BACKGROUND_GRADIENT_TOP"], COLOR["BACKGROUND_GRADIENT_BOTTOM"])
    
    def create_gradient_surface(self, width, height, top_color, bottom_color):
        """Create a vertical gradient surface"""
        surface = pygame.Surface((width, height))
        for y in range(height):
            ratio = y / height
            r = int(top_color[0] * (1 - ratio) + bottom_color[0] * ratio)
            g = int(top_color[1] * (1 - ratio) + bottom_color[1] * ratio)
            b = int(top_color[2] * (1 - ratio) + bottom_color[2] * ratio)
            pygame.draw.line(surface, (r, g, b), (0, y), (width, y))
        return surface

    def load_assets(self):
        global FONT_PATH
        try:
            # Try to load the new modern font
            FONT_PATH = "assets/Poppins-Regular.ttf"
            self.font_small = pygame.font.Font(FONT_PATH, 24)
            self.font_medium = pygame.font.Font(FONT_PATH, 42)
            self.font_large = pygame.font.Font(FONT_PATH, 74)
        except FileNotFoundError:
            try:
                # Fallback to original font
                FONT_PATH = "assets/GameFont.ttf"
                self.font_small = pygame.font.Font(FONT_PATH, 22)
                self.font_medium = pygame.font.Font(FONT_PATH, 40)
                self.font_large = pygame.font.Font(FONT_PATH, 72)
            except FileNotFoundError:
                # Final fallback to system font
                FONT_PATH = None
                self.font_small = pygame.font.SysFont("Arial", 24)
                self.font_medium = pygame.font.SysFont("Arial", 42, bold=True)
                self.font_large = pygame.font.SysFont("Arial", 74, bold=True)

        if FONT_PATH:
            self.font_tiny = pygame.font.Font(FONT_PATH, 20)
        else:
            self.font_tiny = pygame.font.SysFont("Arial", 20)
        
        self.sounds = {}
        try:
            pygame.mixer.init()
            pygame.mixer.set_num_channels(32)
            # Try loading sounds with fallback for file format
            sound_files = ['place', 'explode', 'win']
            for sound_name in sound_files:
                try:
                    self.sounds[sound_name] = pygame.mixer.Sound(f"assets/{sound_name}.ogg")
                except:
                    try:
                        self.sounds[sound_name] = pygame.mixer.Sound(f"assets/{sound_name}.wav")
                    except:
                        print(f"Could not load {sound_name} sound")
            
            # Try loading music
            try:
                pygame.mixer.music.load("assets/music.ogg")
                pygame.mixer.music.play(-1, fade_ms=2000)
                pygame.mixer.music.set_volume(0.3)
            except:
                try:
                    pygame.mixer.music.load("assets/music.wav")
                    pygame.mixer.music.play(-1, fade_ms=2000)
                    pygame.mixer.music.set_volume(0.3)
                except:
                    print("Could not load background music")
                    
        except (pygame.error, FileNotFoundError) as e:
            print(f"Sound loading error: {e}. Running without sound.")
            self.sounds = None

    def play_sound(self, name):
        if self.sounds and name in self.sounds:
            self.sounds[name].play()
            
    def reset_game(self):
        self.grid = [[Cell(row, col) for col in range(GRID_WIDTH)] for row in range(GRID_HEIGHT)]
        self.current_player, self.turn_count, self.winner = 0, 0, None
        self.explosion_queue = deque()
        self.animated_orbs = []
        self.particles = []  # Add particle effects
        self.shake_duration = 0
        self.explosion_timer = 0  # Timer for explosion delay
        self.is_turn_processed = True # Flag to ensure next_turn is called only once

    def get_neighbors(self, row, col):
        neighbors = []
        if row > 0: neighbors.append(self.grid[row-1][col])
        if row < GRID_HEIGHT - 1: neighbors.append(self.grid[row+1][col])
        if col > 0: neighbors.append(self.grid[row][col-1])
        if col < GRID_WIDTH - 1: neighbors.append(self.grid[row][col+1])
        return neighbors

    def handle_click(self, pos):
        if self.explosion_queue or self.animated_orbs: return
        
        col, row = pos[0] // CELL_SIZE, pos[1] // CELL_SIZE
        if 0 <= col < GRID_WIDTH and 0 <= row < GRID_HEIGHT:
            cell = self.grid[row][col]
            if cell.owner is None or cell.owner == self.current_player:
                self.play_sound('place')
                self.is_turn_processed = False
                self.turn_count += 1
                cell.owner = self.current_player
                cell.orbs += 1
                cell.start_placement()
                if cell.orbs >= cell.critical_mass:
                    self.explosion_queue.append(cell)

    def trigger_shake(self):
        self.shake_duration = SHAKE_DURATION

    def update(self, dt):
        for row in self.grid:
            for cell in row:
                cell.update(dt)
        
        # Update particles
        self.particles = [p for p in self.particles if p.update(dt)]
                
        # Handle screen shake
        if self.shake_duration > 0:
            self.shake_duration -= dt
        
        # Update explosion timer
        if self.explosion_timer > 0:
            self.explosion_timer -= dt
        
        # Process explosions with delay for better visual feedback
        if self.explosion_queue and not self.animated_orbs and self.explosion_timer <= 0:
            cell = self.explosion_queue.popleft()
            self.play_sound('explode')
            self.trigger_shake()
            
            # Create particle effects at explosion
            color = PLAYER_COLORS[cell.owner]
            for _ in range(15):
                self.particles.append(Particle(cell.rect.center, color))
            
            cell.orbs -= cell.critical_mass
            if cell.orbs == 0: cell.owner = None
            
            for neighbor in self.get_neighbors(cell.row, cell.col):
                self.animated_orbs.append(AnimatedOrb(cell, neighbor, self.current_player))
            
            # Set timer for next explosion
            if self.explosion_queue:
                self.explosion_timer = EXPLOSION_DELAY

        # Update orb animations
        for orb in self.animated_orbs[:]:
            if orb.update(dt):
                self.animated_orbs.remove(orb)
                target = orb.target_cell
                target.owner = orb.player_id
                target.orbs += 1
                if target.orbs >= target.critical_mass:
                    self.explosion_queue.append(target)
        
        # Check if turn is over
        if not self.explosion_queue and not self.animated_orbs and not self.is_turn_processed:
            self.next_turn()
            self.is_turn_processed = True

    def next_turn(self):
        if self.turn_count >= self.num_players:
            active = {c.owner for r in self.grid for c in r if c.owner is not None}
            if len(active) == 1:
                self.winner = active.pop()
                self.game_state = "game_over"
                self.play_sound('win')
                return

        while True:
            self.current_player = (self.current_player + 1) % self.num_players
            if self.turn_count < self.num_players: break
            if any(c.owner == self.current_player for r in self.grid for c in r): break

    def draw(self):
        # Draw gradient background
        self.screen.blit(self.background_gradient, (0, 0))
        
        offset = [0, 0]
        if self.shake_duration > 0:
            offset[0] = random.randint(-SHAKE_INTENSITY, SHAKE_INTENSITY)
            offset[1] = random.randint(-SHAKE_INTENSITY, SHAKE_INTENSITY)

        # Get mouse position for hover effect
        mouse_pos = pygame.mouse.get_pos()
        hover_cell = None
        if not self.explosion_queue and not self.animated_orbs:
            col, row = mouse_pos[0] // CELL_SIZE, mouse_pos[1] // CELL_SIZE
            if 0 <= col < GRID_WIDTH and 0 <= row < GRID_HEIGHT:
                cell = self.grid[row][col]
                if cell.owner is None or cell.owner == self.current_player:
                    hover_cell = cell

        # Draw cells
        for row in self.grid:
            for cell in row:
                cell.rect.topleft = (cell.col * CELL_SIZE + offset[0], cell.row * CELL_SIZE + offset[1])
                
                # Draw hover highlight
                if cell == hover_cell:
                    hover_color = PLAYER_COLORS[self.current_player]
                    hover_alpha = tuple(int(c * 0.15) for c in hover_color)
                    pygame.draw.rect(self.screen, hover_alpha, cell.rect)
                
                cell.draw(self.screen)
        
        # Draw 3D grid lines with player color
        self.draw_3d_grid(offset)
        
        # Draw particles (behind orbs)
        for particle in self.particles:
            particle.draw(self.screen)
        
        for orb in self.animated_orbs:
            orb.pos.x += offset[0]
            orb.pos.y += offset[1]
            orb.draw(self.screen)
        
        self.draw_ui()
        pygame.display.flip()

    def _draw_gradient_line(self, start, end, base_color, start_alpha, end_alpha, width):
        """Render a line with opacity gradient to give a subtle depth effect."""
        if start[0] == end[0]:
            length = abs(end[1] - start[1])
            if length == 0:
                return
            surf = pygame.Surface((width, length), pygame.SRCALPHA)
            for i in range(length):
                ratio = i / max(1, length - 1)
                alpha = start_alpha + (end_alpha - start_alpha) * ratio
                pygame.draw.line(surf, (*base_color, int(alpha)), (0, i), (width - 1, i))
            top = min(start[1], end[1])
            self.screen.blit(surf, (int(start[0] - width // 2), int(top)))
        else:
            length = abs(end[0] - start[0])
            if length == 0:
                return
            surf = pygame.Surface((length, width), pygame.SRCALPHA)
            for i in range(length):
                ratio = i / max(1, length - 1)
                alpha = start_alpha + (end_alpha - start_alpha) * ratio
                pygame.draw.line(surf, (*base_color, int(alpha)), (i, 0), (i, width - 1))
            left = min(start[0], end[0])
            self.screen.blit(surf, (int(left), int(start[1] - width // 2)))
    
    def draw_3d_grid(self, offset):
        """Draw semi-transparent grid lines that fade across their length."""
        player_color = PLAYER_COLORS[self.current_player]
        line_color = tuple(min(255, int(player_color[i] * 0.85 + 70)) for i in range(3))
        start_alpha, end_alpha = 45, 155

        grid_height_px = GRID_HEIGHT * CELL_SIZE
        grid_width_px = GRID_WIDTH * CELL_SIZE

        for col in range(GRID_WIDTH + 1):
            x = col * CELL_SIZE + offset[0]
            start = (x, offset[1])
            end = (x, grid_height_px + offset[1])
            self._draw_gradient_line(start, end, line_color, start_alpha, end_alpha, 2)

        for row in range(GRID_HEIGHT + 1):
            y = row * CELL_SIZE + offset[1]
            start = (offset[0], y)
            end = (grid_width_px + offset[0], y)
            self._draw_gradient_line(start, end, line_color, start_alpha, end_alpha, 2)

    def draw_player_card(self, rect, player_id, orb_count, is_current, is_eliminated):
        """Render a compact player summary card in the UI strip."""
        base_color = PLAYER_COLORS[player_id]
        blend_color = tuple(int(COLOR["UI_BACKGROUND"][i] * 0.7 + base_color[i] * 0.3) for i in range(3))
        if is_eliminated:
            blend_color = tuple(int(blend_color[i] * 0.55 + 35) for i in range(3))

        pygame.draw.rect(self.screen, blend_color, rect, border_radius=12)

        border_color = COLOR["ACCENT"] if is_current else (70, 80, 105)
        if is_eliminated:
            border_color = (110, 60, 70)
        pygame.draw.rect(self.screen, border_color, rect, width=2, border_radius=12)

        orb_center = (rect.left + 26, rect.centery)
        shadow_color = (18, 20, 32)
        pygame.draw.circle(self.screen, shadow_color, (orb_center[0] + 2, orb_center[1] + 3), 18)

        orb_color = base_color if not is_eliminated else tuple(int(base_color[i] * 0.35 + 70) for i in range(3))
        pygame.draw.circle(self.screen, orb_color, orb_center, 16)
        highlight_color = tuple(min(255, int(orb_color[i] * 1.3)) for i in range(3))
        pygame.draw.circle(self.screen, highlight_color, (orb_center[0] - 5, orb_center[1] - 5), 6)

        label = self.font_small.render(f"P{player_id + 1}", True, COLOR["WHITE"])
        self.screen.blit(label, (rect.left + 54, rect.top + 8))

        status_text = "Your turn" if is_current else ("Eliminated" if is_eliminated else "In play")
        status_color = COLOR["ACCENT"] if is_current else ((220, 120, 130) if is_eliminated else (190, 200, 218))
        status_surf = self.font_tiny.render(status_text, True, status_color)
        self.screen.blit(status_surf, (rect.left + 54, rect.top + rect.height // 2 - 6))

        count_surf = self.font_tiny.render(f"{orb_count} orbs", True, (210, 215, 230))
        self.screen.blit(count_surf, (rect.left + 54, rect.bottom - 22))

    def draw_ui(self):
        ui_y = SCREEN_HEIGHT - UI_HEIGHT
        ui_rect = pygame.Rect(0, ui_y, SCREEN_WIDTH, UI_HEIGHT)

        # Draw gradient background
        for y in range(UI_HEIGHT):
            ratio = y / UI_HEIGHT
            r = int(COLOR["UI_GRADIENT_TOP"][0] * (1 - ratio) + COLOR["UI_GRADIENT_BOTTOM"][0] * ratio)
            g = int(COLOR["UI_GRADIENT_TOP"][1] * (1 - ratio) + COLOR["UI_GRADIENT_BOTTOM"][1] * ratio)
            b = int(COLOR["UI_GRADIENT_TOP"][2] * (1 - ratio) + COLOR["UI_GRADIENT_BOTTOM"][2] * ratio)
            pygame.draw.line(self.screen, (r, g, b), (0, ui_y + y), (SCREEN_WIDTH, ui_y + y))

        # Top accent line
        pygame.draw.line(self.screen, COLOR["ACCENT"], ui_rect.topleft, ui_rect.topright, 3)
        pygame.draw.line(self.screen, (50, 60, 100), (0, ui_y + 1), (SCREEN_WIDTH, ui_y + 1), 1)

        player_color = PLAYER_COLORS[self.current_player]

        # Current player indicator - left side with smaller text
        turn_label = self.font_tiny.render("Current Turn", True, (185, 195, 215))
        self.screen.blit(turn_label, (20, ui_y + 15))

        turn_text = self.font_small.render(f"Player {self.current_player + 1}", True, player_color)
        self.screen.blit(turn_text, (20, ui_y + 35))

        # Calculate orb counts for dominance bar
        orb_counts = [0] * self.num_players
        for row in self.grid:
            for cell in row:
                if cell.owner is not None:
                    orb_counts[cell.owner] += cell.orbs

        total_orbs = sum(orb_counts)
        
        # Polished dominance bar with modern glass effect
        if total_orbs > 0:
            bar_y = ui_y + 80
            bar_h = 36
            bar_padding = 30
            max_w = SCREEN_WIDTH - (bar_padding * 2)
            
            # Outer shadow for depth
            shadow_rect = pygame.Rect(bar_padding - 2, bar_y + 3, max_w + 4, bar_h + 2)
            shadow_surf = pygame.Surface((shadow_rect.width, shadow_rect.height), pygame.SRCALPHA)
            pygame.draw.rect(shadow_surf, (0, 0, 0, 60), shadow_surf.get_rect(), border_radius=20)
            self.screen.blit(shadow_surf, shadow_rect.topleft)
            
            # Main background with subtle gradient
            bg_rect = pygame.Rect(bar_padding, bar_y, max_w, bar_h)
            for y_off in range(bar_h):
                shade_ratio = y_off / bar_h
                shade = int(10 + shade_ratio * 8)
                pygame.draw.line(self.screen, (shade, shade + 2, shade + 8), 
                               (bar_padding + 18, bar_y + y_off), 
                               (bar_padding + max_w - 18, bar_y + y_off))
            
            # Rounded background
            pygame.draw.rect(self.screen, (8, 10, 18), bg_rect, border_radius=18)
            
            # Inner container
            inner_padding = 3
            inner_rect = pygame.Rect(bar_padding + inner_padding, bar_y + inner_padding, 
                                    max_w - inner_padding * 2, bar_h - inner_padding * 2)
            pygame.draw.rect(self.screen, (5, 7, 12), inner_rect, border_radius=16)

            # Draw player segments with polished style
            current_x = bar_padding + inner_padding
            segment_height = bar_h - inner_padding * 2
            
            for i in range(self.num_players):
                if orb_counts[i] > 0:
                    perc = orb_counts[i] / total_orbs
                    width = max(10, perc * (max_w - inner_padding * 2))
                    
                    if width > 0:
                        base_color = PLAYER_COLORS[i]
                        
                        # Create segment surface for smooth blending
                        seg_surf = pygame.Surface((int(width), segment_height), pygame.SRCALPHA)
                        
                        # Glass-like gradient effect
                        for y_offset in range(segment_height):
                            progress = y_offset / segment_height
                            
                            # Multi-stop gradient for depth
                            if progress < 0.15:
                                # Top highlight
                                blend = progress / 0.15
                                r = int(base_color[0] + (255 - base_color[0]) * (1 - blend) * 0.4)
                                g = int(base_color[1] + (255 - base_color[1]) * (1 - blend) * 0.4)
                                b = int(base_color[2] + (255 - base_color[2]) * (1 - blend) * 0.4)
                            elif progress < 0.5:
                                # Main color
                                r, g, b = base_color
                            else:
                                # Bottom shadow
                                darken = (progress - 0.5) / 0.5 * 0.3
                                r = int(base_color[0] * (1 - darken))
                                g = int(base_color[1] * (1 - darken))
                                b = int(base_color[2] * (1 - darken))
                            
                            alpha = 255
                            pygame.draw.line(seg_surf, (r, g, b, alpha), (0, y_offset), (int(width), y_offset))
                        
                        # Blit segment
                        self.screen.blit(seg_surf, (int(current_x), bar_y + inner_padding))
                        
                        # Add subtle separator between segments
                        if i < self.num_players - 1 and current_x + width < bar_padding + max_w - inner_padding:
                            sep_x = int(current_x + width)
                            pygame.draw.line(self.screen, (20, 25, 35), 
                                           (sep_x, bar_y + inner_padding + 4), 
                                           (sep_x, bar_y + bar_h - inner_padding - 4), 2)
                        
                        # Percentage text with better contrast
                        if width > 60:
                            percent_text = f"{int(perc * 100)}%"
                            percent_surf = self.font_tiny.render(percent_text, True, COLOR["WHITE"])
                            text_x = int(current_x + width/2 - percent_surf.get_width()/2)
                            text_y = int(bar_y + bar_h/2 - percent_surf.get_height()/2)
                            
                            # Multi-layer shadow for readability
                            for offset in [(0, 2), (1, 1), (2, 0)]:
                                shadow = self.font_tiny.render(percent_text, True, (0, 0, 0))
                                self.screen.blit(shadow, (text_x + offset[0], text_y + offset[1]))
                            
                            self.screen.blit(percent_surf, (text_x, text_y))
                        
                        current_x += width
            
            # Glass highlight overlay on top half
            highlight_surf = pygame.Surface((max_w - inner_padding * 2, segment_height // 3), pygame.SRCALPHA)
            for y in range(segment_height // 3):
                alpha = int(40 * (1 - y / (segment_height // 3)))
                pygame.draw.line(highlight_surf, (255, 255, 255, alpha), 
                               (0, y), (max_w - inner_padding * 2, y))
            self.screen.blit(highlight_surf, (bar_padding + inner_padding, bar_y + inner_padding + 2))
            
            # Polished border with gradient glow
            border_color = tuple(min(255, int(c * 0.6 + 100)) for c in PLAYER_COLORS[self.current_player])
            pygame.draw.rect(self.screen, border_color, bg_rect, width=2, border_radius=18)
            
            # Subtle outer glow
            glow_rect = bg_rect.inflate(4, 4)
            glow_color = tuple(int(c * 0.4) for c in border_color)
            pygame.draw.rect(self.screen, (*glow_color, 80), glow_rect, width=1, border_radius=20)

        # Player cards in bottom section
        cards_per_row = min(self.num_players, 4) if self.num_players else 1
        card_height = 40
        card_margin = 20
        card_spacing = 12
        
        card_width = SCREEN_WIDTH - 2 * card_margin
        if cards_per_row > 1:
            card_width = (SCREEN_WIDTH - 2 * card_margin - (cards_per_row - 1) * card_spacing) / cards_per_row

        card_y_start = ui_y + 130

        for idx in range(self.num_players):
            col_idx = idx % cards_per_row
            row_idx = idx // cards_per_row
            x = card_margin + col_idx * (card_width + card_spacing)
            y = card_y_start + row_idx * (card_height + 8)
            card_rect = pygame.Rect(int(x), int(y), int(card_width), card_height)

            is_current = idx == self.current_player
            is_eliminated = orb_counts[idx] == 0 and self.turn_count >= self.num_players
            self.draw_player_card(card_rect, idx, orb_counts[idx], is_current, is_eliminated)
            
    def run_menu(self):
        # Title with glow effect
        title = self.font_large.render("Chain Reaction", True, COLOR["WHITE"])
        title_glow = self.font_large.render("Chain Reaction", True, COLOR["ACCENT"])
        title_rect = title.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT * 0.15))
        
        # Subtitle
        subtitle = self.font_small.render("Select number of players to begin", True, (180, 190, 210))
        subtitle_rect = subtitle.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT * 0.25))
        
        # 8 player buttons arranged in 2 columns for better layout
        buttons = [Button((0,0,220,55), f"{i} Players") for i in range(2, 10)]
        
        # Arrange in 2 columns
        col_spacing = SCREEN_WIDTH / 3
        row_spacing = 75
        start_y = SCREEN_HEIGHT * 0.35
        
        for i, btn in enumerate(buttons):
            col = i % 2
            row = i // 2
            btn.rect.center = (col_spacing * (col + 1), start_y + row * row_spacing)

        while self.game_state == "menu":
            for event in pygame.event.get():
                if event.type == pygame.QUIT: pygame.quit(); sys.exit()
                for i, btn in enumerate(buttons):
                    if btn.handle_event(event):
                        self.num_players = i + 2
                        self.reset_game()
                        self.game_state = "playing"

            # Draw gradient background
            self.screen.blit(self.background_gradient, (0, 0))
            
            # Draw glowing title
            for offset in [(2, 2), (-2, 2), (2, -2), (-2, -2)]:
                glow_rect = title_glow.get_rect(center=(title_rect.centerx + offset[0], title_rect.centery + offset[1]))
                self.screen.blit(title_glow, glow_rect)
            self.screen.blit(title, title_rect)
            
            # Draw subtitle
            self.screen.blit(subtitle, subtitle_rect)
            
            # Draw buttons
            for btn in buttons:
                btn.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(FPS)

    def run_game_over(self):
        winner_text = self.font_large.render(f"Player {self.winner + 1} Wins!", True, PLAYER_COLORS[self.winner])
        winner_glow = self.font_large.render(f"Player {self.winner + 1} Wins!", True, COLOR["WHITE"])
        winner_rect = winner_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 60))
        menu_button = Button((0,0,300,70), "Main Menu")
        menu_button.rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 60)

        while self.game_state == "game_over":
            for event in pygame.event.get():
                if event.type == pygame.QUIT: pygame.quit(); sys.exit()
                if menu_button.handle_event(event):
                    self.game_state = "menu"
            
            # Draw gradient background
            self.screen.blit(self.background_gradient, (0, 0))
            
            # Draw glowing winner text
            for offset in [(3, 3), (-3, 3), (3, -3), (-3, -3)]:
                glow_rect = winner_glow.get_rect(center=(winner_rect.centerx + offset[0], winner_rect.centery + offset[1]))
                self.screen.blit(winner_glow, glow_rect)
            self.screen.blit(winner_text, winner_rect)
            
            menu_button.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(FPS)

    def run(self):
        while True:
            if self.game_state == "menu": self.run_menu()
            elif self.game_state == "playing":
                dt = self.clock.tick(FPS) / 1000.0
                for event in pygame.event.get():
                    if event.type == pygame.QUIT: pygame.quit(); sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN: self.handle_click(event.pos)
                self.update(dt)
                self.draw()
            elif self.game_state == "game_over": self.run_game_over()

if __name__ == "__main__":
    game = Game()
    game.run()