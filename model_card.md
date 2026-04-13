# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

**TuneMatch Recommender**

---

## 2. Intended Use  

This model generates personalized music recommendations by scoring songs based on how well they match a user's stated preferences for genre, mood, energy level, and tempo. It assumes users have clear preferences for one specific genre and mood, along with target energy and tempo levels. This is designed for classroom exploration and learning about recommendation systems, not for production use with real users.

---

## 3. How the Model Works  

The model looks at each song's genre, mood, energy level, and tempo. For a user's preferences, it checks if the song's genre and mood exactly match what the user likes, giving 10 points for each match. Then it measures how close the song's energy and tempo are to what the user wants - the closer they are, the more points (up to 5 each). Songs get ranked by their total points, with the highest scoring ones recommended. I added tempo matching and made the scoring more structured compared to the starter code.

---

## 4. Data  

The dataset contains 18 songs from various genres including pop, lofi, rock, jazz, and others. Moods range from happy and chill to intense and romantic. The data includes numerical features like energy (0-1 scale) and tempo (BPM). I didn't add or remove songs from the original CSV. The dataset might miss some musical dimensions like lyrics, cultural context, or user listening history.

---

## 5. Strengths  

The system works well for users with clear, specific preferences who want songs that closely match their stated criteria. It correctly prioritizes exact genre and mood matches while still considering energy and tempo closeness. The scoring is transparent and easy to understand, making it good for educational purposes. It performed well in tests with users preferring pop/happy music with moderate energy and tempo around 120 BPM.  

---

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

Building this recommender showed me how simple weighted scoring can create effective recommendations when the criteria are well-chosen. I was surprised by how much the exact genre/mood matches dominated the rankings, teaching me about the importance of balancing different scoring components. This experience made me appreciate how real music apps like Spotify must handle much more complex user data and preferences to provide personalized recommendations.

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
