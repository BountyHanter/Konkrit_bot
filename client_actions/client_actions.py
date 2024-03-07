import json
import os


def actions(action, client_id):
    def save_data(data, file_path):
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)

    def load_data(file_path):
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                data = json.load(file)
        else:
            data = {"client_id": client_id, "actions": []}
        return data

    file_path = f"client_actions/client_id_{client_id}.json"
    client_data = load_data(file_path)
    client_data["actions"].append(action)
    save_data(client_data, file_path)
    print(f"Action client_id_{client_id} have been saved")

