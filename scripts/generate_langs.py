from github import Github, Auth
import matplotlib.pyplot as plt
from collections import Counter
import os

# --- 1. SETUP AND DATA COLLECTION ---
try:
    # GitHub Actions token
    token = os.environ.get("MY_PAT")
    if not token:
        raise ValueError("MY_PAT token not found. Please ensure the secret is configured.")
    
    g = Github(auth=Auth.Token(token))
    user = g.get_user()
    print(f"Authenticated as: {user.login}")

    # Create assets directory if it doesn't exist
    os.makedirs("assets", exist_ok=True)

    langs = Counter()

    # Collect languages from all repositories
    print("Collecting data from repositories...")
    for repo in user.get_repos():
        # Ignore forks for more accurate stats
        if repo.fork:
            continue
        for lang, size in repo.get_languages().items():
            langs[lang] += size
    print("Data collection complete.")

    # Sort and get the top 6 most used languages
    top_langs = dict(sorted(langs.items(), key=lambda x: x[1], reverse=True)[:6])
    total_size = sum(top_langs.values())
    
    # Convert byte sizes to percentages
    lang_percentages = {lang: (size / total_size) * 100 for lang, size in top_langs.items()}

except Exception as e:
    print(f"An error occurred during data collection: {e}")
    exit(1) # Exit script on API error

# --- 2. VISUAL CONFIGURATION ---

# Color sequence from the reference image.
# The first color will be for the most used language, the second for the next, and so on.
color_sequence = [
    "#00B4AB", # 1st language (Teal)
    "#F0DB4F", # 2nd language (Yellow)
    "#8892BF", # 3rd language (Purple)
    "#f34b7d", # 4th language (Pink)
    "#DA3434", # 5th language (Red)
    "#F7523F"  # 6th language (Orange)
]

# Map the retrieved top languages to the color sequence
lang_color_map = {lang: color for lang, color in zip(lang_percentages.keys(), color_sequence)}

# Theme colors
BG_COLOR = "#22272e"  # Dark background color
TEXT_COLOR = "#c9d1d9" # Light text color
TITLE_COLOR = "#58a6ff" # Blue title color

# --- 3. CHART CREATION ---

fig, ax = plt.subplots(figsize=(8, 2.5), facecolor=BG_COLOR)
ax.set_facecolor(BG_COLOR)

# Chart title
ax.set_title(
    "Most Used Languages",
    color=TITLE_COLOR,
    fontsize=18,
    fontweight='bold',
    loc='left', # Align to the left
    pad=20 # Padding from the top
)

# Create the stacked progress bar
left_offset = 0
for lang, percentage in lang_percentages.items():
    color = lang_color_map.get(lang, "#c9d1d9") # Use the mapped color, with a fallback
    ax.barh(
        [''], # Y position (empty to hide label)
        [percentage], # Bar width
        left=[left_offset],
        height=0.4, # Bar height
        color=color,
        edgecolor=BG_COLOR, # Edge color to create a small gap
        linewidth=1.5
    )
    left_offset += percentage

# Remove all axis elements (spines, ticks, labels)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.tick_params(axis='both', which='both', bottom=False, top=False, left=False, right=False, labelbottom=False, labelleft=False)

# --- 4. CUSTOM LEGEND CREATION ---

legend_y_start = -0.6 # Initial Y position for the legend
legend_y_step = -0.5  # Space between legend rows
legend_x_col1 = 0.0   # X position for the first column
legend_x_col2 = 0.5   # X position for the second column

for i, (lang, percentage) in enumerate(lang_percentages.items()):
    # Determine the position (row and column)
    col = i % 2
    row = i // 2
    
    x_pos = legend_x_col1 if col == 0 else legend_x_col2
    y_pos = legend_y_start + (row * legend_y_step)
    
    color = lang_color_map.get(lang, "#c9d1d9")

    # Colored legend circle
    ax.text(
        x_pos, 
        y_pos, 
        "●", 
        color=color,
        fontsize=14,
        ha='left',
        va='center'
    )
    
    # Legend text (Language Name and Percentage)
    ax.text(
        x_pos + 0.04, # Small space after the circle
        y_pos,
        f"{lang} {percentage:.2f}%",
        color=TEXT_COLOR,
        fontsize=12,
        ha='left',
        va='center'
    )

# --- 5. SAVING THE IMAGE ---

# Adjust layout to ensure nothing is clipped
plt.tight_layout(pad=0.5)

# Save the final image
output_path = "assets/LANGS.png"
plt.savefig(
    output_path, 
    dpi=300, # High resolution
    bbox_inches='tight', # Ensures the custom legend is not clipped
    facecolor=BG_COLOR
)
