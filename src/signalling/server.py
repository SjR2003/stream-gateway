"""
Roadmap:
- WebSocket signaling server for WebRTC
- Responsibilities:
    - Accept UI connections
    - Manage peer lifecycle (connect / disconnect)
    - Relay:
        - SDP offers
        - SDP answers
        - ICE candidates
- Does NOT handle media or data itself
- Only transports signaling messages
"""
