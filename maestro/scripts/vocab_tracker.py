#!/usr/bin/env python3
"""
Vocabulary Tracker - Spaced Repetition System for Spanish Learning

Features:
- Track vocabulary mastery using spaced repetition algorithm
- Calculate next review dates
- Generate daily review lists
- Statistics and progress tracking
"""

import json
import os
from datetime import datetime, timedelta
from pathlib import Path
import argparse

# Data file location
# Supports custom directory via SPANISH_LEARNING_DIR environment variable
DATA_DIR = Path(os.getenv("SPANISH_LEARNING_DIR", str(Path.home() / "spanish-learning")))
VOCAB_FILE = DATA_DIR / "vocabulary_data.json"


def load_vocabulary_data():
    """Load vocabulary tracking data from JSON file."""
    if not VOCAB_FILE.exists():
        return {}

    with open(VOCAB_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)


def save_vocabulary_data(data):
    """Save vocabulary tracking data to JSON file."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    with open(VOCAB_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def calculate_next_review(mastery_level):
    """
    Calculate next review date based on spaced repetition algorithm.

    Mastery levels:
    0: New word - review tomorrow
    1: Seen once - review in 3 days
    2: Getting it - review in 7 days
    3: Know it - review in 14 days
    4: Master it - review in 30 days
    5+: Mastered - review in 60+ days
    """
    intervals = {
        0: 1,   # 1 day
        1: 3,   # 3 days
        2: 7,   # 1 week
        3: 14,  # 2 weeks
        4: 30,  # 1 month
        5: 60,  # 2 months
    }

    days = intervals.get(mastery_level, 90)
    return (datetime.now() + timedelta(days=days)).strftime('%Y-%m-%d')


def add_vocabulary(words_str):
    """Add new vocabulary words to tracking system."""
    data = load_vocabulary_data()
    words = [w.strip() for w in words_str.split(',')]
    today = datetime.now().strftime('%Y-%m-%d')

    added = []
    for word in words:
        if word and word not in data:
            data[word] = {
                'added_date': today,
                'mastery_level': 0,
                'last_reviewed': today,
                'next_review': calculate_next_review(0),
                'review_count': 0,
                'correct_count': 0,
                'incorrect_count': 0
            }
            added.append(word)

    save_vocabulary_data(data)

    if added:
        print(f"✅ Added {len(added)} new words to vocabulary tracker:")
        for word in added:
            print(f"   - {word}")
    else:
        print("ℹ️  No new words added (all already in tracker)")


def update_mastery(updates_str):
    """
    Update mastery levels based on review results.
    Format: "word1:correct,word2:wrong,word3:correct"
    """
    data = load_vocabulary_data()
    updates = updates_str.split(',')
    today = datetime.now().strftime('%Y-%m-%d')

    for update in updates:
        if ':' not in update:
            continue

        word, result = update.split(':')
        word = word.strip()
        result = result.strip().lower()

        if word in data:
            data[word]['review_count'] += 1
            data[word]['last_reviewed'] = today

            if result in ['correct', 'right', 'yes', 'good']:
                data[word]['correct_count'] += 1
                # Increase mastery
                data[word]['mastery_level'] = min(5, data[word]['mastery_level'] + 1)
                print(f"✅ {word}: Correct! Mastery level: {data[word]['mastery_level']}")
            else:
                data[word]['incorrect_count'] += 1
                # Decrease mastery (but not below 0)
                data[word]['mastery_level'] = max(0, data[word]['mastery_level'] - 1)
                print(f"❌ {word}: Incorrect. Mastery level: {data[word]['mastery_level']}")

            # Recalculate next review date
            data[word]['next_review'] = calculate_next_review(data[word]['mastery_level'])
            print(f"   Next review: {data[word]['next_review']}")
        else:
            print(f"⚠️  Word '{word}' not found in tracker. Add it first.")

    save_vocabulary_data(data)


def get_due_words():
    """Get words due for review today."""
    data = load_vocabulary_data()
    today = datetime.now().strftime('%Y-%m-%d')

    due_words = []
    for word, info in data.items():
        if info['next_review'] <= today:
            due_words.append((word, info))

    if not due_words:
        print("🎉 No words due for review today!")
        return

    print(f"📚 {len(due_words)} words due for review today:\n")
    for i, (word, info) in enumerate(due_words, 1):
        print(f"{i}. {word}")
        print(f"   Mastery: {info['mastery_level']}/5")
        print(f"   Last reviewed: {info['last_reviewed']}")
        print(f"   Review count: {info['review_count']}")
        print()


def show_statistics():
    """Show vocabulary statistics."""
    data = load_vocabulary_data()

    if not data:
        print("No vocabulary data yet. Start adding words!")
        return

    total_words = len(data)
    mastery_counts = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0}

    for info in data.values():
        level = info['mastery_level']
        mastery_counts[level] += 1

    print("📊 Vocabulary Statistics\n")
    print(f"Total words tracked: {total_words}")
    print(f"\nMastery distribution:")
    print(f"  Level 0 (New):        {mastery_counts[0]} words")
    print(f"  Level 1 (Seen):       {mastery_counts[1]} words")
    print(f"  Level 2 (Getting it): {mastery_counts[2]} words")
    print(f"  Level 3 (Know it):    {mastery_counts[3]} words")
    print(f"  Level 4 (Master it):  {mastery_counts[4]} words")
    print(f"  Level 5 (Mastered):   {mastery_counts[5]} words")

    mastered = mastery_counts[4] + mastery_counts[5]
    if total_words > 0:
        mastery_percent = (mastered / total_words) * 100
        print(f"\n✨ Mastery rate: {mastery_percent:.1f}% ({mastered}/{total_words})")


def generate_review_list():
    """Generate and save review list to file."""
    data = load_vocabulary_data()
    today = datetime.now().strftime('%Y-%m-%d')

    due_words = [(word, info) for word, info in data.items() if info['next_review'] <= today]

    if not due_words:
        print("No words due for review today.")
        return

    review_file = DATA_DIR / "vocabulary_review.md"

    with open(review_file, 'w', encoding='utf-8') as f:
        f.write(f"# Vocabulary Review - {today}\n\n")
        f.write(f"**Words to review**: {len(due_words)}\n\n")
        f.write("---\n\n")

        for i, (word, info) in enumerate(due_words, 1):
            f.write(f"## {i}. {word}\n\n")
            f.write(f"- **Mastery level**: {info['mastery_level']}/5\n")
            f.write(f"- **Last reviewed**: {info['last_reviewed']}\n")
            f.write(f"- **Times reviewed**: {info['review_count']}\n")
            f.write(f"- **Correct**: {info['correct_count']} | **Incorrect**: {info['incorrect_count']}\n\n")
            f.write("**Practice**:\n")
            f.write("- [ ] Can recall meaning\n")
            f.write("- [ ] Can use in a sentence\n")
            f.write("- [ ] Correct pronunciation\n\n")
            f.write("---\n\n")

    print(f"✅ Review list generated: {review_file}")
    print(f"📝 {len(due_words)} words ready for review")


def main():
    parser = argparse.ArgumentParser(description='Spanish Vocabulary Tracker')
    parser.add_argument('--add', type=str, help='Add new words (comma-separated)')
    parser.add_argument('--update', type=str, help='Update mastery (format: word1:correct,word2:wrong)')
    parser.add_argument('--due-today', action='store_true', help='Show words due today')
    parser.add_argument('--stats', action='store_true', help='Show statistics')
    parser.add_argument('--generate-review-list', action='store_true', help='Generate review list file')

    args = parser.parse_args()

    if args.add:
        add_vocabulary(args.add)
    elif args.update:
        update_mastery(args.update)
    elif args.due_today:
        get_due_words()
    elif args.stats:
        show_statistics()
    elif args.generate_review_list:
        generate_review_list()
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
