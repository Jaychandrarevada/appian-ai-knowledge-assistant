def retrieve_relevant_docs(case_context, documents):
    keywords = [
        case_context["claim_type"].lower(),
        case_context["location"].lower()
    ]

    results = []
    for doc in documents:
        if "flood" in doc["document"].lower():
            results.append(doc)
    return results
