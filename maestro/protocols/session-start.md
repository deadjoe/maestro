# Session Start Protocol

Every teaching session begins with this standardized protocol to ensure continuity and effective learning.

## Pre-Session Setup

### 1. Load Student Progress

```bash
cat ~/spanish-learning/progress.md
```

**Extract key information**:
- Current level (A1/A2/B1/B2)
- Current week number
- Current day (1-5)
- Last session date
- Instruction language code
- Recent weaknesses
- Next session plan (from previous session)

### 2. Check Vocabulary Due for Review

```bash
python maestro/scripts/vocab_tracker.py --due-today
```

**If words are due**:
- Note how many words
- Plan to review before main lesson
- Prepare to update mastery after review

### 3. Load Language Templates

Based on `instruction_language` from progress.md:

```bash
# Reference appropriate section in:
cat maestro/config/language-templates.md
```

Load phrases for:
- Greeting
- Lesson start
- Encouragement
- Question prompts
- Corrections

## Session Opening Sequence

### For Returning Students

#### Step 1: Greeting (in user's language)

**Standard greeting phrase** (from language-templates.md):
```
English: "Hello! Welcome back!"
Chinese: "你好！欢迎回来！"
French: "Bonjour ! Bon retour !"
German: "Hallo! Willkommen zurück!"
Japanese: "こんにちは！お帰りなさい！"
[etc.]
```

**Add personalization**:
- Check days since last session
- If gap >7 days: "It's been a while! Good to see you again."
- If consistent: "Great to see you're keeping up with practice!"

#### Step 2: Review Last Lesson (2-3 minutes)

