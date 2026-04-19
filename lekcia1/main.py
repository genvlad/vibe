import os

from dotenv import load_dotenv
from google import genai
from google.genai import types


def square_number(number: int) -> int:
    return number * number


load_dotenv()

api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    raise RuntimeError("Missing GEMINI_API_KEY.")

tools = [
    {
        "name": "square_number",
        "description": "Use this function to get the square of a number.",
        "parameters": {
            "type": "object",
            "properties": {
                "number": {
                    "type": "integer",
                    "description": "The number to square, e.g. 4",
                }
            },
            "required": ["number"],
        },
    }
]

client = genai.Client(api_key=api_key)
gemini_tools = types.Tool(function_declarations=tools)
config = types.GenerateContentConfig(tools=[gemini_tools])
prompt = "Daj mi druhu mocninu cisla 4."

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt,
    config=config,
)

tool_call = response.candidates[0].content.parts[0].function_call
tool_result = square_number(int(tool_call.args["number"]))

tool_response = types.Content(
    role="tool",
    parts=[
        types.Part.from_function_response(
            name=tool_call.name,
            response={"result": tool_result},
        )
    ],
)

final_response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=[
        prompt,
        response.candidates[0].content,
        tool_response,
    ],
    config=config,
)

print("--- Response Tool call: ---")
print(tool_call)
print("--- Final response: ---")
print(final_response.text)
