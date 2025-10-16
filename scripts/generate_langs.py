from github import Github, Auth
import matplotlib.pyplot as plt
from collections import Counter
import os
import numpy as np

# --- 1. SETUP AND DATA COLLECTION ---
try:
    # GitHub Actions token
    token = os.environ.get("MY_PAT")
    if not token:
        raise ValueError("MY_PAT token not found.")

    g = Github(auth=Auth.Token(token))
    user = g.get_user()
    print(f"Authenticated as: {user.login}")

    # Create assets directory if it doesn't exist
    os.makedirs("assets", exist_ok=True)
    langs = Counter()

    # Organizations to ignore when collecting data
    organizations_to_ignore = ["EpicGames"]

    # print("Collecting data from repositories...")
    for repo in user.get_repos():
        # Get the repository owner
        owner_login = repo.owner.login
        # Skip repositories from specific organizations
        if owner_login in organizations_to_ignore:
            # print(f"Skipping organization repository {owner_login}: {repo.name}")
            continue
        for lang, size in repo.get_languages().items():
            langs[lang] += size
        # print("repos:", repo.name)

    # Get the top 6 languages
    top_langs = dict(sorted(langs.items(), key=lambda x: x[1], reverse=True)[:6])
    total_size = sum(top_langs.values())

    # Calculate percentage for each language
    lang_percentages = {
        lang: (size / total_size) * 100 for lang, size in top_langs.items()
    }
    # print("Data collection complete.")

except Exception as e:
    print(f"An error occurred during data collection: {e}")
    exit(1)

# --- 2. VISUAL CONFIGURATION ---

# Color sequence from the reference image.
# The first color will be for the most used language, the second for the next, and so on.
color_sequence = [
    "#00B4AB",  # 1st language (Teal)
    "#F0DB4F",  # 2nd language (Yellow)
    "#8892BF",  # 3rd language (Purple)
    "#f34b7d",  # 4th language (Pink)
    "#DA3434",  # 5th language (Red)
    "#F7523F",  # 6th language (Orange)
]
lang_color_map = {
    lang: color for lang, color in zip(lang_percentages.keys(), color_sequence)
}

# Theme colors
BG_COLOR = "#22272e"
TEXT_COLOR = "#b7c0c9"
TITLE_COLOR = "#58a6ff"

# Padding and Position Constants (Axes Coordinates: 0 to 1)
# Initial padding to align TITLE, BAR and LEGEND
LEFT_PADDING_AXES = 0.05
RIGHT_PADDING_AXES = 0.05

# Bar Position Constants
BAR_Y_POS = 0.88  # Y position (vertical) of the bar (near the top)
BAR_HEIGHT_AXES = 0.04  # Bar height in Axes
BAR_CENTER_Y = BAR_Y_POS  # Where the bar will be plotted

# Total width of the bar, discounting side paddings
BAR_WIDTH_AXES = 1.0 - LEFT_PADDING_AXES - RIGHT_PADDING_AXES

# --- 3. CHART CREATION ---

fig, ax = plt.subplots(
    # Width: 4 * 300 dpi = 1200px (plus bbox_tight = ~1260px)
    # Height: 1.2 * 300 dpi = 360px (plus bbox_tight = ~527px)
    figsize=(4, 1.2),
    facecolor=BG_COLOR,
    width_ratios=[5],
    height_ratios=[5],
)
ax.set_facecolor(BG_COLOR)

# Chart title
TITLE_FONT_SIZE = 14

ax.set_title(
    "Most Used Languages",
    color=TITLE_COLOR,
    fontsize=TITLE_FONT_SIZE,
    fontweight="bold",
    loc="left",  # Align to the left
    pad=15,  # Padding from the top
    x=LEFT_PADDING_AXES,  # Align title with left padding
)

# Create the stacked progress bar
bar_segments = list(lang_percentages.values())
bar_colors = list(lang_color_map.values())
bar_positions = np.cumsum([0] + bar_segments[:-1])
bar_positions_norm = bar_positions / 100.0  # Normalize to 0-1 (Axes width)
bar_segments_norm = np.array(bar_segments) / 100.0

# Draw the bar
for i in range(len(bar_segments)):
    # The left position is now the initial padding + the normalized position
    left_position = LEFT_PADDING_AXES + (bar_positions_norm[i] * BAR_WIDTH_AXES)

    # The width of the segment is the total width * the segment percentage
    segment_width = bar_segments_norm[i] * BAR_WIDTH_AXES

    ax.barh(
        [BAR_CENTER_Y],
        [segment_width],
        left=[left_position],  # Starting position
        height=BAR_HEIGHT_AXES,  # Bar height
        color=bar_colors[i],
        edgecolor=BG_COLOR,  # Edge color to create a small gap
        linewidth=0.005,
        transform=ax.transAxes,
    )

# Force the limit from 0 to 1 in X and Y
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)

# Remove all axis elements (spines, ticks, labels)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["bottom"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.tick_params(
    axis="both",
    which="both",
    bottom=False,
    top=False,
    left=False,
    right=False,
    labelbottom=False,
    labelleft=False,
)

# --- 4. CUSTOM LEGEND CREATION ---

# The legend is moved UP along with the bar
legend_y_start = BAR_Y_POS - BAR_HEIGHT_AXES - 0.18  # Starts a little below the bar
legend_y_step = 0.20  # Spacing between legend lines

legend_x_col1 = LEFT_PADDING_AXES  # Alignment of the first column
legend_x_col2 = 0.5  # Alignment of the second column

# Font and circle size
CIRCLE_FONT_SIZE = 12
FONT_SIZE = 10

for i, (lang, percentage) in enumerate(lang_percentages.items()):
    # Determine the position (row and column)
    col = i % 2
    row = i // 2

    x_pos = legend_x_col1 if col == 0 else legend_x_col2
    y_pos = legend_y_start - (row * legend_y_step)

    color = lang_color_map.get(lang, "#c9d1d9")

    # Colored legend circle
    ax.text(
        x_pos,
        y_pos,
        "●",
        color=color,
        fontsize=CIRCLE_FONT_SIZE,
        ha="left",
        va="center",
        transform=ax.transAxes,
    )

    # Legend text (Language Name and Percentage)
    ax.text(
        x_pos + 0.05,  # Small space after the circle
        y_pos - 0.014,  # Small vertical adjustment to better align with the circle
        f"{lang} {percentage:.2f}%",
        color=TEXT_COLOR,
        fontsize=FONT_SIZE,
        ha="left",
        va="center",
        transform=ax.transAxes,
    )

# --- 5. SAVING THE IMAGE ---

# Adjust layout to ensure nothing is clipped
plt.subplots_adjust(left=0.0, right=1.0, top=1.0, bottom=0.0)

output_path = "assets/LANGS.png"
plt.savefig(
    output_path,
    dpi=300,
    bbox_inches="tight",  # Essential to not clip the legend
    facecolor=BG_COLOR,
)
