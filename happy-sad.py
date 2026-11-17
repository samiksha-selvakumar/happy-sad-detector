
sentence = input("Enter a sentence: ")

if "happy" in sentence.lower() or "good" in sentence.lower():
    print("The sentence is Happy")
elif "sad" in sentence.lower() or "bad" in sentence.lower():
    print("The sentence is Sad")
else:
    print("Not sure about the sentence")