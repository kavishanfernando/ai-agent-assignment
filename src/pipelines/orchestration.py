from agents.explorer_agent import ExplorerAgent
from agents.manager_agent import ManagerAgent
from services.inference import perform_inference

class Orchestrator:
    def __init__(self):
        self.explorer_agent = ExplorerAgent()
        self.manager_agent = ManagerAgent()

    def run(self, user_input):
        analysis = self.explorer_agent.analyze_request(user_input)
        tool_selection = self.manager_agent.select_tool(analysis)
        result = perform_inference(tool_selection, analysis)
        return result

if __name__ == "__main__":
    orchestrator = Orchestrator()
    user_input = input("Enter your request: ")
    output = orchestrator.run(user_input)
    print("Output:", output)