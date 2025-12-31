"""
Roadmap:
- Maintains signaling state machine per peer
- Tracks:
    - connection state (NEW, OFFER_SENT, CONNECTED, CLOSED)
    - peer role (gateway / ui)
    - pending SDP / ICE candidates
- Prevents invalid signaling transitions
- This is where WebRTC complexity is controlled
"""
