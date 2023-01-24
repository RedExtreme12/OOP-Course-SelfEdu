from typing import List


class RenderList:

    def __init__(self, type_list):
        self._type_list = None
        self.type_list = type_list

    @property
    def type_list(self):
        return self._type_list

    @type_list.setter
    def type_list(self, _type):
        if _type in ('ul', 'ol'):
            self._type_list = _type
        else:
            self._type_list = 'ul'

    @staticmethod
    def generate_html_list_content(html_list_content: List[str]):
        list_of_content = (f'<li>{li_element}</li>' for li_element in html_list_content)

        return '\n'.join(list_of_content)

    def __call__(self, html_list_content: List[str]):
        html_code = f'<{self._type_list}>\n{self.generate_html_list_content(html_list_content)}\n</{self._type_list}>'

        return html_code
