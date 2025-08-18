from ninja import Schema
from datetime import datetime, timedelta
from pydantic import EmailStr


class WaitlistEntryCreateSchema(Schema):
    # Create -> Data
    # WaitlistEntryIn
    email: EmailStr


class WaitlistEntryListSchema(Schema):
    # List -> Data
    # WaitlistEntryOut
    id: int
    email: EmailStr


class WaitlistEntryDetailSchema(Schema):
    # Get -> Data
    # WaitlistEntryOut
    id: int
    email: EmailStr
    timestamp: datetime  # ISO 8601 format, e.g., "2023-10-01T12:00:00Z