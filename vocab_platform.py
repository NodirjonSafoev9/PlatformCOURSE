import random
import datetime
from typing import List, Dict, Tuple, Optional

class VocabularyPlatform:
    """Simple in-memory platform for English-Uzbek vocabulary learning."""
    def __init__(self) -> None:
        self.vocab: Dict[str, str] = {}
        self.passage: Optional[Dict[str, object]] = None

    def upload_vocab(self, words: List[Dict[str, str]]) -> None:
        """Upload vocabulary list.

        Args:
            words: List of dicts with keys 'english' and 'uzbek'.
        """
        for w in words:
            eng = w.get('english')
            uz = w.get('uzbek')
            if eng and uz:
                self.vocab[eng] = uz

    def get_flashcards(self) -> List[Tuple[str, str]]:
        """Return vocabulary as list of flashcards."""
        return list(self.vocab.items())

    def contest(self, n: int = 5) -> List[Tuple[str, str]]:
        """Return *n* random vocabulary items for contest mode."""
        if not self.vocab:
            raise ValueError("No vocabulary available")
        sample = random.sample(list(self.vocab.items()), min(n, len(self.vocab)))
        return sample

    def schedule_reviews(self) -> Dict[str, datetime.datetime]:
        """Very naive spaced-repetition schedule: review all words tomorrow."""
        tomorrow = datetime.datetime.now() + datetime.timedelta(days=1)
        return {word: tomorrow for word in self.vocab}

    def upload_passage(self, text: str, words: List[str], phrases: List[str], idioms: List[str]) -> None:
        """Store passage with associated clickable vocabulary."""
        self.passage = {
            'text': text,
            'words': words,
            'phrases': phrases,
            'idioms': idioms,
        }

    def get_passage(self) -> Optional[Dict[str, object]]:
        """Return stored passage information."""
        return self.passage
