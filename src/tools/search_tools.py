from src.data.vendors import vendors

def search_vendors(user_query):

    results = []

    for v in vendors:

        if (
            v["category"] == user_query["category"]
            and v["budget"] <= user_query["budget"]
        ):
            results.append(v)

    return results