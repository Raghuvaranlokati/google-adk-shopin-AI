from typing import List, Dict


def flipkart_search(query: str, max_results: int = 5) -> List[Dict]:
    """
    Search Flipkart for products matching `query`.

    Returns a list of dicts with keys:
      - title: str
      - price: float
      - rating: float
      - url: str
      - platform: str (always 'flipkart')
      - specs: dict (arbitrary additional fields)
    """
    # TODO: Replace this stub with a real implementation that calls your backend/API.
    # For now, return 5 demo products so the agent can show top-5 links with prices/ratings.
    products: List[Dict] = []
    for i in range(1, max_results + 1):
        products.append(
            {
                "title": f"Sample Flipkart product {i} for: {query}",
                "price": 950.0 * i,
                "rating": 4.6 - (i * 0.1),
                "url": f"https://www.flipkart.com/search?q={query.replace(' ', '+')}&sample={i}",
                "platform": "flipkart",
                "specs": {"sample_rank": i},
            }
        )
    return products


