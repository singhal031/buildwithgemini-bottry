# 🚀 NovaSphere AI Core

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![ADK 1.6+](https://img.shields.io/badge/ADK-1.6.1-green.svg)](https://cloud.google.com/)
[![Model](https://img.shields.io/badge/Model-Gemini%202.5%20Pro-orange.svg)](https://deepmind.google/technologies/gemini/)
[![License](https://img.shields.io/badge/License-Apache%202.0-lightgrey.svg)](LICENSE)

An intelligent agent built with the **Google Agent Development Kit (ADK)** and `agents-cli`, powered by Vertex AI's **`gemini-2.5-pro`** model.

![NovaSphere Demo](demo.gif)

---

## 💡 Key Capabilities

NovaSphere Core provides real-time intelligent assistance equipped with four built-in tool modules:

- **🌤️ Weather Telematics (`get_weather`)**: Structured weather data, humidity, and wind conditions across global cities.
- **🕒 Global Timezone Engine (`get_current_time`)**: High-precision local timestamps with ISO timezone offsets using Python `zoneinfo`.
- **💱 Currency Exchange Rates (`get_currency_exchange_rate`)**: Instant FX market conversion rates between major fiat currencies.
- **📰 Tech News Feed (`get_tech_news`)**: Real-time developer highlights and AI ecosystem news summaries.

### 🌐 Infrastructure & Stack
- **AI Foundation**: Google GenAI SDK (`gemini-2.5-pro`) on Vertex AI
- **Framework**: Agent Development Kit (ADK) & Agent Engine
- **Deployment Target**: Google Cloud Agent Runtime

---

## 🛠️ Local Setup & Quickstart

### 1. Environment Configuration
Define your Vertex AI credentials:
```bash
export GOOGLE_GENAI_USE_VERTEXAI=true
export GOOGLE_CLOUD_PROJECT=<YOUR_GCP_PROJECT_ID>
export GOOGLE_CLOUD_LOCATION=us-central1
```

### 2. Installation
Install project dependencies with `agents-cli`:
```bash
agents-cli install
```

### 3. Verification & Testing
Execute the complete integration test suite:
```bash
uv run pytest
```

### 4. Interactive Playground
Launch the local ADK Dev UI playground:
```bash
agents-cli playground
```
