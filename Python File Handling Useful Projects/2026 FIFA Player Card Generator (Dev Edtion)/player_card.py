"""
=====================================================================
 FIFA Ultimate Team (FUT) Style Coding Player Card Generator
=====================================================================

Run this script:

    python player.py

It will ask a few questions in the terminal, then generate a premium,
original, football-card-inspired "Legendary Gold" coding player card
as a single self-contained HTML file:

    Your Player Card.html

No database. No backend. No JavaScript. No external Python packages.
Just open the generated HTML file in any browser.
=====================================================================
"""

import webbrowser
import os


# ---------------------------------------------------------------------------
# Small input helpers
# ---------------------------------------------------------------------------

def ask_text(prompt, default=""):
    """Ask for a free-text answer. Falls back to `default` if left blank."""
    value = input(prompt).strip()
    return value if value else default


def ask_yes_no(prompt):
    """Ask a Yes/No question. Returns True for yes, False for no."""
    while True:
        answer = input(prompt + " (Yes/No): ").strip().lower()
        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False
        print("  Please answer with Yes or No.")


def ask_rating(prompt):
    """Ask for a 0-100 rating. Keeps asking until a valid number is given."""
    while True:
        raw = input(prompt + " (0-100): ").strip()
        try:
            value = int(raw)
        except ValueError:
            print("  Please enter a whole number between 0 and 100.")
            continue
        if 0 <= value <= 100:
            return value
        print("  Please enter a number between 0 and 100.")


# ---------------------------------------------------------------------------
# 1. Collect basic player info
# ---------------------------------------------------------------------------

print("=" * 60)
print(" FIFA ULTIMATE TEAM STYLE CODING PLAYER CARD GENERATOR")
print("=" * 60)
print()

player_name = ask_text("Name : ", default="Unknown Coder")
jersey_number = ask_text("Jersey Number : ", default="10")
photo_url = ask_text(
    "Player Photo URL : ",
    default="https://placehold.co/500x600/1a1a1a/d4af37?text=Player",
)
flag_url = ask_text(
    "Country Flag URL : ",
    default="https://placehold.co/40x28/1a1a1a/d4af37?text=%20",
)

print()
print("--- Technology Knowledge (Yes / No) ---")
knows_html = ask_yes_no("Do you know HTML?")
knows_css = ask_yes_no("Do you know CSS?")
knows_bootstrap = ask_yes_no("Do you know Bootstrap?")
knows_tailwind = ask_yes_no("Do you know Tailwind CSS?")
knows_js = ask_yes_no("Do you know JavaScript?")
knows_react = ask_yes_no("Do you know React?")
knows_python = ask_yes_no("Do you know Python?")
knows_git = ask_yes_no("Do you know Git?")
knows_github = ask_yes_no("Do you know GitHub?")

print()
print("--- Skill Ratings (0 - 100) ---")
rating_python = ask_rating("Python Skill")
rating_js = ask_rating("JavaScript Skill")
rating_problem = ask_rating("Problem Solving")
rating_ui = ask_rating("UI Design")
rating_database = ask_rating("Database")
rating_communication = ask_rating("Communication")


# ---------------------------------------------------------------------------
# 2. Compute Overall Rating (0-99, FIFA-style cap)
# ---------------------------------------------------------------------------

all_ratings = [
    rating_python,
    rating_js,
    rating_problem,
    rating_ui,
    rating_database,
    rating_communication,
]
overall_rating = round(sum(all_ratings) / len(all_ratings))
overall_rating = min(overall_rating, 99)  # legendary cards never show 100


# ---------------------------------------------------------------------------
# 3. Determine Player Position (FRONTEND / BACKEND / FULL STACK)
# ---------------------------------------------------------------------------

# Frontend leaning = JavaScript + UI Design
# Backend leaning  = Python + Database
frontend_score = (rating_js + rating_ui) / 2
backend_score = (rating_python + rating_database) / 2
diff = frontend_score - backend_score

if abs(diff) <= 8:
    position = "FULL STACK"
elif diff > 0:
    position = "FRONTEND"
else:
    position = "BACKEND"


# ---------------------------------------------------------------------------
# 4. Build Technology Badges (only the ones the player knows)
# ---------------------------------------------------------------------------

