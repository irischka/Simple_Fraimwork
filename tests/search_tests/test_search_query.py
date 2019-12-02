from page_objects.pages.search_page import SearchPage


def test_search_query(browser):
    """ The test searches for the entered query """
    search_page = SearchPage(browser)
    search_page.enter_query(world="Картинки")
    search_page.submit_query()
    title = search_page.get_text_query()
    assert title == "Картинки"


