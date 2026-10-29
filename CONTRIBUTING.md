# Contributing to Studio Bohème 🌿

Thank you for your interest in contributing to **Studio Bohème**! We welcome improvements, bug reports, and mindful design suggestions.

---

## 🎨 Design Guidelines (TasteSkill Anti-Slop)

All frontend additions must adhere to the project's **Bohemian Risograph** aesthetic:
1. **Palette Integrity**: Use CSS tokens defined in `style.css` (`--color-terracotta`, `--color-sage`, `--color-forest`, `--color-mustard`, `--color-aubergine`, `--bg-oat`). Do not introduce neon accents, harsh `#000` or `#FFF`.
2. **Typography**: Headings use `Fraunces`, body/UI uses `Karla`. Maximum 2 font families.
3. **No System Emojis**: Always use semantic inline SVGs styled with the palette.
4. **Architectural Arches & Print Shadows**: Maintain flat arch frames and woodblock-style print shadows (`box-shadow: 4px 4px 0px var(--border-boho)`).

---

## 🛠️ Development Workflow

1. Fork the repo and create your branch from `main`:
   ```bash
   git checkout -b feature/your-feature-name
   ```
2. Set up your virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # or .\venv\Scripts\Activate.ps1 on Windows
   pip install -r requirements.txt
   ```
3. Test your changes locally:
   ```bash
   python app.py
   ```
4. Verify security: ensure all new forms include CSRF tokens and endpoints validate input boundaries.

---

## 📝 Commit Message Guidelines

Use clear, structured commit messages following conventional commits:
- `feat: add tag filtering in knowledge vault`
- `fix: resolve review date interval reset on hard ratings`
- `style: refine matisse frond svg positioning for mobile`
- `docs: update quickstart instructions in README`

---

Thank you for helping keep our learning studio beautiful and focused!

