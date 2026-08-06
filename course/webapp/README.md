# Courseware Web App

This folder contains a small Flask site that renders the course design and lab markdown as a browsable web experience.

## Setup

From `e:\Code\ALDOT\course\webapp`:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
python app.py
```

Open `http://localhost:8000` in a browser.

## Routes

- `/` course home page
- `/page/course-design` design document
- `/page/implementation-plan` implementation and test plan
- `/page/missing-items` readiness gaps checklist
- `/labs` lab index
- `/labs/<lab-slug>` individual lab page

## Content Source

The app reads markdown from the existing course files, so updates to the labs automatically flow into the web UI.