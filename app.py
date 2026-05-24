from src.agents.matching_agent import (
    run_vendor_matching
)

import time


def loading_screen():

    print("\nLaunching AI Systems", end="")

    for _ in range(5):

        print(".", end="", flush=True)

        time.sleep(0.4)

    print("\n")


def print_header():

    print("=" * 60)

    print("        AI VENDOR MATCHING ASSISTANT")

    print("=" * 60)


def get_user_input():

    print("\nEnter Vendor Requirements\n")

    category = input(
        "Category (catering/office/electronics): "
    )

    budget = int(
        input("Budget: ")
    )

    location = input(
        "Location: "
    )

    delivery = input(
        "Delivery (express/standard): "
    )

    return {

        "category": category,

        "budget": budget,

        "location": location,

        "delivery": delivery
    }


def print_workflow():

    print("\n" + "=" * 60)

    print("                 AGENT WORKFLOW")

    print("=" * 60)

    workflows = [

        "Understanding User Request",

        "Searching Vendor Database",

        "Calculating Match Scores",

        "Ranking Best Vendors",

        "Generating AI Recommendations"
    ]

    for item in workflows:

        print(f"✓ {item}")

        time.sleep(0.5)


def print_results(results):

    print("\n" + "=" * 60)

    print("               TOP VENDOR MATCHES")

    print("=" * 60)

    for i, vendor in enumerate(results, 1):

        print(f"\n{i}. {vendor['name']}")

        print("-" * 40)

        print(
            f"Match Score : {vendor['score']}%"
        )

        print(
            f"Vendor Rating : {vendor['rating']}"
        )

        print(
            f"Delivery Type : {vendor['delivery']}"
        )

        print("\nWhy matched?")

        for reason in vendor["reasons"]:

            print(f"• {reason}")

        print("\nAI Recommendation:")

        print(
            vendor["explanation"]
        )

        print("\n")


def print_visual_bars(results):

    print("\n" + "=" * 60)

    print("              VENDOR MATCH SCORES")

    print("=" * 60)

    for vendor in results:

        filled = "█" * (
            vendor["score"] // 10
        )

        empty = "░" * (
            10 - len(filled)
        )

        print(
            f"{vendor['name'][:20]:<20} "
            f"{filled}{empty} "
            f"{vendor['score']}%"
        )


def final_screen():

    print("\n" + "=" * 60)

    print("         AI ANALYSIS COMPLETED")

    print("=" * 60)

    print(
        "\nBest vendors ranked successfully.\n"
    )


def main():

    loading_screen()

    print_header()

    user_query = get_user_input()

    print_workflow()

    results = run_vendor_matching(
        user_query
    )

    print_results(results)

    print_visual_bars(results)

    final_screen()


if __name__ == "__main__":

    main()