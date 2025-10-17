import json
import os

def load_config():
    """
    Load configuration from config.json file.
    
    Returns:
        dict: Configuration dictionary
    """
    config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config.json')
    
    try:
        with open(config_path, 'r') as f:
            return json.load(f)
    except Exception as e:
        raise Exception(f"Failed to load configuration: {str(e)}")

def save_generated_code(code, path):
    """
    Save generated code to a file.
    
    Args:
        code (str): Generated code content
        path (str): Path to save the code
    """
    try:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, 'w') as f:
            f.write(code)
    except Exception as e:
        raise Exception(f"Failed to save generated code: {str(e)}")