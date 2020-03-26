from page_objects.pages.search_page import SearchPage


def test_get_text_search_button(browser):
    """ The test checks the text into the button"""
    search_page = SearchPage(browser)
    button = search_page.get_text_search_button()
    assert button == "Пошук"
