import streamlit as st
import numpy as np
import matplotlib.pyplot as plt


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
    unsafe_allow_html=True)

st.title("📡 Wavelength Division Multiplexing Simulator", text_alignment="center")

st.divider()

# ---------------- SIDEBAR INPUT ---------------- #
st.header("Input Parameters")


# Presets
preset = st.segmented_control(
    "Distance Mode",
    ["Normal", "Long Distance", "High Capacity", "Custom",], width="stretch")

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

run = st.button("Run Simulation", use_container_width=True, type="primary")


# ---------------- MAIN OUTPUT ---------------- #
if run:
    try:
        # Calculations
        capacity = n * bitrate
        loss = att * length
        recv = power - loss

        wl_spacing = 0.8 if spacing == 100 else 0.4
        wavelengths = [center + (i - n//2) * wl_spacing for i in range(int(n))]

        # ---------------- RESULTS ---------------- #
        st.divider()
        st.header("📊 Results")

        col1, col2, col3 = st.columns(3)
        col1.metric("Total Capacity (Gbps)", capacity)
        col2.metric("Fiber Loss (dB)", round(loss, 2))
        col3.metric("Received Power (dBm)", round(recv, 2))

        # ---------------- GRAPHS ---------------- #
        fig, axs = plt.subplots(2, 2, figsize=(10, 6))

        # Spectrum
        axs[0, 0].stem(wavelengths, [1]*int(n))
        axs[0, 0].set_title("Input Spectrum")

        # Signal propagation
        x = np.linspace(0, length, 200)
        for i in range(min(int(n), 5)):
            y = np.exp(-((x-(i*10))**2)/50)*np.exp(-0.02*x)
            axs[0, 1].plot(x, y)
        axs[0, 1].set_title("Signal in Fiber")

        # Power decay
        dist = np.linspace(0, length, 50)
        p = power - att*dist
        axs[1, 0].plot(dist, p)
        axs[1, 0].set_title("Power vs Distance")

        # Output spectrum
        axs[1, 1].stem(wavelengths, [np.exp(-0.02*length)]*int(n))
        axs[1, 1].set_title("Output Spectrum")

        plt.tight_layout()
        st.pyplot(fig)

    except Exception as e:
        st.error("Invalid Input")