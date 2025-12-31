"""
Roadmap:
- Custom VideoStreamTrack implementation
- Receives frames from Stream Hub (via ZMQ)
- Converts frames to WebRTC-compatible format
- Handles:
    - frame pacing
    - timestamping
    - synchronization with metadata
- Must never block the event loop
"""
