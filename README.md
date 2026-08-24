# 🧭 CivicCompass (Pro Bono Legal Assistant)

CivicCompass is an automated, AI-powered amicus and compliance drafting assistant designed to optimize legal services for pro bono clinics, public defenders, and nonprofit legal organizations.

---

## 🛠️ Repository Architecture

The project files have been systematically organized into logical subdirectories according to software engineering best practices:

```
civiccompass-probono/
├── app.py                     # Main Streamlit Dashboard Application
├── requirements.txt           # Python Project Dependency List
├── config/                    # YAML / JSON / Config validation modules
├── core/                      # Intake scrapers, OCR engines, PDF parsers
├── data/                      # Structured databases, JSON/CSV tax matrices
├── logs/                      # System events, connection debug logs
├── models/                    # AI prompt pipelines & agent definitions
├── scripts/                   # Shell automation and setup scripts
└── tests/                     # Unit test suites & integration tests
```

---

## 🚀 Key Features

*   **Intake Scraping:** Automatically queries Supreme Court case listings to identify high-priority pro bono opportunities.
*   **Compliance Audit:** Compiles automated compliance check nodes (HIPAA, FERPA, CFR, FEMA) to audit municipal or regulatory documents.
*   **Sequential Red Team Gauntlet:** Iteratively critiques and refines legal drafts using a multi-agent adversarial personification model (Trial Judge, skepticism clerk, opposing counsel).

---

## 📦 Installation & Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/ShawnSNGit/civiccompass-probono.git
   cd civiccompass-probono
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit Dashboard:**
   ```bash
   streamlit run app.py
   ```

---

## ⚖️ Licensing & Disclaimer

*This tool is designed to assist human attorneys in processing research. It is not a substitute for professional legal judgment or advice.*
