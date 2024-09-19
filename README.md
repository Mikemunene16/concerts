# Concerts Challenge

## Overview

This project involves managing a Concert domain with three primary entities: `Band`, `Venue`, and `Concert`. The relationships between these entities are as follows:

- A `Band` can have many `Concerts`.
- A `Venue` can host many `Concerts`.
- A `Concert` is associated with one `Band` and one `Venue`.

The project uses SQLAlchemy for ORM and Alembic for database migrations.

## Project Structure

- `models.py`: Contains SQLAlchemy model definitions for `Band`, `Venue`, and `Concert`.
- `app.py`: Contains the code to create and query instances of `Band`, `Venue`, and `Concert`.
- `migrations/`: Contains migration scripts generated by Alembic.

## Setup

### Prerequisites

- Python 3.x
- Virtual environment (recommended)
- SQLAlchemy
- Alembic

### Installation

1. **Clone the Repository**

   ```sh
   git clone [https://github.com/Mikemunene16/concerts]
   cd concerts-challenge
   ```

2. **Create and Activate Virtual Environment**

   ```sh
   python -m venv .venv
   source .venv/bin/activate 
   ```

3. **Install Dependencies**

   ```sh
   pip install sqlalchemy alembic
   ```

4. **Initialize Alembic**

   Run the following command to initialize Alembic, if you haven't done so:

   ```sh
   alembic init migrations
   ```

5. **Set Up Database**

   Run the following command to create the database schema:

   ```sh
   alembic upgrade head
   ```

## Usage

1. **Run the Application**

   Run `app.py` to test the functionality.

   ```sh
   python app.py
   ```

3. **Run Tests**

   Press run python file button in vs code to run test data
 ```

## Methods and Usage

### `Band` Methods

- **`Band.concerts()`**: Returns a collection of all concerts the band has played.
- **`Band.venues()`**: Returns a collection of all venues where the band has performed.
- **`Band.play_in_venue(venue, date)`**: Creates a new concert for the band in the specified venue on the given date.
- **`Band.all_introductions()`**: Returns an array of strings representing all introductions for the band.
- **`Band.most_performances()`**: Returns the band that has played the most concerts.

### `Venue` Methods

- **`Venue.concerts()`**: Returns a collection of all concerts held at the venue.
- **`Venue.bands()`**: Returns a collection of all bands that have performed at the venue.
- **`Venue.concert_on(date)`**: Finds and returns the first concert on the given date at the venue.
- **`Venue.most_frequent_band()`**: Returns the band with the most concerts at the venue.

### `Concert` Methods

- **`Concert.band()`**: Returns the `Band` instance for this concert.
- **`Concert.venue()`**: Returns the `Venue` instance for this concert.
- **`Concert.hometown_show()`**: Returns `True` if the concert is in the band's hometown, otherwise `False`.
- **`Concert.introduction()`**: Returns a string with the band's introduction for this concert.
