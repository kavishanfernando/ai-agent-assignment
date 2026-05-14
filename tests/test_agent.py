import unittest
from agent import Agent

class TestAgent(unittest.TestCase):
    def setUp(self):
        self.agent = Agent(test_mode=True)

    def test_calculator_tool(self):
        response = self.agent.handle_user_input('Calculate 5 * 3')
        self.assertIn('15', str(response))

    def test_file_reader_tool(self):
        # This test assumes a file named 'sample.txt' exists with content 'test'.
        try:
            with open('sample.txt', 'w') as f:
                f.write('test')
            response = self.agent.handle_user_input('Read file sample.txt')
            self.assertIn('test', response)
        finally:
            import os
            os.remove('sample.txt')

    def test_translation_tool(self):
        response = self.agent.handle_user_input('Translate hello to French')
        self.assertTrue(isinstance(response, str))

    def test_invalid_input(self):
        response = self.agent.handle_user_input('Do something unknown')
        self.assertIn('not understood', response.lower())

if __name__ == '__main__':
    unittest.main()
