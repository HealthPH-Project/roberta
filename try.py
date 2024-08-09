import roBERTa as rb

# Test the prediction function
sample_text = "will this work out?"
prediction = rb.predict(sample_text)
print(f"Prediction for '{sample_text}': {prediction}")