# JungHo Lee’s website

Personal academic website at [jungholeestat.github.io](https://jungholeestat.github.io/), built with Jekyll and published through GitHub Pages.

## Editing the site

- `_pages/about.md`: introduction, portrait, and selected research.
- `_data/research.yml`: public research list; `selected: true` also displays a paper on About.
- `_pages/talks.md`: talks and presentations.
- `assets/css/academic.css`: typography, burgundy palette, and responsive layout.
- `_layouts/academic.liquid` and `_includes/`: shared page structure and research entries.
- `_news/`: personal announcements retained at `/news/`.

The previous `/publications/` address redirects to `/research/`. Personal PDFs and portraits remain in `assets/`. The bibliography in `_bibliography/papers.bib` and CV data in `_data/cv.yml` are retained as reference material; the displayed research list uses `_data/research.yml`. The CV link on About points to the existing public Google Drive document.

## Build and preview

Use Ruby 3.2.2 and Bundler 2.5.7, matching the deployment workflow:

```sh
bundle install
bundle exec jekyll build --strict_front_matter
python3 bin/check_site.py _site
```

For a local Jekyll development server:

```sh
bundle exec jekyll serve
```

To preview an already built `_site` with Vite, use Node 24:

```sh
npm ci
npm run preview
```

Check source formatting with `npm run format:check`.

## Deployment

Pull requests build the production site and check its pages and internal links without publishing. Merging into `master` builds and validates the site, then publishes that same output to the `gh-pages` branch. GitHub Pages serves that branch.

The repository retains the original MIT license notice in `LICENSE`.
