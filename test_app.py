import pytest
from app import Figure


@pytest.mark.unit
def test_triangle_type():
    triangle = Figure("трикутник", 4)
    assert triangle.type == "трикутник"


def test_invalid_length():
    with pytest.raises(AssertionError):
        Figure("квадрат", 0)


@pytest.mark.parametrize("figure", Figure.FIGURES)
def test_allowed_figure(figure):
    assert Figure(figure, 1).type == figure


@pytest.fixture
def square():
    return Figure("квадрат", 10)


@pytest.mark.unit
def test_square_length(square):
    assert square.get_figure_length == 10


@pytest.mark.parametrize("figure", [
    "прямокутник",
    "ромб",
    "п'ятикутник"
])
def test_invalid_figure(figure):
    with pytest.raises(AssertionError):
        Figure(figure, 10)


@pytest.mark.parametrize("length", [
    0,
    -1,
    -10
])
def test_invalid_length_values(length):
    with pytest.raises(AssertionError):
        Figure("квадрат", length)


@pytest.fixture(scope="module")
def allowed_figures():
    return Figure.FIGURES


def test_first_figure(allowed_figures):
    assert "трикутник" in allowed_figures


def test_second_figure(allowed_figures):
    assert "квадрат" in allowed_figures