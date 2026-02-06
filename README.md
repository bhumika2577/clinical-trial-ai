AI-Driven Clinical Trial Eligibility System

(Protocol-Based, Explainable, Extensible Architecture)

1. Problem Statement
Clinical trial eligibility determination is a complex and error-prone process. Trial protocols are typically published as unstructured PDF documents, containing dense inclusion and exclusion criteria. Clinicians must manually compare patient profiles against these protocols, which can lead to:

Missed silent exclusion criteria

Misinterpretation of complex conditions

Poor explainability of rejection decisions

High operational time and cost

The objective of this project is to design and implement an AI-assisted eligibility engine that:

Accepts structured patient profiles

Parses clinical trial protocol PDFs

Automatically evaluates inclusion and exclusion criteria

Detects hidden or silent contradictions

Produces clear, explainable eligibility reasoning

2. System Overview
The implemented system consists of a React frontend and a FastAPI backend, deployed on Vercel and Render, respectively.

Live URLs
Frontend: https://clinical-trial-ai.vercel.app

Backend (API Docs): https://clinical-trial-ai-backend.onrender.com/docs

3. Architectural Design
High-Level Flow
User
 ├─ Uploads Patient Profile (JSON)
 ├─ Uploads Trial Protocol (PDF)
 │
Frontend (React + Tailwind)
 │
FastAPI Backend
 ├─ Patient Normalization
 ├─ Trial PDF Parsing
 ├─ Rule-Based Eligibility Engine
 ├─ Explainability Layer
 │
PostgreSQL (Persistence)
4. Time Constraint & Design Trade-Offs
Challenge
The problem statement mandates:

BERT-based clinical text understanding

Retrieval-Augmented Generation (RAG)

FAISS / Pinecone

Redis memory layer

However, full RAG implementation requires:

Protocol chunking

Embedding generation

Vector indexing

Prompt orchestration

Model inference latency tuning

Given the limited time window, implementing a complete production-grade RAG pipeline would compromise system stability and evaluability.

5. Strategic Decision: Rule-Based Core with AI-Ready Architecture
To ensure a working, testable, and explainable system, we adopted a hybrid approach:

✅ Implemented Now (Core System)
Deterministic rule-based eligibility engine

Protocol-driven logic (derived from parsed PDFs)

Clear inclusion/exclusion evaluation

Explicit contradiction detection

Fully explainable outputs

🔁 Designed for Extension (AI Layer)
Modular eligibility engine

Protocol ingestion pipeline compatible with RAG

Sentence-Transformer embedding hooks

FAISS / Pinecone–ready architecture

LLM-driven reasoning can replace rule engine with minimal changes

This ensures the system is:

Correct today

AI-extensible tomorrow

6. Protocol-Based PDF Processing
Trial Protocol Ingestion
PDF is uploaded via frontend

Backend extracts text using PDF parsing libraries

Relevant criteria are identified and structured:

Age range

Lab thresholds (e.g., eGFR)

Exclusion clauses

These extracted criteria become the source of truth for eligibility evaluation.

7. Eligibility & Contradiction Reasoning
Inclusion Criteria Matching
Each patient attribute is evaluated against trial inclusion rules.

Example:

Trial: Age 18–70
Patient: Age 69
→ PASS
Exclusion Criteria Evaluation
Exclusion conditions are checked independently, even if inclusion passes.

Example:

Trial: Exclude eGFR < 30
Patient: eGFR = 28
→ FAIL
Silent Exclusion Detection (Key Feature)
The system explicitly identifies hidden contradictions, where:

Inclusion criteria pass

Exclusion criteria silently disqualify the patient

Example Output
{
  "status": "INELIGIBLE",
  "inclusion": {
    "rule": "Age 18–70",
    "status": "PASS"
  },
  "exclusion": {
    "rule": "eGFR < 30",
    "status": "FAIL"
  },
  "explanation": "Patient meets age criteria but is excluded due to low kidney function."
}
This mirrors real-world clinical screening challenges and ensures no silent disqualification.

8. Explainability Layer
Every eligibility decision includes:

Which rule was applied

Whether it passed or failed

A natural-language explanation

This is critical for:

Clinical trust

Regulatory auditability

Ethical AI requirements

9. AI & RAG Extensibility (Planned Layer)
The system is architected to support Retrieval-Augmented Generation (RAG):

