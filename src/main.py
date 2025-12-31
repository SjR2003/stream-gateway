"""
Roadmap:
- Application entry point
- Bootstraps the Gateway process
- Loads configuration (env, settings)
- Starts:
    - REST API (for dashboard & control)
    - WebSocket Signaling Server
    - WebRTC Gateway runtime
- Handles graceful shutdown (SIGINT / SIGTERM)
- This file should NOT contain business logic
"""