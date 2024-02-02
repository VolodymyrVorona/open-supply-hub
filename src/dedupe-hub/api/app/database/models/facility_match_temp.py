from app.database.sqlalchemy import Base
from sqlalchemy import TIMESTAMP, Column, String, Boolean, Integer, DECIMAL, ForeignKey
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.sql import func

class FacilityMatchTemp(Base):

    PENDING = 'PENDING'
    AUTOMATIC = 'AUTOMATIC'
    CONFIRMED = 'CONFIRMED'
    REJECTED = 'REJECTED'
    MERGED = 'MERGED'

    __tablename__ = 'api_facilitymatchtemp'

    id = Column(Integer, primary_key=True)
    facility_list_item_id = Column(Integer, ForeignKey('api_facilitylistitem.id'), nullable=False)
    facility_id = Column(String, nullable=True)
    results = Column(JSONB)
    confidence = Column(DECIMAL, nullable=False, default=0.0)
    status = Column(String, nullable=False, default='PENDING')
    is_active = Column(Boolean, nullable=False, default=True)
    version = Column(String, nullable=True)
    created_at = Column(TIMESTAMP(timezone=True),
                       nullable=False, default=func.now(), server_default=func.now())
    updated_at = Column(TIMESTAMP(timezone=True),
                       default=None, onupdate=func.now())