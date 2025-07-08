import pytest
from src.decorators import log


def test_log_success(capsys):
    @log()
    def multi(x, y):
        return x * y

    result = multi(2, 3)
    assert result == 6
    captured = capsys.readouterr()
    assert "multi ok" in captured.out


def test_log_exception(capsys):
    @log()
    def fail():
        raise Exception

    with pytest.raises(Exception):
        fail()
    captured = capsys.readouterr()
    assert "Exception" in captured.out


def test_log_args_kwargs(capsys):
    @log()
    def func(a, b=2, **kwargs):
        return a + b + kwargs.get("c")

    result = func(9, b=13, c=70)
    assert result == 92
    captured = capsys.readouterr()
    assert "func ok" in captured.out


def test_log_name_and_doc(capsys):
    @log()
    def my_func():
        """Doc"""
        pass

    assert my_func.__name__ == "my_func"
    assert my_func.__doc__ == "Doc"
    my_func()
    captured = capsys.readouterr()
    assert "my_func ok" in captured.out
