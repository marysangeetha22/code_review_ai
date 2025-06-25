import pandas as pd
from extract_features import extract_features_from_code  # Make sure this import path matches your file
from tqdm import tqdm

# Sample code snippets (good, bad, average)
examples = [
    {
        "code": '''def greet(name):\n    """Greet user"""\n    return "Hello " + name''',
        "score": 9
    },
    {
        "code": '''def add(x,y)\nreturn x+y''',
        "score": 3
    },
    {
        "code": '''def foo():\n    print("bar")\n    print("done")''',
        "score": 8
    },
    {
        "code": '''def bad():\nprint("oops")''',
        "score": 2
    },
    {
        "code": '''def area(radius):\n    return 3.14 * radius ** 2''',
        "score": 10
    },
    {
        "code": '''def __():\n    return 123''',
        "score": 4
    },
]

# Extract features
rows = []
for example in tqdm(examples):
    code = example["code"]
    score = example["score"]
    features = extract_features_from_code(code)
    features["score"] = score
    rows.append(features)

# Save to CSV
df = pd.DataFrame(rows)
df.to_csv("code_quality_dataset.csv", index=False)
print("✅ Dataset saved as code_quality_dataset.csv")
