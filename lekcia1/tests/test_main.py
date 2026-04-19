import sys
from pathlib import Path
from types import SimpleNamespace

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from main import MODEL_NAME, PROMPT, load_env_file, run_square_example, square_number


def test_square_number_returns_square() -> None:
    assert square_number(4) == 16


def test_load_env_file_sets_missing_values(tmp_path: Path, monkeypatch) -> None:
    env_file = tmp_path / ".env"
    env_file.write_text("GEMINI_API_KEY=test-key\n", encoding="utf-8")

    monkeypatch.delenv("GEMINI_API_KEY", raising=False)
    load_env_file(env_file)

    assert __import__("os").environ["GEMINI_API_KEY"] == "test-key"


def test_run_square_example_handles_manual_tool_flow() -> None:
    first_response = SimpleNamespace(
        function_calls=[
            SimpleNamespace(
                name="square_number",
                args={"number": 4},
            )
        ],
        candidates=[SimpleNamespace(content="model requested tool")],
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

    answer = run_square_example(fake_client)

    assert answer == "Druha mocnina cisla 4 je 16."
    assert len(fake_models.calls) == 2
    assert fake_models.calls[0]["model"] == MODEL_NAME
    assert fake_models.calls[0]["contents"][0].parts[0].text == PROMPT
