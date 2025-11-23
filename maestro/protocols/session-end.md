# Session End Protocol

Every teaching session ends with this standardized protocol to consolidate learning and prepare for next session.

## Session Closing Sequence

### Step 1: Summary (2-3 minutes)

**In user's language**, recap main points:

```
You: "Today we learned [main topics]. Let's review the key points:"

1. [Main concept 1]
2. [Main concept 2]
3. [Key vocabulary: list 3-5 most important words]
4. [Grammar point if applicable]
```

**Examples by language**:

**English**:
```
"Today we learned the verb 'estar' for describing locations and temporary states. The key points are:
1. Estar is used for locations (Estoy en casa)
2. Estar is used for temporary conditions (Estoy cansado)
3. Key vocabulary: cansado (tired), feliz (happy), en (in/on/at)
```

**Chinese**:
```
"今天我们学习了动词'estar'，用于描述位置和临时状态。要点是：
1. Estar 用于位置（Estoy en casa - 我在家）
2. Estar 用于临时状态（Estoy cansado - 我累了）
3. 关键词汇：cansado（累的）、feliz（快乐的）、en（在）
```

**French**:
```
"Aujourd'hui nous avons appris le verbe 'estar' pour décrire les emplacements et les états temporaires. Les points clés sont :
1. Estar est utilisé pour les emplacements (Estoy en casa)
2. Estar est utilisé pour les conditions temporaires (Estoy cansado)
3. Vocabulaire clé : cansado (fatigué), feliz (heureux), en (dans/sur/à)
```

### Step 2: Check Understanding (1-2 minutes)

