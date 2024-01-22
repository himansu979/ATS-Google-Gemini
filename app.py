'''
https://github.com/krishnaik06/Google-Gemini-Crash-Course/tree/main/atsllm
'''

import streamlit as st
import google.generativeai as genai 
import os
import sys
import PyPDF2 as pdf 

from dotenv import load_dotenv

load_dotenv() ## load all environmental variables
#print("Google api key : ", os.environ.get("GOOGLE_API_KEY"))

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

st.set_page_config(page_title="ATS Resume Expert")

## Gemini Pro Response

def get_gemini_response(input):
    model = genai.GenerativeModel("gemini-pro")
    #model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(input)
    return response.text

# read the pdf to extract text
def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in range(len(reader.pages)):
        page=reader.pages[page]
        text += str(page.extract_text())
    return text



input_prompt1 = """
 You are an experienced Technical Human Resource Manager,your task is to review the provided resume against the job description. 
  Please share your professional evaluation on whether the candidate's profile aligns with the role. 
 Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
 resume:{text}
description:{jd}
"""

input_prompt22 = """
You are an skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality, 
your task is to evaluate the resume against the provided job description. give me the percentage of match if the resume matches
the job description. First the output should come as percentage and then keywords missing and last final thoughts.
Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
resume:{text}
description:{jd}
"""

input_prompt23 = """
You are an skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and machine learning, 
your task is to evaluate the resume against the provided job description. give me the percentage of match if the resume matches
the job description. First the output should come as percentage and then keywords missing and last final thoughts.
Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements and provide recommendations to improve it.
resume:{text}
description:{jd}
"""

input_prompt2 = """
provide a summary of the candidate profile. Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
resume:{text}
description:{jd}
"""

input_prompt3="""
Hey Act Like a skilled or very experience ATS(Application Tracking System)
with a deep understanding of tech field,software engineering,data science ,data analyst
and big data engineer. Your task is to evaluate the resume based on the given job description.
You must consider the job market is very competitive and you should provide 
best assistance for improving thr resumes. Assign the percentage Matching based 
on Jd and the missing keywords with high accuracy
resume:{text}
description:{jd}

I want the response in one single string having the structure
{{"JD Match":"%", "MissingKeywords:[]", "Profile Summary":""}}
"""

## streamlit app
st.title("Smart ATS")
st.text("Improve Your Resume ATS")
jd=st.text_area("Paste the Job Description")

uploaded_file = st.file_uploader("Upload Your Resume", type="pdf", help="Please upload the pdf")
if uploaded_file is not None:
    st.write("PDF Uploaded Successfully")

#submit = st.button("Submit")

submit1 = st.button("Tell Me About the Resume based on HR")
submit2 = st.button("Percentage match based on data science")
submit3 = st.button("Percentage match based on tech field")

if submit1:
    if uploaded_file is not None:
        resume=input_pdf_text(uploaded_file)
        response = get_gemini_response(input_prompt1)
        st.header("Response")
        st.write(response)

elif submit2:
    if uploaded_file is not None:
        resume=input_pdf_text(uploaded_file)
        response = get_gemini_response(input_prompt2)
        st.header("Response")
        st.write(response)

elif submit3:
    if uploaded_file is not None:
        resume=input_pdf_text(uploaded_file)
        st.header("Job description")
        #st.text(jd)
        st.header("Resume")
        #st.subheader(resume)
        #st.text(resume)
        response = get_gemini_response(input_prompt3)
        st.header("Response")
        st.subheader(response)






















































