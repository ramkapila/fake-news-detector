# Design System Specification: Ethereal Intelligence

## 1. Overview & Creative North Star
**Creative North Star: "The Celestial Truth"**
This design system moves away from the clinical, often aggressive aesthetic of fact-checking tools. Instead, it positions fake news detection as a moment of clarity within a vast digital cosmos. We lean into a "High-End Editorial" experience that feels like a quiet, nocturnal observatory. 

By utilizing **intentional asymmetry**, we break the rigid "template" look. Layouts should feel like constellations—elements are connected by logic and flow but are not strictly boxed in. Overlapping glass panels and high-contrast typography scales create a sense of deep, intellectual luxury. This system is designed to evoke a feeling of calm authority and crystalline transparency.

---

## 2. Colors & Atmospheric Depth
The palette is rooted in the deep reaches of the night sky, transitioning from ink-blot indigos to radiant, neon-tinged purples.

### The "No-Line" Rule
**Explicit Instruction:** Prohibit 1px solid borders for sectioning. Structural boundaries must be defined solely through background color shifts or subtle tonal transitions. For example, a `surface-container-low` section should sit directly on a `background` without a dividing line.

### Surface Hierarchy & Nesting
Treat the UI as a series of physical layers of frosted glass.
- **Base:** `background` (#0d0a27) – The deep void.
- **Level 1:** `surface-container-low` (#120f2f) – For secondary content areas.
- **Level 2:** `surface-container` (#181538) – For standard cards and modular pieces.
- **Level 3:** `surface-container-high` (#1e1a41) – For interactive elements that need to feel "closer" to the user.

### The "Glass & Gradient" Rule
Floating elements (modals, dropdowns, primary alerts) must use **Glassmorphism**.
- **Fill:** `primary` (#b1a2ff) or `surface-variant` (#24204a) at 20–40% opacity.
- **Effect:** `backdrop-blur` (12px to 20px).
- **Signature Textures:** Apply a linear gradient from `primary` (#b1a2ff) to `primary-container` (#a391ff) at a 135-degree angle for Hero CTAs to provide a "pulsing" soul that flat colors lack.

---

## 3. Typography
We use a high-contrast pairing to balance editorial authority with modern readability.

*   **Display & Headlines (Manrope):** A geometric sans-serif that feels architectural and precise. The generous `display-lg` (3.5rem) should be used for impactful truth-claims or data visualizations, creating a sense of scale.
*   **Body & Labels (Plus Jakarta Sans):** A contemporary sans-serif with a high x-height. This ensures that even at `body-sm` (0.75rem), the detailed evidence behind a news verification remains perfectly legible.
*   **Hierarchy Note:** Use `title-lg` for article headlines and `headline-sm` for section headers. The contrast between the bold `manrope` headers and the soft `plusJakartaSans` body creates a premium, curated feel.

---

## 4. Elevation & Depth
In this system, depth is a function of light and atmosphere, not drop shadows.

*   **The Layering Principle:** Stacking is the primary method of organization. Place a `surface-container-lowest` card on a `surface-container-low` background. This "tonal lift" is more sophisticated than a border.
*   **Ambient Shadows:** Use only for high-priority floating objects. Shadows must be extra-diffused.
    *   *Blur:* 40px–60px.
    *   *Opacity:* 6% of `on-surface` (#e7e2ff). This mimics a soft purple glow rather than a grey shadow.
*   **The "Ghost Border" Fallback:** If accessibility requires a stroke, use `outline-variant` (#474464) at **15% opacity**. This creates a suggestion of an edge without breaking the ethereal flow.
*   **Glow Accents:** Use `tertiary` (#ffa4fc) for subtle "star-point" glows behind key icons or "Truth Score" indicators.

---

## 5. Components

### Buttons
*   **Primary:** Gradient fill (`primary` to `primary-container`), `full` roundedness, white text. No shadow; use a 4px outer glow of `primary` at 30% opacity on hover.
*   **Secondary:** Glassmorphic fill (10% opacity `primary`), `outline-variant` Ghost Border.
*   **Tertiary:** No background. `title-sm` typography with a subtle underline that appears on hover.

### Input Fields (The Search/Verify Bar)
*   Forbid standard boxes. Use a wide, `full` rounded `surface-container-highest` bar with a subtle `backdrop-blur`. 
*   **Placeholder text:** `on-surface-variant` (#aca7cc) in `body-md`.

### Cards (The News Feed)
*   **Constraint:** No dividers. 
*   **Structure:** Use vertical whitespace (referencing the `xl` 1.5rem spacing) and `surface` shifts. Each card should feel like a pane of glass floating in the nebula.
*   **Corners:** Use `xl` (1.5rem) for main cards to emphasize the "soft" ethereal aesthetic.

### Additional Specialty Component: The "Truth Orbit"
A custom data visualization component for fake news scores. A central node (the news item) surrounded by orbiting "evidence" chips. Use `tertiary` (#ffa4fc) for "False" flags and `secondary` (#bab5f3) for "Verified" facts, utilizing neon-glow effects (`box-shadow: 0 0 15px currentColor`).

---

## 6. Do’s and Don’ts

### Do:
*   **Use breathing room:** Give every element significant whitespace. The "Starry Night" needs space to be seen.
*   **Embrace asymmetry:** Offset text blocks or images to create a dynamic, editorial rhythm.
*   **Layer your surfaces:** Always ask "can I define this section with a color shift instead of a line?"

### Don’t:
*   **Don't use pure black:** Use `surface-container-lowest` (#000000) only for the deepest UI elements; never for text.
*   **Don't use 100% opacity borders:** This instantly kills the glassmorphism and ethereal feel.
*   **Don't use standard "Drop Shadows":** Grey shadows feel dirty in a purple/indigo environment. Always tint shadows with the `on-surface` or `primary` hue.
*   **Don't clutter:** If the screen feels busy, remove elements. The system thrives on minimalism and "Atmospheric Intelligence."