# Structured Learning Workflow (Type 1)

This workflow is for curriculum-based learning sessions following the CEFR progression.

## Trigger Conditions

- Student says: "Start today's lesson" / "开始今天的课程" / "Commencer la leçon"
- Student says: "Continue curriculum" / "继续学习"
- It's a new week and student starts session
- Progress.md indicates scheduled curriculum day

## Workflow Steps

### Step 1: Load Student Progress

```bash
# Read current position
cat ~/spanish-learning/progress.md
```

Extract:
- Current level (A1/A2/B1/B2)
- Current week number
- Current day (1-5)
- Instruction language code
- Last session date

### Step 2: Load Appropriate Curriculum

Based on level, read:
- **A1**: `curriculum/A1_curriculum.md` (Weeks 1-12)
- **A2**: `curriculum/A2_curriculum.md` (Weeks 13-24)
- **B1**: `curriculum/B1_curriculum.md` (Weeks 25-40)
- **B2**: `curriculum/B2_curriculum.md` (Weeks 41-52)

Find the section for current week and day.

### Step 3: Execute Daily Lesson (Days 1-4)

**Session Structure Checklist** (copy to context):
```
Today's Lesson Progress:
- [ ] Opening: Review previous lesson (5 min)
- [ ] Objectives: State today's goals (2 min)
- [ ] Teaching: Introduce new content (10-15 min)
- [ ] Practice: Interactive exercises (20-30 min)
- [ ] Closing: Summary and check understanding (5 min)
```

#### 3.1 Opening (5 minutes)

**In user's language** (get from language-templates.md):

1. Review last lesson:
   - "Last time we learned [topic], do you remember?"
   - Quick quiz: 1-2 questions from previous session
   - Check understanding before proceeding

2. Preview today:
   - "Today we'll learn [new topic]"
   - Set expectations for session length

**Example (English)**:
```
"Last time we learned the verb 'ser' (to be). Can you tell me how to say 'I am a student' in Spanish?"
[Student responds]
"Great! Today we're going to learn 'estar', another verb for 'to be', and when to use it. Ready? ¡Vamos!"
```

**Example (Chinese)**:
```
"我们上次学了动词 'ser'（是）。你能告诉我怎么说'我是学生'吗？"
[Student responds]
"很好！今天我们要学习 'estar'，另一个表示'是'的动词，以及何时使用它。准备好了吗？¡Vamos!"
```

#### 3.2 Objectives (2 minutes)

State clearly **in user's language**:
- "Today's goal is to [objective]"
- "After this lesson you'll be able to [capability]"
- "We'll do [X] exercises"

**Load from curriculum**: Each day has predefined objectives.

#### 3.3 Teaching (10-15 minutes)

**Content delivery** (Spanish + English):

1. **Introduce concept**:
   - Show the Spanish term
   - Provide English translation
   - Explain usage in user's language

2. **Provide examples** (3-5 sentences):
   - Spanish sentence
   - English translation
   - Context explanation in user's language

3. **Explain usage scenarios**:
   - When to use this
   - Common mistakes to avoid
   - Regional differences if relevant

4. **Answer questions**:
   - Student may ask for clarification
   - Explain in their native language
   - Provide additional examples if needed

**Example Teaching Block**:
```
[In user's language]: "The verb 'estar' is used for temporary states and locations."

Examples:
1. Estoy cansado (I am tired) - temporary state
2. Ella está en Madrid (She is in Madrid) - location
3. Estamos felices (We are happy) - temporary emotion
4. ¿Dónde estás? (Where are you?) - asking location
5. El libro está en la mesa (The book is on the table) - location

[In user's language]: "Notice that we use estar for things that can change: emotions, locations, conditions. Later we'll compare this with 'ser' which is for permanent characteristics."
```

#### 3.4 Practice (20-30 minutes)

Run **3-5 progressive rounds**:

**Round 1: Guided Practice** (5-7 min)
- You provide structure, student fills in
- Example: "Complete: Yo _____ (estar) en casa"
- Give 5-7 exercises
- Correct immediately using correction protocol

**Round 2: Semi-Guided** (5-7 min)
- Student creates sentences with prompts
- Example: "Use 'estar' to describe how you feel today"
- Less structure, more creativity
- 4-5 exercises

**Round 3: Free Practice** (5-7 min)
- Student creates original sentences
- Example: "Describe where three objects in your room are"
- No structure provided
- Encourage longer, more complex responses

**Round 4: Role-Play Scenario** (5-10 min)
- Simulate real-world usage
- Load scenario from `teaching_guides/scenarios.md`
- Interactive dialogue
- Example: Asking for directions, describing your location

**Round 5: Challenge Round** (optional, if time permits)
- Combine today's topic with previous learning
- Example: "Use both 'ser' and 'estar' to introduce yourself and describe your current state"
- Test integration of knowledge

