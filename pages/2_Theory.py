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

st.image("media/WDM_operating_principle.png", width="stretch")

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