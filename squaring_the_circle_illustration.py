"""
Figure 3 — Squaring the circle
==============================

Illustration for Blog 5.

The figure shows the map

    d_i = c_i^2

for three representative points in the positive quadrant of the 2->1 RAC
advantage space:

    A: inside the quantum circle
    B: exactly on the quantum circle
    C: slightly outside the quantum circle

Under the map:

    c_1^2 + c_2^2 < 1  ->  d_1 + d_2 < 1
    c_1^2 + c_2^2 = 1  ->  d_1 + d_2 = 1
    c_1^2 + c_2^2 > 1  ->  d_1 + d_2 > 1

The central visual point is that the full quantum quarter-circle maps exactly
onto the classical one-bit RAC boundary d_1 + d_2 = 1.

Dependencies
------------
pip install numpy matplotlib
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import ConnectionPatch, Polygon
import numpy as np


# =============================================================================
# OUTPUT / LAYOUT
# =============================================================================

OUTPUT = Path(__file__).with_name("Figure_3_squaring_the_circle.png")

FIGURE_SIZE_INCH = (15.36, 8.90)
DPI = 200

LEFT_PANEL_BOX = [0.055, 0.16, 0.37, 0.68]
RIGHT_PANEL_BOX = [0.575, 0.16, 0.37, 0.68]

TITLE_SIZE = 22
SUBTITLE_SIZE = 14.5
PANEL_TITLE_SIZE = 15.5
FONT_SIZE = 13


# =============================================================================
# APPEARANCE
# Kept consistent with advantage_space_2D_Blog5_Fig1.py
# =============================================================================

QUANTUM_COLOR = "#E69F00"
QUANTUM_WIDTH = 2.6

NO_SIGNALLING_COLOR = "#555555"
NO_SIGNALLING_WIDTH = 1.6
NO_SIGNALLING_LINESTYLE = (0, (6, 4))

CLASSICAL_FILL_COLOR = "#0072B2"
CLASSICAL_FILL_ALPHA = 0.22
CLASSICAL_COLOR = "#00263D"
CLASSICAL_WIDTH = 2.2

AXIS_COLOR = "#111111"
AXIS_WIDTH = 1.20

DIAGONAL_COLOR = "#8A8A8A"
DIAGONAL_WIDTH = 1.20
DIAGONAL_LINESTYLE = (0, (4, 4))

MAPPING_ARROW_COLOR = "#777777"
MAPPING_ARROW_WIDTH = 1.15
MAPPING_ARROW_ALPHA = 0.72

POINT_INSIDE_COLOR = "#0072B2"
POINT_ON_COLOR = QUANTUM_COLOR
POINT_OUTSIDE_COLOR = "#555555"

MARKER_SIZE = 115
MARKER_EDGE_COLOR = "white"
MARKER_EDGE_WIDTH = 0.9

LABEL_SIZE = 12.2
FORMULA_SIZE = 13.0

SHOW_DIAGONAL_GUIDE = True
SHOW_MAPPING_ARROWS = True
SHOW_POINT_COORDINATES = True


# =============================================================================
# EXAMPLE POINTS
# =============================================================================

# Symmetric points make the geometry immediately readable.
POINTS_C = {
    "A": np.array([0.60, 0.60]),                       # inside
    "B": np.array([1.0 / np.sqrt(2.0)] * 2),          # on circle
    "C": np.array([0.80, 0.80]),                       # outside
}

POINT_COLORS = {
    "A": POINT_INSIDE_COLOR,
    "B": POINT_ON_COLOR,
    "C": POINT_OUTSIDE_COLOR,
}

POINT_DESCRIPTIONS = {
    "A": "inside",
    "B": "on the circle",
    "C": "outside",
}


# =============================================================================
# GEOMETRY
# =============================================================================

def quantum_quarter_circle(num: int = 600):
    theta = np.linspace(0.0, np.pi / 2.0, num)
    return np.cos(theta), np.sin(theta)


def classical_triangle():
    """Positive-quadrant part of |c1| + |c2| <= 1."""
    return np.array([
        [0.0, 0.0],
        [1.0, 0.0],
        [0.0, 1.0],
    ])


def no_signalling_positive_square():
    """Positive-quadrant logical region 0 <= c_i <= 1."""
    return np.array([
        [0.0, 0.0],
        [1.0, 0.0],
        [1.0, 1.0],
        [0.0, 1.0],
        [0.0, 0.0],
    ])


def square_map(point: np.ndarray) -> np.ndarray:
    """Apply d_i = c_i^2 coordinate-wise."""
    return point**2


# =============================================================================
# DRAWING HELPERS
# =============================================================================

def format_coord(point: np.ndarray) -> str:
    return f"({point[0]:.2f}, {point[1]:.2f})"


def setup_axes(ax, x_label: str, y_label: str):
    ax.set_xlim(-0.035, 1.08)
    ax.set_ylim(-0.035, 1.08)
    ax.set_aspect("equal", adjustable="box")

    # Coordinate axes.
    ax.axhline(0.0, color=AXIS_COLOR, linewidth=AXIS_WIDTH, zorder=7)
    ax.axvline(0.0, color=AXIS_COLOR, linewidth=AXIS_WIDTH, zorder=7)

    # Minimal ticks: enough to anchor 0 and 1 without turning the figure into
    # a conventional chart.
    ax.set_xticks([0.0, 0.5, 1.0])
    ax.set_yticks([0.0, 0.5, 1.0])
    ax.tick_params(axis="both", labelsize=10.5, length=3.5, width=0.8)

    for spine in ax.spines.values():
        spine.set_visible(False)

    ax.set_xlabel(x_label, fontsize=FONT_SIZE + 1, labelpad=6)
    ax.set_ylabel(y_label, fontsize=FONT_SIZE + 1, labelpad=8)


def draw_source_panel(ax):
    """Original c-space: classical triangle, quantum circle, NS square."""
    ns = no_signalling_positive_square()
    ax.plot(
        ns[:, 0], ns[:, 1],
        color=NO_SIGNALLING_COLOR,
        linewidth=NO_SIGNALLING_WIDTH,
        linestyle=NO_SIGNALLING_LINESTYLE,
        zorder=2,
    )

    tri = classical_triangle()
    ax.add_patch(
        Polygon(
            tri,
            closed=True,
            facecolor=CLASSICAL_FILL_COLOR,
            alpha=CLASSICAL_FILL_ALPHA,
            edgecolor="none",
            zorder=1,
        )
    )
    ax.plot(
        [1.0, 0.0],
        [0.0, 1.0],
        color=CLASSICAL_COLOR,
        linewidth=CLASSICAL_WIDTH,
        zorder=4,
    )

    qx, qy = quantum_quarter_circle()
    ax.plot(
        qx, qy,
        color=QUANTUM_COLOR,
        linewidth=QUANTUM_WIDTH,
        zorder=5,
    )

    if SHOW_DIAGONAL_GUIDE:
        ax.plot(
            [0.0, 1.02],
            [0.0, 1.02],
            color=DIAGONAL_COLOR,
            linewidth=DIAGONAL_WIDTH,
            linestyle=DIAGONAL_LINESTYLE,
            zorder=2,
        )

    setup_axes(ax, r"$c_1$", r"$c_2$")

    ax.set_title(
        "Before the classical relay",
        fontsize=PANEL_TITLE_SIZE,
        fontweight="bold",
        pad=14,
    )

    ax.text(
        0.06, 0.975,
        r"quantum boundary:  $c_1^2+c_2^2=1$",
        transform=ax.transAxes,
        fontsize=11.7,
        color=QUANTUM_COLOR,
        ha="left",
        va="top",
    )


def draw_destination_panel(ax):
    """Mapped d-space: classical one-bit boundary is the key object."""
    ns = no_signalling_positive_square()
    ax.plot(
        ns[:, 0], ns[:, 1],
        color=NO_SIGNALLING_COLOR,
        linewidth=NO_SIGNALLING_WIDTH,
        linestyle=NO_SIGNALLING_LINESTYLE,
        zorder=2,
    )

    tri = classical_triangle()
    ax.add_patch(
        Polygon(
            tri,
            closed=True,
            facecolor=CLASSICAL_FILL_COLOR,
            alpha=CLASSICAL_FILL_ALPHA,
            edgecolor="none",
            zorder=1,
        )
    )

    # Classical boundary.
    ax.plot(
        [1.0, 0.0],
        [0.0, 1.0],
        color=CLASSICAL_COLOR,
        linewidth=CLASSICAL_WIDTH + 0.5,
        zorder=5,
    )

    # A short orange annotation makes the coincidence explicit without
    # drawing a second, visually competing line on top of the same boundary.
    ax.annotate(
        "image of the\nquantum circle",
        xy=(0.52, 0.48),
        xytext=(0.77, 0.76),
        fontsize=11.5,
        color=QUANTUM_COLOR,
        ha="left",
        va="center",
        arrowprops=dict(
            arrowstyle="->",
            color=QUANTUM_COLOR,
            linewidth=1.25,
            shrinkA=3,
            shrinkB=5,
            mutation_scale=12,
        ),
        zorder=7,
    )

    if SHOW_DIAGONAL_GUIDE:
        ax.plot(
            [0.0, 1.02],
            [0.0, 1.02],
            color=DIAGONAL_COLOR,
            linewidth=DIAGONAL_WIDTH,
            linestyle=DIAGONAL_LINESTYLE,
            zorder=2,
        )

    setup_axes(ax, r"$d_1$", r"$d_2$")

    ax.set_title(
        "After  $d_i=c_i^2$",
        fontsize=PANEL_TITLE_SIZE,
        fontweight="bold",
        pad=14,
    )

    ax.text(
        0.06, 0.975,
        r"classical boundary:  $d_1+d_2=1$",
        transform=ax.transAxes,
        fontsize=11.7,
        color=CLASSICAL_COLOR,
        ha="left",
        va="top",
    )


def add_source_points(ax):
    offsets = {
        "A": (0.035, -0.075),
        "B": (0.035, 0.050),
        "C": (0.035, 0.050),
    }

    for key, point in POINTS_C.items():
        color = POINT_COLORS[key]
        ax.scatter(
            [point[0]], [point[1]],
            s=MARKER_SIZE,
            c=[color],
            edgecolors=MARKER_EDGE_COLOR,
            linewidths=MARKER_EDGE_WIDTH,
            zorder=10,
        )

        dx, dy = offsets[key]
        label = f"{key}  {POINT_DESCRIPTIONS[key]}"
        if SHOW_POINT_COORDINATES:
            label += f"\n{format_coord(point)}"

        ax.text(
            point[0] + dx,
            point[1] + dy,
            label,
            fontsize=LABEL_SIZE,
            color=color,
            ha="left",
            va="center",
            zorder=11,
        )


def add_destination_points(ax):
    offsets = {
        "A": (0.035, -0.070),
        "B": (0.035, -0.080),
        "C": (0.035, 0.055),
    }

    for key, source in POINTS_C.items():
        point = square_map(source)
        color = POINT_COLORS[key]

        ax.scatter(
            [point[0]], [point[1]],
            s=MARKER_SIZE,
            c=[color],
            edgecolors=MARKER_EDGE_COLOR,
            linewidths=MARKER_EDGE_WIDTH,
            zorder=10,
        )

        dx, dy = offsets[key]
        relation = point.sum()
        if key == "A":
            status = rf"$d_1+d_2={relation:.2f}<1$"
        elif key == "B":
            status = r"$d_1+d_2=1$"
        else:
            status = rf"$d_1+d_2={relation:.2f}>1$"

        label = f"{key}'"
        if SHOW_POINT_COORDINATES:
            label += f"  {format_coord(point)}"
        label += f"\n{status}"

        ax.text(
            point[0] + dx,
            point[1] + dy,
            label,
            fontsize=LABEL_SIZE,
            color=color,
            ha="left",
            va="center",
            zorder=11,
        )


def add_mapping_arrows(fig, ax_left, ax_right):
    if not SHOW_MAPPING_ARROWS:
        return

    for key, source in POINTS_C.items():
        target = square_map(source)

        con = ConnectionPatch(
            xyA=(source[0], source[1]),
            coordsA=ax_left.transData,
            xyB=(target[0], target[1]),
            coordsB=ax_right.transData,
            arrowstyle="-|>",
            mutation_scale=13,
            linewidth=MAPPING_ARROW_WIDTH,
            color=MAPPING_ARROW_COLOR,
            alpha=MAPPING_ARROW_ALPHA,
            shrinkA=8,
            shrinkB=8,
            connectionstyle="arc3,rad=0.0",
            zorder=3,
        )
        fig.add_artist(con)


def add_central_mapping_label(fig):
    fig.text(
        0.500,
        0.525,
        r"$d_i=c_i^2$",
        fontsize=18,
        fontweight="bold",
        ha="center",
        va="center",
        color="#333333",
    )

    fig.text(
        0.500,
        0.475,
        "square each advantage",
        fontsize=11.5,
        ha="center",
        va="center",
        color="#555555",
    )


def add_bottom_note(fig):
    fig.text(
        0.50,
        0.065,
        r"inside $\rightarrow$ inside      •      circle $\rightarrow$ classical edge      •      outside $\rightarrow$ outside",
        fontsize=13.0,
        ha="center",
        va="center",
        color="#333333",
    )


# =============================================================================
# FIGURE
# =============================================================================

def compose():
    fig = plt.figure(
        figsize=FIGURE_SIZE_INCH,
        dpi=DPI,
        facecolor="white",
    )

    fig.text(
        0.035,
        0.955,
        "Squaring the circle",
        fontsize=TITLE_SIZE,
        fontweight="bold",
        ha="left",
        va="top",
    )

    fig.text(
        0.035,
        0.910,
        "Under a classical relay, identical RAC biases multiply:  $d_i=c_i^2$.",
        fontsize=SUBTITLE_SIZE,
        ha="left",
        va="top",
    )

    ax_left = fig.add_axes(LEFT_PANEL_BOX)
    ax_right = fig.add_axes(RIGHT_PANEL_BOX)

    draw_source_panel(ax_left)
    draw_destination_panel(ax_right)

    add_source_points(ax_left)
    add_destination_points(ax_right)
    add_mapping_arrows(fig, ax_left, ax_right)
    add_central_mapping_label(fig)
    add_bottom_note(fig)

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
