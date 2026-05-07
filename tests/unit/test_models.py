import unittest
from src.models.llm_wrapper import LLMWrapper

class TestLLMWrapper(unittest.TestCase):

    def setUp(self):
        self.llm = LLMWrapper(api_key="test_api_key")

    def test_process_input(self):
        input_text = "Hello, how can I help you?"
        expected_output = "Processed: Hello, how can I help you?"
        self.assertEqual(self.llm.process_input(input_text), expected_output)

    def test_generate_response(self):
        input_text = "What is the weather today?"
        response = self.llm.generate_response(input_text)
        self.assertIsInstance(response, str)
        self.assertNotEqual(response, "")

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            self.llm.process_input(None)

if __name__ == '__main__':
    unittest.main()