# -*- coding: utf-8 -*-
"""
Find time window of Short segment in RV:
YouTube Shorts can have a clickable link on their interface that can redirect us to the start of a regular
video (RV) in case it links to one. Here we provide a code that given the transcript of both the RV and the Short,
it finds the longest segment of the Shorts that coincides with it. 
"""

import difflib

# Example transcripts (representing the RV transcript and the Short one (has slight modifications))
large_transcript = [
    {'text': 'Hey there', 'start': 7.58, 'duration': 6.13},
    {'text': 'how are you', 'start': 14.08, 'duration': 7.58},
    {'text': 'I am fine', 'start': 21.66, 'duration': 5.32},
    {'text': 'thanks for asking', 'start': 27.00, 'duration': 4.20},
    {'text': 'this is a large document with many sentences', 'start': 31.20, 'duration': 7.00},
    {'text': 'it contains various extracts from different sources', 'start': 38.20, 'duration': 6.50},
    {'text': 'this particular example is meant to demonstrate text comparison', 'start': 44.70, 'duration': 8.30},
    {'text': 'sometimes, texts are modified slightly and spread across multiple parts', 'start': 53.00, 'duration': 9.50},
    {'text': 'this makes the detection of original extracts more challenging', 'start': 62.50, 'duration': 7.50},
    {'text': 'additional sentences are here to provide more context', 'start': 70.00, 'duration': 6.50},
    {'text': 'each part of the document adds more information', 'start': 76.50, 'duration': 5.50},
    {'text': 'another sentence for good measure', 'start': 82.00, 'duration': 4.00},
    {'text': 'more sentences to simulate a longer document', 'start': 86.00, 'duration': 6.00},
    {'text': 'continuing to expand the document', 'start': 92.00, 'duration': 4.50},
    {'text': 'still more text to analyze', 'start': 96.50, 'duration': 4.00},
    {'text': 'even more sentences to ensure a thorough test', 'start': 100.50, 'duration': 6.00},
    {'text': 'sentences continue to be added', 'start': 106.50, 'duration': 5.00},
    {'text': 'testing with a substantial amount of text', 'start': 111.50, 'duration': 7.00},
    {'text': 'another line here', 'start': 118.50, 'duration': 3.00},
    {'text': 'and another one here', 'start': 121.50, 'duration': 3.00},
    {'text': 'the document keeps growing', 'start': 124.50, 'duration': 4.50},
    {'text': 'more and more text', 'start': 129.00, 'duration': 4.00},
    {'text': 'yet another sentence', 'start': 133.00, 'duration': 3.50},
    {'text': 'further expanding the document', 'start': 136.50, 'duration': 5.00},
    {'text': 'text continues', 'start': 141.50, 'duration': 2.50},
    {'text': 'sentence number 22, which will be used', 'start': 144.00, 'duration': 5.00},
    {'text': 'final sentence to wrap up', 'start': 149.00, 'duration': 4.00}
]

modified_transcript = [
    {'text': 'this is a large document with many sentences', 'start': 31.20, 'duration': 7.00},
    {'text': 'it contains various extracts from different sources', 'start': 38.20, 'duration': 6.50},
    {'text': 'sentence number 22, which will be used', 'start': 144.00, 'duration': 5.00}
]

def find_longest_contiguous_original_extract_transcripts(large_transcript, modified_transcript):
    large_texts = [segment['text'] for segment in large_transcript]
    modified_texts = [segment['text'] for segment in modified_transcript]

    match_indices = []
    for mod_text in modified_texts:
        closest_matches = difflib.get_close_matches(mod_text, large_texts, n=1, cutoff=0.5)
        if closest_matches and len(closest_matches[0].split()) >= 3:
            match_index = large_texts.index(closest_matches[0])
            match_indices.append(match_index)

    if not match_indices:
        return None, None, None

    longest_sequence = []
    current_sequence = [match_indices[0]]

    for i in range(1, len(match_indices)):
        if match_indices[i] == match_indices[i-1] + 1:
            current_sequence.append(match_indices[i])
        else:
            if len(current_sequence) > len(longest_sequence):
                longest_sequence = current_sequence
            current_sequence = [match_indices[i]]

    if len(current_sequence) > len(longest_sequence):
        longest_sequence = current_sequence

    original_extract = [large_transcript[i] for i in longest_sequence]
    start_time = original_extract[0]['start']
    end_time = original_extract[-1]['start'] + original_extract[-1]['duration']

    return start_time, end_time, original_extract

start_time, total_duration, original_extract = find_longest_contiguous_original_extract_transcripts(large_transcript, modified_transcript)
print('Text matched from the RV:', original_extract)
print("Start Time:", start_time)
print("Total Duration:", total_duration)
