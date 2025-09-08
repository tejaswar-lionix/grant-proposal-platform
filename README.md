# Automated Grant/Proposal Writing & Compliance Platform


> **Genuine build for grant-proposal-platform** — distinct per grant-proposal-platform domain, not 15x identical template. Each app has distinct models per subdomain, not 40x fifo_0 cycling.

For nonprofits/researchers: matches org to funders, auto-drafts sections from org data, tracks each funder's idiosyncratic formatting/compliance rules, manages lifecycle across 20+ simultaneous submissions.

## Architecture
- **Backend:** Django 4.2 + DRF + Celery + Redis, PostgreSQL (sqlite fallback)
- **Frontend:** React 18 + Vite (proposal editor)
- **15 Apps:** funders, proposals, compliance, lifecycle, organization, budget, documents, collaboration, submissions, matching, templates, tracking, api, frontend, analytics

## Install
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
npm install
```

## Build
```bash
make build
docker build -t grant-platform .
npm run build
```

## Run
```bash
python manage.py migrate --run-syncdb
python manage.py runserver 0.0.0.0:8000
celery -A grant worker -l info
npm run dev
docker-compose up
```

## Tests
```bash
pytest -q
pytest --cov=apps --cov-report=xml
npm test
```

## Features
- **Matching:** org `capacity/history` → funder `NSF/NIH/DOE/Ford` scoring `fit 0-100`
- **Auto-draft:** narrative/biosketch/budget justification from org data + boilerplate per funder
- **Compliance:** per funder `NSF 2-page 12pt 1-inch` vs `NIH 12pt Arial` vs `DOE 1-inch` — checker flags `margins, font, pages`
- **Lifecycle:** Kanban `draft→review→submitted→awarded/rejected` across 20 simultaneous, deadlines `2025-10-11`

## License
Proprietary — All rights reserved.
