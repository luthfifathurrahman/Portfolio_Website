from pathlib import Path
import streamlit as st
from PIL import Image
import webbrowser

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "Resume - Luthfi Fathurrahman.pdf"
profile_pic = current_dir / "assets" / "Photo - Luthfi Fathurrahman.png"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Portfolio | Luthfi Fathurrahman"
PAGE_ICON = '🗂️'
NAME = "Luthfi Fathurrahman"
DESCRIPTION = """
Data Analyst
"""
EMAIL = "luthfifathurrahman22@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/luthfi-fathurrahman/",
    "GitHub" : "https://github.com/luthfifathurrahman",
    "Medium": "https://luthfifathurrahman.medium.com/"
}

st.set_page_config(
    page_title="Portfolio | Luthfi Fathurrahman",
    page_icon="🗂️"
)

# --- LOAD CSS, PDF, & PROFILE PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

profile_pic = Image.open(profile_pic)

# --- HERO SECTION ---
col_photo, col_profile = st.columns(2, gap="small")
with col_photo:
    st.image(profile_pic, width=230)

with col_profile:
    st.markdown("<h1 style='font-size: 48px;'>{}</h1>".format(NAME), unsafe_allow_html=True)
    st.download_button(
        label=" 📃 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream"
    )
    st.write("📧", EMAIL)

# --- SOCIAL LINKS ---
st.markdown("<br>", unsafe_allow_html=True)
cols = st.columns(len(SOCIAL_MEDIA))
for col, (platform, link) in zip(cols, SOCIAL_MEDIA.items()):
    if col.button(platform):
        webbrowser.open_new_tab(link)

# --- SKILLS ---
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: left; font-size: 36px;'>Hard Skills</h2>", unsafe_allow_html=True)
st.write("---")
st.markdown("""
<div>
    <ol>
        <li  style="text-align: justify; font-size: 18px;">Programming Language: Python (Pandas, Numpy, Selenium, Streamlit, Scikit-learn), SQL</li>
        <li  style="text-align: justify; font-size: 18px;">Data Visulization: PowerBi, Microsoft Excel, Python (Altair, Matplotlib, Seaborn)</li>
        <li  style="text-align: justify; font-size: 18px;">Modeling: Supervised Learning (Regressor, Classification), Unsupervised Learning (Clustering)</li>
        <li  style="text-align: justify; font-size: 18px;">Databases: MySQL</li>
    </ol>
</div>
""", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# --- WORK HISTORY ---
st.write('\n')
st.markdown("<h2 style='text-align: left; font-size: 36px;'>Work Experience</h2>", unsafe_allow_html=True)
st.write("---")

# --- JOB 1
st.markdown("<font size='5'>**PT. ORISOL INDONESIA MACHINERY | Field Application Engineer | Team Leader**</font>", unsafe_allow_html=True)
st.markdown("<font size='4'>**Salatiga, Central Java, Indonesia**</font>", unsafe_allow_html=True)
st.markdown("<font size='4'>**06/2022 - 07/2023**</font>", unsafe_allow_html=True)
st.markdown("""
<div>
    <li  style="text-align: justify; font-size: 18px;">Conducted machine installations, inspections, and maintenance, as well as repairs.</li>
    <li  style="text-align: justify; font-size: 18px;">Served as a team leader for the Central Java Province, overseeing and coordinating the team's activities.</li>
    <li  style="text-align: justify; font-size: 18px;">Maintained positive relationships with customers, ensuring high levels of customer satisfaction.</li>
    <li  style="text-align: justify; font-size: 18px;">Provided regular updates to customers regarding machine-related information.</li>
    <li  style="text-align: justify; font-size: 18px;">Submitted detailed reports to the headquarters in Taiwan, keeping them informed about on-site activities and developments.</li>
</div>
""", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")

































































































