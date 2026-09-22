# ruff: noqa
# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import datetime
from zoneinfo import ZoneInfo

from google.adk.agents import Agent
from google.adk.apps import App
from google.adk.models import Gemini
from google.genai import types


MODEL = "gemini-2.5-flash"


def get_weather(query: str) -> str:
    """Retrieves live simulated weather telematics and forecast data for a queried city.

    Args:
        query: The name of the city or location to retrieve weather telemetry for.

    Returns:
        Structured string containing temperature, condition, humidity, and wind speed.
    """
    q = query.lower()
    if "sf" in q or "san francisco" in q:
        return "San Francisco, CA: 60°F (15.5°C), Foggy / Partly Cloudy. Humidity: 82%, Wind: West 12 mph."
    elif "ny" in q or "new york" in q:
        return "New York, NY: 72°F (22.2°C), Clear & Sunny. Humidity: 45%, Wind: SW 8 mph."
    elif "london" in q:
        return "London, UK: 58°F (14.4°C), Light Rain. Humidity: 88%, Wind: NE 10 mph."
    elif "tokyo" in q:
        return "Tokyo, Japan: 68°F (20.0°C), Clear skies. Humidity: 55%, Wind: East 6 mph."
    elif "paris" in q:
        return "Paris, France: 64°F (17.8°C), Mild & Sunny. Humidity: 50%, Wind: North 7 mph."
    elif "sydney" in q:
        return "Sydney, Australia: 75°F (23.9°C), Fair. Humidity: 40%, Wind: SE 14 mph."
    return f"Weather for {query}: 68°F (20.0°C), Clear skies with light breeze."


def get_current_time(query: str) -> str:
    """Computes exact current local timestamp for a requested city using zoneinfo timezones.

    Args:
        query: The name of the city to calculate current local time for.

    Returns:
        Formatted local timestamp string with ISO timezone details.
    """
    q = query.lower()
    tz_map = {
        "san francisco": "America/Los_Angeles",
        "sf": "America/Los_Angeles",
        "new york": "America/New_York",
        "ny": "America/New_York",
        "london": "Europe/London",
        "tokyo": "Asia/Tokyo",
        "paris": "Europe/Paris",
        "sydney": "Australia/Sydney",
        "mumbai": "Asia/Kolkata",
        "delhi": "Asia/Kolkata",
        "bangalore": "Asia/Kolkata",
    }

    tz_identifier = None
    for city, timezone in tz_map.items():
        if city in q:
            tz_identifier = timezone
            break

    if not tz_identifier:
        tz_identifier = "UTC"

    tz = ZoneInfo(tz_identifier)
    now = datetime.datetime.now(tz)
    return f"Current time in {query} ({tz_identifier}): {now.strftime('%A, %B %d, %Y - %H:%M:%S %Z (%z)')}"


def get_currency_exchange_rate(from_currency: str, to_currency: str) -> str:
    """Fetches real-time simulated currency exchange rates and conversion factors.

    Args:
        from_currency: ISO currency code (e.g. USD, EUR, GBP, JPY, INR).
        to_currency: Target ISO currency code (e.g. EUR, USD, INR).

    Returns:
        String with current exchange rate and market timestamp.
    """
    rates = {
        ("USD", "EUR"): 0.92,
        ("USD", "GBP"): 0.79,
        ("USD", "INR"): 83.50,
        ("USD", "JPY"): 155.20,
        ("EUR", "USD"): 1.09,
        ("GBP", "USD"): 1.27,
    }
    pair = (from_currency.upper(), to_currency.upper())
    rate = rates.get(pair, 1.15)
    return f"Exchange Rate ({pair[0]} ➔ {pair[1]}): 1 {pair[0]} = {rate:.4f} {pair[1]}"


def get_tech_news(topic: str) -> str:
    """Retrieves curated trending news headlines for AI, cloud engineering, or developer topics.

    Args:
        topic: Keyword topic (e.g. 'AI', 'Gemini', 'Cloud', 'Python').

    Returns:
        Formatted summary of recent developer highlights.
    """
    return (
        f"Top headlines for '{topic}':\n"
        f"1. Google GenAI & ADK 1.6 Release bringing ultra-low latency streaming.\n"
        f"2. Vertex AI Memory Bank integration expanding multi-session agent context.\n"
        f"3. Next-Gen Agentic Workflows powering enterprise automation across Cloud Run."
    )


root_agent = Agent(
    # Keep in sync with agents-cli-manifest.yaml
    name="simple_agent",
    model=Gemini(
        model=MODEL,
        retry_options=types.HttpRetryOptions(attempts=3),
    ),
    instruction=(
        "You are NovaSphere Core, a state-of-the-art AI assistant powered by Gemini on Google Cloud Vertex AI.\n"
        "Provide elegant, accurate, and structured responses using modern Markdown formatting (bullet points, bold text, code blocks).\n"
        "Leverage your tools to answer real-time queries on weather, global timezones, currency conversion, and tech news."
    ),
    tools=[get_weather, get_current_time, get_currency_exchange_rate, get_tech_news],
)

app = App(
    root_agent=root_agent,
    name="app",
)

