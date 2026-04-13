"""
Command line runner for the Music Recommender Simulation.
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
    print(f"Loaded songs: {len(songs)}\n")

    profiles = {
        "High-Energy Pop": {
            "favorite_genres": ["pop", "indie pop"],
            "favorite_moods": ["happy", "energetic"],
            "target_energy": 0.8,
            "target_tempo_bpm": 120
        },
        "Chill Lofi": {
            "favorite_genres": ["lofi", "acoustic"],
            "favorite_moods": ["calm", "chill"],
            "target_energy": 0.3,
            "target_tempo_bpm": 85
        },
        "Deep Intense Rock": {
            "favorite_genres": ["rock", "alternative"],
            "favorite_moods": ["intense", "dark"],
            "target_energy": 0.9,
            "target_tempo_bpm": 140
        },
        "Conflicting Metal Calm": {
            "favorite_genres": ["metal"],
            "favorite_moods": ["calm"],
            "target_energy": 0.1,
            "target_tempo_bpm": 50
        }
    }

    # ✅ LOOP INSIDE MAIN
    for profile_name, user_profile in profiles.items():
        print("=" * 60)
        print(f"Profile: {profile_name}")
        print("=" * 60)

        recommendations = recommend_songs(user_profile, songs, k=5)

        for song, score, explanation in recommendations:
            print(f"{song['title']} by {song['artist']}")
            print(f"Score: {score:.2f}")
            print(f"Reasons: {explanation}")
            print("-" * 40)

        print()


if __name__ == "__main__":
    main()