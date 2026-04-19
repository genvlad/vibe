import sys
from pathlib import Path
from types import SimpleNamespace

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

def test_square_number_returns_square(monkeypatch) -> None:
    monkeypatch.setenv("GEMINI_API_KEY", "test-key")

    first_response = SimpleNamespace(
        candidates=[
            SimpleNamespace(
                content=SimpleNamespace(
                    parts=[
                        SimpleNamespace(
                            function_call=SimpleNamespace(
                                name="square_number",
                                args={"number": 4},
                            )
                        )
                    ]
                )
            )
        ]
    )
    final_response = SimpleNamespace(text="Druha mocnina cisla 4 je 16.")

    class FakeModels:
        def generate_content(self, **kwargs):
            if kwargs["contents"] == "Daj mi druhu mocninu cisla 4.":
                return first_response
            return final_response

    fake_client = SimpleNamespace(models=FakeModels())

    monkeypatch.setattr("google.genai.Client", lambda api_key: fake_client)

    if "main" in sys.modules:
        del sys.modules["main"]
    import main

    assert main.square_number(4) == 16


def test_main_script_handles_simple_tool_flow(monkeypatch) -> None:
    monkeypatch.setenv("GEMINI_API_KEY", "test-key")

    first_response = SimpleNamespace(
        candidates=[
            SimpleNamespace(
                content=SimpleNamespace(
                    parts=[
                        SimpleNamespace(
                            function_call=SimpleNamespace(
                                name="square_number",
                                args={"number": 4},
                            )
                        )
                    ]
                )
            )
        ]
    )
    final_response = SimpleNamespace(text="Druha mocnina cisla 4 je 16.")

    class FakeModels:
        def __init__(self) -> None:
            self.calls = []

        def generate_content(self, **kwargs):
            self.calls.append(kwargs)
            if len(self.calls) == 1:
                return first_response
            return final_response

    fake_models = FakeModels()
    fake_client = SimpleNamespace(models=fake_models)

    monkeypatch.setattr("google.genai.Client", lambda api_key: fake_client)

    if "main" in sys.modules:
        del sys.modules["main"]
    import main

    assert main.tool_result == 16
    assert main.final_response.text == "Druha mocnina cisla 4 je 16."
    assert len(fake_models.calls) == 2
    assert fake_models.calls[0]["contents"] == "Daj mi druhu mocninu cisla 4."
