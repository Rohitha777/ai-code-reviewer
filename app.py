import streamlit as st

# Inject Custom CSS for Sleek UI
st.markdown("""
    <style>
        /* Hide Streamlit footer and menu */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}

        /* App background and font */
        body {
            background-color: #f8f9fa;
            font-family: 'Segoe UI', sans-serif;
        }

        /* Container adjustments */
        .stApp {
            background-color: #ffffff;
            padding: 2rem;
        }

        /* Heading styles */
        h1, h2, h3 {
            color: #1f77b4;
        }

        /* Custom button */
        .stButton > button {
            background-color: #1f77b4;
            color: white;
            border-radius: 8px;
            padding: 0.5rem 1rem;
        }

        /* File uploader */
        .stFileUploader {
            border: 1px solid #ddd;
            border-radius: 5px;
        }
    </style>
""", unsafe_allow_html=True)

st.set_page_config(page_title="AI Code Reviewer", layout="wide")
st.title("🤖 AI Code Reviewer")

code_input = st.text_area("Paste your Python code:", height=300)
uploaded_file = st.file_uploader("Or upload a Python (.py) file")

if uploaded_file:
    code_input = uploaded_file.read().decode("utf-8")
if st.button("Analyze Code"):
    if not code_input.strip():
        st.warning("Please input code or upload a file.")
    else:
        st.success("Ready to analyze!")

from utils.analysis import run_flake8, run_black, run_radon

flake8_out = run_flake8(code_input)
formatted_code = run_black(code_input)
radon_data = run_radon(code_input)

st.subheader("🔍 Flake8 Style Issues")
st.code(flake8_out or "No issues found.")

st.subheader("📦 Code Complexity (Radon)")
for item in radon_data:
    col = "🟢" if item["complexity"] < 5 else "🟡" if item["complexity"] < 10 else "🔴"
    st.write(f"{col} `{item['name']}` - Line {item['lineno']} - Complexity: {item['complexity']}")

flake8_count = flake8_out.count("\n") if flake8_out else 0
complex_functions = sum(1 for r in radon_data if r["complexity"] > 10)
score = max(0, 100 - (flake8_count * 2 + complex_functions * 5))

st.subheader("📊 Code Quality Score")
st.progress(score / 100)
st.metric("Score", f"{score}%", delta=None)

col1, col2 = st.columns(2)
with col1:
    st.markdown("### 📝 Original Code")
    st.code(code_input, language="python")

with col2:
    st.markdown("### ✅ Formatted Code (Black)")
    st.code(formatted_code, language="python")

from utils.report import generate_report

report_text = generate_report("Taylor", code_input, formatted_code, flake8_out, radon_data, score)

st.download_button("📥 Download Code Report", report_text, file_name="code_review.txt")

st.image("your_logo.jpg", width=100)

st.markdown("#### 🔧 Suggestions")
if flake8_out:
    st.write("⚠️ Please fix the style warnings.")
if complex_functions:
    st.write("📌 Consider breaking down complex functions.")

from utils.send_email import send_email

st.markdown("---")
st.subheader("📧 Email Report")
email = st.text_input("Enter your email to receive the report")

if st.button("Send Report to Email"):
    if email and report_text:
        result = send_email(email, report_text)
        if result is True:
            st.success("✅ Report sent to your email!")
        else:
            st.error(f"❌ Failed to send email: {result}")
    else:
        st.warning("Please enter a valid email.")
