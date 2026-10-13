import streamlit as st
import json
import os
from datetime import datetime


# ---------------- CUSTOM CAMPUS NOTIFY DESIGN ----------------

st.markdown("""
<style>
/* =================================
   CAMPUS NOTIFY — SOFT PINK THEME
   ================================= */

/* Main application background */
.stApp {
    background: linear-gradient(135deg, #fff9fc 0%, #fff1f7 100%) !important;
    color: #352632;
    font-family: "Segoe UI", sans-serif;
}
/* Main content spacing */
.main .block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1350px;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #fbe0ec 0%, #fff0f6 100%);
    border-right: 1px solid #f0c5d8;
}

[data-testid="stSidebar"] > div:first-child {
    padding-top: 1.5rem;
}

[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3 {
    color: #92345f !important;
    font-weight: 750;
}

/* Main title */
h1 {
    color: #96365f !important;
    font-weight: 800 !important;
    letter-spacing: -0.8px;
}

/* Section headings */
h2, h3 {
    color: #a04470 !important;
    font-weight: 700 !important;
}

/* General text */
p, label, .stMarkdown {
    color: #493642;
}

/* Buttons */
.stButton > button,
.stFormSubmitButton > button {
    background: linear-gradient(135deg, #d95791, #c7437d);
    color: #ffffff !important;
    border: 1px solid #d95791;
    border-radius: 10px;
    padding: 0.55rem 1.2rem;
    font-weight: 650;
    transition: all 0.2s ease;
    box-shadow: 0 3px 8px rgba(190, 65, 119, 0.12);
}

.stButton > button:hover,
.stFormSubmitButton > button:hover {
    background: #ad3268;
    border-color: #ad3268;
    color: #ffffff !important;
    transform: translateY(-1px);
    box-shadow: 0 5px 12px rgba(190, 65, 119, 0.2);
}

/* Text inputs */
.stTextInput input {
    background-color: #ffffff !important;
    color: #29212a !important;
    border: 1px solid #e8c0d3 !important;
    border-radius: 9px !important;
}

.stTextInput input:focus {
    border-color: #d95791 !important;
    box-shadow: 0 0 0 2px rgba(217, 87, 145, 0.15) !important;
}

/* White notification message box */
.stTextArea textarea {
    background-color: #ffffff !important;
    color: #29212a !important;
    caret-color: #29212a !important;
    border: 1px solid #e8c0d3 !important;
    border-radius: 10px !important;
}

.stTextArea textarea::placeholder {
    color: #8b7b85 !important;
}

.stTextArea textarea:focus {
    background-color: #ffffff !important;
    color: #29212a !important;
    border-color: #d95791 !important;
    box-shadow: 0 0 0 2px rgba(217, 87, 145, 0.15) !important;
}

/* Dropdowns */
div[data-baseweb="select"] > div {
    background-color: #ffffff !important;
    border: 1px solid #e8c0d3 !important;
    border-radius: 9px !important;
}

div[data-baseweb="select"] * {
    color: #352632;
}

/* Dashboard metric cards */
[data-testid="stMetric"] {
    background: rgba(255, 255, 255, 0.96);
    border: 1px solid #f0d2e0;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0 4px 14px rgba(151, 53, 96, 0.07);
    transition: all 0.2s ease;
}

[data-testid="stMetric"]:hover {
    border-color: #e4a6c4;
    box-shadow: 0 7px 18px rgba(151, 53, 96, 0.11);
}

[data-testid="stMetricLabel"] {
    color: #806777 !important;
}

[data-testid="stMetricValue"] {
    color: #96365f !important;
    font-weight: 750;
}

/* Tabs */
.stTabs [data-baseweb="tab-list"] {
    gap: 8px;
    border-bottom: 1px solid #f0d2e0;
}

.stTabs [data-baseweb="tab"] {
    background: transparent;
    border-radius: 8px 8px 0 0;
    color: #80576b;
    padding: 10px 16px;
}

.stTabs [aria-selected="true"] {
    color: #ad3268 !important;
    border-bottom-color: #d95791 !important;
}

/* Expanders and bordered containers */
[data-testid="stExpander"] {
    background: #ffffff;
    border: 1px solid #f0d2e0;
    border-radius: 12px;
}

[data-testid="stVerticalBlockBorderWrapper"] {
    border-color: #f0d2e0;
    border-radius: 14px;
}

/* Notification and status messages */
[data-testid="stAlert"] {
    border-radius: 10px;
    border: 1px solid #f0d2e0;
}

/* Horizontal dividers */
hr {
    border-color: #f0d2e0 !important;
}

/* Checkboxes and radio buttons */
[data-testid="stCheckbox"] label,
[data-testid="stRadio"] label {
    color: #493642;
}

/* File upload area */
[data-testid="stFileUploader"] {
    background: #fffafd;
    border: 1px dashed #e5aac5;
    border-radius: 12px;
}

/* Keep tables clean and readable */
[data-testid="stDataFrame"],
[data-testid="stTable"] {
    border: 1px solid #f0d2e0;
    border-radius: 10px;
    overflow: hidden;
}

/* Links */
a {
    color: #b43c75 !important;
}

/* Smooth visual transitions */
[data-testid="stSidebar"],
[data-testid="stMetric"],
.stButton > button {
    transition: all 0.2s ease;
}
</style>

""", unsafe_allow_html=True)

