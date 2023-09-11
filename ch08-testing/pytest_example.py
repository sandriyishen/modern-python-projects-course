import pytest


class TestStringMethods:
    def test_upper(self):
        assert "foo".upper() == "FOO"

    def test_isupper(self):
        assert "foo".isupper(), "Foo is not upper!"
        assert not "Foo".isupper()

    # @pytest.mark.slow
    def test_split(self):
        s = "hello world"
        assert s.split() == ["hello", "world"]
        with pytest.raises(TypeError):
            s.split(2)
