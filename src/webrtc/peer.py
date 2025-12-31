"""
Roadmap:
- Wraps RTCPeerConnection
- Abstracts WebRTC complexity behind a clean API
- Responsibilities:
    - Create offer / answer
    - Handle ICE candidates
    - Attach media tracks
    - Attach data channels
    - Track connection state
- One instance = one UI peer
"""
