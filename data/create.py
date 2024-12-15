from fpdf import FPDF

# Function to sanitize text for latin-1 compatibility
def sanitize_text(text):
    replacements = {
        "—": "-", "’": "'", "“": '"', "”": '"', "•": "-"
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text

# Custom PDF class with proper margins and text wrapping
class PDF(FPDF):
    def __init__(self):
        super().__init__()
        self.set_left_margin(20)  # Increase left margin
        self.set_right_margin(20)  # Increase right margin
        self.set_top_margin(20)  # Top margin
        self.set_auto_page_break(auto=True, margin=20)  # Bottom margin for safe text flow

    def header(self):
        # Header for name and contact information
        self.set_font("Arial", "B", 18)
        self.cell(0, 10, "Aimee Ramirez", align="C", ln=True)
        self.set_font("Arial", "", 12)
        self.cell(0, 10, "Rhode Island | aimeelramirez@outlook.com | 401-636-5003", align="C", ln=True)
        self.ln(8)

    def section_title(self, title):
        # Bold and slightly larger font for section titles
        self.set_font("Arial", "B", 16)
        self.set_text_color(33, 37, 41)  # Dark grey color
        self.cell(0, 8, sanitize_text(title), ln=True)
        self.ln(2)

    def add_bullet_point(self, text, bold=False, apa_reference=False):
        # Handle bullet points with optional bold and APA formatting
        self.set_font("Arial", "B" if bold else "", 11)
        if apa_reference:
            text = sanitize_text(text) + ""
        self.cell(10)  # Indent for bullet point
        self.multi_cell(0, 8, f"{text}")
        self.ln(1)

    def section_body(self, body):
        # Body text with proper wrapping
        self.set_font("Arial", "", 12)
        self.multi_cell(0, 8, sanitize_text(body))
        self.ln(3)

# Content for the resume
# Content for the resume
resume_content = {
    "Summary": """A devoted, capable, and adaptable Software Engineer with a Bachelor of Science in Technology (Web Design Patterns and Development) and over five years of programming experience. Proficient in a wide range of technologies, software development, system analysis, and project management. Currently contributing to the field of AI and Large Language Models (LLMs), with expertise in designing software solutions, system validation, and AI-driven evaluations. Eager to continue solving complex technical challenges and advancing innovations.""",

    "Work Experience": [
        ("Outlier.ai - Software Engineer (AI Role), Providence, RI - November 2024 - Present", True, True),
        "Assisting in the training of Large Language Models (LLMs) for Outlier's clients, with a focus on integrating software engineering expertise into AI development.",
        "Evaluating LLM responses to ensure precision, quality, and applicability for client-specific needs.",
        "Designing and generating prompts to enhance training and alignment of LLMs with project goals.",
        "Leveraging technical and programming skills to refine AI-driven solutions, contributing to the advancement of AI technologies.",
        
        # Make the job title bold and apply APA formatting
        ("US Naval Undersea Warfare Center/DOD - IT Specialist (APPSW), Newport, RI - February 2024 - May 2024 (Probationary Period)", True, True),
        "Developed and maintained application software to support mission-critical operations, ensuring high performance and reliability.",
        "Conducted system analysis and designed solutions tailored to business and operational requirements.",
        "Provided advanced technical support, resolving complex issues and minimizing downtime.",
        "Successfully completed projects within tight deadlines, adhering to budgetary constraints."
    ],

    "Education": [
        "Full Sail University",
        " Master's of Computer Science | October 2023 - Present",
        " Bachelor's of Science in Technology | November 2021"
    ],

    "Skills": [
        " AI Training & Prompt Engineering",
        " Software Development & Validation",
        " System Analysis & Project Management",
        " Data Manipulation & Mathematical Modeling",
        " Advanced Technical Support"
    ]
}

# Generate the PDF
pdf = PDF()
pdf.add_page()

# Add content to the PDF
for section, content in resume_content.items():
    pdf.section_title(section)
    if isinstance(content, list):
        for item in content:
            # Check if item is a tuple for bold or APA-specific content
            if isinstance(item, tuple):
                pdf.add_bullet_point(item[0], bold=item[1], apa_reference=item[2])
            else:
                pdf.add_bullet_point(item)
    else:
        pdf.section_body(content)

# Save the PDF
file_path = "../assets/Aimee_Ramirez_Resume.pdf"
pdf.output(file_path)
print(f"Resume saved to: {file_path}")
