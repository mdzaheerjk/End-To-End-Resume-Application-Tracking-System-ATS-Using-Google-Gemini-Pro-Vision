# ATS Resume Expert — End-to-End Resume & ATS Matching (Google Gemini)

A lightweight Streamlit app that leverages Google Gemini (via the google-genai SDK) to perform two resume-focused workflows:

- Resume Review: a recruiter-style evaluation of an uploaded PDF resume against a job description.
- ATS Match: an automated Applicant Tracking System (ATS) style comparison that returns a match percentage, missing keywords, and improvement suggestions.

This repository demonstrates how to upload a resume PDF to the Gemini files API and generate content that analyzes and scores the resume for hiring decisions.

---

## Table of Contents

- Project Overview
- Features
- How it works
- Requirements
- Installation
- Usage
- Configuration
- Tips for getting great results
- Security & Privacy
- Troubleshooting
- Contributing
- License
- Acknowledgements

---

## Project Overview

ATS Resume Expert is a Streamlit-based proof-of-concept that connects a simple web UI to Google Gemini (via the google-genai package). Users paste a job description, upload a resume (PDF), and choose between two analyses: a recruiter-style resume review or an ATS-style match and scoring.

The app is intentionally minimal so it can be extended or integrated into larger ATS pipelines, HR tooling, or interview-prep products.

---

## Features

- Upload PDF resume and provide a job description
- Two analysis modes:
  - "Resume Review": recruiter-style evaluation and recommendations
  - "ATS Match": automated match percentage, missing keywords, skill overlap, and improvement suggestions
- Simple Streamlit UI for quick experiments and demos
- Uses Google Gemini models via google-genai for content generation and file handling

---

## How it works

1. The user enters a job description and uploads a resume (PDF).
2. The app uploads the PDF to Google Gemini's files API (via google-genai).
3. It sends a composite prompt (system prompt + job description + uploaded file reference) to Gemini to generate an analysis.
4. The model returns structured text which the app renders in the Streamlit UI.

Note: The effectiveness of the analysis depends on the prompt design, the chosen Gemini model, and the quality of the resume/job description.

---

## Requirements

- Python 3.10+ (recommended)
- A Google Gemini API key with access to the model specified in the app
- Internet connection to reach the Gemini API

Provided requirements.txt contains the minimal dependencies:

- google-genai
- streamlit

---

## Installation

1. Clone this repository:

   git clone https://github.com/mdzaheerjk/End-To-End-Resume-Application-Tracking-System-ATS-Using-Google-Gemini-Pro-Vision.git
   cd End-To-End-Resume-Application-Tracking-System-ATS-Using-Google-Gemini-Pro-Vision

2. Create and activate a virtual environment (recommended):

   python -m venv .venv
   source .venv/bin/activate   # macOS / Linux
   .venv\Scripts\activate    # Windows (PowerShell)

3. Install dependencies:

   pip install -r requirements.txt

---

## Usage

Start the Streamlit app locally:

   streamlit run app.py

Then open the Streamlit UI in your browser (Streamlit will print the local URL). In the sidebar you will be prompted to enter your Gemini API Key and then:

1. Paste the job description into the "Job Description" field.
2. Upload a resume (PDF) using the uploader.
3. Click one of the two buttons: "Resume Review" or "ATS Match".

The app will upload the PDF to Gemini, call the selected prompt, and render the returned analysis under the "Analysis" section.

---

## Configuration

- Gemini API Key: Enter your API key in the Streamlit sidebar when the app runs. Do NOT commit API keys to the repository.

- Model: The app currently uses `gemini-3.6-flash` in app.py. You can change the model name in the call to client.models.generate_content if you have access to another model.

Prompt templates are defined in the code and can be customized directly in `app.py`:

- `resume_prompt` — recruiter-style review
- `ats_prompt` — ATS matching and scoring

---

## Tips for getting great results

- Provide a clear, specific job description — longer and more detailed descriptions typically give better alignment results.
- Use polished, text-based resumes (PDFs that contain selectable text). Scanned images or poorly OCRed PDFs may reduce accuracy.
- Experiment with prompt wording and model choice for higher-quality or more structured outputs.

---

## Security & Privacy

- The app uploads resumes to the Gemini files API to enable the model to analyze the PDF. Treat uploaded resumes as sensitive data.
- Never commit your API key or any private resumes to version control.
- If you plan to use this in production, add strong access controls, logging, and data retention policies. Consider redacting or anonymizing PII before sending data to third-party APIs.

---

## Troubleshooting

- Error: "Please enter your Gemini API Key." — enter a valid Gemini API key in the sidebar.
- Error uploading file — check network connectivity and ensure the uploaded file is a valid PDF.
- Unexpected model output — try using a different Gemini model or revise the prompt.

If you hit an exception printed by the app, the Streamlit UI will display the exception message.

---

## Contributing

Contributions, improvements, and feature requests are welcome. Suggested improvements:

- Add environment variable support for the Gemini API key (instead of manual sidebar input).
- Parse the model-generated text into JSON for structured rendering (percentages, lists, tables).
- Add unit tests and CI checks.
- Add optional anonymization/PII redaction for uploaded files.

If you'd like help implementing any of the above, open an issue or a PR with a clear description.

---

## License

This repository includes an existing LICENSE file. Please review it for license details.

---

## Acknowledgements

- Powered by Google Gemini (via the google-genai SDK)
- Built with Streamlit for rapid UI prototyping

---

If you'd like, I can also:
- Add screenshots and example outputs to the README (if you provide them),
- Add a demo GIF showing the app in action, or
- Extend the app to support environment-based API keys and structured JSON output.
