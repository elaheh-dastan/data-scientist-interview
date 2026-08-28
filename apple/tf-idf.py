# TFIDF (term frequency * inverse document frequency) is a weighting scheme
# for terms in documents, or in our case, tags for songs.

# TF for tag t in song s is defined as:
# number of times t appears in s / total number of tags in s

# However, in our case, each tag can appear only once per song, so:
# 1 / total number of tags in s

# IDF for tag t is defined as:
# log ( total number of songs / number of songs containing t )

# Finally, TFIDF = TF * IDF

# Given a file of song IDs and their tags, like:

# 1 electronic house
# 2 rock metal spanish
# 3 jungle drum&bass
# 4 pop r&b soul
# ...

# write a short program that prints out the TFIDF weighted tags, like:

# 1 electronic:0.66 house:0.82
# 2 rock:0.51 metal:0.49 spanish:1.35
# 3 jungle:1.06 drum&bass:0.72
# 4 pop:0.15 r&b:0.21 soul:0.36
# ...

# The file is called /home/coderpad/data/song_tag_assignments
import math

data_file_path = "/home/coderpad/data/song_tag_assignments"


def load_songs(path: str) -> dict[str, list[str]]:
    songs = {}
    with open(path) as f:
        for line in f:
            song_id, *tags = line.split()
            songs[song_id] = tags
    return songs


def compute_tfidf(songs: dict[str, list[str]]) -> dict[str, dict[str, float]]:
    # number of songs each tag appears in, O(n*m)
    document_frequency: dict[str, int] = {}
    for tags in songs.values():
        for tag in set(tags):
            document_frequency[tag] = document_frequency.get(tag, 0) + 1

    num_songs = len(songs)

    # TF and TFIDF per song, O(n*m)
    tfidf: dict[str, dict[str, float]] = {}
    for song_id, tags in songs.items():
        term_frequency: dict[str, float] = {}
        for tag in tags:
            term_frequency[tag] = term_frequency.get(tag, 0) + 1 / len(tags)

        tfidf[song_id] = {
            tag: tf * math.log(num_songs / document_frequency[tag])
            for tag, tf in term_frequency.items()
        }

    return tfidf


if __name__ == "__main__":
    songs = load_songs(data_file_path)
    for song_id, weights in compute_tfidf(songs).items():
        weighted_tags = " ".join(f"{tag}:{weight:.2f}" for tag, weight in weights.items())
        print(f"{song_id} {weighted_tags}")
