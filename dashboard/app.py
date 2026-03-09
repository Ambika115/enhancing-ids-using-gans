import streamlit as st
import pandas as pd

st.title("GAN-based Intrusion Detection System")
st.subheader("Network Traffic Monitoring Dashboard")

# Load dataset
data = pd.read_csv("dataset/KDDTrain+.csv", header=None)

# Show dataset shape
st.write("Dataset Shape:", data.shape)

# Show sample data
st.subheader("Sample Network Traffic Data")
st.dataframe(data.head())

# ---------------- Protocol Usage ----------------
st.subheader("Protocol Usage")

protocol_counts = data[1].value_counts()

# show table
st.write(protocol_counts)

# show chart
st.bar_chart(protocol_counts)

# ---------------- Clear Attack Names ----------------
attack_names = {
    "normal": "Normal Traffic",
    "neptune": "SYN Flood DoS",
    "smurf": "ICMP Flood Attack",
    "pod": "Ping of Death",
    "teardrop": "Fragmentation Attack",
    "back": "Web Server DoS",
    "land": "LAND Attack",
    "satan": "Network Scan Attack",
    "ipsweep": "IP Sweep Scan",
    "portsweep": "Port Scan Attack",
    "nmap": "Network Mapper Scan",
    "guess_passwd": "Password Guessing Attack",
    "ftp_write": "FTP Write Attack",
    "imap": "Email Server Attack",
    "multihop": "Multi-hop Intrusion",
    "phf": "CGI Script Exploit",
    "warezclient": "Illegal File Download",
    "warezmaster": "Illegal Software Upload",
    "buffer_overflow": "Buffer Overflow Attack",
    "rootkit": "Rootkit Attack",
    "loadmodule": "Load Module Attack",
    "perl": "Perl Exploit Attack"
}

# Replace attack labels
data[41] = data[41].map(attack_names).fillna(data[41])

# ---------------- Attack Distribution ----------------
st.subheader("Attack Distribution")

attack_counts = data[41].value_counts()

# show table
st.write(attack_counts)

# show chart
st.bar_chart(attack_counts)

st.markdown("Made with Streamlit")
