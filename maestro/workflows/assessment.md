# Weekly Assessment Workflow (Type 3)

Day 5 of each week is dedicated to comprehensive assessment of the week's learning.

## Trigger Conditions

- Current day is Day 5 of any week
- Student explicitly requests assessment
- End of level assessment (Week 12, 24, 40, 52)

## Assessment Structure

Copy this checklist at session start:
```
Week [X] Assessment Progress:
- [ ] Part 1: Vocabulary test (10 words) - /25
- [ ] Part 2: Grammar test (conjugation + usage) - /25
- [ ] Part 3: Translation (5 sentences) - /15
- [ ] Part 4: Conversation scenario - /20
- [ ] Part 5: Regional variations (Spain vs Mexico) - /15
- [ ] Part 6: Score and analyze weaknesses
- [ ] Part 7: Plan next week
```

**Total Score**: /100

## Part 1: Vocabulary Test (/25 points)

### Selection Criteria

Test 10 words from this week's learning:
- 5 words from vocabulary_tracker.py (recently added)
- 3 words from curriculum Week X vocabulary
- 2 words from previous weeks (spaced repetition)

### Test Format

**Round 1: Recognition** (5 words)
```
You (in user's language): "I'll say a Spanish word, you tell me what it means in [user's language]."

1. "cansado" → ?
2. "feliz" → ?
... [5 words]
```

**Round 2: Production** (5 words)
```
You (in user's language): "I'll say a word in [user's language], you give me the Spanish."

1. [User language word] → ?
2. [User language word] → ?
... [5 words]
```

### Scoring
- 2.5 points per word
- Must be exact (gender, spelling) for full points
- Close answers (minor spelling): 1.5 points
- Wrong: 0 points

### Record Results
```bash
# Update mastery levels based on performance
python maestro/scripts/vocab_tracker.py --update "cansado:correct,feliz:correct,mesa:wrong,..."
```

## Part 2: Grammar Test (/25 points)

### Section A: Conjugation (15 points)

Test the main verbs/tenses taught this week.

**Format** (3 verbs, 5 forms each):
```
You (in user's language): "Conjugate the verb [verb] in [tense]."

Example - Week 2 (present tense estar):
1. Yo / estar →
2. Tú / estar →
3. Él / estar →
4. Nosotros / estar →
5. Ellos / estar →

[Repeat for 2 more verbs]
```

**Scoring**: 1 point per correct conjugation

### Section B: Usage (10 points)

Test understanding of when/how to use grammar structures.

**Format** (5 questions, 2 points each):
```
You (in user's language): "Fill in the blank with the correct form."

1. Yo _____ (ser/estar) estudiante.
2. María _____ (ser/estar) en Madrid.
3. Nosotros _____ (ser/estar) cansados.
4. Tú _____ (ser/estar) de México.
5. El libro _____ (ser/estar) interesante.
```

**Scoring**:
- Correct verb AND conjugation: 2 points
- Correct verb, wrong conjugation: 1 point
- Wrong verb: 0 points

## Part 3: Translation Test (/15 points)

### Format

5 sentences to translate (3 points each):
- 3 sentences: User's language → Spanish
- 2 sentences: Spanish → User's language

**Content**: Based on week's topics

**Example (A1 Week 3, English speaker)**:
```
You: "Translate these sentences to Spanish:"

1. I am happy today.
2. She is in the office.
3. We are tired.

"Translate these sentences to English:"

4. El gato está en la mesa.
5. Ellos son estudiantes de español.
```

### Scoring
- Perfect translation: 3 points
- Minor error (one word wrong): 2 points
- Comprehensible but multiple errors: 1 point
- Incomprehensible or mostly wrong: 0 points

## Part 4: Conversation Scenario (/20 points)

### Setup

Choose a scenario related to week's content:
- Consult: `teaching_guides/scenarios.md`
- Select appropriate complexity for level
- 6-8 exchange dialogue

### Format
```
You (in user's language): "We're going to have a conversation. [Describe scenario in user's language]. You start."

[Interactive dialogue - 6-8 exchanges]
[Student must use week's vocabulary and grammar]
```

**Example (A1 Week 4 - Describing locations)**:
```
You (in user's language): "You're calling a friend. Describe where you are and what you see around you. I'll be your friend. You start the call."

Student: "Hola, ¿cómo estás?"
You: "Bien, ¿dónde estás?"
Student: [must describe location using estar + location vocabulary]
... [continue dialogue]
```

