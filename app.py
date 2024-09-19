# app.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Band, Venue, Concert

# Create an engine and session
engine = create_engine('sqlite:///concerts.db')
Session = sessionmaker(bind=engine)
session = Session()

def test_methods():
    # Create instances of Band, Venue, and Concert
    rolling_stones = Band(name='The Rolling Stones', hometown='London')
    madison_square_garden = Venue(title='Madison Square Garden', city='New York')
    concert = Concert(date='2024-09-30', band=rolling_stones, venue=madison_square_garden)
    
    session.add(rolling_stones)
    session.add(madison_square_garden)
    session.add(concert)
    session.commit()

    # Test Band methods
    band = session.query(Band).first()
    print(f"Band: {band.name}")
    print("Concerts:")
    for concert in band.concerts: 
        print(f" - {concert.date} at {concert.venue.title}")

    # Test Venue methods
    venue = session.query(Venue).first()
    print(f"\nVenue: {venue.title}")
    print("Bands:")
    for band in venue.bands(): 
        print(f" - {band.name}")

if __name__ == '__main__':
    Base.metadata.create_all(engine)
    test_methods()
