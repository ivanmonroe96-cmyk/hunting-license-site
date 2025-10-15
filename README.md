# Hunting License Site (English-first)

This repository contains a Hugo static site scaffolded to provide English-first content focused on obtaining hunting licenses. The project includes basic TailwindCSS scaffolding and shortcodes.

Quick start (dev):

```bash
# install node deps (if you don't have a package-lock.json yet, use `npm install` to generate one)
npm install

# build css once (requires PostCSS + Tailwind installed)
npm run build:css

# run Hugo dev server
hugo server -D
```

Build for production:

```bash
npm run build
# or run hugo --minify directly
hugo --minify
```

Deploy:
- There's a GitHub Actions workflow `.github/workflows/deploy-cloudflare-pages.yml` which expects the following repository secrets:
  - `CF_PAGES_API_TOKEN` - Cloudflare Pages API token with Pages Deploy permissions
  - `CF_ACCOUNT_ID` - Cloudflare account id
  - `CF_PROJECT_NAME` - Pages project name

Notes on Tailwind:

- For quick development without running the Tailwind build, the site includes a CDN fallback that loads Tailwind from the official CDN when Hugo is not running in production. This is useful for prototyping but not recommended for production.
- For production, build the CSS with `npm run build:css` (this generates `assets/css/styles.build.css` which you should copy to `static/css/` or adjust templates to use the built asset).

Next steps (suggested):
- Finalize legal pages (`content/en/legal/`)
- Add real reviews and downloads under `content/en/reviews` and `static/downloads/`
- Run Lighthouse audits and iterate on Tailwind-based styling
