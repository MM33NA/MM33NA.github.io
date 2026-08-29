# Portfolio Website Architecture — Plain Language Reference

**Project:** Meena Maharjan's Professional Portfolio  
**Live URL:** https://MM33NA.github.io  
**Last updated:** August 2026

---

## What This Website Is

A **static professional portfolio website** built with free tools and hosted for free on GitHub. 
It displays research experience, publications, projects, education, and skills for professional 
and academic audiences.

"Static" means the website is made of plain HTML files — there is no database, no server 
running code, no login system. Just files served directly to the browser.

---

## The Three-Layer System

The entire site works in three layers that stay separate from each other:

```
LAYER 1 — CONTENT       LAYER 2 — DISPLAY         LAYER 3 — STYLE
data/*.yaml         →   *.qmd pages           →   styles/custom.css
(what it says)          (how it is structured)     (how it looks)
```

**Why this matters:** You can update your publications without touching the page layout. 
You can redesign the colors without touching your content. Each layer is independent.

---

## The Files and What They Do

### The Control File
```
_quarto.yml
```
The master settings file. Controls:
- Site title
- Navigation bar (which pages appear and in what order)
- Visual theme
- CSS file location

If you want to add a new page to the nav bar, this is the only file you touch.

---

### The Content Files (your filing cabinet)
```
data/
├── education.yaml       ← degrees, institutions, years
├── experience.yaml      ← jobs, responsibilities, projects
├── publications.yaml    ← papers, reports, abstracts, in-progress work
├── projects.yaml        ← technical tools and portfolio projects
└── skills.yaml          ← skills organized by category
```

These are plain text files written in **YAML format** — a structured way of 
organizing information, like a clean spreadsheet saved as text.

**The rule:** When your professional information changes (new paper, new job, new skill), 
you only edit these files. You never touch the pages themselves.

Example — adding a new publication means adding this to `publications.yaml`:
```yaml
- authors: "Maharjan, M., et al."
  year: 2027
  title: "Your new paper title"
  journal: "Journal Name"
  status: "published"
  doi: "https://doi.org/..."
```
Save the file, push to GitHub, done. The publications page updates automatically.

---

### The Page Files (display templates)
```
index.qmd          ← Home page
about.qmd          ← About / background / research interests
education.qmd      ← Education (reads from data/education.yaml)
experience.qmd     ← Experience (reads from data/experience.yaml)
research.qmd       ← Research areas and methodology
publications.qmd   ← Publications (reads from data/publications.yaml)
projects/
└── index.qmd      ← Projects (reads from data/projects.yaml)
skills.qmd         ← Skills (reads from data/skills.yaml)
contact.qmd        ← Contact and profile links
```

Each file is a **QMD file** (Quarto Markdown). It is a mix of:

- **Plain Markdown text** — headings, paragraphs, bullet points written by hand 
  (used in about.qmd, research.qmd, contact.qmd)
- **Python code blocks** — code that opens a YAML file, reads through it, and 
  prints formatted content (used in education.qmd, experience.qmd, publications.qmd, 
  projects/index.qmd, skills.qmd)

The Python code pages follow this logic:
```
Open YAML file → Loop through each item → Print formatted text → Quarto renders as HTML
```

---

### The Style File
```
styles/custom.css
```
Controls all visual appearance — fonts, colors, spacing, layout. Currently minimal 
(using default Quarto theme). Phase 3 design work happens entirely here without 
touching any content or page files.

---

### The Deployment File
```
.github/workflows/deploy.yml
```
Instructions for GitHub's automated system (GitHub Actions). Every time you push 
to the `main` branch, GitHub reads this file and:

1. Starts a fresh computer in the cloud
2. Installs Python and Quarto on it
3. Copies all your project files onto it
4. Runs `quarto render` — builds the complete website into HTML files
5. Publishes those HTML files to GitHub Pages (your live URL)

You never run this manually. Push to `main` → site updates automatically in 2-3 minutes.

---

### The Ignore File
```
.gitignore
```
Tells Git which files and folders to ignore — things that should never be uploaded 
to GitHub. Currently ignores:
- `_site/` — the built HTML files (GitHub rebuilds these automatically)
- `__pycache__/` — Python temporary files
- `.env` — where API keys or secrets would live
- `.DS_Store` — Mac system files

