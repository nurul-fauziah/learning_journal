---
trigger: model_decision
description: "Guidelines for existing brands, redesign/review workflows, app screens, edge case fallbacks, and reference tooling index."
globs: "*.html, *.css, *.js, *.jsx, *.tsx, *.vue, *.svelte, *.jinja, *.j2"
---

# Frontend Special Cases & Technical Reference

This guide covers workflows for adapting existing design systems, conducting legacy redesigns, handling edge-case environments, and locating reference assets.

---

## 1. Existing Brands & Design Systems

When an existing project has established brand guidelines:
- **Preserve Established Identity**: Keep fixed brand colors, brand typography, and official logos.
- **Adopt Compositional Discipline**: Apply the layout geometry, high-contrast scale, and section variety rules to the existing brand tokens.
- **Handle Banned Brand Devices**: If an established corporate asset strictly requires a banned device (e.g. an official gradient logo), preserve the brand asset while maintaining house discipline across the rest of the layout.

---

## 2. Redesign, Restyle, or Review Workflows

When tasked with improving an existing website or application interface:

1. **Document the Baseline**:
   - Inspect the current application before writing code. Capture screenshots of key pages across desktop and mobile.
   - Audit the existing codebase: dependencies, CSS architecture (Tailwind, CSS Modules, styled-components, vanilla CSS), components, and core user journeys that must not break.
2. **Review-Only Requests**:
   - Critique baseline screenshots, record violations against house rules, and present the top 3 highest-impact improvements.
3. **Preserve the Technical Stack**:
   - Do not perform unrequested framework or CSS library migrations. Work within the project's existing build system.
4. **Order of Execution (Maximum Impact, Minimum Risk)**:
   1. *Typography*: Correct headline line limits, scale ratios, tracking, and leading.
   2. *Colour*: Enforce the ground/ink/accent triad; convert soft gray body text to full ink.
   3. *Frame & Structure*: Balance outer margins; establish clear 120–240px section spacing; ensure `<h1>` title on the first screen.
   4. *Component States*: Add explicit `:focus-visible`, hover, active, and empty states.
   5. *Replace Generic Components*: Replace icon cards, pill badges, and gradient panels with content-driven layouts.
5. **Verification**:
   - Verify all existing forms, navigation links, and dynamic interactions continue functioning post-redesign.

---

## 3. App Screens & Software Interfaces

When designing dashboards, admin panels, settings screens, or data views:
- **Distinct Conventions**: App screens are worked in rather than scrolled through.
- **Allowed App Elements**: Quiet 1px borders around tables, compact form labels, and modular sidebars are standard and encouraged.
- **Prohibited App Slop**: Do not include glowing cards, icons inside tinted pastel squares, rainbow pie charts, or placeholder metric cards with fictional numbers.
- **Real Data**: Every chart and statistic must represent coherent, realistic domain data.

---

## 4. Technical Fallbacks & Edge Cases

- **No Form Backend / Checkout**:
  - Never generate fake, non-functional credit card or checkout forms.
  - Route the primary action to a legitimate `mailto:` link with pre-filled subject/body parameters, or point explicitly to an anchor `#contact` with clear user feedback.
- **Headless / Limited Environments**:
  - If headless browser tools or Node runtime inspectors cannot be executed, perform manual code audits against the 19 house rules and inspect static markup directly.
- **Network-Restricted Environments**:
  - If external image archives cannot be queried, render subject-specific motifs using inline SVG or CSS shapes derived directly from the subject's architectural features.

---

## 5. Reference File Index

For deeper guidelines and tool implementations, refer to the following assets:

| Reference Document | Context & Purpose |
| :--- | :--- |
| `references/app-screens.md` | Dedicated workflows and component patterns for dashboards, admin tools, and data tables. |
| `references/copy.md` | Headline length formulas, claim-and-proof structure, and full-density content drafting. |
| `references/type.md` | Font pairing, fluid typography formulas, and line measure guidelines. |
| `references/colour.md` | Palette proportions, dark mode adjustments, and WCAG contrast validation. |
| `references/layout.md` | Grid configuration, responsive breakpoints, and asymmetrical balance techniques. |
| `references/imagery.md` | Curated public image sourcing, museum APIs, licensing verification, and image crops. |
| `references/motion.md` | Animation curves, stagger timings, and `prefers-reduced-motion` recipes. |
| `references/critique.md` | Step-by-step 14-pass visual evaluation rubric for generated layouts. |