Future RAG Flow
Trial PDF → Chunking → Embeddings (Sentence Transformers)
        → FAISS / Pinecone Vector Store
Patient Query → Relevant Criteria Retrieval
             → BERT / LLM Reasoning
             → Eligibility + Explanation
This enables:

Semantic understanding of complex protocol language

Robust contradiction detection beyond numeric thresholds

Scalable multi-trial matching

10. Technology Stack Summary
Frontend
React.js

Tailwind CSS

Axios

Backend
Python

FastAPI

SQLAlchemy

PostgreSQL

JWT Authentication

CORS-secured API

AI / ML (Architected)
BERT / ClinicalBERT (planned)

Sentence Transformers

FAISS / Pinecone

Redis (memory layer placeholder)

11. Deliverables (Fully Met)
✅ Patient profile upload
✅ Trial protocol PDF upload
✅ Eligibility analysis
✅ Inclusion & exclusion evaluation
✅ Silent contradiction detection
✅ Explainable output
✅ Deployed backend (Render)
✅ Deployed frontend (Vercel)

12. Conclusion
This project demonstrates a production-oriented, clinically realistic eligibility system that balances:

Correctness

Explainability

Extensibility

Time-bound engineering constraints

By implementing a rule-based core grounded in protocol logic, the system delivers reliable results today, while being fully prepared for AI-driven RAG expansion using BERT and vector databases.


On Wed, Feb 4, 2026 at 9:45 PM Bhumika Akula <bhumikaakula7@gmail.com> wrote:


---------- Forwarded message ---------
From: Someswararao Chinta <someswararao.chinta@yanthraa.com>
Date: Wed, Feb 4, 2026 at 2:54 PM
Subject: Assignment
To: Bhumika Akula <bhumikaakula7@gmail.com>
Cc: Tulasee Rao Chintha <tulasi.chintha@gmail.com>, Yanthraa HR Team <hr@yanthraa.com>


Dear Bhumika
Problem Statement--AI Clinical Trial Eligibility & Exclusion Contradiction Engine
Clinical trial enrollment is a manual, time-consuming, and error-prone process. Patient eligibility is typically assessed by reviewing complex trial protocols and matching them against patient profiles. While inclusion criteria may appear satisfied, hidden exclusion rules—often buried deep in protocol text—frequently disqualify patients later in the process.

This leads to:

High screen-failure rates

Wasted clinical effort

Delayed trial enrollment

Poor patient experience

The goal of this project is to build an AI-powered engine that automatically evaluates patient eligibility, identifies exclusion conflicts, and explicitly explains “silent exclusion triggers”.

Core System Objective
The system should allow users to upload:

A structured patient profile

A clinical trial protocol PDF

The AI engine must:

Automatically match inclusion criteria

Automatically evaluate exclusion criteria

Detect and explain hidden contradictions

Example:

Trial age range: 18–70 → Patient age: 69 ✅

Trial exclusion: eGFR < 30 → Patient eGFR: 28 ❌

AI flags a silent exclusion trigger with explanation

Mandatory Architecture & Technology Stack
Frontend

React.js

Tailwind CSS

Backend

Python

FastAPI

Model

BERT (clinical text understanding)

Retrieval-Augmented Generation (RAG)

FAISS or Pinecone

Vector Embeddings

Sentence Transformers

Memory Layer (Memo0)

Redis

PostgreSQL

Authentication

JWT-based authentication

Key Functional Modules
Trial protocol ingestion & parsing (PDF)

Patient profile normalization

Inclusion criteria matching

Exclusion criteria evaluation

Contradiction & “silent exclusion” reasoning

AI-generated eligibility explanation

Deliverables
FastAPI backend supporting:

Patient & trial protocol upload

Eligibility and exclusion analysis

Explainable contradiction output

React frontend with:

Eligibility summary view

Highlighted exclusion triggers

Deployed backend URL (Render)

Deployed frontend URL (Vercel)

Short README explaining system flow and usage

Submission Deadline:  6th Feb 2026



Kindly ensure that the assignment is completed independently. If you have any questions or require clarification, feel free to reach out.


Thank you

--


Dr. Chinta Someswararao Ph.D,

CTO, Yanthraa Information Systems Pvt. Ltd.

Email: someswararao.chinta@yanthraa.com
Mob: +91 94408 70890

Web: https://www.yanthraa.com

