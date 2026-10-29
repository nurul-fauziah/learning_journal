<div align="center">

# 🌿 Studio Bohème &mdash; Learning Journal
### *A Mindful Spaced-Repetition Vault & Active Recall Journal*

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.x-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![SQLite](https://img.shields.io/badge/SQLite-SQLAlchemy-003B57?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![Design](https://img.shields.io/badge/Design-TasteSkill%20Bohemian-C8704F?style=for-the-badge)](https://github.com)
[![License](https://img.shields.io/badge/License-MIT-E0A23B?style=for-the-badge)](LICENSE)
[![Security](https://img.shields.io/badge/Security-CSRF%20%2B%20RateLimit%20%2B%20CSP-3F5B48?style=for-the-badge)](https://owasp.org/)

<p align="center">
  A sunlit studio for your thoughts. Designed with a bespoke <strong>Bohemian Risograph Aesthetic</strong>, mathematical <strong>Spaced Repetition</strong>, and locked <strong>Active Recall Reminders</strong> to make continuous learning effortless and enduring.
</p>

[Key Features](#-key-features) &bull;
[Design Philosophy](#-design-philosophy) &bull;
[Quickstart](#-quickstart) &bull;
[Architecture](#-architecture--security) &bull;
[Security Highlights](#-security-hardened)

---

</div>

## 📖 Overview

Most note-taking tools are either sterile corporate dashboards or messy text files where forgotten insights go to die.

**Studio Bohème** reimagines your personal learning log as a warm, soulful botanical atelier. It bridges cognitive retention science (**Ebbinghaus Spaced Repetition + Active Recall**) with intentional, anti-slop art direction inspired by Matisse cut-outs, flat arch shapes, and earthy risograph palettes.

---

## ✨ Key Features

### 1. 🧠 Intelligent Spaced Repetition (SRS Engine)
- Implements an adaptive review algorithm inspired by the **Leitner Box** and **SuperMemo SM-2**.
- Notes are categorized by difficulty (*Easy, Medium, Hard*) with dynamic review interval growth based on recall quality (*Effortless, Adequate, Challenging*).
- Overdue manuscripts automatically surface on your dashboard, with an optional **Practice Mode** for random recall sessions.

### 2. ☀️ Bohemian Activity Heatmap (Pebble Consistency)
- Visualizes your 30-day learning rhythm through tactile, organic leaf-bud and pebble shapes instead of generic grid blocks.
- Seamlessly aggregates both note creation and daily mindful reflections across an earthy palette gradient:
  $$\text{Oat} \longrightarrow \text{Dusty Peach} \longrightarrow \text{Sun Mustard} \longrightarrow \text{Terracotta} \longrightarrow \text{Forest Green}$$

### 3. ⏰ Active Reminder & "Recall-to-Unlock" Modal
- Set focused study timers directly inside the studio.
- When the timer concludes, an interactive arch-window modal engages and locks the screen until you transcribe the key concept or keyword from a randomly chosen note.
- Features resilient concept matching with token overlap, punctuation stripping, and keyboard accessibility.

### 4. 🪴 Daily Reflection with Debounced Autosave
- A dedicated botanical arch card inviting daily metacognitive grounding: *"What is one new thing I understood today? What confused me?"*.
- Automatically synchronizes drafts to the SQLite database via debounced asynchronous API endpoints &mdash; your thoughts are never lost upon reload.

### 5. 🗃️ Knowledge Vault with Instant Search
- Clean masonry repository displaying all codified notes, categories, and human-friendly scheduling metrics (*"Due today"*, *"Due tomorrow"*, *"Overdue"*).
- Instant client-side search filtering across titles, summaries, and tags.

---

## 🎨 Design Philosophy: Bohemian Atelier

Adheres strictly to **TasteSkill v2 Anti-Slop** frontend guidelines:

| Characteristic | Anti-Slop Implementation |
| :--- | :--- |
| **Color Triad** | Earthy risograph screen-print palette: Warm Oat Canvas (`#F3E9DA`), Burnt Terracotta (`#C8704F`), Sage Green (`#9AA68A`), Forest Green (`#3F5B48`), Sun Mustard (`#E0A23B`), and Deep Aubergine Ink (`#4A2C2A`). No neon, no harsh `#000` or `#FFF`. |
| **Architectural Arches** | Structural arch-top frames (`border-radius: 48px 48px 24px 24px`) mirroring Mediterranean art studios. |
| **Matisse Cut-outs** | Asymmetrical, hand-drawn vector foliage and fronds at page margins. |
| **Tactile Buttons** | Chunky pill buttons with flat offset woodblock print shadows (`box-shadow: 4px 4px 0px var(--border-boho)`). |
| **Typography** | Strict 2-family pairing: **Fraunces** (groovy retro display serif) for expressive headings, paired with **Karla** (grounded warm sans-serif) for high-legibility UI text. |
| **Zero System Emoji** | All default emojis replaced with curated, semantic inline SVGs (radiant sun, ceramic vases, sundials, and leafy sprigs). |
| **Paper Grain** | Subtle tactile paper grain overlay rendered in real-time via SVG `<feTurbulence>`. |

---

## 🛡️ Security Hardened

Designed from the ground up with defensive engineering best practices:

- **🔐 Robust User Authentication**: Salted, cryptographic password hashing via `werkzeug.security` with complete session isolation per user.
- **🛡️ Universal CSRF Protection**: Every state-changing form and asynchronous JSON fetch (`POST`) is verified with `Flask-WTF` tokens.
- **🧱 Defensive HTTP Security Headers**:
  - `X-Frame-Options: DENY` (anti-clickjacking)
  - `X-Content-Type-Options: nosniff` (anti-MIME sniffing)
  - `Referrer-Policy: strict-origin-when-cross-origin`
  - Strict `Content-Security-Policy (CSP)` restricting scripts, styles, and font origins.
- **🚦 In-Memory IP Rate Limiting**: Built-in sliding window rate limiter (80 requests/min per IP) to prevent denial-of-service and brute-force flooding.
- **📏 Strict Input Validation**: Strict payload bounds (8 MB max body) and character caps on all form fields preventing database exhaustion.
- **🔒 Persistent Secret Keys**: Automatically generates and stores a 256-bit cryptographic secret key in git-ignored instance storage.

---

## 🚀 Quickstart

### Prerequisites
- **Python 3.10+** (Tested up to Python 3.14)
- **Git**

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/studio-boheme-journal.git
   cd studio-boheme-journal
   ```

2. **Create and activate a virtual environment**:
   ```bash
   # Windows PowerShell
   python -m venv venv
   .\venv\Scripts\Activate.ps1

   # Linux / macOS
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Initialize & Run the Application**:
   ```bash
   python app.py
   ```

5. **Open in your browser**:
   Navigate to [http://127.0.0.1:5000](http://127.0.0.1:5000). On your first visit, you will be invited to register your master studio account!

---

## 📁 Project Structure

```text
learning_journal/
├── app.py                 # Core Flask application, secure routing, APIs & SRS logic
├── models.py              # SQLAlchemy models (User, Entry, Category, Reflection)
├── requirements.txt       # Production dependencies
├── .env.example           # Example configuration file
├── .gitignore             # Git exclusion rules (SQLite DBs, secrets, cache)
├── LICENSE                # MIT License
├── README.md              # Project documentation
│
├── static/
│   ├── css/
│   │   └── style.css      # Bohemian design system tokens, arch frames & print shadows
│   └── js/
│       └── script.js      # Active reminder timer, concept verification & modals
│
└── templates/
    ├── base.html          # Global layout, SVG paper grain, header & nav
    ├── dashboard.html     # Studio dossier, sun streak, stats, pebble heatmap & reflection
    ├── vault.html         # Knowledge repository with live search & due-date filter
    ├── add_entry.html     # Note creation form with difficulty assignment
    ├── review.html        # Flashcard recall session & spaced repetition rating
    ├── login.html         # Bohemian arch card authentication
    └── register.html      # Master account onboarding
```

---

## ⚙️ Environment Variables (Optional)

Create a `.env` file in the project root to override default settings:

```ini
FLASK_DEBUG=0
SECRET_KEY=your-custom-super-secret-key-here
```

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!  
Feel free to check out the [issues page](https://github.com/your-username/studio-boheme-journal/issues).

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/MindfulFeature`)
3. Commit your Changes (`git commit -m 'Add MindfulFeature'`)
4. Push to the Branch (`git push origin feature/MindfulFeature`)
5. Open a Pull Request

---

## 📜 License

Distributed under the **MIT License**. See [`LICENSE`](LICENSE) for more information.

<div align="center">
  <sub>Crafted with intention &bull; Studio Bohème &bull; Nourish your curiosity</sub>
</div>