badge_data = [
    (knows_html, "HTML"),
    (knows_css, "CSS"),
    (knows_bootstrap, "Bootstrap"),
    (knows_tailwind, "Tailwind CSS"),
    (knows_js, "JavaScript"),
    (knows_react, "React"),
    (knows_python, "Python"),
    (knows_git, "Git"),
    (knows_github, "GitHub"),
]

known_labels = [label for known, label in badge_data if known]

badges_html = ""
for label in known_labels:
    badges_html += f'<span class="tech-badge">{label}</span>\n'

if not badges_html:
    badges_html = '<span class="tech-badge">No Skills Selected</span>'


# ---------------------------------------------------------------------------
# 5. Build Skill Stats block (two-column football-card style stat list)
# ---------------------------------------------------------------------------

# HTML / CSS don't have their own numeric rating input (only Yes/No),
# so we derive a display value from related ratings when known.
html_stat = round((rating_js + rating_ui) / 2) if knows_html else None
css_stat = round((rating_ui + rating_js) / 2) if knows_css else None

stat_rows = [
    ("HTML", html_stat),
    ("CSS", css_stat),
    ("PYTHON", rating_python),
    ("JAVASCRIPT", rating_js),
    ("PROBLEM", rating_problem),
    ("DATABASE", rating_database),
]

# Only show stats that actually apply (HTML/CSS hidden if unknown)
stat_rows = [(label, value) for label, value in stat_rows if value is not None]

stats_html = ""
for label, value in stat_rows:
    stats_html += (
        '<div class="stat-row">'
        f'<span class="stat-label">{label}</span>'
        f'<span class="stat-value">{value}</span>'
        "</div>\n"
    )


# ---------------------------------------------------------------------------
# 6. HTML Template (Bootstrap 5 + Bootstrap Icons, no JavaScript)
# ---------------------------------------------------------------------------

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{{PLAYER_NAME}} - Legendary Coding Card</title>

<!-- Bootstrap 5 (CDN) -->
<link href="https://cdn.jsdelivr.net/npm/[email protected]/dist/css/bootstrap.min.css" rel="stylesheet">
<!-- Bootstrap Icons (CDN) -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/[email protected]/font/bootstrap-icons.css">

