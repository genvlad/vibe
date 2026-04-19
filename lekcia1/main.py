from __future__ import annotations

import os
from pathlib import Path
from typing import Any

from google import genai
from google.genai import types


MODEL_NAME = "gemini-2.5-flash"
PROMPT = "Daj mi druhu mocninu cisla 4."


def load_env_file(env_path: Path) -> None:
    if not env_path.exists():
        return

    for raw_line in env_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue

        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip())


def square_number(number: int) -> int:
    return number * number


def build_square_tool() -> types.Tool:
    function = types.FunctionDeclaration(
        name="square_number",
        description="Returns the square of a number.",
        parameters_json_schema={
            "type": "object",
            "properties": {
                "number": {
                    "type": "integer",
                    "description": "The number to square.",
                }
            },
            "required": ["number"],
        },
    )
    return types.Tool(function_declarations=[function])


def run_square_example(client: genai.Client) -> str:
    tool = build_square_tool()
    user_prompt_content = types.Content(
        role="user",
        parts=[types.Part.from_text(text=PROMPT)],
    )

    first_response = client.models.generate_content(
        model=MODEL_NAME,
        contents=[user_prompt_content],
        config=types.GenerateContentConfig(tools=[tool]),
    )

    if not first_response.function_calls:
        raise RuntimeError("The model did not request a tool call.")

    function_call = first_response.function_calls[0]
    if function_call.name != "square_number":
        raise RuntimeError(f"Unexpected tool call: {function_call.name}")

    result = square_number(int(function_call.args["number"]))
    function_response_part = types.Part.from_function_response(
        name=function_call.name,
        response={"result": result},
    )
    function_response_content = types.Content(
        role="tool",
        parts=[function_response_part],
    )

    final_response = client.models.generate_content(
        model=MODEL_NAME,
        contents=[
            user_prompt_content,
            first_response.candidates[0].content,
            function_response_content,
        ],
        config=types.GenerateContentConfig(tools=[tool]),
    )

    if not final_response.text:
        raise RuntimeError("The model returned an empty final response.")

    return final_response.text


def create_client() -> genai.Client:
    load_env_file(Path(__file__).with_name(".env"))
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("Missing GEMINI_API_KEY in lekcia1/.env or environment.")
    return genai.Client(api_key=api_key)


def main() -> None:
    client = create_client()
    answer = run_square_example(client)
    print(answer)


if __name__ == "__main__":
    main()
