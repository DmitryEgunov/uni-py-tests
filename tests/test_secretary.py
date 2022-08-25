import unittest
from unittest.mock import patch
from secretary import documents, directories, search_by_number, shelf_search, disp_list_docs, add_doc, \
    disp_list_shelf, deleting_doc, moving_doc, add_shelf


class TestFunction(unittest.TestCase):

    @patch('builtins.input', lambda *args: '2207 876234')
    def test_search_by_number(self):
        self.assertEqual(search_by_number(documents), 'Владелец документа :Василий Гупкин')

    @patch('builtins.input', lambda *args: '2207 876234')
    def test_shelf_search(self):
        self.assertEqual(shelf_search(directories), 'Документ находится на полке :1')

    def test_disp_list_docs(self):
        self.assertEqual(type(disp_list_docs(documents)), list)

    @patch('builtins.input', lambda *args: '3')
    def test_add_doc(self):
        self.assertEqual(add_doc(documents, directories),
                         ('3', {'name': '3', 'number': '3', 'type': '3'}))

    @patch('builtins.input', lambda *args: '10006')
    def test_deleting_doc(self):
        self.assertEqual(deleting_doc(documents, directories), '')

    @patch('builtins.input', lambda *args: '000')
    def test_deleting_doc_1(self):
        self.assertEqual(deleting_doc(documents, directories), 'Документ не существует.')

    @patch('builtins.input', lambda *args: '4')
    def test_add_shelf(self):
        self.assertEqual(add_shelf(directories), 'Добавлена новая полка - 4.')



