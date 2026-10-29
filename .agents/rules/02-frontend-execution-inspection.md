---
trigger: model_decision
description: "Guidelines for frontend execution, asset hierarchy, browser inspection, screenshot critique, and motion design (TasteSkill v2 Steps 6-10)."
globs: "*.html, *.css, *.js, *.jsx, *.tsx, *.vue, *.svelte, *.jinja, *.j2"
---

# Frontend Design: Execution & Quality Gate (TasteSkill v2)

Build the page with motion switched off in your head; a page that needs animation to look finished is not finished.

---

## 1. Step 6: Build It, Still

Follow this exact order of implementation:

1. **Tokens**:
   - Define color and typography roles as CSS custom properties (`--color-ground`, `--color-ink`, `--color-accent`, font scales).
   - Everything downstream must reference tokens only.
2. **The Hero**:
   - Match the blueprint exactly at both desktop (1440px) and phone (390px) widths.
   - Establish high contrast between large and small elements before building other sections.
3. **Sections**:
   - Build each section from its blueprint with subject-specific content.
   - Neighboring sections must never share identical layouts. Carry the central idea into every section, including FAQ and footer.
4. **Imagery Hierarchy & The Floor**:
   - **Order of preference**:
     1. Project's own authentic photographs / product screenshots.
     2. Generated images (if tools are available).
     3. Real pictures from open collections (commercial-use archives, museum open access, historical postcards, local maps).
     4. Drawn in code / flat graphic language based on actual subject objects/architecture.
     5. Pure type and colour.
   - **The Floor**: At least **4 real pictures** on the page (typically 6 to 12). Real photographs, maps, engravings, or cropped interface fragments. SVGs do not count toward this floor.
   - Include **one moving picture** (muted video loop with poster frame or subtle pan).
   - Never write disclaimer text like *"none of these shows our real bar"*; provide proper captions and footer credits.
5. **The Live Thing**:
   - Integrated into the section where it proves a claim (e.g. hero, booking, or calculator). Real content, thumb-sized mobile version, plain non-JS fallback.
6. **Scroll Scenes**:
   - Build scenes as structural composition from the start, not as an afterthought.
7. **Fullness**:
   - Treat each desktop screen like a poster: one dominant element and the content it carries.
   - Maximum **1 deliberate rest** per page. Running text must use full ink at 16px+.
8. **The Frame**:
   - Equal outer margins on both left and right at every width.
   - Section gaps: 120–240px on desktop.
   - Page title in `<h1>` on the first screen; every section opens with a clear heading.
9. **States and Semantics**:
   - Semantic HTML elements (`<button>`, `<a>`, `<nav>`, `<main>`).
   - Visible keyboard `:focus-visible` styles, accessible labels (`aria-label` or visible text), and alternative text for all images.

---

## 2. Step 7: The Gate (Inspection & Verification)

Before declaring any frontend work complete, verify against the gate:

- **Linting**: Scan source code for banned patterns, inline styles where tokens belong, and generic stock phrases.
- **Browser Inspection**:
  - Test at three viewport widths: **1440px (Desktop)**, **768px (Tablet)**, and **390px (Mobile)**.
  - Verify headline line counts (<= 2 lines), loaded web fonts, color contrast, lack of horizontal overflow, and equal outer margins.
  - **Zero FAIL requirement**: Fix every failing test. Treat warnings as defects unless explicitly defensible.
- **Inspect Production Builds**: Verify the actual shipped output (built assets, minified CSS/JS), not merely dev server outputs.

---

## 3. Step 8: Visual Critique

Passing code checks ensures nothing banned exists, but does not guarantee great design:
1. Review full-page screenshots at all three viewports.
2. Critique against visual balance:
   - Does the first screen command attention?
   - Is spacing deliberate or accidental?
   - Are sections rhythmically varied?
3. Identify the top 3 visual weaknesses, adjust code, re-inspect, and re-evaluate (maximum 3 iterations).

---

## 4. Step 9: The Motion Layer

Once the static layout is solid, apply intentional motion:
- **Rule of Movement**: Minimum 8 moving elements across page load and scroll.
- **Four Layers of Motion**:
  1. **Signature Move**: One distinctive, well-crafted motion interaction.
  2. **Staggered Section Entrances**: Heading, text, and media staggered by 60–90ms, rising 16–32px with opacity on scroll trigger. Never hide content if script fails.
  3. **Control Feedback**: Instant visual states on hover, press, active, and focus.
  4. **One Moving Picture**: Subtle slow pan/zoom or muted looping footage.
- **Performance & Accessibility**: Restrict animations to `transform` and `opacity`. Always supply a clean `@media (prefers-reduced-motion: reduce)` fallback that preserves all content.

---

## 5. Step 10: Final Delivery Checklist

Do not finalize delivery until:
- [ ] 0 FAIL across 1440px, 768px, and 390px viewports.
- [ ] First screen communicates subject and action within 5 seconds.
- [ ] Every section has a clear heading; margins are balanced.
- [ ] All imagery is attributed and properly licensed.
- [ ] Keyboard navigation and accessibility contrast requirements pass.

