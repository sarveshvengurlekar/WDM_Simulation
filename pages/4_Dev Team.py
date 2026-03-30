import streamlit as st

st.set_page_config(
    page_title="WDM Simulator",
    layout="wide",
    initial_sidebar_state="expanded",
    )

# ---------------- UI STYLING ---------------- #
st.markdown("""
<style>

/* ---------- REMOVE DEFAULT SPACING ---------- */
body {
    margin: 0 !important;
    padding: 0 !important;
}

.block-container {
    padding-top: 0rem !important;
}

/* ---------- HEADER ---------- */
.header {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 90px;
    background: linear-gradient(135deg, #0f2027, #2c5364);
    color: white;
    z-index: 1000;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0 4px 20px rgba(0,0,0,0.3);
}

.header-title {
    font-size: 26px;
    font-weight: 700;
}

/* ---------- MAIN OFFSET ---------- */
.stApp {
    margin-top: 90px;
    padding-bottom: 120px;   /* prevents footer overlap */
}

/* ---------- SIDEBAR ---------- */
section[data-testid="stSidebar"] {
    background: linear-gradient(135deg, #0f2027, #2c5364);
    color: white;
}

section[data-testid="stSidebar"] * {
    color: #f1f1f1 !important;
}

/* ---------- BUTTON ---------- */
.stButton > button {
    border-radius: 12px;
    background: linear-gradient(135deg, #00c6ff, #0072ff);
    color: white;
    font-weight: bold;
}

/* ---------- METRICS ---------- */
[data-testid="metric-container"] {
    background: white;
    border-radius: 12px;
    padding: 15px;
}

/* ---------- FOOTER (NO OVERLAP) ---------- */
.footer {
    position: relative;
    width: 100%;
    background: #0f2027;
    color: #bbb;
    text-align: center;
    padding: 10px;
    margin-top: 40px;
}

/* ---------- TITLE ---------- */
h1 {
    text-align: center;
}

/* Hide default Streamlit header */
header {
    display: none !important;
}

</style>

<!-- HEADER -->
<div class="header">
    <div class="header-title">
        📡 WDM Optical Network Simulator
    </div>
</div>

""", unsafe_allow_html=True)


