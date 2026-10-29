---
trigger: model_decision
description: "Strict anti-slop constraints, banned aesthetic patterns, and house rules for all web pages and components."
globs: "*.html, *.css, *.js, *.jsx, *.tsx, *.vue, *.svelte, *.jinja, *.j2"
---

# Frontend House Rules (Strict Anti-Slop Constraints)

These rules apply to every frontend build regardless of style direction. They eliminate generic, AI-generated aesthetic clichés and enforce high design standards.

---

## 1. Table of House Rules

| Prohibited Pattern | Strict Requirement | Approved Alternative |
| :--- | :--- | :--- |
| **Long Headlines** | Max **2 lines** at every viewport width (`h1`–`h6`). | Trim words, widen container measure, reduce font size as last resort. |
| **Vague Titles** | First screen must have a clear `<h1>`; every section needs an explicit heading. | State explicitly what the subject is, what it does, or date/place. |
| **Asymmetrical Frame** | Equal outer margins on left and right. No huddled content with half an empty screen. | Balance every void with supporting picture, secondary column, list, or figure. |
| **Blank Stretches** | No empty vertical space taller than ~0.5 screen height. | Maintain standard section gap (120–240px). Intentional rests must use a placed image or flat field of colour (max 1 per page). |
| **Large Intro Statements** | Sentences set large (>36px) must not break the 2-line rule. | Mark as `<p>` or `<blockquote>` at <=36px desktop (<=24px mobile), ~25 words max. |
| **Eyebrows / Badges** | **No small labels above headings**, no pill chips (e.g. "New ·", "Overview"). | Integrate context directly into the main heading or supporting sentence. |
| **Monospace Abuse** | **No monospace fonts** outside actual code blocks. | Use standard body typeface. Use tabular figures (`font-variant-numeric: tabular-nums`) for aligned data. |
| **Index Numbering** | **No fake indexing** (`01`, `02`, `03`, `(001)`, `Step 2`). | Convey progression through spatial placement, typography scale, or semantic `<ol>`. |
| **Thin Lines & Grids** | **No hairline dividers**, no 1px outline boxes, no crosshairs or decorative grid lines. | Use negative space, subtle background tone shifts, or scale contrast. |
| **Gradients** | **No gradient backgrounds**, gradient buttons, or gradient text fills. | Solid flat colours or real authentic photography. (Neutral photo scrim is the only exception). |
| **Resting Shadows** | **No shadows or glows on elements at rest**. | Distinguish layered surfaces through subtle tonal background steps. Shadows permitted only on truly floating dialogs/dropdowns. |
| **Assistant Palette** | **No generic AI colors**: avoid yellow-cream ground paired with terracotta/rust; avoid purple/indigo. | Use a deliberate, subject-tailored palette (ground, ink, accent). |
| **Tiny Uppercase Labels** | **No tracked-out uppercase micro-text** (`letter-spacing` with 10px uppercase). | Use readable sentence case at 14px+. |
| **Icon Feature Cards** | **No rows of identical 3-column cards with icons on top**. | Use varied section blueprints derived from the content's actual structure. |
| **Glassmorphism** | **No frosted glass**, `backdrop-filter: blur`, or floating pill navigation bars. | Solid, clean navbar: wordmark, 3–5 links, one primary action button. |
| **Decorative Blobs** | **No decorative floating emojis**, gradient blobs, or fake dashboards of gray bars. | Real photography, functional interface fragments, or clean typography. |
| **Styled Accent Words** | **No single italicized/serif/colored accent word** inside a headline. | Keep headline uniform in face and color; allow copy semantics to provide emphasis. |
| **Font Proliferation** | **Maximum 2 typefaces** across the entire page (usually 1 is sufficient). | Establish hierarchy through scale, weight, and tracking rather than different families. |

---

## 2. Permitted Exceptions

Only three specific areas may deviate from these constraints:
1. **Real Code**: Inside `<pre>` and `<code>` blocks, monospace fonts and syntax borders are correct.
2. **Tabular Data & Form Inputs**: Legitimate data tables and form input controls may use subtle container borders for usability.
3. **Real Interface Fragments**: Embedded screenshots or live mockups of the actual application software marked with `data-ui` attributes may retain the application's native controls, borders, and UI conventions.

---

## 3. Why These Rules Exist

Data from curated design studies (e.g. Awwwards Sites of the Day, One Page Love) shows:
- Award-winning sites use icon cards in **1%** of cases vs. **28%** in lower-tier generic sites.
- Pill badges appear in **14%** of top sites vs. **34%** in generic templates.
- Gradient fills are present in **22%** of top sites vs. **52%** in generic templates.
- Unnecessary drop shadows are used in **24%** of top sites vs. **48%** in generic templates.
- Monospace labels and decorative hairlines are heavily overused by AI generators as a faux-technical costume.

Eliminating these clichés forces the layout to rely on **typographic scale, deliberate spacing, and real content density**.

