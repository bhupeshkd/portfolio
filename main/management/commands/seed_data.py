from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from main.models import (
    Profile, Project, Technology, Skill, Experience,
    Education, Achievement, Resume, ContactMessage
)


class Command(BaseCommand):
    help = 'Seed initial portfolio data for the admin panel'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Seeding portfolio data...'))

        # Create default admin user
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'bhupeshdeww@gmail.com', 'admin123')
            self.stdout.write('  ✓ Admin user created (username: admin, password: admin123)')
        else:
            self.stdout.write('  - Admin user already exists')

        # Create profile
        if not Profile.objects.exists():
            Profile.objects.create(
                name='Bhupesh Dewangan',
                title='Python & Django Developer',
                about_text=(
                    "I'm passionate about turning complex problems into elegant, scalable solutions. "
                    "My journey in software development started with Python and evolved into building "
                    "full-stack Django applications. I specialize in backend architecture, real-time "
                    "features, API design, and performance optimization."
                ),
                email='bhupeshdeww@gmail.com',
                phone='+91 00000 00000',
                location='Chhattisgarh, India',
                github_url='https://github.com/bhupeshdew',
                linkedin_url='https://linkedin.com/in/bhupesh-dew',
                twitter_url='https://x.com/bhupeshdew',
                available=True,
                available_text='Available for work',
            )
            self.stdout.write('  ✓ Profile created')
        else:
            self.stdout.write('  - Profile already exists')

        # Technologies
        techs = {
            'Python': 'fab fa-python',
            'Django': 'fab fa-python',
            'DRF': 'fas fa-server',
            'JavaScript': 'fab fa-js-square',
            'HTML': 'fab fa-html5',
            'CSS': 'fab fa-css3-alt',
            'SQL': 'fas fa-database',
            'MySQL': 'fas fa-database',
            'SQLite': 'fas fa-database',
            'Git': 'fab fa-git-alt',
            'GitHub': 'fab fa-github',
            'Docker': 'fab fa-docker',
            'REST APIs': 'fas fa-plug',
            'React': 'fab fa-react',
        }
        tech_objs = {}
        for name, icon in techs.items():
            obj, created = Technology.objects.get_or_create(name=name, defaults={'icon': icon})
            tech_objs[name] = obj
            if created:
                self.stdout.write(f'  ✓ Technology added: {name}')

        # Skills
        skills_data = [
            ('Python', 'backend', 'fab fa-python', 95),
            ('Django', 'backend', 'fab fa-python', 90),
            ('Django REST Framework', 'backend', 'fas fa-server', 85),
            ('REST API Design', 'backend', 'fas fa-plug', 82),
            ('JavaScript', 'frontend', 'fab fa-js-square', 75),
            ('HTML5', 'frontend', 'fab fa-html5', 90),
            ('CSS3', 'frontend', 'fab fa-css3-alt', 80),
            ('MySQL', 'database', 'fas fa-database', 85),
            ('SQLite', 'database', 'fas fa-database', 90),
            ('SQL', 'database', 'fas fa-database', 88),
            ('Git & GitHub', 'tools', 'fab fa-git-alt', 85),
            ('Docker', 'tools', 'fab fa-docker', 65),
            ('Linux', 'tools', 'fab fa-linux', 70),
            ('VS Code', 'tools', 'fas fa-code', 92),
        ]
        for skill_name, cat, icon, pct in skills_data:
            obj, created = Skill.objects.get_or_create(
                name=skill_name,
                defaults={'category': cat, 'icon': icon, 'percentage': pct}
            )
            if created:
                self.stdout.write(f'  ✓ Skill added: {skill_name} ({pct}%)')

        # Experiences
        exp_data = [
            {
                'position': 'Python/Django Developer (Freelance)',
                'company': 'Self-employed',
                'start_date': '2024 - Present',
                'description': 'Building scalable web applications and REST APIs for clients. Handling complete software lifecycle from requirements to deployment.',
                'technologies': 'Python, Django, DRF, MySQL, Git',
            },
            {
                'position': 'Web Developer (Intern)',
                'company': 'Tech Startup',
                'start_date': '2023 - 2024',
                'description': 'Developed and maintained web applications using Django. Collaborated with cross-functional teams to ship features.',
                'technologies': 'Python, Django, JavaScript, HTML, CSS',
            },
            {
                'position': 'Self-Taught Programmer',
                'company': 'Personal Learning Journey',
                'start_date': '2020 - 2023',
                'description': 'Started learning programming with Python. Built numerous personal projects to master backend development.',
                'technologies': 'Python, SQL, Git, Linux',
            },
        ]
        for exp in exp_data:
            obj, created = Experience.objects.get_or_create(
                position=exp['position'],
                defaults={**exp}
            )
            if created:
                self.stdout.write(f'  ✓ Experience added: {exp["position"]}')

        # Education
        edu_data = [
            {
                'degree': 'Bachelor of Technology (B.Tech)',
                'institution': 'University / College Name',
                'start_date': '2020 - 2024',
                'description': 'Major in Computer Science with focus on software engineering and web technologies.',
            },
            {
                'degree': 'Higher Secondary (12th)',
                'institution': 'School Name',
                'start_date': '2018 - 2020',
                'description': 'Science stream with Mathematics and Computer Science.',
            },
        ]
        for edu in edu_data:
            obj, created = Education.objects.get_or_create(
                degree=edu['degree'],
                defaults={**edu}
            )
            if created:
                self.stdout.write(f'  ✓ Education added: {edu["degree"]}')

        # Achievements
        ach_data = [
            {
                'title': '100+ Problems Solved',
                'description': 'Solved over 100 coding problems on LeetCode and HackerRank',
                'icon': 'fas fa-trophy',
            },
            {
                'title': '5-Star Python Badge',
                'description': 'Achieved 5-star rating in Python on HackerRank',
                'icon': 'fas fa-star',
            },
            {
                'title': 'Open Source Contributor',
                'description': 'Contributed to open source projects on GitHub',
                'icon': 'fab fa-github',
            },
        ]
        for ach in ach_data:
            obj, created = Achievement.objects.get_or_create(
                title=ach['title'],
                defaults={**ach}
            )
            if created:
                self.stdout.write(f'  ✓ Achievement added: {ach["title"]}')

        # Sample Projects
        sample_projects = [
            {
                'title': 'Task Manager App',
                'description': 'A full-featured task management application built with Django. Features user authentication, task CRUD operations, email notifications, and a responsive dashboard with charts.',
                'category': 'web',
                'techs': ['Python', 'Django', 'DRF', 'SQLite', 'JavaScript', 'CSS'],
                'featured': True,
            },
            {
                'title': 'RESTful API for E-commerce',
                'description': 'Production-ready RESTful API for an e-commerce platform. Includes JWT authentication, product catalog, cart, orders, and payment integration.',
                'category': 'web',
                'techs': ['Python', 'Django', 'DRF', 'MySQL', 'REST APIs'],
                'featured': True,
            },
            {
                'title': 'Portfolio Website',
                'description': 'Modern, multi-page portfolio website with 3D particle background, dark/light theme, and full admin panel for content management.',
                'category': 'web',
                'techs': ['Python', 'Django', 'HTML', 'CSS', 'JavaScript'],
                'featured': True,
            },
        ]
        for sp in sample_projects:
            if not Project.objects.filter(title=sp['title']).exists():
                project = Project.objects.create(
                    title=sp['title'],
                    description=sp['description'],
                    category=sp['category'],
                    featured=sp['featured'],
                )
                for t in sp['techs']:
                    project.technologies.add(tech_objs.get(t) or Technology.objects.get_or_create(name=t)[0])
                self.stdout.write(f'  ✓ Project added: {sp["title"]}')

        self.stdout.write(self.style.SUCCESS('✔ Seed data complete!'))
        self.stdout.write(self.style.SUCCESS('Login to admin at /admin/ with username: admin, password: admin123'))