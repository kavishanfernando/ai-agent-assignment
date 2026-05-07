from flask import Flask, request, jsonify
from agents.explorer_agent import ExplorerAgent
from agents.manager_agent import ManagerAgent
from services.inference import perform_inference

app = Flask(__name__)

# Initialize agents
explorer_agent = ExplorerAgent()
manager_agent = ManagerAgent()

@app.route('/api/ask', methods=['POST'])
def ask():
    user_input = request.json.get('input')
    if not user_input:
        return jsonify({'error': 'No input provided'}), 400

    # Analyze the request and select the appropriate tool
    tool = explorer_agent.analyze_request(user_input)
    
    # Perform inference using the selected tool
    response = perform_inference(tool, user_input)
    
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)