<style>
  :root {
    --gold: #d9b24c;
    --gold-bright: #f6e5ad;
    --gold-deep: #8a6a22;
    --card-black: #0c0b10;
    --card-purple: #201830;
  }

  * { box-sizing: border-box; }
  html, body { height: 100%; }

  body {
    margin: 0;
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 40px 16px;
    font-family: 'Arial Narrow', 'Segoe UI', system-ui, -apple-system, sans-serif;

    background:
      radial-gradient(circle at 50% 15%, rgba(217, 178, 76, 0.12), transparent 55%),
      linear-gradient(160deg, #05050a 0%, #17101f 45%, #0b0b0d 100%);
  }

  /* ----------------------------------------------------------- */
  /* CARD SHELL — custom premium shape, NOT a plain rectangle    */
  /* ----------------------------------------------------------- */

  .fut-card {
    position: relative;
    width: 440px;
    max-width: 94vw;
    padding: 30px 26px 46px;
    color: var(--gold-bright);
    text-align: center;

    background:
      linear-gradient(180deg, rgba(255, 255, 255, 0.05), transparent 30%),
      linear-gradient(160deg, var(--card-purple) 0%, var(--card-black) 60%, #000 100%);

    border: 2px solid var(--gold);
    /* Premium shield-style silhouette using ONLY border-radius (no clip-path).
       The card is sized bigger and given generous bottom padding FIRST, so
       every line of text (including the stats) sits well above this curve
       and is never hidden behind it. */
    border-radius: 36px 36px 100px 100px / 36px 36px 60px 60px;

    box-shadow:
      0 0 25px rgba(217, 178, 76, 0.45),
      0 0 55px rgba(217, 178, 76, 0.2),
      inset 0 0 35px rgba(217, 178, 76, 0.08);
  }

  /* soft glossy highlight sweeping across the top (purely decorative, sits
     behind the content and never overlaps or hides any text/stats) */
  .fut-card::before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 40%;
    border-radius: 36px 36px 0 0;
    background: linear-gradient(180deg, rgba(255, 255, 255, 0.10), transparent);
    pointer-events: none;
    z-index: 0;
  }

  /* small decorative gold gem at the top, like a premium crest emblem */
  .fut-card::after {
    content: "";
    position: absolute;
    top: -11px;
    left: 50%;
    transform: translateX(-50%) rotate(45deg);
    width: 18px;
    height: 18px;
    background: linear-gradient(135deg, var(--gold-bright), var(--gold) 60%, var(--gold-deep));
    border: 1px solid var(--gold-bright);
    box-shadow: 0 0 10px rgba(217, 178, 76, 0.7);
    z-index: 1;
  }

  /* ----------------------------------------------------------- */
  /* TOP: rating / position / flag                                */
  /* ----------------------------------------------------------- */

  .card-top {
    position: relative;
    display: flex;
    align-items: flex-start;
    justify-content: space-between;
    z-index: 2;
  }

  .rating-side {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
  }

  .rating-title {
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 2px;
    color: var(--gold);
    opacity: 0.8;
    margin-bottom: 2px;
  }

  .overall-rating {
    font-size: 46px;
    font-weight: 800;
    line-height: 1;
    background: linear-gradient(180deg, #fff6d8, var(--gold) 55%, var(--gold-deep));
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
    text-shadow: 0 0 14px rgba(217, 178, 76, 0.45);
  }

  .position-label {
    margin-top: 2px;
    font-size: 13px;
    font-weight: 700;
    letter-spacing: 1.5px;
    color: var(--gold-bright);
  }

  .country-side {
    display: flex;
    flex-direction: column;
    align-items: flex-end;
  }

  .jersey-number {
    font-size: 26px;
    font-weight: 800;
    line-height: 1;
    color: var(--gold-bright);
    text-shadow: 0 0 10px rgba(217, 178, 76, 0.5);
    margin-bottom: 6px;
  }

  .flag-img {
    width: 46px;
    height: 32px;
    object-fit: cover;
    border: 1px solid var(--gold);
    border-radius: 4px;
    box-shadow: 0 0 10px rgba(217, 178, 76, 0.35);
  }

  /* ----------------------------------------------------------- */
  /* CENTER: large player photo, the main focus                    */
  /* ----------------------------------------------------------- */

  .photo-frame {
    position: relative;
    z-index: 2;
    width: 230px;
    height: 230px;
    margin: 6px auto 6px;
    border-radius: 50%;
    overflow: hidden;
    border: 2px solid var(--gold);
    box-shadow: 0 0 24px rgba(217, 178, 76, 0.5);
    background: #000;
  }

  .photo-frame img {
    width: 100%;
    height: 100%;
    object-fit: cover;
  }

  /* ----------------------------------------------------------- */
  /* NAME + TECH BADGES                                             */
  /* ----------------------------------------------------------- */

  .player-name {
    position: relative;
    z-index: 2;
    font-size: 22px;
    font-weight: 800;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    color: #fdf7e6;
    text-shadow: 0 0 10px rgba(217, 178, 76, 0.4);
    border-bottom: 1px solid rgba(217, 178, 76, 0.5);
    padding-bottom: 8px;
    margin-bottom: 8px;
  }

  .badge-row {
    position: relative;
    z-index: 2;
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 6px;
    margin-bottom: 10px;
  }

  .tech-badge {
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 0.3px;
    padding: 4px 10px;
    border-radius: 14px;
    border: 1px solid rgba(217, 178, 76, 0.65);
    background: linear-gradient(180deg, rgba(217, 178, 76, 0.16), rgba(217, 178, 76, 0.03));
    color: var(--gold-bright);
    white-space: nowrap;
  }

  /* ----------------------------------------------------------- */
  /* BOTTOM: stats                                                  */
  /* ----------------------------------------------------------- */

  .card-bottom {
    position: relative;
    z-index: 2;
    padding-top: 8px;
    border-top: 1px solid rgba(217, 178, 76, 0.45);
  }

  .stats-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    column-gap: 16px;
    row-gap: 5px;
  }

  .stat-row {
    display: flex;
    align-items: center;
    justify-content: space-between;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 0.3px;
  }

  .stat-label { color: var(--gold-bright); opacity: 0.9; }
  .stat-value { color: #fdf7e6; font-weight: 800; min-width: 20px; text-align: right; }

  /* ----------------------------------------------------------- */
  /* FOOTER                                                          */
  /* ----------------------------------------------------------- */

  /* ----------------------------------------------------------- */
  /* CARD FRAME — wraps the card so the footer can sit outside it  */
  /* ----------------------------------------------------------- */

  .card-frame {
    position: relative;
    display: inline-block;
  }

  .card-footer {
    position: absolute;
    left: 4px;
    bottom: -20px;
    text-align: left;
    font-size: 10px;
    color: var(--gold);
    opacity: 0.75;
    letter-spacing: 0.3px;
  }

  /* ----------------------------------------------------------- */
  /* RESPONSIVE                                                      */
  /* ----------------------------------------------------------- */

  @media (max-width: 480px) {
    .fut-card { width: 94vw; padding: 24px 18px 40px; }
    .photo-frame { width: 180px; height: 180px; }
    .overall-rating { font-size: 38px; }
    .player-name { font-size: 18px; }
    .jersey-number { font-size: 22px; }
    .flag-img { width: 40px; height: 28px; }
  }
</style>
</head>
<body>

  <div class="card-frame">
    <div class="fut-card">

      <!-- TOP: Overall Rating + Position (left) | Jersey Number + Flag (right) -->
      <div class="card-top">
        <div class="rating-side">
          <div class="rating-title">OVERALL</div>
          <div class="overall-rating">{{OVERALL_RATING}}</div>
          <div class="position-label">{{POSITION}}</div>
        </div>
        <div class="country-side">
          <div class="jersey-number">{{JERSEY_NUMBER}}</div>
          <img class="flag-img" src="{{FLAG_URL}}" alt="Country Flag">
        </div>
      </div>

      <!-- CENTER: Large Player Photo -->
      <div class="photo-frame">
        <img src="{{PHOTO_URL}}" alt="{{PLAYER_NAME}}">
      </div>

      <!-- NAME -->
      <div class="player-name">{{PLAYER_NAME}}</div>

      <!-- TECH BADGES -->
      <div class="badge-row">
        {{TECH_BADGES}}
      </div>

      <!-- STATS -->
      <div class="card-bottom">
        <div class="stats-grid">
          {{SKILL_STATS}}
        </div>
      </div>

    </div>

    <!-- FOOTER: sits outside the card, bottom-left corner -->
    <div class="card-footer">Developed by Ks Shafin</div>
  </div>

<!-- Bootstrap 5 JS Bundle (CDN, included for component support only) -->
<script src="https://cdn.jsdelivr.net/npm/[email protected]/dist/js/bootstrap.bundle.min.js"></script>

</body>
</html>
"""


# ---------------------------------------------------------------------------
# 7. Fill in the template
# ---------------------------------------------------------------------------

html_output = HTML_TEMPLATE
html_output = html_output.replace("{{PLAYER_NAME}}", player_name)
html_output = html_output.replace("{{PHOTO_URL}}", photo_url)
html_output = html_output.replace("{{FLAG_URL}}", flag_url)
html_output = html_output.replace("{{OVERALL_RATING}}", str(overall_rating))
html_output = html_output.replace("{{JERSEY_NUMBER}}", jersey_number)
html_output = html_output.replace("{{POSITION}}", position)
html_output = html_output.replace("{{TECH_BADGES}}", badges_html)
html_output = html_output.replace("{{SKILL_STATS}}", stats_html)


# ---------------------------------------------------------------------------
# 8. Save the file
# ---------------------------------------------------------------------------

output_filename = "Your Player Card.html"
file = open(output_filename, "w", encoding="utf-8")
file.write(html_output)
file.close()

print()
print("=" * 60)
print(f" SUCCESS! '{output_filename}' has been generated.")
print(f" Overall Rating : {overall_rating}")
print(f" Position       : {position}")
print(" Open the HTML file in your browser to see your")
print(" Legendary Gold Coding Player Card!")
print("=" * 60)

try:
    webbrowser.open("file://" + os.path.abspath(output_filename))
except Exception:
    pass
