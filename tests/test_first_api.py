import pytest
import requests

class TestFirstAPI:

    names = [("Vladislav"), ("Nikita"), ("Daniil"), ("")]

    @pytest.mark.parametrize('name', names)
    def test_hello_call(self, name):
        url = "https://playground.learnqa.ru/api/hello"
        name = 'Vladislav'
        data = {'name':name}

        response = requests.get(url, params=data)
        assert response.status_code == 200, "Wrong response code"

        response_dict = response.json()
        assert "answer" in response_dict, "There is no field 'answer' "

        if len(name) == 0:
            expected_response_text = "Hello,someone"
        else:
            expected_response_text = f"Hello, {name}"
        actual_response_text = response_dict["answer"]
        assert actual_response_text == expected_response_text, "Actual text not correct"