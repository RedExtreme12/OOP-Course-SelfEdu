from copy import copy


class Graph:
    def __init__(self, data):
        self.data = data[:]
        self.is_show = True

    @staticmethod
    def check_show(func):
        def wrapper(self):
            if not self.is_show:
                print('Отображение данных закрыто')
            else:
                return func(self)

        return wrapper

    def set_data(self, data):
        self.data = data[:]

    @check_show
    def show_table(self):
        return ' '.join(map(str, self.data))

    @check_show
    def show_graph(self):
        print(f"Графическое отображение данных: {self.show_table()}")

    @check_show
    def show_bar(self):
        print(f'Столбчатая диаграмма: {self.show_table()}')

    def set_show(self, fl_show):
        self.is_show = fl_show


data_graph = list(map(int, input().split()))
gr = Graph(data_graph)
gr.show_bar()
gr.set_show(False)
gr.show_table()
