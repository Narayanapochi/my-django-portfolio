from portfolio_app.models import SiteConfig, Skill, Project, ProjectBullet, Training, Certificate, Achievement

Skill.objects.all().delete()
Project.objects.all().delete()
ProjectBullet.objects.all().delete()
Training.objects.all().delete()
Certificate.objects.all().delete()
Achievement.objects.all().delete()

# SiteConfig
config, created = SiteConfig.objects.get_or_create(id=1)
config.name = "Narayana Reddy"
config.tagline = "Computer Science Student & Cybersecurity Enthusiast"
config.bio = "Passionate developer with expertise in cybersecurity and full-stack web development. I love building secure, scalable applications and solving complex problems with elegant solutions."
config.email = "pnarayanareddy218@gmail.com"
config.mobile = "+91-6302673567"
config.github = "https://github.com/Narayanapochi"
config.linkedin = "https://www.linkedin.com/in/pochireddygari-narayanareddy"
config.education_text = "Currently pursuing B.Tech in Computer Science & Engineering at Lovely Professional University, Phagwara, Punjab with a CGPA of 6.78. Passionate about cybersecurity, ethical hacking, and building secure full-stack applications."
config.tags = "JavaScript,Python,C++,Cybersecurity,MERN Stack,Django,Kali Linux"
config.stat1_value = "6.78"
config.stat1_label = "CGPA"
config.stat2_value = "3"
config.stat2_label = "Certificates"
config.stat3_value = "2"
config.stat3_label = "Projects"
config.stat4_value = "1"
config.stat4_label = "Training"
config.save()

# Skills
def add_skill(name, category, order=0):
    Skill.objects.create(name=name, category=category, order=order)

# Languages
add_skill("Java", "language", 1)
add_skill("Python", "language", 2)
add_skill("JavaScript", "language", 3)

# Frameworks requested
add_skill("HTML", "framework", 1)
add_skill("CSS", "framework", 2)
add_skill("React", "framework", 3)
add_skill("Node.js", "framework", 4)
add_skill("Django", "framework", 5)

# Tools requested
add_skill("Wireshark", "tool", 1)
add_skill("Nmap", "tool", 2)
add_skill("Kali Linux", "tool", 3)
add_skill("Metasploit", "tool", 4)
add_skill("Git", "tool", 5)

# Soft Skills
add_skill("Problem-Solving", "soft", 1)
add_skill("Analytical Thinking", "soft", 2)
add_skill("Quick Learning", "soft", 3)
add_skill("Adaptability", "soft", 4)

# Projects
p1 = Project.objects.create(
    title="E-commerce Web Application",
    description="Scalable MERN-stack platform for product discovery and catalog management with Stripe API payment processing.",
    tech_stack="React, Node.js, MongoDB, Stripe API",
    start_date="Nov '23",
    end_date="Dec '23",
    featured=True,
    order=1
)
ProjectBullet.objects.create(project=p1, text="Architected a scalable MERN-stack platform for product discovery and catalog management.", order=1)
ProjectBullet.objects.create(project=p1, text="Implemented secure JWT authentication and role-based access.", order=2)
ProjectBullet.objects.create(project=p1, text="Engineered a high-performance shopping cart with real-time updates.", order=3)
ProjectBullet.objects.create(project=p1, text="Integrated Stripe API for secure, PCI-compliant checkout.", order=4)

p2 = Project.objects.create(
    title="Hotel Reservation System",
    description="Java-based Hotel Reservation System enabling seamless room booking and payment processing.",
    tech_stack="Java, OOP",
    featured=True,
    order=2
)
ProjectBullet.objects.create(project=p2, text="Applied OOP principles by designing modular classes (Hotel, Room, Reservation, Payment) for scalability.", order=1)
ProjectBullet.objects.create(project=p2, text="Built a console-based application to manage bookings, check room availability, and process transactions.", order=2)

# Training
t1 = Training.objects.create(
    title="Data Structures & Algorithms Training",
    organization="Cipher Schools",
    start_date="Jun '20",
    end_date="Jul '23",
    order=1
)
t1.bullets.create(text="Covered essential concepts including arrays, linked lists, stacks, queues, trees, graphs, and dynamic programming.", order=1)
t1.bullets.create(text="Tackled 100+ coding challenges, strengthening analytical reasoning and logical problem-solving.", order=2)
t1.bullets.create(text="Examined time/space complexity and applied efficient algorithmic strategies.", order=3)
t1.bullets.create(text="Completed a Java console-based Library Management System as the capstone project.", order=4)

# Certificates
Certificate.objects.create(
    title="Oracle Cloud Infrastructure 2025 Certified AI Foundations Associate",
    issuer="Oracle University",
    end_date="Mar '26",
    order=1
)
Certificate.objects.create(
    title="Object Oriented Programming",
    issuer="IAM Neo Platform",
    start_date="Aug '24",
    end_date="Dec '24",
    order=2
)
Certificate.objects.create(
    title="Responsive Web Design",
    issuer="Free Code Camp",
    end_date="Nov '23",
    order=3
)

# Achievements
Achievement.objects.create(text="Earned IBM's verified proficiency badge for Introduction to Hardware and Operating Systems via Coursera & Credly (Nov 2024)", order=1)
Achievement.objects.create(text="Participated in the Code of Duty Web Hackathon 2024, demonstrating strong teamwork and innovative problem-solving (Mar 2024)", order=2)

print("Database successfully updated with requested custom details!")
