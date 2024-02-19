import json, os, random, string

FOLDERS = ['react-latest', 'react-legacy']
NUM_DATA_POINTS = 10000
HOBBIES = [
    'swimming',
    'running',
    'cycling',
    'hiking',
    'reading',
    'writing',
    'cooking',
    'baking',
    'gardening',
    'painting',
    'drawing',
    'knitting',
    'sewing',
    'woodworking',
    'metalworking',
    'pottery',
    'sculpting',
    'photography',
    'videography',
    'music',
    'singing',
    'dancing',
    'acting',
    'yoga',
    'pilates',
    'boxing',
    'martial arts',
    'meditation',
]

def populate_data(data, folder: str):
    current_dir = os.path.dirname(os.path.realpath(__file__))
    data_file = os.path.join(current_dir, folder, 'src', 'data.json')

    with open(data_file, 'w') as f:
        json.dump(data, f)

if __name__ == '__main__':
    data = [
        {
            'id': random.randint(1, 100),
            'name': ''.join(random.choice(string.ascii_uppercase) for _ in range(48)),
            'age': random.randint(1, 100),
            'hobbies': random.sample(HOBBIES, random.randint(len(HOBBIES) // 2, len(HOBBIES)))
        } for _ in range(NUM_DATA_POINTS)
    ]

    for folder in FOLDERS:
        populate_data(data, folder)