### Scoring Rubric (see `teaching_guides/assessment_rubrics.md`)

- **Grammar Accuracy** (5 points): Correct conjugation and structure
- **Vocabulary Range** (5 points): Use of week's new vocabulary
- **Fluency** (5 points): Natural flow, appropriate responses
- **Comprehension** (5 points): Understanding and appropriate reactions

## Part 5: Regional Variations (/15 points)

### Purpose

Test awareness of Spain vs Mexico/Latin America differences.

**Reference**: `teaching_guides/regional_differences.md`

### Format (3 questions, 5 points each)

**Question 1: Vocabulary Difference**
```
You (in user's language): "How would you say 'computer' in Spain? And in Mexico?"
Expected: ordenador (Spain), computadora (Mexico)
```

**Question 2: Grammar Difference**
```
You (in user's language): "How do you say 'you all are' in Spain? And in Latin America?"
Expected: vosotros sois (Spain), ustedes son (Latin America)
```

**Question 3: Cultural/Usage Difference**
```
You (in user's language): "In which region would you use 'vosotros'? Why?"
Expected: Spain; it's the informal plural 'you'
```

### Scoring
- Complete, accurate answer: 5 points
- Partially correct: 3 points
- Attempted but mostly wrong: 1 point
- No answer or completely wrong: 0 points

## Part 6: Scoring and Analysis

### Calculate Total Score

```
Part 1: Vocabulary     /25
Part 2: Grammar        /25
Part 3: Translation    /15
Part 4: Conversation   /20
Part 5: Regional       /15
─────────────────────────
TOTAL:                /100
```

### Score Interpretation

| Score | Level | Action |
|-------|-------|--------|
| 90-100 | Excellent | Advance; consider acceleration |
| 80-89 | Good | Advance normally |
| 70-79 | Passing | Continue, note weaknesses |
| 60-69 | Needs improvement | Review week before advancing |
| <60 | Not ready | Repeat week's content |

### Identify Weaknesses

Analyze performance by category:
- **Vocabulary**: Which words were missed?
- **Grammar**: Which structures caused errors?
- **Skills**: Production vs comprehension vs conversation?

```markdown
Update in progress.md:

## Identified Weaknesses (from Week X Assessment)
- Vocabulary: [specific words missed]
- Grammar: [specific structures struggled with]
- Skills: [conversation/translation/etc.]
- Notes: [any patterns observed]
```

### Generate Analytics Report

```bash
python maestro/scripts/progress_analyzer.py --generate-report weekly
```

This creates: `~/spanish-learning/weekly_reports/week-[X]-report.md`

## Part 7: Plan Next Week

### Based on Performance

**If 80+ score**:
```
You (in user's language): "Congratulations! You scored [X]/100 on this week's assessment. You're ready to move to Week [X+1]. Next week we'll focus on [next week's topics from curriculum]."

[Update progress.md: Week → X+1, Day → 1]
```

**If 70-79 score**:
```
You (in user's language): "Good work! You scored [X]/100. You can advance to Week [X+1], but let's pay special attention to [weaknesses] as we go. Next week we'll learn [topics] while reviewing [weak areas]."

[Update progress.md: Week → X+1, Day → 1, add weaknesses to review list]
```

**If 60-69 score**:
```
You (in user's language): "You scored [X]/100. You're making progress, but let's review this week's material once more before advancing. Next session, we'll focus on [weak areas], then retry the assessment."

[Update progress.md: Mark week as "needs review", add weaknesses]
```

**If <60 score**:
```
You (in user's language): "You scored [X]/100. Let's spend more time on this week's content. I can see you're having trouble with [specific weaknesses]. Don't worry - this is normal. We'll go through the week again with a different approach."

[Update progress.md: Restart week, note specific areas needing focus]
[Plan modified teaching approach for retry]
```

### Track Assessment History

```markdown
In progress.md, add:

## Assessment History
- Week 1: 75/100 (Advanced)
- Week 2: 82/100 (Advanced) ✓
- Week 3: 68/100 (Reviewed Week 3)
- Week 3 (retry): 79/100 (Advanced)
- Week 4: [current]
```

### Check Level Advancement Criteria

**For level transitions** (End of Weeks 12, 24, 40, 52):

Must have:
- ✅ 3 consecutive assessment scores ≥80
- ✅ Demonstrated mastery in all 4 rubric dimensions
- ✅ Comfortable with spontaneous conversation at target level

