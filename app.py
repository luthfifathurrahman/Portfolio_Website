from pathlib import Path
import streamlit as st
from PIL import Image
import requests
from streamlit_lottie import st_lottie

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
    "Medium": "https://luthfifathurrahman.medium.com/",
    "Email": "mailto:luthfifathurrahman22@gmail.com"
}
LOTTIE_HOUSE = "https://lottie.host/72c1c5d5-b5eb-449c-a168-5e2d9f4fd842/PNw7ogM9dI.json"
LOTTIE_AIRBNB = "https://lottie.host/89a84c80-9cb4-4ef3-865a-9d71b49cfc05/wp5MrvNGws.json"
LOTTIE_LIFEPLUS = "https://lottie.host/1362c96a-68bb-4e97-99ee-6d06c7688d50/3OYoCc33QN.json"

st.set_page_config(
    page_title="Portfolio | Luthfi Fathurrahman",
    page_icon="🗂️"
)


# --- LOTTIE ---
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

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
    st.markdown("<h1 style='font-size: 40px;'>{}</h1>".format(NAME), unsafe_allow_html=True)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📃 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream"
    )

# --- SOCIAL LINKS ---
st.markdown("<br>", unsafe_allow_html=True)
cols = st.columns(len(SOCIAL_MEDIA))
for col, (platform, link) in zip(cols, SOCIAL_MEDIA.items()):
    col.link_button(
        label=platform,
        url=link,
        use_container_width=True
    )   

# --- Projects & Accomplishments ---
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; font-size: 36px;'>Projects</h2>", unsafe_allow_html=True)
st.write("---")
colA1, colA2 = st.columns(2, gap="small")
with colA1:
    st_lottie(load_lottieurl(LOTTIE_HOUSE))
with colA2:
    st.markdown("<h3 style='text-align: left; font-size: 22px;'>Evaluating the 35-Year Mortgage Policy in Indonesia</h3>", unsafe_allow_html=True)
    st.markdown("""
        <div>
            <p style="text-align: justify; hyphens: auto; font-size: 15px;">
                Assessing the impact of Indonesia's 35-year mortgage policy on homeownership amidst a 11.84 million household housing backlog. Evaluating extending KPR tenor to 35 years, considering regional, demographic, and societal factors. Offering recommendations for balanced housing policies.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )   
    colA21, colA22 =  st.columns(2, gap="small")
    with colA21:
        st.link_button(
            label="GitHub Repo",
            url="https://github.com/luthfifathurrahman/The-35-Year-Mortgage-Policy-In-Indonesia",
            use_container_width=True
        )
    with colA22:
        st.link_button(
            label="Report",
            url="https://the-35-year-mortgage-policy-in-indonesia-luthfifathurrahman.streamlit.app/",
            use_container_width=True
        ) 
      

st.write("---")
colA1, colA2 = st.columns(2, gap="small")
with colA1:
    st_lottie(load_lottieurl(LOTTIE_AIRBNB))
with colA2:
    st.markdown("<h3 style='text-align: left; font-size: 22px;'>Airbnb Singapore</h3>", unsafe_allow_html=True)
    st.markdown("""
        <div>
            <p style="text-align: justify; hyphens: auto; font-size: 15px;">
                Maximize Airbnb profits: Evaluate competitors and properties in each area. Analyze customer behavior for effective pricing and marketing strategies. Tailor offerings to stand out and optimize revenue.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )   
    # st.write("")
    # st.write("")
    # st.write("")
    # st.write("")
    # st.write("")
    colA21, colA22 =  st.columns(2, gap="small")
    with colA21:
        st.link_button(
            label="GitHub Repo",
            url="https://github.com/luthfifathurrahman/Airbnb-Singapore",
            use_container_width=True
        )
    # with colA22:
    #     st.link_button(
    #         label="Report",
    #         url="https://the-35-year-mortgage-policy-in-indonesia-luthfifathurrahman.streamlit.app/",
    #         use_container_width=True
    #     ) 

st.write("---")
colA1, colA2 = st.columns(2, gap="small")
with colA1:
    st_lottie(load_lottieurl(LOTTIE_LIFEPLUS))
with colA2:
    st.markdown("<h3 style='text-align: left; font-size: 22px;'>LifePlus</h3>", unsafe_allow_html=True)
    st.markdown("""
        <div>
            <p style="text-align: justify; hyphens: auto; font-size: 15px;">
                A fall detection system incorporating accelerometer and gyroscope sensors, augmented by adaptive neuro fuzzy inference system (ANFIS), achieves 100% sensitivity and specificity, distinguishing falls from daily activities. Data collected via Arduino, processed in Excel, validated, and further automated using MATLAB to enhance device reliability. Validation conducted with Arduino ensures system accuracy.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )
    colA21, colA22 =  st.columns(2, gap="small")
    with colA21:
        st.link_button(
            label="See Details",
            url="https://repository.its.ac.id/50802/",
            use_container_width=True
        ) 
      
































































































