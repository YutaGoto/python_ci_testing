import app


def test_greeting():
    assert app.greeting('name') == 'hello name'
