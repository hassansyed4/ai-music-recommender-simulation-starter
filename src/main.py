"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

import csv
from typing import List, Dict
from src.recommender import load_songs, recommend_songs


def load_songs(csv_path: str) -> List[Dict]:
    """Load songs from CSV and return a list of dictionaries."""
    songs = []
    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            songs.append({
                "id": int(row["id"]),
                "title": row["title"],
                "artist": row["artist"],
                "genre": row["genre"],
                "mood": row["mood"],
                "energy": float(row["energy"]),
                "tempo_bpm": float(row["tempo_bpm"]),
                "valence": float(row["valence"]),
                "danceability": float(row["danceability"]),
                "acousticness": float(row["acousticness"]),
            })
    return songs

def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"Loaded songs: {len(songs)}")

    user_profile = {
        "favorite_genres": ["pop", "indie pop"],
        "favorite_moods": ["happy", "energetic"],
        "target_energy": 0.8,
        "target_tempo_bpm": 120
    }

    recommendations = recommend_songs(user_profile, songs, k=5)

    print("\nTop recommendations:\n")
    for song, score, explanation in recommendations:
        print(f"{song['title']} by {song['artist']}")
        print(f"Score: {score:.2f}")
        print(f"Reasons: {explanation}")
        print("-" * 40)


if __name__ == "__main__":
    main()