**Ask for feedback** (in user's language):

```
"How do you feel about today's material?"
"你觉得今天的内容怎么样？"
"Qu'est-ce que tu penses du contenu d'aujourd'hui ?"
```

**Follow-up questions**:
```
"Is there anything you'd like to review?"
"有什么地方还不太清楚吗？"
"Y a-t-il quelque chose que tu aimerais revoir ?"
```

```
"What was most challenging?"
"什么部分最难？"
"Qu'est-ce qui était le plus difficile ?"
```

```
"What would you like more practice on?"
"你想多练习什么？"
"Sur quoi voudrais-tu pratiquer davantage ?"
```

**Response handling**:

**If student mentions specific difficulty**:
- Note in progress.md under "Identified Weaknesses"
- Offer: "We can spend extra time on that next session" (in user's language)
- Suggest practice: "Try reviewing [specific topic] before next time"

**If student feels confident**:
- Praise: "Great! You're making excellent progress"
- Note in progress.md: "Strong understanding of [topic]"

### Step 3: Update Progress File (2-3 minutes)

**Edit** `~/spanish-learning/progress.md`:

#### Update Current Status
```markdown
## Current Status
- Level: [unchanged or advanced if level transition]
- Week: [X]
- Day: [Y] → [Y+1 or next appropriate day]
- Last session: [YYYY-MM-DD] → [TODAY]
- Instruction language: [unchanged unless student changed it]
```

#### Mark Today's Progress
```markdown
## Week Progress
- [✓] Day [Y]: [Today's topic] ← Mark as complete
- [ ] Day [Y+1]: [Next topic]
```

#### Add to Completed Topics (if day or week complete)
```markdown
## Completed Topics
- [✓] Week [X], Day [Y]: [Topic description]
```

#### Update Identified Weaknesses (if any emerged)
```markdown
## Identified Weaknesses
- [New weakness]: [description and context]
  - Example: "Estar conjugation: confused 'está' with 'es' 3 times"
  - Example: "Gender agreement with -ción endings"
```

#### Update Vocabulary to Review (if new words learned)
```markdown
## Vocabulary to Review
- [new word 1]: [context/example]
- [new word 2]: [context/example]
```

#### Set Next Session Plan
```markdown
## Next Session Plan
[What will happen next time]:
- Review: [any carryover items]
- New content: [next day's topic from curriculum]
- Focus on: [any specific weaknesses to address]
```

### Step 4: Update Vocabulary Tracker (1-2 minutes)

**Add new vocabulary learned today**:

```bash
python maestro/scripts/vocab_tracker.py --add "word1,word2,word3,word4"
```

**Example**:
```bash
python maestro/scripts/vocab_tracker.py --add "estar,cansado,feliz,ubicación,en casa"
```

**What this does**:
- Adds words to spaced repetition system
- Sets initial mastery level to 0 (New)
- Schedules first review for 1 day later
- Tracks in `~/spanish-learning/vocabulary_data.json`

**If vocabulary was reviewed this session** (not new):
```bash
python maestro/scripts/vocab_tracker.py --update "estar:correct,cansado:correct,mesa:wrong"
```

This updates mastery levels based on performance.

### Step 5: Generate Reports (if applicable)

#### Weekly Reports (Day 5 only)

**If today was an assessment** (Day 5):

```bash
python maestro/scripts/progress_analyzer.py --generate-report weekly
```

**Tell student** (in user's language):
```
"I've generated your weekly learning report. You can find it in ~/spanish-learning/weekly_reports/week-[X]-report.md. It shows your progress, strengths, and areas for improvement."

"我已经生成了你的每周学习报告。你可以在 ~/spanish-learning/weekly_reports/week-[X]-report.md 中查看。它显示了你的进步、优势和需要改进的地方。"

"J'ai généré ton rapport d'apprentissage hebdomadaire. Tu peux le trouver dans ~/spanish-learning/weekly_reports/week-[X]-report.md. Il montre tes progrès, tes forces et les domaines à améliorer."
```

#### Analytics (optional, upon request)

**If student asks about progress**:

```bash
python maestro/scripts/progress_analyzer.py --analyze weaknesses
python maestro/scripts/progress_analyzer.py --predict-advancement
```

Share insights with student in their language.

### Step 6: Preview Next Session (1 minute)

**In user's language**, describe what's coming:

**For next day in same week**:
```
"Next time we'll continue with Day [Y+1]: [topic from curriculum]. We'll build on what you learned today about [connection to today's lesson]."

"下次我们将继续第[Y+1]天：[topic]。我们会在今天学习的[connection]基础上继续。"

"La prochaine fois, nous continuerons avec le Jour [Y+1] : [topic]. Nous nous appuierons sur ce que tu as appris aujourd'hui sur [connection]."
```

**For assessment next (Day 5)**:
```
"Next session is Week [X] assessment day. We'll test what you've learned this week. No need to worry - just review today's material if you have time."

"下一节课是第[X]周的评估日。我们会测试你这周学到的内容。不用担心——如果有时间的话复习一下今天的内容就好。"

"La prochaine session est le jour d'évaluation de la Semaine [X]. Nous testerons ce que tu as appris cette semaine. Pas besoin de t'inquiéter - révise juste le contenu d'aujourd'hui si tu as le temps."
```

**For new week**:
```
"Next time we start Week [X+1]! We'll learn [preview of first topic]. You're making great progress!"

"下次我们开始第[X+1]周！我们会学习[preview]。你进步很大！"

"La prochaine fois, nous commençons la Semaine [X+1] ! Nous apprendrons [preview]. Tu fais d'excellents progrès !"
```

### Step 7: Encouragement and Farewell (30 seconds)

**Praise specific achievements** (in user's language):

**Specific praise examples**:
```
"Your pronunciation of 'estar' was excellent today!"
"你今天的'estar'发音非常好！"
"Ta prononciation de 'estar' était excellente aujourd'hui !"
```

```
"I can see you've really understood the difference between ser and estar."
"我看得出你真的理解了ser和estar的区别。"
"Je vois que tu as vraiment compris la différence entre ser et estar."
```

```
"You created 5 perfect sentences in the practice round - well done!"
"你在练习环节造了5个完美的句子——干得好！"
"Tu as créé 5 phrases parfaites dans la ronde de pratique - bien joué !"
```

**Generic encouragement if needed**:
```
"Great work today! Keep it up!"
"今天做得很好！继续加油！"
"Excellent travail aujourd'hui ! Continue !"
```

**Farewell** (in user's language + Spanish):
```
"See you next time! ¡Hasta la próxima!"
"下次见！¡Hasta la próxima!"
"À la prochaine ! ¡Hasta la próxima!"
```

```
"Good job today! ¡Buen trabajo! ¡Hasta luego!"
"今天干得好！¡Buen trabajo! ¡Hasta luego!"
"Bon travail aujourd'hui ! ¡Buen trabajo! ¡Hasta luego!"
```

## Special Cases

### Session Ended Early (Time Constraint)

**If lesson incomplete**:

```markdown
Update progress.md:
## Next Session Plan
- Complete: [remaining content from today]
- Then: [next scheduled content]

Note: "Partial completion of Day [X] due to time constraint"
```

**Tell student** (in user's language):
```
"We didn't finish today's full lesson due to time. Next time we'll complete [remaining content] first, then move forward. No problem!"
```

### Student Struggled Significantly

**Extra encouragement** (in user's language):
```
"Today's topic was challenging - that's completely normal! Many students find [topic] difficult at first. We'll keep practicing and you'll get it. Don't be discouraged!"

"今天的主题很有挑战性——这完全正常！很多学生一开始都觉得[topic]很难。我们会继续练习，你一定会掌握的。不要气馁！"

"Le sujet d'aujourd'hui était difficile - c'est tout à fait normal ! Beaucoup d'étudiants trouvent [topic] difficile au début. Nous continuerons à pratiquer et tu y arriveras. Ne te décourage pas !"
```

**Adjust next session plan**:
```markdown
## Next Session Plan
- Review: [today's challenging topic] with different approach
- Simplified exercises for [topic]
- Build confidence before advancing
```

### Student Exceeded Expectations

**Extra praise**:
```
"You're doing exceptionally well! You grasped [topic] faster than most students. I'm very impressed!"

"你表现得非常好！你比大多数学生更快地掌握了[topic]。我印象非常深刻！"

"Tu te débrouilles exceptionnellement bien ! Tu as saisi [topic] plus rapidement que la plupart des étudiants. Je suis très impressionné !"
```

**Consider acceleration**:
```markdown
## Next Session Plan
- Possibly accelerate: Student showing strong mastery
- Consider preview of Week [X+1] content if Day [Y] goes smoothly
```

### Long Gap Expected Before Next Session

**If student mentions they'll be away**:

```
You (in user's language): "No problem! When you come back, we'll start with a quick review of today's content. To keep your skills sharp, try reviewing the vocabulary in your free time."
```

**Note in progress.md**:
```markdown
## Next Session Plan
- Note: Gap of [X] days expected
- Start with comprehensive review of Week [X] content
- Check vocabulary retention before advancing
```

## End-of-Session Checklist

```
Session End Checklist:
- [ ] Summarize today's learning in user's language
- [ ] Ask for feedback and understanding check
- [ ] Update progress.md:
  - [ ] Current status
  - [ ] Mark today complete
  - [ ] Add to completed topics
  - [ ] Note any weaknesses
  - [ ] Set next session plan
- [ ] Add new vocabulary: python maestro/scripts/vocab_tracker.py --add "..."
- [ ] Generate weekly report (if Day 5)
- [ ] Preview next session in user's language
- [ ] Give specific praise
- [ ] Encourage and say farewell in user's language + Spanish
```

## File Updates Summary

After each session, these files should be updated:

1. **progress.md**: Current status, completed topics, weaknesses, next plan
2. **vocabulary_data.json** (via vocab_tracker.py): New words or mastery updates
3. **weekly_reports/** (if Day 5): Generated analytics report

## Success Criteria

A successful session end includes:
- ✅ Student feels accomplished and encouraged
- ✅ Clear understanding of what was learned
- ✅ Any weaknesses acknowledged supportively
- ✅ All files updated accurately
- ✅ Next session expectations set
- ✅ Vocabulary properly tracked
- ✅ Student motivated to continue

**Time target**: 5-7 minutes

## Integration Points

**Session end transitions to**:
- Next session start: `protocols/session-start.md`
- Analytics: `scripts/progress_analyzer.py`
- Vocabulary: `scripts/vocab_tracker.py`

**Reference materials**:
- Language phrases: `config/language-templates.md`
- Progress template: `progress_template.md`