DATA_FILE = "notifications.json"
SMS_LOG_FILE = "sms_log.json"
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "campus123"  # simple hardcoded login for demo purposes

st.set_page_config(page_title="Campus Notify", page_icon="📢", layout="wide")


# ---------- Data helpers ----------
def load_json(path):
    if os.path.exists(path):
        with open(path, "r") as f:
            return json.load(f)
    return []


def save_json(path, data):
    with open(path, "w") as f:
        json.dump(data, f, indent=2)


def add_notification(title, message, ntype):
    notifications = load_json(DATA_FILE)
    entry = {
        "id": len(notifications) + 1,
        "title": title,
        "message": message,
        "type": ntype,  # "Routine" or "Emergency"
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }
    notifications.insert(0, entry)  # newest first
    save_json(DATA_FILE, notifications)

    if ntype == "Emergency":
        send_simulated_sms(entry)

    return entry


def send_simulated_sms(entry):
    """
    Simulates sending an SMS blast for emergency notifications.
    In a full production version this would call a real SMS gateway
    (e.g. Africa's Talking, Twilio). For this project it logs the
    'sent' message so the behaviour can be demonstrated and verified.
    """
    sms_log = load_json(SMS_LOG_FILE)
    sms_log.insert(0, {
        "notification_id": entry["id"],
        "message_sent": f"[EMERGENCY] {entry['title']}: {entry['message']}",
        "sent_at": entry["timestamp"],
        "recipients": "All registered student & staff numbers (simulated)",
    })
    save_json(SMS_LOG_FILE, sms_log)


# ---------- UI ----------
st.title("📢 Campus Notify")
st.caption("A unified platform for routine campus announcements and emergency alerts")

page = st.sidebar.radio("Navigate", ["Student View", "Admin Login"])

# ---------------- STUDENT VIEW ----------------
if page == "Student View":
    st.subheader("Campus Notifications")

    notifications = load_json(DATA_FILE)

    if not notifications:
        st.info("No notifications yet. Check back soon.")
    else:
        for n in notifications:
            if n["type"] == "Emergency":
                st.error(f"🚨 EMERGENCY: {n['title']}\n\n"
                         f"{n['message']}\n\n"
                         f"Posted: {n['timestamp']}"
                         )
            else:
                st.info(f"📌 {n['title']}\n\n"
                        f"{n['message']}\n\n"
                        f"Posted: {n['timestamp']}")

# ---------------- ADMIN VIEW ----------------
elif page == "Admin Login":
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if not st.session_state.logged_in:
        st.subheader("Admin Login")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
                st.session_state.logged_in = True
                st.rerun()
            else:
                st.error("Invalid credentials.")
        st.caption("Demo credentials — admin / campus123")

    else:
        st.subheader("Admin Dashboard")
        st.success("Logged in as central admin")

        with st.form("post_notification", clear_on_submit=True):
            title = st.text_input("Title")
            message = st.text_area("Message")
            ntype = st.selectbox("Type", ["Routine", "Emergency"])
            submitted = st.form_submit_button("Post Notification")

            if submitted:
                if title and message:
                    add_notification(title, message, ntype)
                    if ntype == "Emergency":
                        st.success("Emergency notification posted and SMS blast simulated.")
                    else:
                        st.success("Notification posted.")
                else:
                    st.warning("Please fill in both title and message.")

        st.divider()
        st.subheader("Posted Notifications")
        notifications = load_json(DATA_FILE)
        st.write(f"Total: {len(notifications)}")
        for n in notifications:
            st.write(f"**[{n['type']}] {n['title']}** — {n['timestamp']}")
            st.caption(n["message"])

        st.divider()
        st.subheader("Simulated SMS Log (Emergency Alerts)")
        sms_log = load_json(SMS_LOG_FILE)
        if sms_log:
            for s in sms_log:
                st.text(f"[{s['sent_at']}] {s['message_sent']}  -> {s['recipients']}")
        else:
            st.caption("No emergency SMS sent yet.")

        if st.button("Log out"):
            st.session_state.logged_in = False
            st.rerun()