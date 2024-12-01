"""
CP1404 Practical 10
Wikipedia API & Python Library demo
Lindsay Ward, IT@JCU
"""

import wikipedia


def main():
    """Get Wikipedia page title or search phrase from user and print details."""
    while True:
        # Get the search phrase from user
        title = input("Enter page title: ")
        if not title:
            break

        try:
            # Get the Wikipedia page and show results
            page = wikipedia.page(title, auto_suggest=False)
            print(page.title)
            print(page.summary)
            print(page.url)

        except wikipedia.DisambiguationError as e:
            print("We need a more specific title. Try one of the following, or a new search:")
            print(e.options[0:5])  # Show first 5 options

        except wikipedia.PageError:
            print(f"Page id \"{title}\" does not match any pages. Try another id!")

    print("Thank you.")


main()