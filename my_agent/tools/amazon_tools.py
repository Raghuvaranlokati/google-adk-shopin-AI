from typing import List, Dict


def amazon_search(query: str, max_results: int = 5) -> List[Dict]:
    """
    Search Amazon for products matching `query`.

    Returns a list of dicts with keys:
      - title: str
      - price: float
      - rating: float
      - url: str
      - platform: str (always 'amazon')
      - specs: dict (arbitrary additional fields)
    """
    # TODO: Replace this stub with a real implementation that calls your backend/API.
    # For now, return 5 demo products so the agent can show top-5 links with prices/ratings.
    products: List[Dict] = []
    for i in range(1, max_results + 1):
        products.append(
            {
                "title": f"Sample Amazon product {i} for: {query}",
                "price": 1000.0 * i,
                "rating": 4.5 - (i * 0.1),
                "url": f"https://www.amazon.in/s?k={query.replace(' ', '+')}&ref=sample_{i}",
                "platform": "amazon",
                "specs": {"sample_rank": i},
            }
        )
    return products


