def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def write_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)

def format_output(data):
    return str(data)  # You can customize this function to format the output as needed

def read_json(file_path):
    import json
    with open(file_path, 'r') as file:
        return json.load(file)

def write_json(file_path, data):
    import json
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)