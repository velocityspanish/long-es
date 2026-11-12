"""VELOCITY LONGFORM - 16:9 chapter lesson, brand and motion constants."""

import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

OUTPUT_DIR = BASE_DIR / "output"
LESSONS_DIR = OUTPUT_DIR / "lessons"
HISTORY_DIR = OUTPUT_DIR / "history"
SCENE_DIR = BASE_DIR / "scene"

VIDEO_WIDTH = 1920
VIDEO_HEIGHT = 1080
FPS = 30

TARGET_CHAPTERS = 8
PHRASES_PER_CHAPTER = 7
TARGET_PHRASES = TARGET_CHAPTERS * PHRASES_PER_CHAPTER

# ---------------------------------------------------------------- brand

BRAND = "VELOCITY SPANISH"
BRAND_LOCKUP_TOP = "VELOCITY"
BRAND_LOCKUP_BOTTOM = "SPANISH"
HANDLE = "@velocityspanish"
MASCOT_NAME = "Velo"

# ==== LANGUAGE PACK START ====
LANGUAGE = {'code': 'es',
 'name': 'Spanish',
 'native_name': 'Español',
 'history_key': 'spanish',
 'english_voice': 'en-US-AvaNeural',
 'english_fallback_voice': 'en-US-GuyNeural',
 'native_voice': 'es-ES-AlvaroNeural',
 'native_fallback_voice': 'es-ES-ElviraNeural',
 'native_engine': 'edge',
 'native_lang_code': 'es',
 'english_rate': '-4%',
 'native_rate': '-10%',
 'english_pitch': '+0Hz',
 'native_pitch': '+0Hz',
 'native_label': 'ESPAÑOL',
 'translit_label': 'SAY IT LIKE',
 'flag': 'es',
 'greeting': '¡Hola!',
 'encouragement': '¡Excelente!',
 'rtl': False,
 'char_tiles': False,
 'script_font': '',
 'glyphs': 'ABCDEFGHIJKLMNOPQRSTUVWXYZÁÉÍÓÚÜÑáéíóúüñ'}
# ==== LANGUAGE PACK END ====

# ==== CATEGORIES START ====
CATEGORIES = {'Motivation': 'Motivación',
 'Love': 'Amor',
 'Success': 'Éxito',
 'Wisdom': 'Sabiduría',
 'Happiness': 'Felicidad',
 'Self Improvement': 'Superación Personal',
 'Gratitude': 'Gratitud',
 'Friendship': 'Amistad',
 'Hope': 'Esperanza',
 'Creativity': 'Creatividad',
 'Inner Peace': 'Paz Interior',
 'Confidence': 'Confianza',
 'Perseverance': 'Perseverancia',
 'Inspiration': 'Inspiración',
 'Positive Life': 'Vida Positiva',
 'Courage': 'Coraje',
 'Kindness': 'Bondad',
 'Patience': 'Paciencia',
 'Forgiveness': 'Perdón',
 'Strength': 'Fortaleza',
 'Joy': 'Alegría',
 'Balance': 'Equilibrio',
 'Growth': 'Crecimiento',
 'Purpose': 'Propósito',
 'Mindfulness': 'Atención Plena',
 'Travel & Airport': 'Viajes y Aeropuerto',
 'Ordering Food & Dining': 'Pedir Comida y Comer Fuera',
 'Shopping & Prices': 'Compras y Precios',
 'Asking for Directions': 'Pedir Direcciones',
 'Hotel & Accommodation': 'Hotel y Alojamiento',
 'Daily Routine': 'Rutina Diaria',
 'Meeting People & Greetings': 'Conocer Gente y Saludos',
 'Emergency & Health': 'Emergencias y Salud',
 'Public Transportation': 'Transporte Público',
 'Work & Office': 'Trabajo y Oficina',
 'Weather & Small Talk': 'Clima y Conversación Ligera',
 'Coffee Shop & Bakery': 'Cafetería y Panadería',
 'Family & Home': 'Familia y Hogar',
 'Hobbies & Free Time': 'Pasatiempos y Tiempo Libre',
 'Dating & Romance': 'Citas y Romance',
 'Phone Calls & Messages': 'Llamadas y Mensajes',
 'Banking & Money': 'Banca y Dinero',
 'Doctor & Pharmacy': 'Médico y Farmacia',
 'Sports & Fitness': 'Deportes y Fitness',
 'Celebrations & Parties': 'Celebraciones y Fiestas',
 'Feelings & Emotions': 'Sentimientos y Emociones',
 'Agreeing & Disagreeing': 'Estar de Acuerdo y en Desacuerdo',
 'Making Plans': 'Hacer Planes',
 'Common Native Slang': 'Jerga Nativa Común',
 'Cultural Traditions': 'Tradiciones Culturales'}
# ==== CATEGORIES END ====

CATEGORY_NAMES = list(CATEGORIES.keys())

AI_MODEL = os.getenv("AI_MODEL", "openai/gpt-5.4-nano")
AI_FALLBACK_MODEL = os.getenv("AI_FALLBACK_MODEL", "gemini-fast")
POLLINATIONS_API_KEY = os.getenv("POLLINATIONS_API_KEY", "")

# ---------------------------------------------------------------- timing (seconds)

INTRO_DURATION = 7.2
CHAPTER_INTRO_DURATION = 4.4
OUTRO_DURATION = 13.0

EN_CARD_IN = 0.70
GAP_EN_NATIVE = 0.60
NATIVE_CARD_LEAD = 0.40
GAP_BEFORE_REPEAT = 1.00
TAIL_HOLD = 1.30

# ---------------------------------------------------------------- palette

INK = "#30303A"
MUTED = "#8A8A8A"
CREAM = "#FFF8E7"
GREEN = "#58CC02"
GREEN_DARK = "#46A302"
GREEN_DEEP = "#3D8F00"
BLUE = "#1CB0F6"
PURPLE = "#7C5CFF"
ORANGE = "#FF7A00"
RED = "#FF4B4B"
YELLOW = "#F5A700"
TEAL = "#00A889"
PINK = "#E056A0"

# ==== HASHTAGS START ====
HASHTAGS = ['#learnspanish',
 '#spanishlessons',
 '#spanishforbeginners',
 '#languagelearning',
 '#spanishvocabulary',
 '#velocityspanish',
 '#dailyspanish',
 '#spanish',
 '#learnlanguages',
 '#speakspanish']
# ==== HASHTAGS END ====
