import pytest
from playwright.sync_api import Page
import time


def search_and_add_to_cart(page: Page, search_term: str) -> str:
    """
    Search Amazon for a product, add to cart, return price.
    """

    # Go to Amazon
    page.goto("https://www.amazon.com/", wait_until="domcontentloaded")
    page.wait_for_load_state("domcontentloaded")
    page.wait_for_timeout(2000)

    # Close any popups
    try:
        page.keyboard.press("Escape")
    except:
        pass

    # Type in search box
   # typing search term in Amazon search box
    search_box = page.locator("#twotabsearchtextbox")
    search_box.fill(search_term)

# pressing enter to trigger search
    page.keyboard.press("Enter")

# waiting for results page to load (Amazon is slow sometimes)
    page.wait_for_load_state("domcontentloaded")

# small buffer wait because Amazon UI sometimes loads late
    page.wait_for_timeout(2000)

    # Take screenshot to debug what Amazon shows
    page.screenshot(path=f"screenshot_{search_term.replace(' ', '_')}.png")

    # Try multiple selectors for product links
    product_clicked = False
    link_selectors = [
        'div[data-component-type="s-search-result"] h2 a.a-link-normal',
        'div[data-component-type="s-search-result"] a.a-link-normal.s-underline-text',
        'div[data-component-type="s-search-result"] h2 a',
        's-result-item h2 a',
        '.s-search-results h2 a',
        'h2.a-size-mini a',
        'h2.a-size-base a',
        '.a-section h2 a',
    ]

    for selector in link_selectors:
        try:
            links = page.locator(selector)
            count = links.count()
            if count > 0:
                links.first.click(timeout=10000)
                product_clicked = True
                print(f" Clicked product using selector: {selector}")
                break
        except Exception as e:
            print(f"Selector failed: {selector} — {str(e)[:50]}")
            continue

    if not product_clicked:
        # Last resort — click any link with product in URL
        try:
            page.locator('a[href*="/dp/"]').first.click(timeout=10000)
            product_clicked = True
            print("✅ Clicked product via /dp/ URL")
        except:
            pass

    if not product_clicked:
        raise Exception(f"Could not find any product link for '{search_term}'")

    page.wait_for_load_state("domcontentloaded")
    time.sleep(3)

    # Take screenshot of product page
    page.screenshot(path=f"product_{search_term.replace(' ', '_')}.png")

    # Get price
    price = "Price not available"
    price_selectors = [
        "span.a-price span.a-offscreen",
        ".priceToPay span.a-price-whole",
        "#priceblock_ourprice",
        "#priceblock_dealprice",
        "#corePrice_feature_div span.a-offscreen",
        ".a-price .a-offscreen",
        "#price_inside_buybox",
        "#newBuyBoxPrice",
    ]

    for selector in price_selectors:
        try:
            el = page.locator(selector).first
            if el.is_visible(timeout=2000):
                price = el.text_content().strip()
                if price:
                    break
        except:
            continue

    # Add to cart
    cart_selectors = [
        "#add-to-cart-button",
        "input[name='submit.add-to-cart']",
        "#submit.add-to-cart",
    ]

    added = False
    for selector in cart_selectors:
        try:
            btn = page.locator(selector).first
            if btn.is_visible(timeout=5000):
                btn.click()
                added = True
                page.wait_for_load_state("domcontentloaded")
                time.sleep(2)
                break
        except:
            continue

    if added:
        # Dismiss any popup after adding
        try:
            no_thanks = page.locator(
                "button:has-text('No thanks'), "
                "span:has-text('No thanks'), "
                "#attachSiNoCoverage"
            ).first
            if no_thanks.is_visible(timeout=3000):
                no_thanks.click()
        except:
            pass
        print(f"✅ '{search_term}' added to cart!")
    else:
        print(f"⚠️  Could not add '{search_term}' to cart")

    return price


# ══════════════════════════════════════════════
# TEST CASE 1: iPhone
# ══════════════════════════════════════════════
def test_iphone_search_and_cart(page: Page):
    """TC1: Search iPhone on Amazon,add to cart ,price details."""

    print("\n" + "=" * 50)
    print("  TEST CASE 1: iPhone Search")
    print("=" * 50)

    price = search_and_add_to_cart(page, "iPhone")

    print("\n" + "─" * 50)
    print(f"    Product : iPhone")
    print(f"    Price   : {price}")
    print("─" * 50 + "\n")

    assert price != "Price not available", "iPhone price not found!"


# ══════════════════════════════════════════════
# TEST CASE 2: Samsung Galaxy
# ══════════════════════════════════════════════
def test_galaxy_search_and_cart(page: Page):
    """TC2: Search Samsung Galaxy on Amazon, add to cart, print price."""

    print("\n" + "=" * 50)
    print("  TEST CASE 2: Samsung Galaxy Search")
    print("=" * 50)

    price = search_and_add_to_cart(page, "Samsung Galaxy")

    print("\n" + "─" * 50)
    print(f"   Product : Samsung Galaxy")
    print(f"    Price   : {price}")
    print("─" * 50 + "\n")

    assert price != "Price not available", "Samsung Galaxy price not found!"