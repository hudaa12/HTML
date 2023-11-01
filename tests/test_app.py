from playwright.sync_api import Page, expect

# Tests for your routes go here

"""
When we visit /hello
We see, "Hello world!"
"""


def test_get_hello(page, test_web_address):
    page.goto(f"http://{test_web_address}/hello")
    heading_tag = page.locator("h1)")
    expect(heading_tag).to_have_text("Hello, world!")


"""
We get a Bye! message from the goodbye page
"""

def test_get_goodbye(page, test_web_address):
    page.goto(f"http://{test_web_address}/goodbye")
    strong_tag = page.locator("strong")
    expect(strong_tag).to_have_text("Bye!")