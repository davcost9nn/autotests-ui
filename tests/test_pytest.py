import pytest
def test_first_try():
    print("Hello World!")

class TestClass:
    def test_1(self):
        ...

    def test_2(self):
        ...
    @pytest.mark.xfail
    def test_greeting(self):
        greeting = "Hello, world!"
        assert greeting == "Hi, world!", "greeting != Hi, world"