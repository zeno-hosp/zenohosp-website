# Frontend Architecture

## Goals
- Use one JavaScript entrypoint across all pages.
- Keep behavior deterministic and page-safe.
- Avoid global function collisions and duplicate event listeners.
- Keep SEO markup server-readable (plain HTML first, JS progressive enhancement second).

## Runtime Shape
- Entry file: `js/app.js`
- Boot guard: `window.__zenoAppBooted`
- Public API: `window.ZenoApp`
- Boot timing: DOM ready via `DOMContentLoaded`.

## CSS Structure
- Base styles: `css/styles.css`
- Product/shared page styles: `css/product-pages.css`
- Theme tokens: `css/zenohosp-theme.css`
- Page-level styles:
  - `css/pages/home.css`
  - `css/pages/hms.css`
  - `css/pages/contact.css`
  - `css/pages/pricing.css`
  - `css/pages/marketing-navbar.css`

## Module Boundaries (inside `js/app.js`)
- `initNavbar`: sticky/scrolled navbar state.
- `initMobileMenu`: mobile nav open/close and overlay handling.
- `initSmoothScroll`: in-page anchors with nav-offset scrolling.
- `initRevealAnimations`: `.reveal`/`.zd-reveal` observer.
- `initDataAosAnimations`: `[data-aos]` observer.
- `initSolutionTabs`: tab/panel activation.
- `initHeroSwitcher`: hero switcher state transitions.
- `initHoverEffects`: optional pointer effects.
- `initParallax`: optional parallax behavior.
- `animateCounters`: optional stat-number animation helper.

## HTML Contract
- Load one script only on every page:
  - `<script src="js/app.js" defer></script>`
- Keep JSON-LD scripts inline in pages.
- Do not add page-level JS bootstrap snippets for features already managed by `js/app.js`.
- Keep page-specific CSS in `css/pages/*.css` instead of inline `<style>` blocks.

## Performance Rules
- Use `defer` for shared script loading.
- Use `passive: true` for scroll listeners.
- Gate motion-heavy behavior behind `prefers-reduced-motion`.
- Prefer IntersectionObserver over scroll polling for reveal effects.

## Maintainability Rules
- Add new shared behavior in `js/app.js` as isolated functions.
- Keep selectors stable and explicit; avoid fragile parent/child traversal.
- If a behavior is page-specific, gate by existence checks for required elements.
- If logic grows beyond this file, split into `js/modules/` and keep `js/app.js` as orchestrator only.

## Next Refactor Targets
- Consolidate repeated nav/footer visual rules into shared CSS components.
- Replace placeholder links (`href="#"`) with real routes or explicit disabled states.
- Introduce automated checks (HTML validation, Lighthouse CI, basic smoke tests).
