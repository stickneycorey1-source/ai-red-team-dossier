#!/usr/bin/env python3
"""
Dr. Lucid Studio & Audio Production Engine
Author: Corey Allen Stickney (corey-allen-stickney)
Artist Persona: Dr. Lucid / Lucid Truth
Description: Manages high-tempo trap instrumental specs, vocal tracking 
             parameters, and BandLab audio production metadata.
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, List, Any

@dataclass
class StudioSessionConfig:
    artist_moniker: str = "Dr. Lucid (Lucid Truth)"
    target_bpm: int = 165
    bpm_range: str = "150-180 BPM"
    primary_key: str = "D Minor"
    instrumental_style: str = "Dark acoustic/electric guitar loops, heavy 808 sub-bass, rapid hi-hat rolls"
    daw_platform: str = "BandLab Pro"
    active_vocal_techniques: List[str] = field(default_factory=lambda: [
        "Head register control",
        "Cadence & tone modulation",
        "Vocal percussion layering",
        "Fast-flow triple-stack rhythmics"
    ])

class StudioEngine:
    def __init__(self, config: StudioSessionConfig = None):
        self.config = config or StudioSessionConfig()
        self.session_logs: List[Dict[str, Any]] = []

    def log_recording_session(self, track_title: str, notes: str) -> Dict[str, Any]:
        """Logs a studio tracking session with production specs."""
        session_entry = {
            "timestamp": datetime.now().isoformat(),
            "artist": self.config.artist_moniker,
            "track_title": track_title,
            "tempo": f"{self.config.target_bpm} BPM ({self.config.primary_key})",
            "daw": self.config.daw_platform,
            "notes": notes
        }
        self.session_logs.append(session_entry)
        return session_entry

    def print_studio_specs(self) -> None:
        """Prints the master production profile for Dr. Lucid."""
        print("="*60)
        print(f" DR. LUCID STUDIO PRODUCTION ENGINE — MASTER PROFILE")
        print("="*60)
        print(f" Artist Persona      : {self.config.artist_moniker}")
        print(f" Target Tempo        : {self.config.target_bpm} BPM (Range: {self.config.bpm_range})")
        print(f" Harmonic Key        : {self.config.primary_key}")
        print(f" Instrumental DNA    : {self.config.instrumental_style}")
        print(f" DAW Environment     : {self.config.daw_platform}")
        print(f" Active Techniques   :")
        for tech in self.config.active_vocal_techniques:
            print(f"   - {tech}")
        print("="*60)

if __name__ == "__main__":
    engine = StudioEngine()
    engine.print_studio_specs()
    
    # Example session log test
    test_session = engine.log_recording_session(
        track_title="PHANTOM VOLTAGE",
        notes="High-energy triple-stack verse tracking with rapid hi-hat synchronization."
    )
    print(f"\n[Session Logged Successfully]")
    print(f" Track : {test_session['track_title']}")
    print(f" Tempo : {test_session['tempo']}")
    print(f" Notes : {test_session['notes']}")
    print("="*60)
