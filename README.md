# KAThu on marketing

Phan Hoai Thu’s marketing portfolio: campaign leadership, paid acquisition, SEO, conversion and supporting analytics.

## Deploy on Vercel

Import `kath-pahotu/marketing-porfolio` and use:

| Setting | Value |
| --- | --- |
| Production branch | `main` |
| Root Directory | `.` (repository root; the default) |
| Framework Preset | Other |
| Build Command | Leave empty (no build required) |
| Output Directory | `website` (set automatically by `vercel.json`) |
| Install Command | Leave empty (no dependencies required) |

The root `vercel.json` publishes only `website/` and disables install/build steps. This also works when importing the repository with the default Root Directory, avoiding a 404 at `/`. If an existing project uses `website` as its Root Directory, its nested configuration still supports that setup with Output Directory `.`.

The generated HTML, CSS, JavaScript, images and public CV are committed, so deployment does not require Python or a build step. The repository does not contain the previous Vercel project association. The owner handles deployment.

The canonical URLs, sitemap and social metadata use `https://kathuonmkt.vercel.app`. If deploying under another address, update `PROFILE['site']` in `source/content.py` and rebuild before publishing.

## Files

- `website/`: ready-to-deploy static site, all 13 case studies and the downloadable public CV.
- `source/content.py`: profile, experience and case-study content.
- `source/build_site.py`: base HTML generator.
- `source/refine_site.py`: final homepage, project library and case-study presentation.
- `source/refinements.css`: additional shared styling, copied during rebuild.
- `website/assets/katherine-ava.png`: supplied banner photograph.

## Preview

```sh
python -m http.server 4173 --directory website
```

Open `http://localhost:4173`.

## Edit and rebuild

For text changes, edit the source files and run:

```sh
python -m pip install -r requirements.txt
python build_website.py
```

The sharing-card generator currently uses Windows Arial (`C:/Windows/Fonts/arialbd.ttf`), so run the optional rebuild on Windows. Deployments use the existing generated files and do not need that font.

Base styles and interactions live in `website/style.css` and `website/app.js`. Update `source/refinements.css` for refinement styles, then rebuild. The public CV is a checked-in PDF; replace it directly if the CV changes. Commit both source edits and generated website files.

Original private reports, tailored job applications, local authentication files and QA artifacts are kept outside version control. The mobility case links to the separately hosted password-protected data portfolio; no password or authentication implementation is included here.
