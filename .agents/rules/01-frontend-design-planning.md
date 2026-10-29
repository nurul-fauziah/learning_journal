---
trigger: model_decision
description: "Guidelines for frontend design planning, subject inventory, artistic direction, concept formulation, and copywriting (TasteSkill v2 Steps 1-5)."
globs: "*.html, *.css, *.js, *.jsx, *.tsx, *.vue, *.svelte, *.jinja, *.j2"
---

# Frontend Design: Strategy & Planning (TasteSkill v2)

A page built by default usually looks like the average of every generic page: a centred headline over three lines, a little label above it, a row of icon cards, a soft gradient, thin rules, and a monospace caption. Nothing in it is wrong, but nothing was intentionally decided.

This rule enforces intentional decisions over generic defaults.

---

## 1. Substance over Restraint
Removing ornaments (labels, rules, cards) is only half the job. A page that has lost its ornaments and gained nothing reads as thin and empty. The other half is **substance**:
- Type set larger.
- Whole fields of flat colour.
- Real pictures of the subject's world (found or drawn).
- Every section carrying its full, rich content.
- Do not trade substance for restraint.

---

## 2. Page vs. App Screen
Decide first which of two kinds of work you are handling:

- **A Page** is read and scrolled: landing page, marketing site, product page, portfolio, one-pager. Follows the standard run below.
- **An App Screen** is worked in: dashboard, admin/analytics view, settings, billing, inbox, queue, editor. It follows app screen rules (quiet borders, small labels, repeated panels are normal; gradients, glows, icons in tinted squares, rainbow charts, and invented numbers are banned).
- **Product site showing an app**: Interface fragments on the page must follow app screen rules. Build them with real data and clean panels (marked with `data-ui`), never placeholder grey bars.

---

## 3. The Run: Steps 1 to 5

### Step 1: Read the Brief and Inventory the Subject
1. Find what is real: the subject, audience, the single action the page must achieve, the stack, existing brand (colours, fonts, logo), and above all **what imagery truly exists**.
2. Never plan around pictures you do not have.
3. If the request is vague, decide and state your reading in one line instead of pausing to ask.
4. **Subject Inventory**: List 8 to 12 specific things unique to this subject:
   - Name and its etymology/meaning.
   - Physical address, street, neighbourhood, tiles, signs, local paint colours, weather, light.
   - Numbers in the brief (seats, rooms, price, year, minutes to destination).
   - Constraints (single batch per month, closed in winter, by appointment only).
   - Materials, textures, and colours.
   - Daily rituals and hours (oven lit at 5 AM, ferry departs at 7 PM).
   - Printed artefacts of its world (timetables, labels, tickets, receipts, menus).

### Step 2: Write the Argument
Before designing, structure the page as a sequence of **claims with proof**, one line per section.
- Claims dictate which sections exist and in what order.
- Delete any section that has no real claim.
- Avoid the stock sequence (Hero -> Logos -> 3 Icon Cards -> Testimonial -> Pricing -> CTA).

### Step 3: Draw the Direction
Select a cohesive direction that fits the subject:
- Compose around what only this client/subject possesses.
- Check the palette against the subject: ground, ink, and accent proportions. If palette colours conflict with the subject's reality, adjust colours directly from the subject's materials.
- Adopt the direction fully. Do not blend it into comfortable generic layouts.

### Step 4: Find the Idea
The direction is a way of composing; the idea makes the page belong exclusively to this subject. Formulate this sentence:
> **"On this page, [something that belongs to the subject] becomes [the device the direction calls for]."**

- **The Competitor Test**: Replace the subject with its nearest competitor. If the sentence still fits, the idea belongs to the category, not the subject. Find a more specific idea.
- **One Live Thing**: Include one interactive feature that visitors can manipulate or that changes per visit (e.g. interactive selector, real calculator, preview of custom material).
  - Rules: Uses real content, thumb-operable on mobile, has plain fallback without JavaScript, never blocks reading.
- **Scenes Carry the Idea**: Scroll scenes must depict elements from the subject inventory, not generic stock animations.

### Step 5: Write the Words (Copy Deck)
Write the complete page copy before markup:
- **Headlines**: Must fit in 2 lines or fewer at every viewport width (~32 characters safe limit).
- **Supporting Sentence**: 32–48px directly below the headline, explaining plainly what the thing is.
- **First Screen Clarity**: Answers the visitor's first question immediately in large type.
- **Full Content Density**: Every section must deliver complete information (full menu items with prices, detailed specs, all talk schedules).
- **No Fake Proof**: Never invent fake customer quotes, fake press logos, or vanity metrics.

