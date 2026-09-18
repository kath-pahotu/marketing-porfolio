# KAThu marketing analytics portfolio

Live: https://kathuonmkt.vercel.app
Repository: https://github.com/kath-pahotu/marketing-porfolio

The Marketing Analyst track leads with marketplace growth, campaign targeting and ad incrementality, backed by Golden Owl campaign experience. The completed-project collection contains the five cases approved in the September 2026 brief.

## Deployment

Pushes to `main` automatically deploy to the existing `kathuonmkt` Vercel project. The separately imported `marketing-porfolio` Vercel project also follows this repository.

- Root Directory: `.`
- Framework: Other
- Build/install commands: empty
- Output Directory: `website` (configured in the root `vercel.json`)

Generated files are committed, so Vercel does not run Python. The canonical URL remains `https://kathuonmkt.vercel.app`.

## Edit and rebuild

1. Edit public content in `source/revamp_content.py`.
2. Run `pip install -r requirements.txt`.
3. Run `python build_website.py` to rebuild both the marketing CV and site.
4. Commit source changes and generated `website/` files.

The CV generator uses Windows Arial. Public styles and interactions are `source/revamp.css` and `source/revamp.js`; the site generator is `source/build_tracks.py`. `source/build_site.py` and `source/refine_site.py` delegate to the current build entry point for compatibility.

Preview: `python -m http.server 4173 --directory website`.

The new downloadable CV is `website/documents/Phan_Hoai_Thu_Marketing_Analyst_CV.pdf`. The old Digital_Marketing filename serves the same current PDF so previous links keep working. Editable CVs remain local in `cv/`.

The five case studies distinguish independent analysis from employment, synthetic data from company data, and recommendations from implemented results. Power BI is independent-project experience; Golden Owl used GA4 and Looker Studio. The confidential case links to the existing protected data-site route. Credentials, raw reports and private evidence are not included in this repository.
