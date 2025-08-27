## Gen AI - Powered Job Recommonder system
# Gen-AI Job Recommender System

**An AI-powered tool that recommends jobs by analyzing resumes and pulling job listings from platforms like LinkedIn and Naukri.**

---

## Table of Contents

- [Demo / Screenshot](#demo--screenshot)  
- [Features](#features)  
- [Architecture & Components](#architecture--components)  
- [Getting Started](#getting-started)  
  - [Prerequisites](#prerequisites)  
  - [Installation](#installation)  
  - [Configuration](#configuration)  
  - [Running the App](#running-the-app)  
- [Usage](#usage)  
- [Project Structure](#project-structure)  
- [Contributing](#contributing)  
- [License](#license)  
- [Acknowledgements](#acknowledgements)

---

## Demo / Screenshot

*Insert screenshots or GIF of the UI in action.*

---

## Features

- Upload a PDF resume → extract text via **PyMuPDF (fitz)**  
- Summarize resume, identify skill gaps, and propose a learning roadmap via the **LLM API**  
- Fetch relevant job listings from **LinkedIn** and **Naukri** using **Apify actors**  
- Interactive UI powered by **Streamlit**

---

## Architecture & Components

| Component | Function |
|----------|----------|
| **`extract_text_from_pdf`** | Reads and extracts text from uploaded PDF resumes |
| **LLM wrapper (`ask_openai` or `ask_gemini`)** | Interacts with the language model API to generate summaries, gaps, roadmaps, etc. |
| **Job Fetchers** (`fetch_linkedin_jobs`, `fetch_naukri_jobs`) | Calls Apify actors to retrieve job listings based on extracted keywords |
| **Streamlit App** | Provides the frontend UI for user interaction |
| **.env** | Stores API keys like OpenAI or Gemini, Apify credentials, etc. |

---

## Getting Started

### Prerequisites

- Python 3.10+  
- Git  
- An **API Key** for:  
  - **OpenAI** or **Google Gemini** (depending on which LLM you're using)  
  - **Apify**

### Installation

1. Clone the repo:
   ```bash
   git clone https://github.com/thilanhasitha/Gen-AI-Job-Recommender-System.git
   cd Gen-AI-Job-Recommender-System
