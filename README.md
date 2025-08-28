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

<<<<<<< HEAD
=======
## screenshots
<img width="1913" height="1078" alt="image" src="https://github.com/user-attachments/assets/a32e728d-a714-4343-8c84-22e1144814f3" />
<img width="1918" height="1078" alt="image" src="https://github.com/user-attachments/assets/b5345dc8-52b0-41c6-8b6d-5e47919b248b" />
<img width="1918" height="1077" alt="image" src="https://github.com/user-attachments/assets/a447108f-2366-4c3a-a07d-247624a2b863" />
<img width="1918" height="1077" alt="image" src="https://github.com/user-attachments/assets/94117ba3-c6a4-4e9e-b17b-99bdb0da3d82" />





>>>>>>> 23f9c183b109aed71a496603bc8a389ce664bf18
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