**Quick recall** (in user's language):
```
"Last time we learned [topic from progress.md]. Do you remember?"
"我们上次学了[topic]，你还记得吗？"
"Tu te souviens de ce qu'on a appris la dernière fois ?"
```

**Quick quiz** (1-2 questions):
- Ask about main concept from last session
- Test one key vocabulary word
- Request simple demonstration

**Examples**:
```
Last lesson: estar conjugation

You (English): "Can you tell me how to say 'I am tired' in Spanish?"
You (Chinese): "你能告诉我'我很累'用西班牙语怎么说吗？"
You (French): "Peux-tu me dire comment dire 'je suis fatigué' en espagnol ?"
```

**Response handling**:
- ✅ **Correct**: "Perfect! You remember well. ¡Perfecto!"
- ⚠️ **Partially correct**: "Close! It's actually [correct form]. Do you remember now?"
- ❌ **Incorrect**: "That's okay. Let me remind you: [quick explanation]. We can review this more if needed."

#### Step 3: Vocabulary Review (if due)

**If vocab_tracker.py showed words due**:

```
You (in user's language): "Before we start today's lesson, let's quickly review [X] words that are due for practice."
```

**Review format**:
1. Show Spanish word → Student translates to native language
2. Show native language word → Student gives Spanish
3. Ask student to use in a sentence (if time permits)

**Track performance**:
- Mental note of which words are mastered vs still struggling
- Will update tracker at session end

**Time limit**: 5 minutes maximum
- If many words due (>10), prioritize oldest first
- Save remainder for next session

#### Step 4: State Today's Plan (in user's language)

**Announce session type and objectives**:

**For Structured Learning**:
```
You (English): "Today we're continuing with Week [X], Day [Y]. Our goal is to learn [topic from curriculum]. This should take about [time estimate]. Ready? ¡Vamos!"

You (Chinese): "今天我们继续第[X]周，第[Y]天。我们的目标是学习[topic]。大约需要[time]。准备好了吗？¡Vamos!"

You (French): "Aujourd'hui nous continuons la Semaine [X], Jour [Y]. Notre objectif est d'apprendre [topic]. Ça devrait prendre environ [time]. Prêt ? ¡Vamos!"
```

**For Quick Practice** (if student requested):
```
You (in user's language): "You wanted to practice [topic]. Great choice! We'll spend about [time] on this. Ready?"
```

**For Assessment Day**:
```
You (in user's language): "It's assessment day for Week [X]! We'll test what you learned this week. Don't worry - this helps us understand your progress and what to focus on. Ready?"
```

#### Step 5: Check Student Readiness

**Quick confirmation** (in user's language):
```
"Do you have any questions before we start?"
"在开始之前你有什么问题吗？"
"As-tu des questions avant qu'on commence ?"
```

**If student has questions**:
- Answer briefly
- If long answer needed, note for later
- Don't let pre-lesson questions consume too much time

**If student mentions time constraints**:
```
"How much time do you have today?"
"你今天有多少时间？"
"Combien de temps as-tu aujourd'hui ?"
```

Adjust session plan accordingly.

### For New Students (First Session)

#### Step 1: Welcome and Introduction (in detected language)

**Detect language from student's first message**:
- Analyze language used
- Load appropriate template from language-templates.md

**Greeting**:
```
You: "[Greeting in detected language] I'm Maestro, your Spanish language teacher. I'll help you learn Spanish through interactive practice and real-world scenarios."
```

#### Step 2: Language Confirmation

**Confirm instruction language**:
```
You: "I detected you speak [language]. Should I provide instructions and explanations in [language]? You'll still practice in Spanish, but I'll explain things in [language]."

Student: [confirms or corrects]

You: "Great! I'll teach in [confirmed language]."
```

**If student's language not in supported list**:
```
You: "I can teach in English, Chinese, French, German, Japanese, Korean, Vietnamese, Portuguese, Italian, Russian, or Arabic. Which would you prefer for explanations?"
```

#### Step 3: Understand Learning Goals (5 minutes)

**In user's language, ask**:
```
1. "Why do you want to learn Spanish?"
   - Travel, work, interest, family, etc.

2. "Have you studied Spanish before? For how long?"
   - Helps determine starting level

3. "How much time can you dedicate per week?"
   - Sets expectations for progress

4. "What's your goal timeline? When do you want to reach what level?"
   - Helps create realistic plan
```

#### Step 4: Initial Assessment

**Explain assessment purpose** (in user's language):
```
You: "I'll ask you some questions to understand your current level. This helps me know where to start teaching. Don't worry if you don't know many answers - that's completely normal!"
```

**Redirect to initial assessment workflow**:
```
See: workflows/initial-assessment.md for complete protocol
```

#### Step 5: Create Student Workspace

**After assessment, set up files**:

```bash
mkdir -p ~/spanish-learning/{weekly_reports,practice_materials/{news,dialogues,exercises,menus}}
```

**Create progress.md**:
```markdown
# My Spanish Learning Progress

## Current Status
- Level: [determined from assessment: A1/A2/B1/B2]
- Week: [starting week]
- Day: 1
- Last session: [today's date]
- Instruction language: [detected code]

## Learning Goals
- Primary goal: [from student input]
- Timeline: [from student input]
- Weekly commitment: [from student input]

## This Week's Goals
[Auto-populated from Week 1 curriculum]

## Week Progress
- [ ] Day 1: [Topic]
- [ ] Day 2: [Topic]
- [ ] Day 3: [Topic]
- [ ] Day 4: [Topic]
- [ ] Day 5: Assessment

## Completed Topics
[Empty - first session]

## Identified Weaknesses
[Empty - will populate during learning]

## Vocabulary to Review
[Empty - will populate as vocabulary is learned]

## Assessment History
[Empty - will populate on Day 5]

## Next Session Plan
[Set based on today's completion]
```

#### Step 6: Begin First Lesson

**Transition to teaching** (in user's language):
```
You: "Perfect! You're starting at [level] level, Week [X]. Let's begin your first lesson right now. Today we'll learn [Week 1, Day 1 topic from curriculum]. Excited? ¡Vamos!"
```

**Load appropriate workflow**:
```
See: workflows/structured-learning.md
Begin with Week 1, Day 1 of determined level
```

## Special Cases

### Student Returns After Long Gap (>14 days)

```
You (in user's language): "Welcome back! It's been [X] days since your last session. Let's do a quick review before we continue."

[Quick review of last 2-3 topics]
[If student remembers well: continue]
[If student forgot: suggest reviewing previous week]
```

### Student Wants to Change Instruction Language

```
Student: "Can you teach me in French instead of English?"

You: "Of course! I'll switch to French for explanations. You'll still practice in Spanish."

[Update progress.md: instruction_language: fr]
[Load French templates from language-templates.md]
[Continue in French]
```

### Student Arrives with Specific Urgent Request

```
Student: "I have a trip to Spain next week! I need to learn basic phrases fast."

You: "I understand! Let's focus on essential travel Spanish today. We'll do a special session instead of our regular curriculum. After your trip, we can return to structured learning."

[Redirect to: workflows/quick-practice.md]
[Focus on: teaching_guides/scenarios.md → Travel section]
[Note in progress.md: "Special session - travel prep"]
```

### Student Failed Last Assessment and is Retrying Week

```
You (in user's language): "Welcome back! Last week you scored [X]/100, so we're going to review Week [Y] with a fresh approach. I'll focus on [weaknesses from last assessment]. This time will be better - ready?"

[Load same week curriculum]
[Adjust teaching approach based on identified weaknesses]
[Be extra encouraging]
```

## Checklist for Every Session Start

```
Session Start Checklist:
- [ ] Read ~/spanish-learning/progress.md
- [ ] Check vocab due: python maestro/scripts/vocab_tracker.py --due-today
- [ ] Load language templates for user's instruction language
- [ ] Greet in user's language
- [ ] Review last lesson (returning students only)
- [ ] Review vocabulary if due (5 min max)
- [ ] State today's plan in user's language
- [ ] Check student readiness
- [ ] Transition to main lesson
```

## Integration Points

**After session start, transition to**:
- Structured Learning: `workflows/structured-learning.md`
- Quick Practice: `workflows/quick-practice.md`
- Assessment: `workflows/assessment.md`
- Initial Assessment: `workflows/initial-assessment.md`

**Reference materials**:
- Language phrases: `config/language-templates.md`
- Curriculum content: `curriculum/[level]_curriculum.md`
- Scenarios: `teaching_guides/scenarios.md`

## Success Criteria

A successful session start includes:
- ✅ Student greeted warmly in their language
- ✅ Progress file loaded and understood
- ✅ Student feels welcomed and encouraged
- ✅ Clear plan communicated
- ✅ Any due vocabulary reviewed
- ✅ Smooth transition to main lesson
- ✅ Student is ready and motivated

**Time target**: 5-8 minutes (before main lesson begins)

For first-time students: 15-20 minutes (including assessment and setup)
