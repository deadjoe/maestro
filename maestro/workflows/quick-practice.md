# Quick Practice Workflow (Type 2)

This workflow handles student-driven practice requests for specific topics or skills.

## Trigger Conditions

- "Practice [topic]" / "练习[主题]" / "Pratiquer [sujet]"
- "I want to practice..." / "我想练习..."
- "Help me review..." / "帮我复习..."
- "Let's work on..." / "让我们练习..."
- Specific requests: "restaurant ordering", "past tense", "directions"

## Workflow Steps

### Step 1: Understand Request

**Clarify if needed**:
- What specific skill/topic?
- Any particular focus area?
- How much time available?

**Example**:
```
Student: "I want to practice restaurant ordering"
You (in user's language): "Great! Would you like to practice ordering food, asking for the bill, or making reservations? Or all of it?"
```

### Step 2: Check Student Level

```bash
cat ~/spanish-learning/progress.md
```

Extract:
- Current CEFR level (A1/A2/B1/B2)
- Instruction language
- Recent weaknesses
- Previously covered topics

**Level-appropriate difficulty**:
- **A1**: Basic vocabulary, simple present tense, short phrases
- **A2**: Past/future tenses, longer dialogues, more vocabulary
- **B1**: Complex structures, subjunctive if taught, nuanced expressions
- **B2**: Sophisticated language, idioms, cultural references

### Step 3: Determine Practice Type

Based on request, choose:

1. **Role-Play Dialogue**: Interactive scenario simulation
2. **Grammar Drills**: Focused conjugation/structure practice
3. **Vocabulary Review**: Spaced repetition of learned words
4. **Translation Practice**: Native language ↔ Spanish
5. **Reading Comprehension**: Authentic materials
6. **Writing Exercise**: Email, story, description
7. **Listening Practice**: Described audio scenarios

See `practice-types/exercises.md` for details on each type.

### Step 4: Gather Materials (if needed)

**For authentic practice**, use WebSearch:

```python
# Restaurant practice example
WebSearch: "menú restaurante Madrid actual"
# Save to ~/spanish-learning/practice_materials/menus/

# Travel practice example
WebSearch: "información turística Barcelona español"
# Save to ~/spanish-learning/practice_materials/travel/

# Housing practice example
WebSearch: "anuncios alquiler pisos España"
# Simplify to student level
```

**Guidelines** (from `practice-types/content-strategy.md`):
- Use "actual" or "reciente" not specific years
- Simplify to student's CEFR level
- Highlight regional differences
- Save for future reuse

### Step 5: Execute Practice Session

**General Structure** (15-30 minutes):

1. **Brief introduction** (2 min):
   - Explain what you'll practice (in user's language)
   - Set expectations: number of exercises/scenarios
   - Preview key vocabulary if needed

2. **Warm-up** (3-5 min):
   - Quick review of relevant vocabulary
   - 2-3 simple exercises to activate knowledge
   - Check vocab_tracker for related words

3. **Main practice** (10-20 min):
   - Execute chosen practice type
   - Interactive, back-and-forth
   - Immediate correction using correction protocol
   - Adjust difficulty dynamically based on performance

4. **Wrap-up** (2-3 min):
   - Quick summary in user's language
   - Note any new vocabulary learned
   - Praise specific improvements

### Step 6: Update Records

**If significant learning occurred**:
```bash
# Add new vocabulary
python maestro/scripts/vocab_tracker.py --add "new,words,learned"

# Brief note in progress.md
# Update "Last session" section with practice topic
# Add to "Vocabulary to Review" if needed
```

**If minor practice**:
- No formal update needed
- Mental note for next structured session

## Practice Type Details

### Type A: Role-Play Dialogue

**Best for**: Real-world scenario practice

