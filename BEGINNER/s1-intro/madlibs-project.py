identifier = "@"
prompts = [
    "Proper Noun (Person's Name)",
    "Noun",
    "Adjective (feeling)",
    "Verb",
    "Adjective (feeling)",
    "Animal",
    "Adjective",
    "Verb",
    "Color",
    "Verb (ending with -ing)",
    "Adverb (ending with -ly)",
    "Number",
    "Unit of time",
    "Color",
    "Animal",
    "Number",
    "Silly word",
    "Noun"
]
sentences = [
    "This week I am going camping with @.",
    "I packed my lantern, sleeping bag, and @.", 
    "I am so @ to @ in a tent.",
    "I am @ we might see a @, they are kind of @. ",
    "We are going to hike, fish, and @. ",
    "I have heard that the @ lake is great for @. ",
    "Then we will @ hike through the forest for @ @. ",
    "If I see a @ @ while hiking, I am going to bring it home as a pet! ",
    "At night we will tell @ @ stories and roast @ around the campfire!",
]
newSentences = []
answers = []
for prompt in prompts:
    answers.append(input(prompt+": "))
print(answers)
answerIndex = 0
sentenceIndex = 0
for sentence in sentences:
    newSentence = ""
    for word in sentence.split(" "):
        if word.find("@") == -1: newSentence += word + " " # fail condition
        else:
            newSentence += word.replace("@", answers[answerIndex]) + " "
            answerIndex += 1 # next answer
    newSentences.append(newSentence)
    sentenceIndex += 1
print("".join(newSentences))