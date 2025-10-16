from github import Github
import matplotlib.pyplot as plt
from collections import Counter
import os

# Token do GitHub Actions ou Personal Access Token
token = os.environ.get("GITHUB_TOKEN")
g = Github(token)
user = g.get_user()

langs = Counter()

# Coletar linguagens de todos os repositórios
for repo in user.get_repos():
    for lang, size in repo.get_languages().items():
        langs[lang] += size

# Ordenar e pegar top 6 linguagens
langs = dict(sorted(langs.items(), key=lambda x: x[1], reverse=True)[:6])
total = sum(langs.values())

# Cores aproximadas do estilo GitHub Insights
colors = ["#00B4AB", "#F0DB4F", "#8892BF", "#E34F26", "#F05340", "#A8B9CC"]

# Criar gráfico horizontal
plt.figure(figsize=(8,4))
bars = plt.barh(list(langs.keys()), [v/total*100 for v in langs.values()], color=colors[:len(langs)])
plt.xlim(0, 100)
plt.gca().invert_yaxis()  # Barra maior em cima

# Adicionar porcentagens na barra
for bar, value in zip(bars, langs.values()):
    width = bar.get_width()
    plt.text(width + 1, bar.get_y() + bar.get_height()/2, f"{width:.1f}%", va='center', fontsize=10)

plt.xlabel("Percentage of total code")
plt.title("Most Used Languages", fontsize=14)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['left'].set_visible(False)
plt.gca().spines['bottom'].set_visible(False)
plt.tight_layout()
plt.savefig("LANGS.png", transparent=True)
