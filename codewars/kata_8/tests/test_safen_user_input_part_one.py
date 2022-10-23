from codewars.kata_8.files.safen_user_input_part_one import html_special_chars
import pytest


@pytest.mark.parametrize('given, expected', [
    ("<h2>Hello World</h2>", "&lt;h2&gt;Hello World&lt;/h2&gt;"),
    ("Hello, how would you & I fare?", "Hello, how would you &amp; I fare?"),
    ('How was "The Matrix"?  Did you like it?',
     'How was &quot;The Matrix&quot;?  Did you like it?'),
    ("<script>alert('Website Hacked!');</script>",
     "&lt;script&gt;alert('Website Hacked!');&lt;/script&gt;")])
def test_html_special_chars(given, expected):
    assert html_special_chars(given) == expected


@pytest.mark.parametrize('given, expected', [
    (
    "l&gt;&lt;:&quot;&lt;&lt;&lt;&lt;tsa&lt;'0#&+}q&&quot;-$&&quot;&quot;v&M*&quot;&quot;&gt;^L&amp; DQ&gt;J&JQ&quot;&amp; &lt;q&",
    "l&gt;&lt;:&quot;&lt;&lt;&lt;&lt;tsa&lt;'0#&amp;+}q&amp;&quot;-$&amp;&quot;&quot;v&amp;M*&quot;&quot;&gt;^L&amp;\rDQ&gt;J&amp;JQ&quot;&amp;\x0c&lt;q&amp;")])
def test_html_special_chars_2(given, expected):
    assert html_special_chars(given) == expected