**Correction During Practice**:
Use 4-step protocol from `protocols/correction-principles.md`:
1. Acknowledge effort (in user's language)
2. Show correct form
3. Explain why (in user's language)
4. Ask to repeat correctly

**Track Errors**:
Note repeated mistakes mentally for progress.md update.

#### 3.5 Closing (5 minutes)

**In user's language**:

1. **Summary**:
   - "Today we learned [recap main points]"
   - Review key vocabulary and rules

2. **Check understanding**:
   - "Is there anything you'd like to review?"
   - "Which part was most challenging?"
   - Address concerns

3. **Update progress.md**:
   ```bash
   # Mark today as complete
   # Note new vocabulary
   # Record any weaknesses observed
   ```

4. **Preview next session**:
   - "Next time we'll learn [next topic]"
   - "If you have time, review today's vocabulary"

5. **Encouragement**:
   - Praise specific improvements
   - "You did great with [specific skill]!"

### Step 4: Update Progress Files

```bash
# Update progress.md
# Mark day complete
# Add to "Completed Topics"
# Update "Identified Weaknesses" if any patterns emerged
# Update "Next Session Plan"

# Add new vocabulary to tracker
python maestro/scripts/vocab_tracker.py --add "estar,cansado,feliz,ubicación"

# If it's Day 4, prepare for assessment
# If it's end of level, prepare for advancement assessment
```

## Special Cases

### Day 5: Weekly Assessment

If today is Day 5, **do NOT follow this workflow**.

Instead, use: `workflows/assessment.md`

### Student Already Knows Material

If student demonstrates mastery during opening:
1. Do quick verification (2-3 questions)
2. If confirmed, mark day complete
3. Ask: "Would you like to continue to tomorrow's lesson?"
4. Update progress.md accordingly
5. Note accelerated progress

### Student Struggles Significantly

If student cannot complete Round 1 practice:
1. Pause and re-explain concept
2. Simplify to even more basic level
3. Provide 2-3 more examples
4. Try practice again
5. If still struggling:
   - Mark day as "needs review"
   - Plan to repeat this day next session
   - Note weakness in progress.md
   - Encourage: "This is a challenging topic, we'll practice more next time"

### Time Constraints

If student has limited time:
1. Prioritize: Opening → Objectives → Teaching → Round 1 Practice → Closing
2. Skip Rounds 2-5 if needed
3. Mark day as "partial completion"
4. Note in progress.md: "Complete remaining practice next session"

## Curriculum-Specific Notes

### A1 Level (Weeks 1-12)
- Keep language very simple
- Use many visual examples and gestures (describe in text)
- Repeat explanations multiple times
- Practice rounds should be shorter (3 rounds max)
- Heavy use of translation exercises

### A2 Level (Weeks 13-24)
- Start reducing native language scaffolding
- Introduce more complex sentence structures
- Expect student to speak more in Spanish during practice
- Add reading comprehension exercises

### B1 Level (Weeks 25-40)
- Reduce translation, increase Spanish immersion
- Complex role-play scenarios
- Introduce subjunctive mood carefully
- Use authentic materials from web search
- Expect paragraph-length responses

### B2 Level (Weeks 41-52)
- Mostly Spanish interaction during practice
- Native language only for complex grammar explanations
- Sophisticated topics: culture, idioms, register
- Authentic content: news, articles, videos (described)
- Expect essay-length production

## Integration with Other Resources

**During Teaching Phase**:
- Reference: `teaching_guides/grammar_reference.md` for detailed conjugation tables
- Regional: `teaching_guides/regional_differences.md` for Spain vs Mexico notes

**During Practice Phase**:
- Scenarios: `teaching_guides/scenarios.md` for role-play templates
- Exercises: `practice-types/exercises.md` for additional practice ideas

**For Authentic Materials**:
- Content: `practice-types/content-strategy.md` for web search guidelines
- Fetch: `scripts/content_fetcher.py` for retrieving real Spanish content

## Success Metrics

A successful structured learning session includes:
- ✅ Student completes all 5 lesson phases
- ✅ Student demonstrates understanding in practice rounds
- ✅ Student can create at least 3 original correct sentences with new content
- ✅ Progress.md updated accurately
- ✅ New vocabulary added to tracker
- ✅ Student feels encouraged and motivated

## Example Session Flow (A1 Week 2, Day 3 - Learning 'estar')

```
[Read progress.md → A1, Week 2, Day 3, instruction_language: en]
[Load curriculum/A1_curriculum.md → Week 2, Day 3 → Topic: "Verb estar"]

You: "Hello! Welcome back! Last time we learned how to describe permanent characteristics with 'ser'. Do you remember how to say 'I am a teacher'?"

Student: "Yo soy profesor"

You: "Perfect! Today we're going to learn 'estar', another verb that means 'to be', but used for different situations. By the end of this lesson, you'll be able to describe locations and temporary states. We'll do about 4 exercises. Ready? ¡Vamos!"

[Continue through Teaching phase...]
[Execute Practice rounds...]
[Close and update progress...]

You: "Great job today! You learned the verb 'estar' and can now describe locations and how you feel. Next time we'll compare 'ser' and 'estar' so you know exactly when to use each one. See you next time! ¡Hasta luego!"

[Update progress.md: Week 2, Day 3 complete]
[Add vocabulary: estar, cansado, feliz, en casa, en la mesa]
```
