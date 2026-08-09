# 🚀 Portfolio Website

A modern, animated personal portfolio built with **Django**, featuring a 3D particle home page, dark/light themes, and a custom admin experience.

## ✨ Features

- 🏠 **Home** — 3D particle background (Three.js), typed text animation, animated skill cards, orbit visualization, featured projects, live stats
- 🗂️ **Projects** — Filterable grid with category & featured badges, hover 3D-tilt cards, project detail pages
- 📄 **Resume** — Sticky profile card, experience/education timeline, achievements grid, PDF download
- ✉️ **Contact** — Custom Django form with 3D-styled inputs, validation, success page
- 🎨 **Extras** — Preloader, custom cursor, scroll progress bar, back-to-top, glitch 404 page, fully custom admin, dark/light theme toggle
- ♿ **Accessible** — Skip-to-content link, ARIA labels, keyboard-friendly navigation
- ⚡ **Performance** — Lazy-loaded images, deferred Three.js (homepage only), AOS animations

## 🛠️ Tech Stack

| Layer    | Tech                              |
|----------|-----------------------------------|
| Backend  | Python, Django 6                  |
| Frontend | HTML, CSS, JavaScript             |
| Animations | Three.js, VanillaTilt, AOS, GSAP |
| Icons    | Font Awesome 6                    |
| Fonts    | Space Grotesk, Inter, JetBrains Mono |
| Database | SQLite                            |

## 📦 Setup

```bash
# 1. Clone the repository
git clone https://github.com/bhupeshkd/portfolio.git
cd portfolio

# 2. Create & activate a virtual environment
python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate    # macOS/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run migrations
python manage.py migrate

# 5. Seed the database with sample content
python manage.py seed_data

# 6. Start the development server
python manage.py runserver
```

Then open http://127.0.0.1:8000 🎉

## 🔑 Admin Access

```bash
python manage.py createsuperuser
```

Admin is available at `/admin/` — fully customized with a custom dashboard index and branding.

## 🗂️ Project Structure

```
portfolio/
├── main/                  # Core app
│   ├── models.py          # Project, Skill, Experience, Education, Achievement, Profile
│   ├── views.py           # Page views
│   ├── forms.py           # Contact form
│   ├── admin.py           # Custom admin
│   ├── context_processors.py  # Global site context
│   ├── middleware.py      # Custom middleware
│   └── management/commands/seed_data.py  # Database seeder
├── portfolio/             # Project config (settings, urls)
├── templates/             # Django templates
│   └── partials/          # Resume sections
├── static/
│   ├── css/               # style.css + templates.css
│   ├── js/                # main.js + theme.js
│   └── images/
└── media/                 # Uploaded project images & resume
```

## 🧪 Useful Commands

```bash
python manage.py check            # System checks
python manage.py seed_data        # Reset/populate demo data
python manage.py collectstatic    # Production static files
```

## 📄 License

MIT © [Bhupesh Dewangan](https://github.com/bhupeshkd)