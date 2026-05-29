# Q46 — Production: Async HTTP with aiohttp
# Fetch multiple URLs concurrently — this is how real AI pipelines fetch data fast.
#
# Write an async function fetch_all(urls) that:
#   - Fetches all URLs concurrently (not one by one)
#   - Returns a list of response texts in the same order as input URLs
#   - Uses aiohttp + asyncio.gather
#
# Test with these URLs (they return fast):
urls = [
    "https://httpbin.org/get",
    "https://httpbin.org/uuid",
    "https://httpbin.org/ip",
]
#
# Compare: sequential would take 3x longer than concurrent.
# pip install aiohttp
