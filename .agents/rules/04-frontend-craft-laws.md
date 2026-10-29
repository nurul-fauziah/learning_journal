---
trigger: model_decision
description: "Core craftsmanship standards for typography, spatial grids, color palettes, imagery, and UI components."
globs: "*.html, *.css, *.js, *.jsx, *.tsx, *.vue, *.svelte, *.jinja, *.j2"
---

# Laws of the Craft (Design Standards)

These quantitative standards reflect measurements from top-tier curated web designs. Follow them to ensure high typographic and spatial polish.

---

## 1. Typography Standards

- **Scale Contrast**:
  - Use 2 to 3 primary type sizes to do the heavy lifting: one dominant hero size and one clean body size.
  - Maintain a high headline-to-body size ratio (typical top-tier ratio is ~4.3:1).
  - Maximum **5 distinct font sizes** across the entire page.
- **Display Typography (Headlines)**:
  - Tight letter-spacing: `letter-spacing: -0.02em` to `-0.05em`.
  - Tight line-height: `line-height: 0.85` to `1.05`.
- **Body Text**:
  - Size: 16px to 20px.
  - Comfortable line-height: `line-height: 1.45` to `1.6`.
  - Line length measure: 45 to 75 characters per line (`max-width: 65ch`).
- **Alignment**:
  - Default to **left-aligned** text. Center at most one isolated focal moment across the page.
- **Families**:
  - One font family is preferred; two is the hard maximum.

---

## 2. Spatial Rhythm & Grid

- **Unified Grid & Margins**:
  - Establish a single global grid with equal outer margins (16–32px).
  - Large graphic elements and backgrounds should extend edge-to-edge.
  - Body text blocks must align to 2 or 3 common left axes across the whole page.
- **Asymmetry**:
  - Introduce asymmetry *inside* the grid columns, never in the outer frame margins.
  - An off-centre heading must be balanced by supporting visual weight on the opposing side.
- **Section Spacing**:
  - The vertical spacing between major sections must be significantly larger than internal component padding: **120px to 240px on desktop**.
  - Adjacent sections must vary their spatial layout; avoid stacking repetitive blocks.

---

## 3. Color Harmony & Hierarchy

- **Color Triad**:
  - Ground (background canvas).
  - Ink (primary high-contrast typography and foreground elements).
  - Accent (reserved for primary interactive calls to action and critical highlights).
- **High-Contrast Text**:
  - Set all primary body copy in the full **ink** color. Avoid low-contrast washed-out light gray for essential paragraphs.
- **Surface Elevation**:
  - Separate distinct UI surfaces using subtle steps in flat tonal contrast, never with drop shadows or border lines.
- **Section Field Shifts**:
  - Allow entire sections to transition to alternating ground colors to mark distinct topical chapters.

---

## 4. Imagery & Visual Assets

- **Single Dominant Subject**:
  - One large, high-impact hero image or media element beats multiple weak thumbnails. Hero media should occupy 40%–60% of the first screen.
- **Consistent Aspect Ratios**:
  - Use unified crop ratios across related media sets. Default to sharp square corners unless brand guidelines explicitly dictate curvature.
- **Authentic Sourcing**:
  - Never use generic placeholder icons, abstract wireframes, or cliché stock photography.
  - Prefer authentic subject photos, curated public-domain museum archives, or purposeful vector artwork.
- **No Text Collisions**:
  - Text must never overlap directly onto busy photographic regions without an adequate contrast scrim.

---

## 5. UI Components

- **Buttons**:
  - Flat solid fill, either strictly square-cornered or fully rounded pill shape (avoid the generic 8–12px soft border-radius default).
  - Limit interactive actions on the hero: either no button or one clear, singular call to action.
- **Navigation Bar**:
  - Clean and minimal: logo/wordmark on the left, 3 to 5 clear text links, and one action button. Avoid bulky floating wrappers.
- **Form Controls & Constraints**:
  - Make controls self-explanatory via visible labels and input patterns.
  - When field limits exist (file formats, sizes, password rules), display them clearly beside the input linked via `aria-describedby`.
- **Footer**:
  - Treat the footer as a bold, designed signature close (e.g. brand name returning in large type), rather than an overcrowded link cemetery.

