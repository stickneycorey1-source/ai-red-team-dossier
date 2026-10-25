from pydantic import BaseModel, Field, field_validator
from typing import List, Optional

class IdentityProfile(BaseModel):
    full_name: str
    birth_timestamp: Optional[str] = None
    birth_place: Optional[str] = None
    current_location: Optional[str] = None
    secondary_education: Optional[str] = None
    jurisdictional_focus: List[str] = Field(default_factory=list)
    artist_persona: Optional[str] = None

    @field_validator("jurisdictional_focus", mode="before")
    @classmethod
    def sanitize_jurisdictions(cls, value: List[str]) -> List[str]:
        return [v.strip() for v in value if v and v.strip()]
