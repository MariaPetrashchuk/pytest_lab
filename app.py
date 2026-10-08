class Figure:
    FIGURES = ["трикутник", "квадрат", "коло"]

    def __init__(self, figure_type, length):
        assert figure_type in self.FIGURES
        assert length > 0

        self.type = figure_type
        self.length = length

    @property
    def get_figure_length(self):
        return self.length