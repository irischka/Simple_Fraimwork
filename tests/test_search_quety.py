from page_objects.pages.search_page import SearchPage


def test_search_query(app):
    """ The test searches for the entered query, return it and passed with correct assert """
    search_page = SearchPage(app)
    search_page.go_to_page()
    search_page.enter_query(world="Pictures")
    search_page.go_to_page()
    search_page.submit_query()
    title = search_page.get_text()
    assert title == "Pictures"