---

## How a Page Gets Built

Using Publications as the example:

```
Step 1:  Quarto reads publications.qmd
         
Step 2:  It finds the Python code block inside
         
Step 3:  It runs the Python code:
         - Opens data/publications.yaml
         - Loops through each publication
         - Prints formatted Markdown text
         
Step 4:  Quarto takes that output and wraps it
         in HTML using the theme from _quarto.yml
         
Step 5:  Result: _site/publications.html
         (a finished webpage ready to serve)
```

The `_site/` folder is where all finished HTML files go. You never edit it directly — 
it gets completely regenerated every time Quarto builds the site.

---

## The Two Branches — Dev and Main

```
dev branch                         main branch
(your workshop)                    (the live shop window)
      |                                   |
You write and edit files here      GitHub Actions watches
Test with: quarto preview          this branch and deploys
      |                            to the internet
      └──── git merge ────────────►
            (when ready)
```

- **`dev`** — where all work happens. Safe to experiment, break things, fix things.
- **`main`** — production only. Merging here triggers a live deployment.

---

## The Full Workflow — From Edit to Live Site

```
1. Edit a file
   (e.g. add a paper to data/publications.yaml)
          │
2. Test locally
   quarto preview
   (opens site in browser at localhost)
          │
3. Confirm it looks right
          │
4. Stage and commit
   git add .
   git commit -m "Add new publication"
          │
5. Push to dev
   git push origin dev
          │
6. Merge to main
   git checkout main
   git merge dev
   git push origin main
          │
7. GitHub Actions runs automatically
   (builds and deploys the site)
          │
8. Live at https://MM33NA.github.io
   (within 2-3 minutes)
```

---

## The Technology Stack — Plain Definitions

| Tool | What it is | What it does here |
|------|-----------|-------------------|
| **Quarto** | A document/website publishing system | Converts .qmd files into HTML pages |
| **Python** | Programming language | Reads YAML data and formats it for display |
| **YAML** | A structured text format | Stores professional content (publications, jobs, etc.) |
| **GitHub** | Code hosting platform | Stores all project files with version history |
| **GitHub Pages** | Free static website hosting | Serves the finished HTML files to the internet |
| **GitHub Actions** | Automated workflow runner | Builds and deploys the site on every push to main |
| **CSS** | Stylesheet language | Controls colors, fonts, spacing, visual design |
| **Markdown** | Simple text formatting | Used to write page content (headings, bullets, bold) |

---

## What Is Free and Why

| Service | Cost | Why free |
|---------|------|----------|
| GitHub repository | Free | Public repositories are free on GitHub |
| GitHub Pages hosting | Free | Included for public repos, up to 1GB |
| GitHub Actions | Free | Included for public repos |
| Quarto | Free | Open source, developed by Posit |
| Python | Free | Open source |
| Custom domain (optional) | ~$10-15/year | Only the domain registration, not hosting |

The only thing you would ever pay for is a custom domain name (e.g. `meenamaharjan.com`). 
The hosting itself is always free.

---

## What NOT to Put on This Website

Never commit these to the GitHub repository:
- Home address (city and state only is fine)
- Personal phone number
- API keys, tokens, or passwords
- Contract details or legal documents
- Confidential employer information
- Private or identifiable research data

---

## Quick Reference — Which File to Edit for What

| What you want to change | File to edit |
|------------------------|--------------|
| Add a new publication | `data/publications.yaml` |
| Add a new job | `data/experience.yaml` |
| Add a new project | `data/projects.yaml` |
| Add a new skill | `data/skills.yaml` |
| Update education | `data/education.yaml` |
| Edit the About page text | `about.qmd` |
| Edit the Research page text | `research.qmd` |
| Change navigation bar | `_quarto.yml` |
| Change colors or fonts | `styles/custom.css` |
| Change site title | `_quarto.yml` |
| Add a whole new page | Create new `.qmd` file + add to `_quarto.yml` |

---

*Built with Quarto 1.10.18 + GitHub Pages + GitHub Actions*  
*Repository: https://github.com/MM33NA/MM33NA.github.io*
