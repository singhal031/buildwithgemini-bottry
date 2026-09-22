# 🌤️ Simple Agent

An AI assistant built with the Google Agent Development Kit (ADK) and `agents-cli`, powered by Vertex AI's `gemini-2.5-flash` model.

![Simple Agent Demo](demo.gif)

---

## 🚀 Capabilities

The agent is implemented in `app/agent.py` using Python ADK and includes the following function tools:

- **Weather Inquiry (`get_weather`)**: Returns simulated weather report data for requested locations (e.g., San Francisco, New York).
- **Timezone Resolution (`get_current_time`)**: Computes and formats real-time timestamps using `zoneinfo` for target cities.

### 🌐 Google Cloud & ADK Integration
- **Model**: `gemini-2.5-flash` via Vertex AI
- **Framework**: Agent Development Kit (ADK)
- **Deployment Target**: Agent Runtime (Agent Engine)

*(Note: Features such as Memory Bank, Firestore, RAG Engine, Image Generation, and A2UI are not implemented in this repository).*

---

## 🛠️ Local Setup & Execution

### 1. Prerequisites
- Python 3.11+
- `uv` package manager (`uv tool install google-agents-cli`)
- Authenticated `gcloud` CLI

### 2. Environment Setup
Set up the required environment variables:
```bash
export GOOGLE_GENAI_USE_VERTEXAI=true
export GOOGLE_CLOUD_PROJECT=<YOUR_GCP_PROJECT_ID>
export GOOGLE_CLOUD_LOCATION=us-central1
```

### 3. Install Dependencies
```bash
agents-cli install
```

### 4. Run Tests
```bash
uv run pytest
```

### 5. Launch the ADK Playground
To launch the interactive agent playground locally:
```bash
agents-cli playground
```
