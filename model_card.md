# 🎧 Model Card - Music Recommender Simulation

## 1. Model Name

TuneMatch Recommender 1.0

---

## 2. Goal / Task

This system recommends songs based on a user's music preferences.  
It tries to predict which songs a user might like by comparing their taste profile with song features.

---

## 3. Data Used

The dataset contains 18 songs with features such as genre, mood, energy, and tempo.  
The dataset is small and does not cover all music styles, which limits the variety of recommendations.

---

## 4. Algorithm Summary

Each song is given a score based on how well it matches the user's preferences.

- Songs get points if their genre matches the user's favorite genres  
- Songs get points if their mood matches the user's preferred moods  
- Additional points are given when the song's energy and tempo are close to the user's target values  

All songs are scored and then ranked from highest to lowest.  
The top songs are recommended to the user.

---

## 5. Observed Behavior / Biases

The system tends to favor songs with similar energy and tempo, even if the genre does not match.  
For example, some songs appeared in multiple profiles because their numerical features were close.  

The system also struggles with conflicting preferences, such as a "metal + calm + low energy" profile.  
In such cases, it produces unexpected results.

Because the dataset is small, some genres are underrepresented, which can create bias in recommendations.

---

## 6. Evaluation Process

The system was tested using multiple user profiles:

- High-Energy Pop  
- Chill Lofi  
- Deep Intense Rock  
- Conflicting Metal Calm (edge case)  

Each profile produced different results based on genre, mood, energy, and tempo.  

An experiment was also performed by adjusting scoring weights, which showed that changing weights can significantly affect recommendations.

---

## 7. Intended Use and Non-Intended Use

**Intended Use:**
- Educational demonstration of how recommendation systems work  
- Simple simulation of content-based filtering  

**Non-Intended Use:**
- Not suitable for real-world music platforms  
- Should not be used for production-level recommendations  
- Does not handle large-scale user behavior or personalization  

---

## 8. Ideas for Improvement

- Add more songs to improve recommendation variety  
- Introduce learning from user feedback (likes/dislikes)  
- Balance scoring weights to avoid over-reliance on energy and tempo  
- Include more features like artist similarity or lyrics  

---

## 9. Personal Reflection

**Biggest Learning Moment:** My biggest learning moment was realizing how sensitive recommendation systems are to scoring weights. When I doubled energy importance and halved genre importance in an experiment, the entire ranking changed dramatically. This taught me that even small parameter tweaks can create very different user experiences, and real systems need careful tuning.

**How AI Tools Helped:** AI tools like GitHub Copilot were incredibly helpful for generating initial code structures, writing docstrings, and creating Mermaid diagrams. They sped up implementation by suggesting scoring logic and test cases. However, I had to double-check suggestions when they didn't match my design - for example, ensuring the scoring math was correct and the class structure aligned with the requirements.

**Surprise About Simple Algorithms:** I was surprised that such a simple algorithm could feel like a real recommender. Just matching genres/moods and comparing energy/tempo created rankings that actually made sense to users. It showed me how even basic rules can simulate complex behavior when the data and weights are reasonable.

**What I'd Try Next:** If I extended this project, I'd implement user feedback learning - allowing the system to adapt weights based on what users actually like/dislike. I'd also add collaborative filtering by comparing user profiles to find similar taste patterns, and incorporate more song features like lyrics themes or artist similarity to make recommendations more nuanced.

## 6. Limitations and Bias 

The system doesn't consider lyrics, artist popularity, user listening history, or collaborative filtering. It requires exact genre and mood matches, which might miss similar but not identical categories. The small dataset (18 songs) limits diversity and may not represent all musical tastes. The scoring could bias toward songs that match multiple criteria, creating filter bubbles. Users with niche or multiple preferences aren't well served by the single genre/mood approach.  

---

## 7. Evaluation  

I tested with a user profile preferring pop genre, happy mood, 0.8 energy, and 120 BPM tempo. The system correctly ranked "Sunrise City" (pop, happy, close energy/tempo) as the top recommendation. I ran the provided unit tests, which check that songs are sorted by score and explanations are generated. I was surprised by how well the closeness scoring worked for energy and tempo, providing nuanced rankings beyond just exact matches.

---

## 8. Future Work  

I would add support for multiple preferred genres and moods, incorporate user listening history, and include diversity controls to avoid recommending too many similar songs. Better explanations could highlight why certain songs scored lower. Adding features like lyrics analysis or acoustic preference usage would make it more comprehensive. Handling tempo ranges instead of exact targets could improve flexibility.  

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  
