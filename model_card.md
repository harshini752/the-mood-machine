# Model Card: Mood Machine

## 1. Model Overview
**Model type:**
I used and compared both the rule-based model and the ML model.

**Intended purpose:**
To classify short social media style text posts as positive, negative, 
neutral, mixed, or sarcasm.

**How it works (brief):**
The rule-based model assigns a score to each post by checking words 
against positive and negative word lists. It also handles negation 
(e.g. "not bad" → positive). The ML model uses scikit-learn and learns 
patterns automatically from labeled examples using bag of words.

## 2. Data
**Dataset description:**
The dataset contains 20 posts in SAMPLE_POSTS. The original dataset had 
10 posts and I added 10 new ones including slang, emojis, and sarcasm.

**Labeling process:**
Labels were chosen based on the overall tone of each post. Some posts 
were hard to label — for example "so tired but we finally did it!!" 
could be positive or mixed depending on interpretation.

**Important characteristics of your dataset:**
- Contains slang ("W day no cap", "this slaps")
- Includes sarcasm ("I love waiting in long lines 🙄")
- Some posts express mixed feelings ("so tired but we finally did it!!")
- Contains emojis (😭, 🥲, 💀)
- Short and ambiguous messages ("meh, nothing special")

**Possible issues with the dataset:**
The dataset is very small (20 posts). Some labels like "sarcasm" only 
appear a few times, making it imbalanced. The language is mostly 
informal English which may not represent all users.

## 3. How the Rule Based Model Works
**Your scoring rules:**
- Positive words (love, great, happy, proud, fun) add +1 to score
- Negative words (hate, bad, awful, annoyed, sad) subtract -1 from score
- Negation words (not, never, don't) flip the next word's score
- Score >= 2 → positive, Score <= -2 → negative
- Score == 0 → neutral, anything else → mixed

**Strengths of this approach:**
- Easy to understand and explain every decision
- Works well for simple, clear sentences like "ugh I hate Mondays"
- Negation handling helps with phrases like "not bad"

**Weaknesses of this approach:**
- Cannot detect sarcasm ("I love being stuck in traffic" → mixed, 
  should be sarcasm)
- Does not understand slang ("that movie was sick" → neutral, 
  should be positive)
- Emojis are mostly ignored
- Only 30% accuracy on our dataset

## 4. How the ML Model Works
**Features used:**
Bag of words using CountVectorizer, which converts each post into 
word frequency counts.

**Training data:**
The model trained on SAMPLE_POSTS and TRUE_LABELS from dataset.py.

**Training behavior:**
Accuracy improved as more labeled examples were added. However the 
model shows 100% accuracy because it is tested on the same data it 
trained on, which means it likely memorized the answers rather than 
truly learning patterns.

**Strengths and weaknesses:**
Strengths: learns patterns automatically, handles sarcasm and slang 
better than rule-based. Weaknesses: overfits to training data, would 
likely fail on new unseen posts it has never seen before.

## 5. Evaluation
**How you evaluated the model:**
Both models were evaluated on the 20 labeled posts in dataset.py 
using accuracy score.

**Examples of correct predictions:**
- "ugh I hate Mondays" → negative ✅ (contains clear negative words)
- "could be worse I guess" → neutral ✅ (no strong positive or negative signal)
- "meh, nothing special" → neutral ✅ (flat, unenthusiastic tone)

**Examples of incorrect predictions:**
- "that movie was sick" → rule-based predicted neutral ❌ 
  because "sick" is not in the positive word list
- "I'm fine :)" → rule-based predicted neutral ❌ 
  because it cannot detect sarcasm from punctuation
- "W day no cap" → rule-based predicted neutral ❌ 
  because it doesn't understand Gen Z slang

## 6. Limitations
- Dataset is very small (20 posts), not enough to generalize well
- Rule-based model cannot detect sarcasm at all
- ML model overfits — 100% on training data but would likely fail 
  on new posts
- Slang and emojis are mostly not handled by the rule-based model
- Dataset is mostly informal English and may misinterpret other 
  dialects or languages

## 7. Ethical Considerations
- A mood classifier that misreads distress as neutral could fail 
  someone who needs help
- Sarcasm misclassification could lead to wrong conclusions about 
  how someone is feeling
- The dataset is biased toward Gen Z English slang, so it may 
  misinterpret posts from other age groups or cultures
- Using mood detection on personal messages raises serious privacy 
  concerns

## 8. Ideas for Improvement
- Add more labeled data (at least 100+ posts)
- Add an emoji dictionary to score emojis as positive or negative
- Add a sarcasm detection rule using context clues
- Use TF-IDF instead of CountVectorizer for better word weighting
- Create a separate test set to get a real accuracy score
- Add slang to the positive/negative word lists
