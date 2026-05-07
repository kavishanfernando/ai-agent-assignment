def calculate_metrics(agent_name, execution_time, success):
    metrics = {
        'agent_name': agent_name,
        'execution_time': execution_time,
        'success': success
    }
    return metrics

def report_metrics(metrics):
    print("Metrics Report:")
    print(f"Agent Name: {metrics['agent_name']}")
    print(f"Execution Time: {metrics['execution_time']} seconds")
    print(f"Success: {'Yes' if metrics['success'] else 'No'}")