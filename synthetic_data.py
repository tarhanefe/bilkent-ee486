from nltk.corpus import wordnet
from random import choice, randint
import random
import openai
import csv
openai.api_key = "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"  

features = ["5_o_Clock_Shadow","Arched_Eyebrows","Attractive","Bags_Under_Eyes","Bald", "Bangs","Big_Lips","Big_Nose",
            "Black_Hair","Blond_Hair","Blurry","Brown_Hair","Bushy_Eyebrows","Chubby","Double_Chin","Eyeglasses","Goatee",
            "Gray_Hair", "Heavy_Makeup","High_Cheekbones","Male","Mouth_Slightly_Open","Mustache","Narrow_Eyes","No_Beard",
            "Oval_Face","Pale_Skin","Pointy_Nose","Receding_Hairline","Rosy_Cheeks","Sideburns","Smiling","Straight_Hair",
            "Wavy_Hair","Wearing_Earrings","Wearing_Hat","Wearing_Lipstick","Wearing_Necklace","Wearing_Necktie","Young"]

def get_synonyms(word):
    synonyms = set()
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonyms.add(lemma.name())
    return list(synonyms)

def generate_sentence_template():
    num_features = random.randint(3, 5)  # choose a random number of features
    chosen_features = random.sample(features, num_features)  # choose random features

    prompt = "Generate a single sentence template describing a person with unique sentences with the following features: "
    prompt += ", ".join(chosen_features) + "."
    prompt += "Dont just write features next to each other as it is. Use a unique sentence structure and with different types of expressions. You may sometimes use synonyms."

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=50,
        top_p=0.9,
        n=1
    )

    template = response.choices[0].text.strip()
    return template, chosen_features

output_file = "sentences.csv"

with open(output_file, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["sentence"] + features)
    count = 0
    for _ in range(3000):  
        count +=1
        template, chosen_features = generate_sentence_template()
        feature_synonyms = {}
        for feature in chosen_features:
            synonyms = get_synonyms(feature)
            if synonyms:
                feature_synonyms[feature] = synonyms
        sentence = template
        feature_values = []
        for feature in features:
            if feature in chosen_features:
                value = 1
            else:
                value = 0
            feature_values.append(value)

        writer.writerow([sentence] + feature_values)
        print("Sentence {} completed".format(count))
