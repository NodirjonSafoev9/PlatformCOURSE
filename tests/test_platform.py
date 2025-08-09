import os, sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from vocab_platform import VocabularyPlatform

def test_upload_and_flashcards():
    p = VocabularyPlatform()
    p.upload_vocab([{'english': 'cat', 'uzbek': 'mushuk'}])
    assert ('cat', 'mushuk') in p.get_flashcards()

def test_contest_and_schedule():
    p = VocabularyPlatform()
    words = [
        {'english': 'cat', 'uzbek': 'mushuk'},
        {'english': 'dog', 'uzbek': 'it'},
        {'english': 'bird', 'uzbek': 'qush'},
    ]
    p.upload_vocab(words)
    contest_words = p.contest(n=2)
    assert len(contest_words) == 2
    schedule = p.schedule_reviews()
    assert set(schedule.keys()) == {w['english'] for w in words}

def test_passage_storage():
    p = VocabularyPlatform()
    p.upload_passage('Hello world', ['world'], ['hello world'], [])
    passage = p.get_passage()
    assert passage['text'] == 'Hello world'
    assert passage['words'] == ['world']
