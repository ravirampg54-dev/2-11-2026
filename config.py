"""
Central configuration for Goat Live Weight Estimation System.
"""
import os
from pathlib import Path

BASE_DIR = Path(__file__).parent

# ── Roboflow Configuration ──────────────────────────────────────────────────
ROBOFLOW_API_KEY     = os.getenv("ROBOFLOW_API_KEY", "YOUR_ROBOFLOW_API_KEY")
ROBOFLOW_WORKSPACE   = os.getenv("ROBOFLOW_WORKSPACE", "YOUR_WORKSPACE")
ROBOFLOW_PROJECT     = os.getenv("ROBOFLOW_PROJECT", "goat-detection")   # project slug
ROBOFLOW_VERSION     = int(os.getenv("ROBOFLOW_VERSION", "1"))

# ── Model Paths ──────────────────────────────────────────────────────────────
SEGMENTATION_MODEL   = str(BASE_DIR / "models" / "goat_segmentation.pt")
REGRESSION_MODEL     = str(BASE_DIR / "models" / "weight_regression.pkl")
MODEL_METRICS        = str(BASE_DIR / "models" / "model_metrics.json")

# ── Dataset ──────────────────────────────────────────────────────────────────
DATASET_DIR          = str(BASE_DIR / "dataset")
WEIGHTS_CSV          = str(BASE_DIR / "dataset" / "weights.csv")

# ── Uploads / Results ────────────────────────────────────────────────────────
UPLOAD_FOLDER        = str(BASE_DIR / "uploads")
RESULTS_FOLDER       = str(BASE_DIR / "results")

# ── Reference / Scale ────────────────────────────────────────────────────────
# Default reference object real-world length in centimetres
REFERENCE_LENGTH_CM  = 100.0

# ── YOLO ─────────────────────────────────────────────────────────────────────
YOLO_CONFIDENCE      = 0.40
YOLO_IOU             = 0.45
# Class name(s) the segmentation model assigns to goats
GOAT_CLASS_NAMES     = {"goat", "animal", "livestock", "sheep"}

# ── Image Quality Thresholds ──────────────────────────────────────────────────
MIN_GOAT_AREA_RATIO  = 0.05   # goat must occupy ≥5 % of the image
MAX_BLUR_VARIANCE    = 50.0   # Laplacian variance threshold (below = blurry)
MAX_GOAT_COUNT       = 1      # only one goat allowed per image

# ── Regression ───────────────────────────────────────────────────────────────
FEATURE_COLS = [
    "body_length_cm",
    "height_cm",
    "body_width_cm",
    "body_area_cm2",
    "chest_girth_cm",
]
TARGET_COL   = "actual_weight_kg"

# ── Physical Sanity Bounds ───────────────────────────────────────────────────
BOUNDS = {
    "body_length_cm": (20, 200),
    "height_cm":      (20, 150),
    "body_width_cm":  (10, 100),
    "body_area_cm2":  (100, 50_000),
    "actual_weight_kg": (1, 200),
}
