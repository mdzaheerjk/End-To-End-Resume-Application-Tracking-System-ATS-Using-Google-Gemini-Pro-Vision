import streamlit as st
from google import genai


st.set_page_config(
    page_title="ATS Resume Expert",
    page_icon="📄",
    layout="wide"
)


st.sidebar.header("⚙️ Settings")
api_key = st.sidebar.text_input(
    "Enter your Gemini API Key",
    type="password"
)


def get_gemini_response(client, prompt, pdf_file, job_description):
    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=[
            prompt,
            job_description,
            pdf_file,
        ],
    )
    return response.text



st.title("📄 ATS Resume Expert")

job_description = st.text_area(
    "Job Description",
    height=220,
    placeholder="Paste the job description here..."
)

uploaded_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

if uploaded_file:
    st.success("✅ Resume uploaded successfully.")

col1, col2 = st.columns(2)

with col1:
    analyze_btn = st.button("Resume Review", use_container_width=True)

with col2:
    match_btn = st.button("ATS Match", use_container_width=True)


resume_prompt = """
You are an experienced Technical Human Resource Manager.

Review the uploaded resume against the provided job description.

Provide:

1. Overall evaluation
2. Candidate strengths
3. Candidate weaknesses
4. Skills alignment
5. Hiring recommendation
"""

ats_prompt = """
You are an advanced ATS (Applicant Tracking System).

Compare the uploaded resume with the job description.

Return:

1. ATS Match Percentage
2. Missing Keywords
3. Matching Skills
4. Improvement Suggestions
5. Final Verdict
"""


if analyze_btn or match_btn:

    if not api_key:
        st.error("Please enter your Gemini API Key.")
        st.stop()

    if uploaded_file is None:
        st.error("Please upload a resume.")
        st.stop()

    if not job_description.strip():
        st.error("Please enter the job description.")
        st.stop()

    try:
        client = genai.Client(api_key=api_key)

        with st.spinner("Uploading resume..."):
            pdf_file = client.files.upload(
                file=uploaded_file,
                config={
                    "mime_type": "application/pdf"
                }
            )

        prompt = resume_prompt if analyze_btn else ats_prompt

        with st.spinner("Analyzing resume..."):
            response = get_gemini_response(
                client,
                prompt,
                pdf_file,
                job_description,
            )

        st.subheader("Analysis")
        st.markdown(response)

    except Exception as e:
        st.error(f"Error: {e}")