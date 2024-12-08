import json

def read_houndify(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            houndify = data.get('houndify', [])
            return houndify
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
        return []
    except json.JSONDecodeError:
        print(f"Error decoding JSON from the file {file_path}.")
        return []

def read_wit(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            wit = data.get('wit', [])
            return wit
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
        return []
    except json.JSONDecodeError:
        print(f"Error decoding JSON from the file {file_path}.")
        return []

if __name__ == "__main__":
    file_path = 'certificates.json'
    
    houndify = read_houndify(file_path)
    if houndify:
        print("houndify found:")
        print(f"id: {houndify[0]['id']}") 
        print(f"key: {houndify[0]['key']}") 
    else:
        print("No certificates found or there was an error reading the file.")

    wit = read_wit(file_path)
    if wit:
        print("wit found:")
        print(f"id: {wit[0]['id']}") 
        print(f"key: {wit[0]['key']}") 
    else:
        print("No certificates found or there was an error reading the file.")
