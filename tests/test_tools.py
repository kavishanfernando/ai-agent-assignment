import unittest
from tools.calculator_tool import CalculatorTool
from tools.file_reader_tool import FileReaderTool
from tools.translation_tool import TranslationTool
from tools.time_tool import TimeTool

class TestCalculatorTool(unittest.TestCase):
    def test_addition(self):
        calc = CalculatorTool()
        result = calc.run('2 + 2')
        self.assertEqual(result, 'Result: 4')

    def test_invalid_expression(self):
        calc = CalculatorTool()
        result = calc.run('2 +')
        self.assertIn('Error', result)

class TestFileReaderTool(unittest.TestCase):
    def test_file_not_found(self):
        reader = FileReaderTool()
        result = reader.run('nonexistent.txt')
        self.assertIn('Error', result)

class TestTranslationTool(unittest.TestCase):
    def test_translation(self):
        translator = TranslationTool()
        result = translator.run('hello', 'es')
        self.assertIsInstance(result, str)

class TestTimeTool(unittest.TestCase):
    def test_time(self):
        time_tool = TimeTool()
        result = time_tool.run()
        self.assertIsInstance(result, str)

if __name__ == '__main__':
    unittest.main()
