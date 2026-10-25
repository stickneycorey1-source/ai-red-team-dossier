#!/usr/bin/env python3
"""
Dr. Lucid Studio & Audio Production Engine
Author: Corey Allen Stickney (corey-allen-stickney)
Artist Persona: Dr. Lucid / Lucid Truth
Description: Manages high-tempo trap instrumental specs, vocal tracking 
             parameters, and BandLab audio production metadata.
"""

import json
from dataclasses import dataclass, field
from pathlib import Path
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
    def __init__(self, config: StudioSessionConfig = None, sessions_path: str = "studio/studio_sessions.json"):
        self.config = config or StudioSessionConfig()
        self.sessions_path = Path(sessions_path)
        self.session_logs: List[Dict[str, Any]] = self._load_sessions()

    def _load_sessions(self) -> List[Dict[str, Any]]:
        """Loads track sessions from the local JSON ledger if available."""
        if self.sessions_path.exists():
            try:
                with open(self.sessions_path, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception:
                return []
        return []

    def print_studio_specs(self) -> None:
        """Prints the master production profile and loaded track ledger for Dr. Lucid."""
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
        print("-" * 60)
        print(f" Loaded Track Ledger ({len(self.session_logs)} tracks found):")
        for session in self.session_logs:
            print(f"   * [{session.get('trackId')}] {session.get('title')} — {session.get('tempo')} ({session.get('key')}) | Status: {session.get('status')}")
        print("="*60)

if __name__ == "__main__":
    engine = StudioEngine()
    engine.print_studio_specs()
