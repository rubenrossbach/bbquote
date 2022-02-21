from bbquote.lib import get_quote

def testing_get_quote():
    # test that length is not 0
    string_response = get_quote()
    assert len(string_response) != 0
