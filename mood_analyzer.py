class MoodAnalyzer:
    def __init__(self):
        self.positive_words = ["love", "great", "happy", "good", "proud", "fun", "amazing", "nice", "well", "best", "win", "joy", "excited"]
        self.negative_words = ["hate", "terrible", "bad", "awful", "done", "annoyed", "sad", "worst", "angry", "exhausted", "wrong", "ugh"]

    def preprocess(self, text):
        text = text.lower()
        tokens = text.split()
        return tokens

    def score_text(self, tokens):
        score = 0
        negation = False
        for token in tokens:
            if token in ["not", "never", "no", "don't", "didn't"]:
                negation = True
                continue
            if token in self.positive_words:
                score += -1 if negation else 1
            elif token in self.negative_words:
                score += 1 if negation else -1
            negation = False
        return score

    def predict_label(self, score):
        if score >= 2:
            return "positive"
        elif score <= -2:
            return "negative"
        elif score == 0:
            return "neutral"
        else:
            return "mixed"

    def analyze(self, text):
        tokens = self.preprocess(text)
        score = self.score_text(tokens)
        return self.predict_label(score)
