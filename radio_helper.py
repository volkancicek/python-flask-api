import json
from flask_api import status

file_path = "data/radios.json"


def post_radio(data, id):
    radios = radios_get()
    for item in radios:
        if radio_matches(id, item.items()):
            content = {'StatusCode': '403', 'Message': 'radio with ID:' + str(id) + ' already exists'}
            return content, status.HTTP_403_FORBIDDEN

    radio = {"ID": id, "alias": data["alias"], "allowed_locations": data["allowed_locations"]}
    radios.append(radio)
    radios_dump(radios)

    return {'StatusCode': '200', 'Message': 'success'}


def post_radio_location(data, id):
    radios = radios_get()
    location = data["location"]
    for idx, item in enumerate(radios):
        if radio_matches(id, item.items()):
            if location in item["allowed_locations"]:
                item["location"] = location
                radios[idx] = item
                radios_dump(radios)
                return {'StatusCode': '200', 'Message': 'success'}
            else:
                return {'StatusCode': '403', 'Message': 'Invalid location'}, status.HTTP_403_FORBIDDEN

    return {'StatusCode': '404', 'Message': 'No radio exist with id: ' + str(id)}, status.HTTP_404_NOT_FOUND


def get_radio_location(id):
    radios = radios_get()
    for item in radios:
        if radio_matches(id, item.items()):
            if "location" in item.keys():
                return {'StatusCode': '200', 'location': item["location"], 'Message': 'success'}
            else:
                return {'StatusCode': '404', 'Message': 'location not found'}, status.HTTP_404_NOT_FOUND

    return {'StatusCode': '404', 'Message': 'No radio exist with id: ' + str(id)}, status.HTTP_404_NOT_FOUND


def radio_matches(id, radios):
    return id in (y for x, y in radios if x == "ID")


def radios_get():
    with open(file_path, "r") as f:
        radios = json.load(f)

    return radios


def radios_dump(radios):
    with open(file_path, "w") as f:
        json.dump(radios, f)
