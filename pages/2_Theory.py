import streamlit as st

st.set_page_config(
    page_title="WDM Simulator",
    layout="wide",
    initial_sidebar_state="expanded",
    )

st.markdown(
    """
    <style>
    /* ---------- HEADER ---------- */
    .header {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 110px;                 /* Reduced height */
        padding-top: 52px;
        background-color: #08f1e4;
        color: white;
        z-index: 1000;
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .header-title {
        font-size: 28px;
        font-weight: 900;        
        color: black;
    }

    /* ---------- MAIN APP OFFSET ---------- */
    .stApp {
        margin-top: 110px;            /* Push content below header */
        padding-bottom: 70px;         /* Avoid footer overlap */
    }

    /* ---------- FOOTER ---------- */
    .footer {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        height: 42px;
        background-color: #08f1e4;
        color: black;
        text-align: center;
        padding-top: 10px;
        font-size: 14px;
        z-index: 1000;
    }
    </style>

    <!-- HEADER -->
    <div class="header">
        <div class="header-title">
            Wavelength Division Multiplexing Simulation
        </div>
    </div>

    <!-- FOOTER -->
    <div class="footer">
        Developed by Dev Team 
    </div>
    """,
    unsafe_allow_html=True
)

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
    unsafe_allow_html=True
)

st.title("Theory", text_alignment="center")

st.divider()

# ---------------- WDM DEFINITION ---------------- #
st.markdown("""
## Define WDM

**Wavelength-Division Multiplexing (WDM)** is a fiber-optic transmission technology that enables the simultaneous transfer of multiple data streams over a single optical fiber by using different wavelengths (colors) of laser light.
By assigning each data signal to a specific wavelength, WDM effectively turns a single physical fiber into multiple virtual high-speed "lanes," drastically increasing the total bandwidth of the network without requiring additional cables.
""")

# ---------------- WDM WORKING ---------------- #
st.markdown("## WDM Working")

st.image("media/WDM_operating_principle.png", use_container_width=True)

st.markdown("""
### 1. Signal Generation (Transponders TP1–TP4)
- Input signals (Link 1–4) enter transponders  
- Convert electrical signals → optical signals  
- Each signal assigned a **unique wavelength (color)**  

### 2. Multiplexer (MUX)
- Combines all wavelengths into one signal  
- No interference due to different wavelengths  

### 3. Transmission (Optical Fiber)
- All signals travel together in **single fiber**  
- Reduces need for multiple cables  

### 4. Demultiplexer (DEMUX)
- Splits combined signal into original wavelengths  
- Works like a prism  

### 5. Signal Reception (TP5–TP8)
- Converts optical signals → electrical signals  
- Sends data to final destination  
""")

# ---------------- TYPES OF WDM ---------------- #
st.markdown("""
## Types of WDM

### 1. CWDM (Coarse WDM)
- **Channel Spacing:** Wide (~20 nm)  
- **Capacity:** Up to ~18 channels  
- **Distance:** Up to ~80 km  
- **Cost:** Low (no cooling required)  
- **Use Case:** Metro networks, campus networks  

### 2. DWDM (Dense WDM)
- **Channel Spacing:** Narrow (0.4–0.8 nm)  
- **Capacity:** 40–100+ channels  
- **Distance:** Long haul (1000+ km)  
- **Cost:** High (precision lasers required)  
- **Use Case:** Backbone networks, submarine cables  
""")

# ---------------- ADVANTAGES ---------------- #
st.markdown("""
## Advantages of WDM

- Massive bandwidth expansion  
- Cost-efficient (no new fiber needed)  
- Protocol transparency (Ethernet, SONET, etc.)  
- Highly scalable  
- High data security  
""")

# ---------------- DISADVANTAGES ---------------- #
st.markdown("""
## Disadvantages of WDM

- High initial equipment cost  
- Complex maintenance  
- Signal degradation over long distances  
- Non-linear effects at high power  
- Limited wavelength capacity  
""")

# ---------------- APPLICATIONS ---------------- #
st.markdown("""
## Applications of WDM

### 1. Long-Haul Networks
- Used in DWDM for national & global communication  
- Submarine cables connect continents  

### 2. Metropolitan Networks (MAN)
- City-wide connectivity  
- CWDM preferred (cost-effective)  

### 3. Data Center Interconnect (DCI)
- High-speed communication between data centers  

### 4. Enterprise Networks
- Connect multiple buildings (campus, factories)  

### 5. FTTH (Fiber to Home)
- Delivers internet & TV services  

### 6. Disaster Recovery
- Real-time backup using high-speed links  
""")