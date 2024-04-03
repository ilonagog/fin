from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Pet  # Assuming Pet model is defined in models.py

# SQLAlchemy database connection
engine = create_engine('sqlite:///pet_app.db')
Session = sessionmaker(bind=engine)

def seed_pets():
    # Create session
    session = Session()

    # Seed new pets
    pets = [
        Pet(name='Fluffy', species='Dog', breed='Golden Retriever', temperament='Friendly', owner_id=1),
        Pet(name='Whiskers', species='Cat', breed='Siamese', temperament='Independent', owner_id=2),
        # Add more pets as needed
    ]

    # Add pets to session
    session.add_all(pets)

    # Commit the session to save changes to the database
    session.commit()

    # Close session
    session.close()

if __name__ == '__main__':
    seed_pets()
