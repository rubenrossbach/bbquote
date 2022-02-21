from bbquote.lib import get_quote

def testing_get_quote():
    string_response = get_quote()
    assert len(string_response) != 0
