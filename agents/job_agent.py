from playwright.sync_api import sync_playwright


def search_jobs(keyword):

    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=False,
            slow_mo=100
        )

        context = browser.new_context()

        page = context.new_page()

        page.goto(
            f"https://www.linkedin.com/jobs/search/?keywords={keyword}",
            wait_until="networkidle"
        )

        page.wait_for_timeout(10000)

        print("\n===== PAGE TITLE =====")
        print(page.title())

        print("\n===== CURRENT URL =====")
        print(page.url)

        print("\n===== FIRST 2000 CHARS =====")
        print(page.content()[:2000])

        browser.close()

        return ["Debug Complete"]


if __name__ == "__main__":
    search_jobs("Data Analyst")