**If criteria met**:
```
You (in user's language): "Congratulations! You've completed [A1/A2/B1] level with strong performance. You're ready to advance to [A2/B1/B2] level. This is a significant milestone! Next week we'll start [next level] Week 1."

[Update progress.md: Level → next level, Week → 1, Day → 1]
[Celebrate achievement!]
```

**If criteria NOT met**:
```
You (in user's language): "You've completed the [level] curriculum, but let's solidify your foundation before advancing. We'll do 2-4 more weeks of [current level] practice focusing on [weak areas]. This will make your transition to [next level] much smoother."

[Design custom review weeks]
[Focus on identified weaknesses]
```

## Special Assessments

### Initial Assessment (First Session)

See: `workflows/initial-assessment.md`

Determines starting level (A1, A2, B1, B2).

### Mid-Level Check (Optional)

At Week 6 of each level, can do optional diagnostic:
- Quick assessment (30 minutes)
- Check pace appropriateness
- Adjust if student is excelling or struggling
- No formal score, just feedback

### Final B2 Assessment

At end of Week 52:
- Comprehensive assessment of all A1-B2 content
- Extended conversation (15-20 minutes)
- Writing sample (300+ words)
- Reading comprehension of authentic text
- If passed: Student has achieved B2 fluency! 🎉

## Integration with Other Tools

### Vocabulary Tracker
```bash
# Before assessment, check mastery levels
python maestro/scripts/vocab_tracker.py --stats

# After assessment, update based on test results
python maestro/scripts/vocab_tracker.py --update "[results]"
```

### Progress Analyzer
```bash
# After scoring, generate weekly report
python maestro/scripts/progress_analyzer.py --generate-report weekly

# Check advancement prediction
python maestro/scripts/progress_analyzer.py --predict-advancement
```

### Progress File
Update all sections:
- Current Status (if advancing)
- Completed Topics (add this week)
- Identified Weaknesses (from analysis)
- Assessment History (add this score)
- Next Session Plan (based on results)

## Encouragement & Feedback

**Always frame feedback positively** (in user's language):

**Good performance**:
- "Your [specific skill] has improved significantly!"
- "I can see you've been practicing [specific area]"
- "You handled [difficult topic] with confidence"

**Areas for improvement**:
- "Let's focus more on [topic] - it's challenging for everyone"
- "With a bit more practice on [grammar point], you'll master it"
- "Your effort is clear - we just need to adjust our approach to [topic]"

**Encouragement**:
- Compare to their own past: "You couldn't do [X] three weeks ago, and now look!"
- Specific praise: "Your pronunciation of [word] was perfect"
- Progress perspective: "You're [%] through [level] - great progress!"

## Example Assessment Session (A1 Week 4)

```
[Student starts session, progress.md shows A1 Week 4 Day 5]

You (in user's language): "It's assessment day! We'll test what you learned this week about locations and describing positions. Don't worry - this helps me understand where to focus our teaching. Ready?"

[Part 1: Vocabulary - test 10 words from Week 4]
Score: 20/25 (2 words missed)

[Part 2: Grammar - estar conjugation + usage]
Score: 22/25 (minor conjugation errors)

[Part 3: Translation - 5 sentences about locations]
Score: 12/15 (one translation had errors)

[Part 4: Conversation - calling friend, describing location]
Score: 17/20 (good vocabulary, minor grammar issues)

[Part 5: Regional - Spain vs Mexico differences]
Score: 12/15 (got vosotros concept correct)

TOTAL: 83/100

You (in user's language): "Excellent work! You scored 83/100. You're clearly ready for Week 5. I noticed you're strongest in conversation and vocabulary, and we should keep practicing estar conjugation - you're close to perfect! Next week we'll learn past tense, and I'm confident you'll do great. Well done! ¡Buen trabajo!"

[Generate report: python maestro/scripts/progress_analyzer.py --generate-report weekly]
[Update progress.md: Week 5, Day 1, add minor estar conjugation to review list]
```

## Success Metrics

A successful assessment session:
- ✅ All 7 parts completed
- ✅ Fair, level-appropriate difficulty
- ✅ Specific feedback provided
- ✅ Weaknesses clearly identified
- ✅ Next steps clearly communicated
- ✅ Student feels encouraged, not discouraged
- ✅ Progress documented in all systems
