from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    target_tempo: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def score_song(self, song: Song, user: UserProfile) -> float:
        """Calculate the recommendation score for a song based on user preferences."""
        score = 0.0
        # Genre match
        if song.genre == user.favorite_genre:
            score += 10
        # Mood match
        if song.mood == user.favorite_mood:
            score += 10
        # Energy closeness (0-5 points)
        energy_diff = abs(song.energy - user.target_energy)
        score += (1 - energy_diff) * 5
        # Tempo closeness (0-5 points, normalized by max diff of 100 bpm)
        tempo_diff = abs(song.tempo_bpm - user.target_tempo)
        tempo_closeness = max(0, 1 - tempo_diff / 100)
        score += tempo_closeness * 5
        return score

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        """Return the top k recommended songs for the user profile."""
        # Sort songs by score descending
        scored_songs = [(song, self.score_song(song, user)) for song in self.songs]
        scored_songs.sort(key=lambda x: x[1], reverse=True)
        return [song for song, _ in scored_songs[:k]]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        """Generate a human-readable explanation for why a song was recommended."""
        reasons = []
        if song.genre == user.favorite_genre:
            reasons.append(f"matches your favorite genre '{user.favorite_genre}'")
        if song.mood == user.favorite_mood:
            reasons.append(f"matches your favorite mood '{user.favorite_mood}'")
        energy_diff = abs(song.energy - user.target_energy)
        if energy_diff < 0.2:  # close enough
            reasons.append(f"has energy level close to your preference ({song.energy:.2f} vs {user.target_energy:.2f})")
        tempo_diff = abs(song.tempo_bpm - user.target_tempo)
        if tempo_diff < 20:  # close enough
            reasons.append(f"has tempo close to your preference ({song.tempo_bpm} vs {user.target_tempo})")
        if reasons:
            return f"This song is recommended because it {', '.join(reasons)}."
        else:
            return "This song is recommended based on overall suitability."

def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    # TODO: Implement CSV loading logic
    print(f"Loading songs from {csv_path}...")
    return []

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Score one song against a user profile and return score plus reasons."""
    score = 0.0
    reasons = []

    if song["genre"] in user_prefs["favorite_genres"]:
        score += 2.0
        reasons.append("genre match (+2.0)")

    if song["mood"] in user_prefs["favorite_moods"]:
        score += 1.0
        reasons.append("mood match (+1.0)")

    energy_diff = abs(song["energy"] - user_prefs["target_energy"])
    energy_score = max(0.0, 1.0 - energy_diff)
    score += energy_score
    reasons.append(f"energy closeness (+{energy_score:.2f})")

    tempo_diff = abs(song["tempo_bpm"] - user_prefs["target_tempo_bpm"])
    tempo_score = max(0.0, 1.0 - (tempo_diff / 100))
    score += tempo_score
    reasons.append(f"tempo closeness (+{tempo_score:.2f})")

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Return the top k recommended songs with score and explanation."""
    scored_results = []

    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = ", ".join(reasons)
        scored_results.append((song, score, explanation))

    ranked_results = sorted(scored_results, key=lambda x: x[1], reverse=True)
    return ranked_results[:k]
