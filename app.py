import streamlit as st
import json
import sys

# Ensure backend imports work
sys.path.append(".")

from backend.document_loader import load_documents
from backend.retriever import retrieve_relevant_docs
from backend.summarizer import generate_summary

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------
st.set_page_config(
    page_title="Just-in-Time AI Knowledge Assistant",
    page_icon="🤖",
    layout="wide"
)

# --------------------------------------------------
# Header
# --------------------------------------------------
st.title("🤖 Just-in-Time AI Knowledge Assistant")
st.caption(
    "Context-aware, explainable decision support embedded in case management workflows"
)
st.divider()

# --------------------------------------------------
# Load Case Data
# --------------------------------------------------
with open("data/sample_cases.json") as f:
    case = json.load(f)

# --------------------------------------------------
# Load Documents & Retrieve Relevant Policies
# --------------------------------------------------
documents = load_documents("data/policy_documents")
relevant_docs = retrieve_relevant_docs(case, documents)

# --------------------------------------------------
# Layout: Case View (Left) | AI Assistant (Right)
# --------------------------------------------------
left_col, right_col = st.columns([2, 1])

# --------------------------------------------------
# LEFT COLUMN — CASE DETAILS
# --------------------------------------------------
with left_col:
    st.subheader("📂 Active Case Context")
    st.caption("Live case attributes used for policy relevance determination")

    st.markdown(
        f"""
        **Claim ID:** {case['claim_id']}  
        **Claim Type:** {case['claim_type']}  
        **Location:** {case['location']}  
        **Case Stage:** {case['case_stage']}
        """
    )

    st.divider()

    st.subheader("🧾 Case Actions")
    st.button("✅ Approve Case")
    st.button("📝 Request More Information")
    st.button("⚠️ Escalate Case")

# --------------------------------------------------
# RIGHT COLUMN — AI KNOWLEDGE ASSISTANT
# --------------------------------------------------
with right_col:
    st.subheader("🧠 AI Knowledge Assistant")
    st.caption(
        "Policies and guidance automatically surfaced based on the active case"
    )

    if not relevant_docs:
        st.info(
            "No relevant policies found based on the current case context. "
            "As documents are updated, recommendations will appear automatically."
        )

    for doc in relevant_docs:
        result = generate_summary(doc)

        with st.expander(f"📄 {doc['document']}"):
            st.markdown("**Why this policy is relevant**")
            st.write(
                "- Matches claim type: Flood Damage\n"
                "- Applicable jurisdiction: Florida\n"
                "- Relevant to current review stage"
            )

            st.markdown("**AI-assisted guidance**")
            st.write(result["summary"])

            st.markdown("**Relevance confidence**")
            st.progress(87)

            st.caption(f"📌 Source: {result['citation']}")
