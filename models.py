# models.py
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, func
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Band(Base):
    __tablename__ = 'bands'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    hometown = Column(String, nullable=False)
    
    # Relationship with Concert
    concerts = relationship('Concert', back_populates='band')

    def venues(self):
        return {concert.venue for concert in self.concerts}

    @classmethod
    def most_performances(cls, session):
        band = session.query(cls, func.count().label('count')) \
                      .join(Concert) \
                      .group_by(cls.id) \
                      .order_by(func.count().desc()) \
                      .first()
        return band[0] if band else None

    def all_introductions(self):
        return [
            f"Hello {concert.venue.city}!!!!! We are {self.name} and we're from {self.hometown}"
            for concert in self.concerts
        ]

    def play_in_venue(self, venue, date, session):
        concert = Concert(date=date, band_id=self.id, venue_id=venue.id)
        session.add(concert)
        session.commit()


class Venue(Base):
    __tablename__ = 'venues'
    
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    city = Column(String, nullable=False)
    
    # Relationship with Concert
    concerts = relationship('Concert', back_populates='venue')

    def bands(self):
        return {concert.band for concert in self.concerts}

    def concert_on(self, date):
        return next((concert for concert in self.concerts if concert.date == date), None)

    def most_frequent_band(self, session):
        band = session.query(Band, func.count().label('count')) \
                      .join(Concert) \
                      .filter(Concert.venue_id == self.id) \
                      .group_by(Band.id) \
                      .order_by(func.count().desc()) \
                      .first()
        return band[0] if band else None


class Concert(Base):
    __tablename__ = 'concerts'
    
    id = Column(Integer, primary_key=True)
    date = Column(String, nullable=False)
    band_id = Column(Integer, ForeignKey('bands.id'))
    venue_id = Column(Integer, ForeignKey('venues.id'))
    
    band = relationship('Band', back_populates='concerts')
    venue = relationship('Venue', back_populates='concerts')

    def hometown_show(self):
        return self.band.hometown == self.venue.city

    def introduction(self):
        return f"Hello {self.venue.city}!!!!! We are {self.band.name} and we're from {self.band.hometown}"
