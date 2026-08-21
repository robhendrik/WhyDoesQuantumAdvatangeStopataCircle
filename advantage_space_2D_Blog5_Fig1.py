"""
Figure 1 — The 2->1 RAC advantage space
========================================

The opening figure for the post. Deliberately minimal: three nested
regions in RAC advantage coordinates

    c_i = 2 P_i - 1

- classical one-bit strategies:  |c1| + |c2| <= 1   (diamond)
- quantum-assisted strategies:   c1^2 + c2^2 <= 1   (circle)
- logically possible / no-signalling: |c1| <= 1, |c2| <= 1  (square)

Four points are marked along the positive quadrant:

    (1, 0)                      -- perfect axis strategy
    (0, 1)                      -- perfect axis strategy
    (1/sqrt(2), 1/sqrt(2))      -- symmetric quantum point
    (1, 1)                      -- no-signalling / PR-box corner

No mutual-information boundary here -- that curve belongs to a later
figure. This one's only job is to put the central question in front of
the reader immediately: why does Nature stop at the circle?

Dependencies
------------
pip install numpy matplotlib
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


# =============================================================================
# OUTPUT / LAYOUT
# =============================================================================

OUTPUT = Path(__file__).with_name("Figure_1_blog5.png")

FIGURE_SIZE_INCH = (15.36, 10.24)
DPI = 200

LEFT_IMAGE_BOX = [0.055, 0.13, 0.60, 0.72]
RIGHT_LEGEND_BOX = [0.69, 0.2, 0.27, 0.42]


# =============================================================================
# APPEARANCE (unchanged palette, kept consistent with the rest of the series)
# =============================================================================

QUANTUM_COLOR = "#E69F00"
QUANTUM_WIDTH = 2.4

NO_SIGNALLING_COLOR = "#555555"
NO_SIGNALLING_WIDTH = 1.8
NO_SIGNALLING_LINESTYLE = (0, (6, 4))

CLASSICAL_FILL_COLOR = "#0072B2"
CLASSICAL_FILL_ALPHA = 0.30
CLASSICAL_COLOR = "#00263D"
CLASSICAL_WIDTH = 2.0
CLASSICAL_LINESTYLE = "-"

AXIS_POINT_COLOR = "#00263D"        # same as classical boundary
QUANTUM_POINT_COLOR = "#E69F00"     # same as quantum boundary
NO_SIGNALLING_POINT_COLOR = "#555555"  # same as no-signalling square

AXIS_COLOR = "#111111"
AXIS_WIDTH = 1.25

DIAGONAL_COLOR = "#8A8A8A"
DIAGONAL_WIDTH = 1.25
DIAGONAL_LINESTYLE = (0, (4, 4))

MARKER_SIZE = 95
MARKER_EDGE_COLOR = "white"
MARKER_EDGE_WIDTH = 0.8

FONT_SIZE = 13
TITLE_SIZE = 22
SUBTITLE_SIZE = 14.5

ARROW_WIDTH = 1.4
ARROW_HEAD_SCALE = 13


# =============================================================================
# SHAPES
# =============================================================================

def quantum_circle(num=1000):
    theta = np.linspace(0.0, 2.0 * np.pi, num)
    return np.cos(theta), np.sin(theta)


def classical_diamond():
    return np.array([
        [ 1.0,  0.0],
        [ 0.0,  1.0],
        [-1.0,  0.0],
        [ 0.0, -1.0],
        [ 1.0,  0.0],
    ])


def no_signalling_square():
    """Outer logical/no-signalling RAC region |c1|<=1, |c2|<=1."""
    return np.array([
        [ 1.0,  1.0],
        [-1.0,  1.0],
        [-1.0, -1.0],
        [ 1.0, -1.0],
        [ 1.0,  1.0],
    ])


# =============================================================================
# ANNOTATIONS
# =============================================================================

def add_point_with_arrow(
    ax,
    point,
    text,
    text_xy,
    color,
    ha="left",
    va="center",
):
    """Draw one marker and an arrow-labelled annotation."""
    x, y = point

    ax.scatter(
        [x], [y],
        s=MARKER_SIZE,
        c=[color],
        edgecolors=MARKER_EDGE_COLOR,
        linewidths=MARKER_EDGE_WIDTH,
        zorder=8,
    )

    ax.annotate(
        text,
        xy=(x, y),
        xytext=text_xy,
        fontsize=12.5,
        color=color,
        ha=ha,
        va=va,
        arrowprops=dict(
            arrowstyle="->",
            color=color,
            linewidth=ARROW_WIDTH,
            shrinkA=3,
            shrinkB=6,
            mutation_scale=ARROW_HEAD_SCALE,
            relpos=(0.0, 0.5),
        ),
        zorder=9,
    )


# =============================================================================
# FIGURE
# =============================================================================

def draw_main_panel(fig):
    ax = fig.add_axes(LEFT_IMAGE_BOX)

    # -------------------------------------------------------------------------
    # Full four-quadrant shapes
    # -------------------------------------------------------------------------

    # Outermost logically possible / no-signalling region.
    ns_square = no_signalling_square()
    ax.plot(
        ns_square[:, 0],
        ns_square[:, 1],
        color=NO_SIGNALLING_COLOR,
        linewidth=NO_SIGNALLING_WIDTH,
        linestyle=NO_SIGNALLING_LINESTYLE,
        zorder=3,
    )

    diamond = classical_diamond()
    ax.fill(
        diamond[:, 0],
        diamond[:, 1],
        facecolor=CLASSICAL_FILL_COLOR,
        alpha=CLASSICAL_FILL_ALPHA,
        edgecolor="none",
        zorder=2,
    )
    ax.plot(
        diamond[:, 0],
        diamond[:, 1],
        color=CLASSICAL_COLOR,
        linewidth=CLASSICAL_WIDTH,
        linestyle=CLASSICAL_LINESTYLE,
        zorder=4,
    )

    qx, qy = quantum_circle()
    ax.plot(
        qx, qy,
        color=QUANTUM_COLOR,
        linewidth=QUANTUM_WIDTH,
        zorder=5,
    )

    # -------------------------------------------------------------------------
    # Coordinate axes
    # -------------------------------------------------------------------------

    ax.axhline(0.0, color=AXIS_COLOR, linewidth=AXIS_WIDTH, zorder=6)
    ax.axvline(0.0, color=AXIS_COLOR, linewidth=AXIS_WIDTH, zorder=6)

    # -------------------------------------------------------------------------
    # Symmetric direction: positive quadrant only
    # -------------------------------------------------------------------------

    ax.plot(
        [0.0, 1.235],
        [0.0, 1.235],
        color=DIAGONAL_COLOR,
        linewidth=DIAGONAL_WIDTH,
        linestyle=DIAGONAL_LINESTYLE,
        zorder=3,
    )

    ax.text(
        1.10, 1.10,
        "(1,1) diagonal",
        fontsize=12.2,
        color="#333333",
        ha="left",
        va="bottom",
    )

    # -------------------------------------------------------------------------
    # Four marked points: (1,0), (0,1), symmetric quantum, PR-box corner
    # -------------------------------------------------------------------------

    c_q = 1.0 / np.sqrt(2.0)

    add_point_with_arrow(
        ax,
        (1.0, 0.0),
        "perfect bit 1",
        (1.10, 0.18),
        AXIS_POINT_COLOR,
    )

    add_point_with_arrow(
        ax,
        (0.0, 1.0),
        "perfect bit 2",
        (-0.2, 1.15),
        AXIS_POINT_COLOR,
        ha="left",
    )

    add_point_with_arrow(
        ax,
        (c_q, c_q),
        "symmetric quantum point",
        (1.10, 0.80),
        QUANTUM_POINT_COLOR,
    )

    add_point_with_arrow(
        ax,
        (1.0, 1.0),
        "no-signalling / PR-box limit",
        (1.10, 1.00),
        NO_SIGNALLING_POINT_COLOR,
    )

    # -------------------------------------------------------------------------
    # Axis labels (kept clear of the (1,0)/(0,1) point annotations)
    # -------------------------------------------------------------------------

    ax.text(
        1.14, -0.06,
        r"$c_1$",
        fontsize=FONT_SIZE + 1,
        color=AXIS_COLOR,
        ha="right",
        va="top",
    )
    ax.text(
        +0.075, 1.065,
        r"$c_2$",
        fontsize=FONT_SIZE + 1,
        color=AXIS_COLOR,
        ha="right",
        va="top",
    )

    ax.set_xlim(-1.08, 1.16)
    ax.set_ylim(-1.08, 1.08)
    ax.set_aspect("equal", adjustable="box")
    ax.axis("off")


def add_legend(fig):
    """Boundary legend only; point labels are placed directly on the figure."""
    ax = fig.add_axes(RIGHT_LEGEND_BOX)
    ax.set_axis_off()

    ax.text(
        0.0, 0.98,
        "Boundaries in advantage space",
        fontsize=14.5,
        fontweight="bold",
        ha="left",
        va="top",
        transform=ax.transAxes,
    )

    rows = [
        (
            0.68,
            NO_SIGNALLING_COLOR,
            NO_SIGNALLING_LINESTYLE,
            "No-signalling / PR-box limit",
            r"$|c_1|\leq 1,\ |c_2|\leq 1$",
        ),
        (
            0.38,
            QUANTUM_COLOR,
            "-",
            "Quantum",
            r"$c_1^2+c_2^2=1$",
        ),
        (
            0.08,
            CLASSICAL_COLOR,
            CLASSICAL_LINESTYLE,
            "Classical",
            r"$|c_1|+|c_2|=1$",
        ),
    ]

    for y, color, ls, title, formula in rows:
        ax.plot(
            [0.02, 0.19],
            [y, y],
            color=color,
            linewidth=2.5,
            linestyle=ls,
            transform=ax.transAxes,
            clip_on=False,
        )
        ax.text(
            0.25,
            y + 0.055,
            title,
            fontsize=12.5,
            fontweight="bold",
            color=color,
            ha="left",
            va="center",
            transform=ax.transAxes,
        )
        ax.text(
            0.25,
            y - 0.055,
            formula,
            fontsize=10.7,
            color="black",
            ha="left",
            va="center",
            transform=ax.transAxes,
        )


def compose():
    fig = plt.figure(
        figsize=FIGURE_SIZE_INCH,
        dpi=DPI,
        facecolor="white",
    )

    fig.text(
        0.035,
        0.955,
        "The 2\u21921 RAC advantage space",
        fontsize=TITLE_SIZE,
        fontweight="bold",
        ha="left",
        va="top",
    )

    fig.text(
        0.035,
        0.915,
        "Classical, quantum, and logically possible correlations. Why does Nature stop at the circle?",
        fontsize=SUBTITLE_SIZE,
        ha="left",
        va="top",
    )

    draw_main_panel(fig)
    add_legend(fig)

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
