import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "Unemployment in India.csv")
OUTPUT_DIR = os.path.join(BASE_DIR, "outputs", "figures")

os.makedirs(OUTPUT_DIR, exist_ok=True)

FIGURE_DPI = 150
FIGURE_SIZE = (12, 6)