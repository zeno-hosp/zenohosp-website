# scripts/

One-off Python codegen / bulk-edit tools used to author and maintain the static
HTML pages in this repo (SEO injection, blog generation, footer/nav
standardization, page scaffolding, etc.).

**These are historical dev-time utilities — not part of the build or the
deployed site.** The deployed site is the static HTML/CSS/JS served as-is by
Vercel (see `../vercel.json`). The only real build step is `../build.js`, which
inlines shared components.

Notes before running any of these:

- Many older scripts hardcode a **stale absolute path**
  (`/Users/iniyananbu/Documents/Zeno Hosp Website`) that no longer matches this
  folder. Update the `directory = ...` line before running.
- They mutate HTML files in place. Commit or stash first so you can diff/revert.
- `generators/` holds the page-generator variants.
