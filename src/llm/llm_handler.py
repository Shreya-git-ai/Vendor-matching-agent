import os

from openai import OpenAI
from dotenv import load_dotenv


load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def generate_vendor_explanation(
    user_query,
    vendor
):

    try:

        prompt = f"""
        User Requirements:

        Category: {user_query['category']}
        Budget: {user_query['budget']}
        Location: {user_query['location']}
        Delivery: {user_query['delivery']}

        Vendor:
        {vendor['name']}

        Explain why this vendor is a good recommendation
        in 2 short lines.
        """

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.choices[0].message.content

    except Exception:

        return (
            f"{vendor['name']} matches your "
            f"requirements based on category, "
            f"budget, and delivery preference."
        )