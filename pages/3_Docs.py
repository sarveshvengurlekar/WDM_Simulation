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


st.title("Docs", text_alignment="center")

st.divider()

st.markdown("""
## 1. NORMAL MODE

### Input (Auto-filled)
- Channels (n) = **8**
- Spacing = **100 GHz**
- Bitrate = **10 Gbps**
- Length = **50 km**
- Attenuation = **0.2 dB/km**
- Power = **0 dBm**
- Dispersion = **17 ps/nm/km**
- Center wavelength = **1550 nm**

### Output
- **Total Capacity** = 8 × 10 = **80 Gbps**
- **Fiber Loss** = 0.2 × 50 = **10 dB**
- **Received Power** = 0 − 10 = **−10 dBm**

### Graph Behavior
- Input Spectrum → 8 wavelength spikes (0.8 nm spacing)
- Signal in Fiber → Slight attenuation
- Power vs Distance → Linear decrease (0 to −10 dBm)
- Output Spectrum → Slightly reduced amplitude

---

## 2. LONG DISTANCE MODE

### Input
- Channels = **8**
- Spacing = **100 GHz**
- Bitrate = **10 Gbps**
- Length = **150 km**
- Attenuation = **0.25 dB/km**
- Power = **0 dBm**

### Output
- **Capacity** = **80 Gbps**
- **Loss** = 0.25 × 150 = **37.5 dB**
- **Received Power** = **−37.5 dBm**

### Graph Behavior
- Input Spectrum → Same as Normal
- Signal in Fiber → More spreading + high attenuation
- Power vs Distance → Steep drop
- Output Spectrum → Very weak signals

---

## 3. HIGH CAPACITY MODE

### Input
- Channels = **16**
- Spacing = **50 GHz**
- Bitrate = **40 Gbps**
- Length = **80 km**
- Attenuation = **0.25 dB/km**
- Power = **5 dBm**

### Output
- **Capacity** = 16 × 40 = **640 Gbps**
- **Loss** = 0.25 × 80 = **20 dB**
- **Received Power** = **−15 dBm**

### Graph Behavior
- Input Spectrum → 16 dense channels (0.4 nm spacing)
- Signal in Fiber → Overlapping signals
- Power vs Distance → Moderate drop
- Output Spectrum → Dense but attenuated

---

## 4. CUSTOM MODE

### Input
- User-defined values

### Output
- Capacity = n × bitrate  
- Loss = att × length  
- Received Power = power − loss  

### Graph Behavior
- Fully dynamic based on input

""")

