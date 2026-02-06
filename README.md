---

# 🧬 AI Clinical Trial Eligibility System

An end-to-end web application that evaluates **patient eligibility for clinical trials** using structured inclusion and exclusion rules, with **clear, explainable results**.

---

## 🚀 Live Deployment

* **Frontend (React – Vercel)**
  👉 [https://clinical-trial-ai.vercel.app/](https://clinical-trial-ai.vercel.app/)

* **Backend (FastAPI – Render)**
  👉 [https://clinical-trial-ai-backend.onrender.com](https://clinical-trial-ai-backend.onrender.com)
  👉 **API Docs (Swagger):** [https://clinical-trial-ai-backend.onrender.com/docs](https://clinical-trial-ai-backend.onrender.com/docs)

---

## 📌 Features

### Backend (FastAPI)

* Patient data creation
* Trial protocol upload (PDF)
* Eligibility & exclusion rule evaluation
* Explainable eligibility output
* PostgreSQL database (Render)
* CORS configured for frontend access

### Frontend (React)

* Patient creation form
* Trial upload interface
* Eligibility analysis trigger
* Eligibility summary view
* Highlighted inclusion/exclusion checks
* Human-readable explanation

---

## 🧠 System Flow

1. **Create Patient**

   * Enter age and eGFR
   * Patient is saved to database
   * Patient ID is generated

2. **Upload Trial Protocol**

   * Upload trial PDF
   * Trial ID is stored

3. **Eligibility Analysis**

   * Combines patient + trial data
   * Applies inclusion/exclusion logic
   * Returns eligibility result with explanation

---

## 🔍 Example Eligibility Output

```
Status: ELIGIBLE

Inclusion: Age 18–70 — PASS
Exclusion: eGFR < 30 — PASS

Explanation:
Patient meets all eligibility criteria.
```

---

## 📂 Project Structure

```
clinical-trial-ai/
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   ├── patient.py
│   │   │   ├── trial.py
│   │   │   ├── eligibility.py
│   │   │   └── auth.py
│   │   ├── db/
│   │   ├── models/
│   │   └── main.py
│
├── frontend/
│   └── src/
│       ├── api/
│       │   ├── client.js
│       │   ├── patient.js
│       │   ├── trial.js
│       │   └── eligibility.js
│       ├── components/
│       │   ├── PatientForm.js
│       │   ├── TrialForm.js
│       │   └── EligibilityResult.js
│       └── App.js
│
└── README.md
```

---

## 🛠 Tech Stack

* **Backend:** FastAPI, SQLAlchemy, PostgreSQL
* **Frontend:** React, Axios
* **Deployment:** Render (backend), Vercel (frontend)
* **Languages:** Python, JavaScript

---

## ✅ Assignment Deliverables Covered

✔ Patient upload
✔ Trial protocol upload
✔ Eligibility and exclusion analysis
✔ Explainable contradiction output
✔ Deployed backend URL
✔ Deployed frontend URL
✔ Eligibility summary UI

---
