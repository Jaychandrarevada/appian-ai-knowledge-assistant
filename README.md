# Just-in-Time AI Knowledge Assistant for Complex Case Management

📌 **Appian AI Application Challenge 2026 – IIT Madras**

This repository contains a lightweight prototype demonstrating a **context-aware, AI-assisted knowledge retrieval system** designed for **Appian-based case management workflows**.

The solution focuses on **embedding intelligence directly into decision-making workflows**, rather than relying on standalone search tools or chatbots.

---

## 🧩 Problem Overview

Organizations using Appian manage thousands of **high-stakes cases** such as:
- Insurance claims
- Government benefit approvals
- Regulatory and compliance reviews

To resolve these cases correctly, agents must consult:
- Government regulations
- Internal policy documents
- Standard Operating Procedures (SOPs)

### Current Challenges
- Knowledge is fragmented across multiple systems  
- Agents must leave Appian to search documents  
- High Average Handling Time (AHT)  
- Increased risk of compliance errors  

**Core Problem:**  
> Critical knowledge is not available at the moment of decision-making.

---

## 💡 Proposed Solution

We propose a **Just-in-Time AI Knowledge Assistant embedded inside Appian** that:

- Understands the **active case context**
- Automatically surfaces **relevant policies and SOPs**
- Provides **AI-assisted guidance**
- Includes **verifiable citations** for compliance and trust
- Keeps the **human agent in full control** (human-in-the-loop)

This transforms knowledge retrieval from a **manual search task** into a **context-aware decision support system**.

---

## 🏗️ High-Level Architecture

1. Case context is extracted from the active case  
2. Policy documents are indexed and retrieved  
3. AI generates concise guidance  
4. Each recommendation includes document-level provenance  
5. Insights are displayed inside the same case interface  

The prototype simulates how this logic would integrate with:
- Appian Case Management
- Intelligent Document Processing (IDP)
- AI Skill Designer

---

## 🖥️ Prototype Features

- 📂 Case-centric UI (mirrors Appian workflow design)
- 🧠 Embedded AI Knowledge Assistant panel
- 📄 Contextually relevant policy recommendations
- 🔍 Explanation of *why* a policy is relevant
- 📌 Source citations (document, page, paragraph)
- 📊 Confidence indicator for relevance
- 🧑‍⚖️ Human-in-the-loop decision support

---

## 📍 Example Use Case

**Insurance Claim Processing**

**Case Attributes**
- Claim Type: Flood Damage  
- Location: Florida  
- Case Stage: Review  

**System Behavior**
- Automatically identifies applicable regulations and SOPs  
- Displays AI-assisted guidance with citations  
- Enables faster, more confident decision-making  

---

## 🛠️ Technology Stack (Prototype)

- Python
- Streamlit (UI demonstration)
- PDF text extraction
- Context-based document retrieval
- Simulated AI summarization logic

> Note: Streamlit is used only to demonstrate UI and workflow logic.  
> In a production environment, this would be implemented using native Appian Interfaces, Records, and AI services.

---

## 📂 Repository Structure

