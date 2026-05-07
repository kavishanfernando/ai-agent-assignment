import unittest
from src.agents.explorer_agent import ExplorerAgent
from src.agents.manager_agent import ManagerAgent

class TestExplorerAgent(unittest.TestCase):
    def setUp(self):
        self.agent = ExplorerAgent()

    def test_analyze_request(self):
        request = "What is the weather like today?"
        analysis = self.agent.analyze_request(request)
        self.assertIsNotNone(analysis)
        self.assertIn('intent', analysis)

    def test_select_tool(self):
        request = "Find me a restaurant nearby."
        tool = self.agent.select_tool(request)
        self.assertEqual(tool, "restaurant_finder")

class TestManagerAgent(unittest.TestCase):
    def setUp(self):
        self.agent = ManagerAgent()

    def test_manage_workflow(self):
        requests = ["Get me a flight to New York.", "Book a hotel in Paris."]
        results = self.agent.manage_workflow(requests)
        self.assertEqual(len(results), 2)
        self.assertIn('flight', results[0])
        self.assertIn('hotel', results[1])

if __name__ == '__main__':
    unittest.main()