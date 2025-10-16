from github import Github, Auth
import matplotlib.pyplot as plt
from collections import Counter
import os

# GitHub Actions token or Personal Access Token
token = os.environ.get("GITHUB_TOKEN")
g = Github(auth=Auth.Token(token))
user = g.get_user()

langs = Counter()

# Collect languages from all repositories
for repo in user.get_repos():
    for lang, size in repo.get_languages().items():
        langs[lang] += size

# Sort and take top 6 languages
langs = dict(sorted(langs.items(), key=lambda x: x[1], reverse=True)[:6])
total = sum(langs.values())

# Approximate GitHub Insights style colors
colors = ["#00B4AB", "#F0DB4F", "#8892BF", "#E34F26", "#F05340", "#A8B9CC"]

# Create horizontal bar chart
plt.figure(figsize=(8, 4))
bars = plt.barh(list(langs.keys()), [v / total * 100 for v in langs.values()], color=colors[:len(langs)])
plt.xlim(0, 100)
plt.gca().invert_yaxis()  # Largest bar on top

# Add percentages on bars
for bar, value in zip(bars, langs.values()):
    width = bar.get_width()
    plt.text(width + 1, bar.get_y() + bar.get_height() / 2, f"{width:.1f}%", va='center', fontsize=10)

plt.xlabel("Percentage of total code")
plt.title("Most Used Languages", fontsize=14)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['left'].set_visible(False)
plt.gca().spines['bottom'].set_visible(False)
plt.tight_layout()
plt.savefig("LANGS.png", transparent=True)
