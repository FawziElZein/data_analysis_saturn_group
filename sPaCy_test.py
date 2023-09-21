import spacy


nlp = spacy.load("en_core_web_sm")
nlp.add_pipe("sentiment")
def analyze_sentiment(text):
  
  doc = nlp(text)
  sentiment_scores = doc._.sentiment
  compound_score = sentiment_scores["compound"]

  if compound_score >= 0.05:
    sentiment = "positive"
  elif compound_score <= -0.05:
    sentiment = "negative"
  else:
    sentiment = "neutral"

  return sentiment, compound_score

texts = [
  "I love this product! It's amazing.",
  "This movie is terrible.",
  "The weather today is okay."
]

for text in texts:
  sentiment, compound_score = analyze_sentiment(text)
  print(f"Text: {text}")
  print(f"Sentiment: {sentiment} (Compound Score: {compound_score})")