**Flow**:
1. Set the scene (in user's language)
2. Introduce your role and student's role
3. Begin dialogue in Spanish
4. Adapt to student responses
5. Correct using 4-step protocol
6. Continue until scenario complete

**Example (Restaurant - A1 level)**:
```
You (in English/Chinese/etc): "You're in a restaurant in Barcelona. I'm the waiter. You want to order a coffee and a sandwich. Ready?"

You (as waiter): "Buenas tardes. ¿Qué desea tomar?"

Student: [responds]

You: [Continue dialogue, correct if needed, adapt to responses]

[After 5-7 exchanges, conclude scenario]

You (in user's language): "Great job! You successfully ordered and asked for the bill. Your use of 'quiero' was perfect!"
```

**Scenarios available**: See `teaching_guides/scenarios.md` for templates.

### Type B: Grammar Drills

**Best for**: Conjugation, structure, specific grammar review

**Flow**:
1. Identify grammar point to practice
2. Brief explanation (if needed)
3. 10-15 drill exercises
4. Progressive difficulty
5. Mix exercise types (fill-blank, translation, creation)

**Example (Present tense conjugation - A1)**:
```
You (in user's language): "Let's practice present tense conjugation with regular -AR verbs. I'll give you the subject and infinitive, you conjugate."

1. Yo / hablar → ?
2. Tú / trabajar → ?
3. Ella / estudiar → ?
... [continue 10-15 exercises]

[Immediate feedback after each]
```

**Use practice_generator.py for variety**:
```bash
python maestro/scripts/practice_generator.py --topic "present-AR" --count 15
```

### Type C: Vocabulary Review

**Best for**: Spaced repetition, consolidation

**Flow**:
1. Check due vocabulary:
   ```bash
   python maestro/scripts/vocab_tracker.py --due-today
   ```
2. If words due, review those first
3. Quiz format: give word, student translates
4. Switch directions: translation → Spanish
5. Use in sentences
6. Update mastery levels

**Example**:
```
You (in user's language): "You have 8 words due for review today. Let's go through them."

You: "How do you say 'tired' in Spanish?"
Student: "Cansado"
You: "Correct! Now use it in a sentence."
Student: "Estoy cansado"
You: "Perfect! ¡Perfecto!"

[Continue through all words]
[Update tracker with results]
```

### Type D: Translation Practice

**Best for**: Accuracy, thinking in both languages

**Flow**:
1. Choose direction: Native → Spanish or Spanish → Native
2. Provide 5-10 sentences
3. Match to student level
4. Focus on recently learned topics
5. Discuss translations, not just right/wrong

**Example (Chinese → Spanish, A2 level)**:
```
You: "Translate these sentences to Spanish:"

1. 我昨天去了超市 (I went to the supermarket yesterday)
Student: "Yo fui al supermercado ayer"
You: "Excellent! Perfect use of preterite tense."

2. 她正在学习法语 (She is studying French)
Student: "Ella está estudiando francés"
You: "Great! You used the present progressive correctly."

[Continue...]
```

### Type E: Reading Comprehension

**Best for**: Building vocabulary, cultural learning

**Flow**:
1. Find or create text at appropriate level
2. Use WebSearch for authentic materials
3. Simplify if needed
4. Student reads (silently or aloud)
5. Comprehension questions
6. Vocabulary extraction

**Example (A2 level - News article)**:
```
You: [Search for simple Spanish news]
You: "I found a short article about a festival in Valencia. Let me share it with you..."

[Provide simplified text]

You (in user's language): "Read this and tell me: What is the festival called? When does it happen? What do people do?"

Student: [answers in Spanish or native language]

You: "Correct! Now let's learn these new words from the article: [list 5-6 new words]"
```

### Type F: Writing Exercise

**Best for**: Production, grammar integration, creativity

**Flow**:
1. Set writing task (level-appropriate)
2. Give length target
3. Student writes
4. Review together
5. Correct errors
6. Discuss improvements

**Length by level**:
- **A1**: 30-50 words
- **A2**: 75-100 words
- **B1**: 125-175 words
- **B2**: 200-300 words

**Example topics**:
- A1: Introduce yourself
- A2: Describe your last weekend
- B1: Write an email to a friend
- B2: Opinion essay on a cultural topic

### Type G: Listening Practice

**Best for**: Comprehension, pronunciation

**Flow** (described audio):
1. Describe a listening scenario
2. "Imagine you hear..."
3. Provide transcript slowly
4. Ask comprehension questions
5. Discuss key phrases

**Example**:
```
You (in user's language): "Imagine you're at a train station and you hear this announcement..."

You (slowly, with pauses): "Atención pasajeros. El tren con destino a Madrid sale del andén número tres en cinco minutos."

You: "What did you understand? Where is the train going? Which platform? When does it leave?"

[Discuss, replay if needed, extract key vocabulary]
```

## Adaptation Rules

### If Student Excels
- Increase difficulty mid-session
- Add more complex vocabulary
- Introduce advanced structures
- Challenge with cultural references
- Preview upcoming curriculum topics

### If Student Struggles
- Simplify immediately
- Reduce quantity of exercises
- Provide more scaffolding
- Use more native language support
- Focus on previously learned material
- Note weakness for structured sessions

### Time Management
- **10 minutes available**: Focus drill (vocab or grammar)
- **20 minutes available**: Role-play or translation
- **30+ minutes available**: Reading/writing or combined practice

## Integration with Curriculum

**If practice topic is upcoming in curriculum**:
- Preview lightly, don't teach fully
- Activate interest
- Note student's curiosity in progress.md

**If practice topic is review**:
- Reinforce learning
- Note mastery level
- Update progress.md if significant review needed

**If practice topic is beyond current level**:
- Acknowledge interest
- Provide simplified version
- Suggest: "We'll cover this in detail in Week X"
- Give taste without full teaching

## Web Search Strategy

**When to search**:
- Student requests real-world materials
- Need current/authentic content
- Cultural context required
- Regional verification needed

**Search query best practices**:
```bash
✅ Good: "menú restaurante Madrid actual"
✅ Good: "noticias fáciles español A1 reciente"
✅ Good: "formulario alquiler España"

❌ Avoid: "menú restaurante Madrid 2025"
❌ Avoid: specific dates that will expire
```

**Content simplification**:
1. Assess original complexity
2. Identify student level
3. Simplify vocabulary if needed
4. Shorten if too long
5. Maintain authenticity
6. Explain cultural context

## Example Quick Practice Sessions

### Example 1: A1 Student - Restaurant Practice (20 min)

```
Student: "I want to practice ordering at a restaurant"

[Check progress.md → A1, Week 5, instruction_language: zh-CN]
[Search: "menú restaurante simple español"]

You (中文): "太好了！我找到了一个简单的餐厅菜单。我们来模拟点餐。你是顾客，我是服务员。准备好了吗？"

[Role-play 7-8 exchanges]
[Practice: ordering, asking price, asking for bill]
[Correct using 4-step protocol]

You (中文): "做得很好！你学会了点餐的基本表达。我们学了这些新词：menú, plato, cuenta。我会把它们加到你的词汇追踪里。"

[Add: python maestro/scripts/vocab_tracker.py --add "menú,plato,cuenta,quiero,por favor"]
```

### Example 2: B1 Student - Subjunctive Practice (25 min)

```
Student: "I need to practice subjunctive mood"

[Check progress.md → B1, Week 28, instruction_language: en]

You: "Great! The subjunctive is challenging. Let's focus on 'espero que' + subjunctive. I'll give you situations, you respond with hopes/wishes."

Exercise pattern:
You: "Your friend has an exam tomorrow. What do you hope?"
Student: "Espero que él study well"
You: "Good try! But it should be 'Espero que él estudie bien', because after 'espero que' we use subjunctive form. Remember: -AR verbs change to -e ending. Try again."
Student: "Espero que él estudie bien"
You: "Perfect! ¡Perfecto!"

[Continue 10-12 exercises]
[Generate more if needed: python maestro/scripts/practice_generator.py --topic "subjunctive-wishes" --count 10]
```

### Example 3: A2 Student - Past Tense Review (15 min)

```
Student: "Ayúdame a revisar el pretérito"

[Check progress.md → A2, Week 16, instruction_language: es]
[Note: Student wrote in Spanish, adapt response]

You (español): "¡Claro! Vamos a practicar el pretérito. Te voy a hacer preguntas sobre tu semana pasada, y tú respondes usando el pretérito. ¿Listo?"

You: "¿Qué hiciste ayer?"
Student: [responds]
[Continue dialogue-based practice]

[Quick grammar drill if needed]
[Focus on irregular verbs if student struggles]
```

## Success Metrics

A successful quick practice session:
- ✅ Addresses student's specific request
- ✅ Appropriate difficulty for level
- ✅ Interactive and engaging
- ✅ Immediate feedback provided
- ✅ Student shows improvement during session
- ✅ Encouragement and motivation maintained

## File References

- Practice exercises: `practice-types/exercises.md`
- Content strategy: `practice-types/content-strategy.md`
- Correction protocol: `protocols/correction-principles.md`
- Scenarios: `teaching_guides/scenarios.md`
- Grammar reference: `teaching_guides/grammar_reference.md`
