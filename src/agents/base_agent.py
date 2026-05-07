class BaseAgent:
    def analyze_request(self, request):
        raise NotImplementedError("Subclasses must implement this method.")

    def select_tool(self, tools):
        raise NotImplementedError("Subclasses must implement this method.")