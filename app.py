import streamlit as st
from google import genai

st.sidebar.header("Settings")
api_key=st.sidebar.text_input("Enter Your Gemini API Key ...",type='password')


def get_gemini_response(client,prompt,pdf_content,input):
    response=client.models.generate_content(
        model='gemini-3.6-flash',
        contents=[prompt,pdf_content,input]
    )
    return response.text

st.set_page_config(page_title='ATS Resume Expert')
st.header("ATS Tracking System")
input_text=st.text_area("Job Description: ",key='input')
uploaded_file=st.file_uploader("Upload Your Resume(PDF)...",type=['pdf'])

if uploaded_file is not None:
    st.write("PDF Uploaded Successfully")

submit1=st.button("Tell Me About The Resume")

submit3=st.button("Percentage Match")

input_prompt1 = """
 You are an experienced Technical Human Resource Manager,your task is to review the provided resume against the job description. 
  Please share your professional evaluation on whether the candidate's profile aligns with the role. 
 Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
"""

input_prompt3 = """
You are an skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality, 
your task is to evaluate the resume against the provided job description. give me the percentage of match if the resume matches
the job description. First the output should come as percentage and then keywords missing and last final thoughts.
"""

if submit1:
    if uploaded_file is not None:
        client=genai.Client(api_key=api_key)
        pdf_content = client.files.upload(
        file=uploaded_file,
        config={
            "mime_type": "application/pdf"
            }
        )
        response=get_gemini_response(client,input_prompt1,pdf_content,input_text)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.write("Please Upload The Pdf")

if submit3:
    if uploaded_file is not None:
        client=genai.Client(api_key=api_key)
        pdf_content= client.files.upload(
        file=uploaded_file,
        config={
            "mime_type": "application/pdf"
            }
        )
        response=get_gemini_response(client,input_prompt3,pdf_content,input_text)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.write("Please Upload the pdf")