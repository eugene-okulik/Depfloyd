def validate_object(obj, expected_name=None, expected_color=None, expected_size=None):
    assert isinstance(obj, dict), "Object must be dict"
    assert "name" in obj, "'name' missing in object"
    assert "data" in obj and isinstance(obj["data"], dict), "'data' missing or not a dict"
    if expected_name is not None:
        assert obj["name"] == expected_name, f"Expected name '{expected_name}', got '{obj['name']}'"
    if expected_color is not None:
        assert obj["data"]["color"] == expected_color, f"Expected color '{expected_color}', got '{obj['data']['color']}'"
    if expected_size is not None:
        assert obj["data"]["size"] == expected_size, f"Expected size '{expected_size}', got '{obj['data']['size']}'"

def validate_object_list(data):
    assert isinstance(data, dict), "Response must be dict"
    assert "data" in data, "'data' missing in response"
    assert isinstance(data["data"], list), "'data' is not a list"
