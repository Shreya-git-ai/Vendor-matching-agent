from src.tools.search_tools import search_vendors

from src.similarity.scoring import calculate_score

from src.llm.llm_handler import (
    generate_vendor_explanation
)


def run_vendor_matching(user_query):

    vendors = search_vendors(user_query)

    final_results = []

    for vendor in vendors:

        score, reasons = calculate_score(
            vendor,
            user_query
        )

        explanation = generate_vendor_explanation(
            user_query,
            vendor
        )

        final_results.append({

            "name": vendor["name"],

            "rating": vendor["rating"],

            "delivery": vendor["delivery"],

            "score": score,

            "reasons": reasons,

            "explanation": explanation
        })

    final_results.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return final_results[:5]