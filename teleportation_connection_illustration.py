"""
Teleportation / entanglement-swapping connection illustration
==============================================================

Reproducible Matplotlib recreation using a stored telephone PNG icon.

Expected files in the SAME directory as this script:
    phone_icon_2.png

The figure shows:
- Before entanglement swapping:
      Alice -- Charlie      Charlie -- Bob
- After entanglement swapping:
      Alice ---------------------- Bob
      Charlie is out of the final connection.

The telephone icon is imported from PNG; cords, dashed boxes, labels and
annotations are drawn in Matplotlib.

Dependencies
------------
pip install numpy matplotlib
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.offsetbox import AnnotationBbox, OffsetImage
from matplotlib.patches import Rectangle


# =============================================================================
# FILES / OUTPUT
# =============================================================================

SCRIPT_DIR = Path(__file__).resolve().parent

PHONE_ICON = SCRIPT_DIR / "phone_icon_2.png"
OUTPUT = SCRIPT_DIR / "TeleportationConnection_AliceCharlieBob.png"

FIGURE_SIZE_INCH = (13.60, 6.90)
DPI = 200


# =============================================================================
# APPEARANCE
# =============================================================================

BLACK = "#111111"
GREY = "#666666"

CORD_LINEWIDTH = 2.4
BOX_LINEWIDTH = 2.0

FONT_SIZE = 14
SMALL_FONT = 12.5
TITLE_SIZE = 18

PHONE_ZOOM = 0.23

# Set True if you want near-white pixels of the PNG to become transparent.
# On a white background there is usually no visual difference, but it helps
# if you later change the figure background.
MAKE_WHITE_TRANSPARENT = False

# Remove empty white border around icon automatically.
AUTO_CROP_ICON = True


# =============================================================================
# LAYOUT
# =============================================================================

X_ALICE = 1.20
X_CHARLIE_LEFT = 3.25
X_CHARLIE_RIGHT = 5.35
X_BOB = 7.40

Y_TOP_PHONE = 4.95
Y_TOP_CORD = 4.70
Y_TOP_LABEL = 4.25

Y_BOTTOM_PHONE = 2.20
Y_BOTTOM_CORD = 1.95
Y_BOTTOM_LABEL = 1.48

CHARLIE_BOX_X0 = 2.45
CHARLIE_BOX_W = 3.65
CHARLIE_BOX_H = 1.55
CHARLIE_BOX_Y_TOP = 4.00
CHARLIE_BOX_Y_BOTTOM = 1.15

TEXT_X = 8.30

BOTTOM_CAPTION = (
    "Entanglement swapping can be pictured as coupling two connections at Charlie: "
    "the outer parties become directly connected\nwhile Charlie drops out of the final link."
)


# =============================================================================
# ICON HANDLING
# =============================================================================

def _to_rgba(img: np.ndarray) -> np.ndarray:
    """Return an RGBA float image regardless of input channel count."""
    if img.ndim != 3:
        raise ValueError("Expected an RGB or RGBA image.")

    if img.shape[2] == 4:
        rgba = img.copy()
    elif img.shape[2] == 3:
        alpha = np.ones((*img.shape[:2], 1), dtype=img.dtype)
        rgba = np.concatenate([img, alpha], axis=2)
    else:
        raise ValueError(f"Unsupported image shape: {img.shape}")

    return rgba


def _crop_white_border(rgba: np.ndarray, threshold: float = 0.97) -> np.ndarray:
    """Crop outer rows/columns that are almost entirely white."""
    rgb = rgba[..., :3]
    alpha = rgba[..., 3]

    non_white = np.any(rgb < threshold, axis=2) & (alpha > 0.01)

    if not np.any(non_white):
        return rgba

    ys, xs = np.where(non_white)
    y0, y1 = ys.min(), ys.max() + 1
    x0, x1 = xs.min(), xs.max() + 1

    pad = 4
    y0 = max(0, y0 - pad)
    y1 = min(rgba.shape[0], y1 + pad)
    x0 = max(0, x0 - pad)
    x1 = min(rgba.shape[1], x1 + pad)

    return rgba[y0:y1, x0:x1]


def load_phone_icon() -> np.ndarray:
    """Load the phone icon from the script directory."""
    if not PHONE_ICON.exists():
        raise FileNotFoundError(
            f"Could not find {PHONE_ICON.name!r} next to the script.\n"
            f"Expected path: {PHONE_ICON}"
        )

    rgba = _to_rgba(mpimg.imread(PHONE_ICON))

    if AUTO_CROP_ICON:
        rgba = _crop_white_border(rgba)

    if MAKE_WHITE_TRANSPARENT:
        rgb = rgba[..., :3]
        near_white = np.all(rgb > 0.97, axis=2)
        rgba[near_white, 3] = 0.0

    return rgba


PHONE_IMG = load_phone_icon()


def add_phone(ax, x, y, zoom=PHONE_ZOOM):
    """Place one telephone icon centred at data coordinate (x, y)."""
    image = OffsetImage(PHONE_IMG, zoom=zoom)
    box = AnnotationBbox(
        image,
        (x, y),
        frameon=False,
        box_alignment=(0.5, 0.5),
        pad=0.0,
        zorder=10,
    )
    ax.add_artist(box)


# =============================================================================
# DRAWING HELPERS
# =============================================================================

def draw_coiled_cord(
    ax,
    x0,
    x1,
    y,
    loops=10,
    radius=0.11,
    lead=0.15,
    color=BLACK,
):
    """
    Draw an old-fashioned coiled telephone cord.

    Unlike a simple sine wave, this traces a sequence of small circular loops
    while the centre of the loop advances horizontally. In a 2D drawing this
    gives the visual impression of a tightly wound spiral/telephone cable.
    """
    if x1 <= x0:
        raise ValueError("x1 must be greater than x0.")

    coil_x0 = x0 + lead
    coil_x1 = x1 - lead
    coil_length = coil_x1 - coil_x0

    ax.plot(
        [x0, coil_x0],
        [y, y],
        color=color,
        linewidth=CORD_LINEWIDTH,
        solid_capstyle="round",
        zorder=3,
    )

    # Parametric projection of a helix:
    # the centre advances along x while each turn traces a small circle.
    # A small x-component in the circular motion makes the loops visibly
    # curl back on themselves instead of looking like a plain sine wave.
    t = np.linspace(0.0, 1.0, max(1200, loops * 140))
    phase = 2.0 * np.pi * loops * t

    centre_x = coil_x0 + coil_length * t
    x = centre_x + radius * np.cos(phase)
    yy = y + radius * np.sin(phase)

    ax.plot(
        x,
        yy,
        color=color,
        linewidth=CORD_LINEWIDTH,
        solid_capstyle="round",
        solid_joinstyle="round",
        zorder=3,
    )

    ax.plot(
        [coil_x1, x1],
        [y, y],
        color=color,
        linewidth=CORD_LINEWIDTH,
        solid_capstyle="round",
        zorder=3,
    )


def add_bullet_block(ax, x, y_top, heading, lines):
    """Add a heading and compact dash-list."""
    ax.text(
        x,
        y_top,
        heading,
        fontsize=FONT_SIZE,
        ha="left",
        va="top",
        color=BLACK,
    )

    y = y_top - 0.35
    for line in lines:
        ax.text(
            x,
            y,
            f"–     {line}",
            fontsize=FONT_SIZE,
            ha="left",
            va="top",
            color=BLACK,
        )
        y -= 0.31


def strike_label(ax, x, y, text):
    """Draw a centred label with a strike-through."""
    ax.text(
        x,
        y,
        text,
        fontsize=FONT_SIZE,
        ha="center",
        va="center",
        color=BLACK,
    )

    # Fixed line length works well for "Charlie".
    ax.plot(
        [x - 0.48, x + 0.48],
        [y, y],
        color=BLACK,
        linewidth=1.4,
        zorder=12,
    )


# =============================================================================
# FIGURE
# =============================================================================

def compose():
    fig, ax = plt.subplots(
        figsize=FIGURE_SIZE_INCH,
        dpi=DPI,
        facecolor="white",
    )

    ax.set_xlim(0.0, 13.6)
    ax.set_ylim(0.0, 6.9)
    ax.axis("off")

    # -------------------------------------------------------------------------
    # TOP ROW — before entanglement swapping
    # -------------------------------------------------------------------------

    # Two separate telephone connections.
    draw_coiled_cord(
        ax,
        X_ALICE + 0.43,
        X_CHARLIE_LEFT - 0.43,
        Y_TOP_CORD,
        loops=8,
        radius=0.11,
    )
    draw_coiled_cord(
        ax,
        X_CHARLIE_RIGHT + 0.43,
        X_BOB - 0.43,
        Y_TOP_CORD,
        loops=8,
        radius=0.11,
    )

    # Four phone endpoints.
    add_phone(ax, X_ALICE, Y_TOP_PHONE)
    add_phone(ax, X_CHARLIE_LEFT, Y_TOP_PHONE)
    add_phone(ax, X_CHARLIE_RIGHT, Y_TOP_PHONE)
    add_phone(ax, X_BOB, Y_TOP_PHONE)

    # Charlie's local lab encloses his two endpoints.
    ax.add_patch(
        Rectangle(
            (CHARLIE_BOX_X0, CHARLIE_BOX_Y_TOP),
            CHARLIE_BOX_W,
            CHARLIE_BOX_H,
            fill=False,
            edgecolor=BLACK,
            linewidth=BOX_LINEWIDTH,
            linestyle="--",
            zorder=2,
        )
    )

    ax.text(
        X_ALICE,
        Y_TOP_LABEL,
        "Alice",
        fontsize=FONT_SIZE,
        ha="center",
        va="top",
    )
    ax.text(
        (X_CHARLIE_LEFT + X_CHARLIE_RIGHT) / 2,
        Y_TOP_LABEL,
        "Charlie",
        fontsize=FONT_SIZE,
        ha="center",
        va="top",
    )
    ax.text(
        X_BOB,
        Y_TOP_LABEL,
        "Bob",
        fontsize=FONT_SIZE,
        ha="center",
        va="top",
    )

    add_bullet_block(
        ax,
        TEXT_X,
        5.72,
        "Before entanglement swapping:",
        [
            "Alice and Charlie are connected",
            "Charlie and Bob are connected",
            "Alice and Bob are not connected",
        ],
    )

    # -------------------------------------------------------------------------
    # BOTTOM ROW — after entanglement swapping
    # -------------------------------------------------------------------------

    # One end-to-end connection.
    draw_coiled_cord(
        ax,
        X_ALICE + 0.43,
        X_BOB - 0.43,
        Y_BOTTOM_CORD,
        loops=23,
        radius=0.11,
    )

    add_phone(ax, X_ALICE, Y_BOTTOM_PHONE)
    add_phone(ax, X_BOB, Y_BOTTOM_PHONE)

    # Charlie's old local position remains visible, but empty.
    ax.add_patch(
        Rectangle(
            (CHARLIE_BOX_X0, CHARLIE_BOX_Y_BOTTOM),
            CHARLIE_BOX_W,
            CHARLIE_BOX_H,
            fill=False,
            edgecolor=BLACK,
            linewidth=BOX_LINEWIDTH,
            linestyle="--",
            zorder=2,
        )
    )

    ax.text(
        X_ALICE,
        Y_BOTTOM_LABEL,
        "Alice",
        fontsize=FONT_SIZE,
        ha="center",
        va="top",
    )

    strike_label(
        ax,
        (X_CHARLIE_LEFT + X_CHARLIE_RIGHT) / 2,
        Y_BOTTOM_LABEL - 0.04,
        "Charlie",
    )

    ax.text(
        X_BOB,
        Y_BOTTOM_LABEL,
        "Bob",
        fontsize=FONT_SIZE,
        ha="center",
        va="top",
    )

    add_bullet_block(
        ax,
        TEXT_X,
        2.93,
        "After entanglement swapping:",
        [
            "Alice and Bob are connected",
            "Charlie is out of the final connection",
        ],
    )

    # -------------------------------------------------------------------------
    # Bottom caption
    # -------------------------------------------------------------------------

    ax.text(
        0.50,
        0.48,
        BOTTOM_CAPTION,
        fontsize=SMALL_FONT,
        ha="left",
        va="bottom",
        color=BLACK,
        wrap=True,
    )

    fig.savefig(
        OUTPUT,
        dpi=DPI,
        facecolor="white",
        bbox_inches=None,
    )
    plt.close(fig)


def main():
    compose()
    print(f"Saved: {OUTPUT}")


if __name__ == "__main__":
    main()