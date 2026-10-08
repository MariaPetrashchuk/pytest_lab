class Figure:
    FIGURES = ["квадрат", "прямокутник", "трикутник"]

    def __init__(self, figure_type, length):
        assert figure_type in self.FIGURES, "Невідомий тип фігури"
        assert length > 0, "Довжина має бути більшою за нуль"

        self.figure_type = figure_type
        self.length = length

    def get_figure_type(self):
        return self.figure_type

    def get_figure_length(self):
        return self.length

    def get_angles(self):
        if self.figure_type in ["квадрат", "прямокутник"]:
            return 4
        elif self.figure_type == "трикутник":
            return 3