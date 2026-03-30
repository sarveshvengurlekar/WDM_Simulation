import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

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
    background: linear-gradient(135deg, #0f2027, #2c5364) !important;
    color: white !important;
    font-weight: bold;
    border: none;
    padding: 10px;
    transition: all 0.3s ease;
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

# ---------------- TITLE ---------------- #
st.title("📡 Wavelength Division Multiplexing Simulator")
st.divider()

# ---------------- INPUT ---------------- #
st.header("Input Parameters")

preset = st.segmented_control(
    "Distance Mode",
    ["Normal", "Long Distance", "High Capacity", "Custom"],
    width="stretch"
)

def load_preset(preset):
    if preset == "Normal":
        return 8, 100, 10, 50, 0.2, 0, 17, 1550
    elif preset == "Long Distance":
        return 8, 100, 10, 150, 0.25, 0, 18, 1550
    elif preset == "High Capacity":
        return 16, 50, 40, 80, 0.25, 5, 16, 1550
    else:
        return 8, 100, 10, 50, 0.2, 0, 17, 1550

n, spacing, bitrate, length, att, power, disp, center = load_preset(preset)

col1, col2 = st.columns(2)

with col2:
    n = st.number_input("Number of Channels", value=n)
    spacing = st.number_input("Channel Spacing (GHz)", value=spacing)
    bitrate = st.number_input("Bit Rate per Channel (Gbps)", value=bitrate)
    length = st.number_input("Fiber Length (km)", value=length)

with col1:
    att = st.number_input("Attenuation (dB/km)", value=att)
    power = st.number_input("Input Power (dBm)", value=power)
    disp = st.number_input("Dispersion (ps/nm/km)", value=disp)
    center = st.number_input("Center Wavelength (nm)", value=center)

run = st.button("Run Simulation", width="stretch")

# ---------------- OUTPUT ---------------- #
if run:
    try:
        capacity = n * bitrate
        loss = att * length
        recv = power - loss

        wl_spacing = 0.8 if spacing == 100 else 0.4
        wavelengths = [center + (i - n//2) * wl_spacing for i in range(int(n))]

        st.divider()
        st.header("Results")

        col1, col2, col3 = st.columns(3)
        col1.metric("Total Capacity (Gbps)", capacity)
        col2.metric("Fiber Loss (dB)", round(loss, 2))
        col3.metric("Received Power (dBm)", round(recv, 2))

        # -------- GRAPHS -------- #
        fig, axs = plt.subplots(2, 2, figsize=(10, 6))

        axs[0, 0].stem(wavelengths, [1]*int(n))
        axs[0, 0].set_title("Input Spectrum")

        x = np.linspace(0, length, 200)
        for i in range(min(int(n), 5)):
            y = np.exp(-((x-(i*10))**2)/50)*np.exp(-0.02*x)
            axs[0, 1].plot(x, y)
        axs[0, 1].set_title("Signal in Fiber")

        dist = np.linspace(0, length, 50)
        p = power - att*dist
        axs[1, 0].plot(dist, p)
        axs[1, 0].set_title("Power vs Distance")

        axs[1, 1].stem(wavelengths, [np.exp(-0.02*length)]*int(n))
        axs[1, 1].set_title("Output Spectrum")

        plt.tight_layout()
        st.pyplot(fig)

    except:
        st.error("Invalid Input")