st.markdown(
    """
    <style>
    div.stLinkButton > a {
        display: block;
        margin: auto;
        border: 2px solid black;         
        border-radius: 10px;
        background-color: #08f1e4;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True)

st.title("</> Dev Team", text_alignment="center")

st.divider()

linkedin_pranali = "https://www.linkedin.com/in/pranali-choudhari-89aa4215/"
email_pranali = "mailto:pranali.choudhari@fcrit.ac.in?subject=Sharing Feedback and Connection Request Regarding FCRIT’s Signal Processing Virtual Lab."

linkedin_sachin = "https://www.linkedin.com/in/sachin-malpe-5161892a7/"
email_sachin = "mailto:3022131@extc.fcrit.ac.in?subject=Sharing Feedback and Connection Request Regarding WDM Simulator."

linkedin_sujal = "https://www.linkedin.com/in/rushikesh-gajbe-2b37932a4/"
email_sujal = "mailto:3022116@extc.fcrit.ac.in?subject=Sharing Feedback and Connection Request Regarding WDM Simulator."

linkedin_rushikesh = "https://www.linkedin.com/in/rushikesh-gajbe-2b37932a4/"
email_rushikesh = "mailto:3022164@extc.fcrit.ac.in?subject=Sharing Feedback and Connection Request Regarding WDM Simulator."

linkedin_sarvesh = "https://www.linkedin.com/in/sarvesh-vengurlekar-"
email_sarvesh = "mailto:3022170@extc.fcrit.ac.in?subject=Sharing Feedback and Connection Request Regarding WDM Simulator."


# UI Design
st.header(" ")

col1, col2, col3, col4 = st.columns(4)

with col1:
    with st.container():
        st.markdown(
            f"""
        <style>
            .profile-card {{
                text-align: center;
                background: linear-gradient(135deg, #0f2027, #2c5364);
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
                display: inline-block;
            }}
            .name {{
                font-size: 24px;
                font-weight: bold;
                margin-top: 10px;
                color: white;
            }}
            .title {{
                font-size: 16px;
                color: white;
                margin-top: 5px;
            }}
            .button-container {{
                display: flex;
                flex-direction: column;
                align-items: center;
                margin-top: 10px;
            }}
            .button {{
                background-color: white;
                border: none;
                padding: 10px 15px;
                text-align: center;
                font-size: 16px;
                border-radius: 5px;
                cursor: pointer;
                text-decoration: none;
                margin: 5px;
                display: inline-flex;
                align-items: center;
                gap: 10px;
            }}
            .linkedin-button {{
                color: black;
            }}
            .icon {{
                width: 20px;
                height: 20px;
            }}
        </style>
        <div class="profile-card">
            <div class="name">Sachin Manesh Malpe</div>
            <div class="title">Developer</div>
                <a href="{linkedin_sachin}" target="_blank" class="button linkedin-button">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png" class="icon">
                </a>
                <a href="{email_sachin}" class="button">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/4/4e/Gmail_Icon.png" class="icon">
                </a>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
        
    st.header(" ")
    
with col2:        
    with st.container():
        st.markdown(
            f"""
        <style>
            .profile-card {{
                text-align: center;
                background: linear-gradient(135deg, #0f2027, #2c5364);
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
                display: inline-block;
            }}
            .name {{
                font-size: 24px;
                font-weight: bold;
                margin-top: 10px;
                color: white;
            }}
            .title {{
                font-size: 16px;
                color: white;
                margin-top: 5px;
            }}
            .button-container {{
                display: flex;
                flex-direction: column;
                align-items: center;
                margin-top: 10px;
            }}
            .button {{
                background-color: white;
                border: none;
                padding: 10px 15px;
                text-align: center;
                font-size: 16px;
                border-radius: 5px;
                cursor: pointer;
                text-decoration: none;
                margin: 5px;
                display: inline-flex;
                align-items: center;
                gap: 10px;
            }}
            .linkedin-button {{
                color: black;
            }}
            .icon {{
                width: 20px;
                height: 20px;
            }}
        </style>
        <div class="profile-card">
            <div class="name">Sujal Prakash Ghadge</div>
            <div class="title">Developer</div>
                <a href="{linkedin_sujal}" target="_blank" class="button linkedin-button">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png" class="icon">
                </a>
                <a href="{email_sujal}" class="button">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/4/4e/Gmail_Icon.png" class="icon">
                </a>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


with col3:
    with st.container():
        st.markdown(
            f"""
        <style>
            .profile-card {{
                text-align: center;
                background: linear-gradient(135deg, #0f2027, #2c5364);
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
                display: inline-block;
            }}
            .name {{
                font-size: 24px;
                font-weight: bold;
                margin-top: 10px;
                color: white;
            }}
            .title {{
                font-size: 16px;
                color: white;
                margin-top: 5px;
            }}
            .button-container {{
                display: flex;
                flex-direction: column;
                align-items: center;
                margin-top: 10px;
            }}
            .button {{
                background-color: white;
                border: none;
                padding: 10px 15px;
                text-align: center;
                font-size: 16px;
                border-radius: 5px;
                cursor: pointer;
                text-decoration: none;
                margin: 5px;
                display: inline-flex;
                align-items: center;
                gap: 10px;
            }}
            .linkedin-button {{
                color: black;
            }}
            .icon {{
                width: 20px;
                height: 20px;
            }}
        </style>
        <div class="profile-card">
            <div class="name">Rushikesh Nitin Gajbe</div>
            <div class="title">Developer</div>
                <a href="{linkedin_rushikesh}" target="_blank" class="button linkedin-button">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png" class="icon">
                </a>
                <a href="{email_rushikesh}" class="button">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/4/4e/Gmail_Icon.png" class="icon">
                </a>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
        
    st.header(" ")
    
with col4:        
    with st.container():
        st.markdown(
            f"""
        <style>
            .profile-card {{
                text-align: center;
                background:linear-gradient(135deg, #0f2027, #2c5364);
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
                display: inline-block;
            }}
            .name {{
                font-size: 24px;
                font-weight: bold;
                margin-top: 10px;
                color: white;
            }}
            .title {{
                font-size: 16px;
                color: white;
                margin-top: 5px;
            }}
            .button-container {{
                display: flex;
                flex-direction: column;
                align-items: center;
                margin-top: 10px;
            }}
            .button {{
                background-color: white;
                border: none;
                padding: 10px 15px;
                text-align: center;
                font-size: 16px;
                border-radius: 5px;
                cursor: pointer;
                text-decoration: none;
                margin: 5px;
                display: inline-flex;
                align-items: center;
                gap: 10px;
            }}
            .linkedin-button {{
                color: black;
            }}
            .icon {{
                width: 20px;
                height: 20px;
            }}
        </style>
        <div class="profile-card">
            <div class="name">Sarvesh Udaykumar Vengurlekar</div>
            <div class="title">Developer</div>
                <a href="{linkedin_sarvesh}" target="_blank" class="button linkedin-button">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png" class="icon">
                </a>
                <a href="{email_sarvesh}" class="button">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/4/4e/Gmail_Icon.png" class="icon">
                </a>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
st.markdown('</div>', unsafe_allow_html=True)


