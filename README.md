# 🎵 Music Recommender Simulation

## Project Summary

This project implements a simple music recommender system that scores songs based on user preferences for genre, mood, energy level, and tempo. The system uses a weighted scoring approach where exact matches for genre and mood provide high points, while closeness to preferred energy and tempo levels provides additional points. Songs are ranked by their total score, and the top recommendations are returned with explanations for why they were chosen. This simulation demonstrates how content-based filtering can work for music recommendations, focusing on transparency and simplicity over complex algorithms.

---

user_profile = {
    "favorite_genre": "pop",
    "favorite_mood": "happy",
    "target_energy": 0.8,
    "target_tempo": 120,
    "likes_acoustic": False
}

## How The System Works

Real-world recommenders combine many signals at scale: what a user has liked before, what similar users are listening to, and the content features of each song. In this simulation, the focus is narrower: we prioritize content similarity by matching a user’s preferred genre and mood exactly, then score candidates by how close their energy and tempo are to the user’s taste.

- `Song` features used:
  - `genre`
  - `mood`
  - `energy`
  - `tempo_bpm`
- `UserProfile` information:
  - preferred `genre` (single)
  - preferred `mood` (single)
  - target `energy`
  - target `tempo`
  - `likes_acoustic` (not currently used in scoring)
- Scoring approach:
  - Exact match for `genre`: +10 points
  - Exact match for `mood`: +10 points
  - Energy closeness: (1 - |song.energy - user.target_energy|) * 5 points (0-5 range)
  - Tempo closeness: max(0, 1 - |song.tempo_bpm - user.target_tempo| / 100) * 5 points (0-5 range, normalized by 100 BPM)
- Recommendation selection:
  - Rank songs by total score (descending) and return the highest-ranking matches
  - Provide explanations for recommendations based on matching criteria

### Data Flow Visualization

<img width="595" height="647" alt="image" src="https://github.com/user-attachments/assets/f95bf03d-df1f-43b8-957c-867c9e575308" />


### Potential Biases

This system might over-prioritize exact genre and mood matches, potentially ignoring songs that are close in style but don't match exactly. The small dataset (18 songs) limits diversity and may not represent all musical tastes fairly. Users with niche preferences might find fewer good matches.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Experiments You Tried

- Implemented a weighted scoring system with 10 points for exact genre/mood matches and up to 5 points each for energy and tempo closeness
- Tested with a user preferring pop genre, happy mood, 0.8 energy, and 120 BPM tempo - the system correctly ranked songs with matching genre/mood highest, followed by those with close energy/tempo
- Verified that the scoring is transparent and explainable, with each recommendation including reasons for the score

---

## Limitations and Risks

- The system only works with a small catalog of 18 songs, limiting diversity and discovery
- It requires exact matches for genre and mood, which may be too strict and miss similar songs (e.g., "indie pop" vs "pop")
- The scoring doesn't account for user history, collaborative filtering, or other features like lyrics, artist popularity, or acoustic preference
- There's a risk of bias toward songs that match multiple criteria, potentially creating filter bubbles
- The tempo closeness normalization (100 BPM) is arbitrary and may not work well for all music styles

---

## Reflection

Building this recommender taught me how AI systems turn user preferences into predictions through weighted scoring and ranking. By assigning different point values to matching criteria, the system creates a simple decision-making process that's transparent and easy to understand. However, it also highlighted the challenges of balancing multiple factors - giving too much weight to exact matches can make the system rigid, while overemphasizing closeness scores might lead to generic recommendations.

Bias and unfairness could emerge in several ways: the dataset might not represent diverse musical tastes or cultures, the exact matching approach could disadvantage users with niche preferences, and the lack of diversity controls might always recommend similar songs. In real-world systems, these issues are amplified by scale and could lead to echo chambers where users only discover music that reinforces their existing tastes, potentially limiting cultural exposure and discovery.


---

## 7. `model_card_template.md`

Combines reflection and model card framing from the Module 3 guidance. :contentReference[oaicite:2]{index=2}  

```markdown
# 🎧 Model Card - Music Recommender Simulation

## 1. Model Name

Give your recommender a name, for example:

> VibeFinder 1.0

---

## 2. Intended Use

- What is this system trying to do
- Who is it for

Example:

> This model suggests 3 to 5 songs from a small catalog based on a user's preferred genre, mood, and energy level. It is for classroom exploration only, not for real users.

---

## 3. How It Works (Short Explanation)

Describe your scoring logic in plain language.

- What features of each song does it consider
- What information about the user does it use
- How does it turn those into a number

Try to avoid code in this section, treat it like an explanation to a non programmer.

---

## 4. Data

Describe your dataset.

- How many songs are in `data/songs.csv`
- Did you add or remove any songs
- What kinds of genres or moods are represented
- Whose taste does this data mostly reflect

---

## 5. Strengths

Where does your recommender work well

You can think about:
- Situations where the top results "felt right"
- Particular user profiles it served well
- Simplicity or transparency benefits

---

## 6. Limitations and Bias

Where does your recommender struggle

Some prompts:
- Does it ignore some genres or moods
- Does it treat all users as if they have the same taste shape
- Is it biased toward high energy or one genre by default
- How could this be unfair if used in a real product

---

## 7. Evaluation

How did you check your system

Examples:
- You tried multiple user profiles and wrote down whether the results matched your expectations
- You compared your simulation to what a real app like Spotify or YouTube tends to recommend
- You wrote tests for your scoring logic

You do not need a numeric metric, but if you used one, explain what it measures.

---

## 8. Future Work

If you had more time, how would you improve this recommender

Examples:

- Add support for multiple users and "group vibe" recommendations
- Balance diversity of songs instead of always picking the closest match
- Use more features, like tempo ranges or lyric themes

---

## 9. Personal Reflection

A few sentences about what you learned:

- What surprised you about how your system behaved
- How did building this change how you think about real music recommenders
- Where do you think human judgment still matters, even if the model seems "smart"

## CLI Output

Here is the terminal output of my recommender simulation:

<img width="704" height="376" alt="image" src="https://github.com/user-attachments/assets/021d73bb-0a06-4f04-bddd-a53c156f9f55" />


## Evaluation Results

### High-Energy Pop Profile
This profile prefers energetic and upbeat songs.

<img width="707" height="395" alt="image" src="https://github.com/user-attachments/assets/541ed27d-817a-41d4-ae51-842160c0f02e" />

---

### Chill Lofi Profile
This profile prefers calm, low-energy, and slower tempo songs.

<img width="695" height="399" alt="image" src="https://github.com/user-attachments/assets/716a9db5-46ee-4490-a153-dbd469264917" />

---

### Deep Intense Rock Profile
This profile prefers intense, high-energy rock music.

<img width="696" height="394" alt="image" src="https://github.com/user-attachments/assets/835d8448-d4c3-44c4-8774-5eb64b243f5b" />

---

### Conflicting Metal Calm Profile (Edge Case)
This profile combines conflicting preferences: metal genre with calm mood and very low energy.

<img width="563" height="387" alt="image" src="https://github.com/user-attachments/assets/2fc37f6b-4aa0-455e-bf57-bcb2ecfb9a68" />
