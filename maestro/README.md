# Maestro - Interactive Spanish Language Teacher 🇪🇸

**An intelligent, adaptive Spanish learning Skill for Claude Code**

Version: 1.2.1
Levels: A1 → A2 → B1 → B2 (CEFR Framework)
Languages: 12+ supported instruction languages
Environment: Claude Code (macOS, Linux, Windows)

---

## 🎯 What is Maestro?

Maestro is an **interactive Spanish language teacher** that goes far beyond traditional language learning tools. It combines:

✨ **Structured Curriculum** - 52 weeks of detailed lessons (A1 to B2)
🤖 **AI-Powered Adaptation** - Dynamically adjusts to your progress and needs
🌐 **Real-World Content** - Uses web search to fetch authentic Spanish materials
📊 **Progress Tracking** - Spaced repetition, analytics, and personalized reports
🗣️ **Interactive Practice** - Role-plays, conversations, not just grammar drills
🌍 **Multilingual Support** - Teach in 12+ languages (English, Chinese, French, German, Japanese, Korean, Vietnamese, Portuguese, Italian, Russian, Arabic, and more)
🇪🇸🇲🇽 **Regional Awareness** - Spain Spanish + Mexican Spanish + Latin American variants

### Key Differentiators

❌ **NOT** a fill-in-the-blank grammar drill system
❌ **NOT** a static textbook converted to AI
✅ **IS** an interactive teacher that responds to YOUR needs
✅ **IS** dynamic, using current web content for authentic practice
✅ **IS** data-driven, tracking your progress and optimizing teaching

---

## 📚 What You'll Learn

### A1 (Weeks 1-12) - Beginner
- Greetings, introductions, basic conversations
- Present tense verbs, daily routines
- Numbers, time, dates
- Family, home, shopping, restaurants
- **Goal**: Handle basic daily interactions

### A2 (Weeks 13-24) - Elementary
- Past tenses (preterite, imperfect)
- Future tense, comparisons
- Weather, commands, preferences
- Narrate past experiences
- **Goal**: Describe experiences and events

### B1 (Weeks 25-40) - Intermediate
- Subjunctive mood (all contexts)
- Conditional, hypotheticals
- Perfect tenses, complex sentences
- Express and justify opinions
- **Goal**: Independent communication

### B2 (Weeks 41-52) - Upper Intermediate
- Advanced subjunctive, passive voice
- Idioms, register, style
- Argumentation, nuanced expression
- Cultural depth
- **Goal**: Fluent, spontaneous, sophisticated communication

---

## 🌍 NEW in v1.2.0: Multilingual Support

**Maestro now speaks YOUR language!**

Learn Spanish with explanations and guidance in your native language. Whether you're from China, France, Germany, Japan, Korea, Vietnam, or anywhere else, Maestro adapts to teach you in the language you're most comfortable with.

### Supported Instruction Languages

| Language | Code | Example Greeting |
|----------|------|------------------|
| English | en | "Hello! Welcome back!" |
| Chinese (Simplified) | zh-CN | "你好！欢迎回来！" |
| Chinese (Traditional) | zh-TW | "你好！歡迎回來！" |
| French | fr | "Bonjour ! Bon retour !" |
| German | de | "Hallo! Willkommen zurück!" |
| Japanese | ja | "こんにちは！お帰りなさい！" |
| Korean | ko | "안녕하세요! 다시 오신 것을 환영합니다!" |
| Vietnamese | vi | "Xin chào! Chào mừng trở lại!" |
| Portuguese | pt | "Olá! Bem-vindo de volta!" |
| Italian | it | "Ciao! Bentornato!" |
| Russian | ru | "Привет! Добро пожаловать обратно!" |
| Arabic | ar | "مرحبا! أهلا بعودتك!" |

### How It Works

**Automatic Detection**: Maestro detects your language from your first message
**Smart Adaptation**: Grammar explanations in your language, practice in Spanish
**Flexible Switching**: Change instruction language anytime during learning

**Example (French speaker)**:
```
You: "Je veux apprendre l'espagnol"
Maestro: "Parfait ! Je vais t'enseigner en français. Commençons par une évaluation rapide..."
[Teaches Spanish with French explanations]
```

**Example (Japanese speaker)**:
```
You: "スペイン語を学びたい"
Maestro: "素晴らしい！日本語で説明します。まず簡単な評価から始めましょう..."
[Teaches Spanish with Japanese explanations]
```

### What Gets Translated

✅ **In your language**:
- Grammar explanations
- Instructions and objectives
- Error corrections (explanations)
- Encouragement and feedback
- Session structure and navigation

✅ **Always in Spanish** (you're learning it!):
- Practice exercises
- Vocabulary words
- Example sentences (with translations)
- Conversation scenarios

---

## 🚀 Quick Start

### 1. Installation

```bash
# Navigate to your spanish learning directory
cd ~/github/deadjoe/spanish

# You should see the maestro/ directory
ls maestro/

# Install Python dependencies
cd maestro
uv pip install -r requirements.txt
```

### 2. Create Your Learning Workspace

```bash
# Create your personal learning directory
mkdir -p ~/spanish-learning/{weekly_reports,practice_materials/{news,dialogues,exercises}}

# Copy progress template
cp ~/github/deadjoe/spanish/maestro/progress_template.md ~/spanish-learning/progress.md
```

### 3. Start Learning!

In Claude Code, simply say:

```
"我想开始学习西班牙语"
```

or

```
"I want to start learning Spanish"
```

Maestro will automatically activate and begin your initial assessment!

---

## 💡 How to Use Maestro

### Two Main Modes

#### 🎓 Mode 1: Structured Learning
**When**: You want to follow the curriculum
**How**: Say "开始今天的课程" or "继续学习"

Maestro will:
- Check your progress.md to see where you are
- Load the appropriate week/day content
- Follow structured lesson plan
- Provide interactive practice
- Update your progress at the end

**Example Session**:
```
You: "开始今天的课程"

Maestro: "你好！我们今天是 Week 3 Day 2。"
Maestro: "上次我们学了 estar 的位置用法，你还记得吗？"
[Quick review]
Maestro: "今天我们要学习用 estar 表达情绪。准备好了吗？"
[Teaching + Practice + Exercises]
Maestro: "太好了！我们今天学了 8 个新的情绪词汇。我已经更新了你的进度文件。"
```

#### 🎯 Mode 2: Quick Practice
**When**: You want to practice something specific
**How**: Say "我想练习..." or ask specific questions

Maestro will:
- Adapt to your current level
- Generate relevant practice
- Use web search for authentic materials
- Provide immediate feedback

**Example Session**:
```
You: "我想练习在餐厅点餐"

Maestro: [Reads your progress → sees you're A1 Week 4]
Maestro: [WebSearch: "menú restaurante Madrid 2025"]
Maestro: "太好了！我找到了马德里一家真实餐厅的菜单。"
Maestro: "假设你坐在这家咖啡馆，服务员过来了..."
Maestro (as waiter): "Buenos días, ¿qué desea tomar?"
[Interactive role-play continues...]
```

### Language Usage

**Maestro adapts to YOUR native language!**

- **Your questions → Maestro answers**: Your chosen language (Chinese, English, French, etc.)
- **Grammar explanations**: Your chosen language
- **Teaching content**: Spanish + English translations
- **Example sentences**: Spanish + English
- **Your practice**: Spanish (the language you're learning!)
- **Corrections**: Spanish + explanations in your language

**You can say**:
- "我想开始学习西班牙语" (Chinese)
- "I want to start learning Spanish" (English)
- "Je veux apprendre l'espagnol" (French)
- "Ich möchte Spanisch lernen" (German)
- "スペイン語を学びたい" (Japanese)
- ...and Maestro will adapt!

---

## 📊 Progress Tracking System

### Your progress.md File

Location: `~/spanish-learning/progress.md`

This is your **learning journal**. Maestro reads it at the start of each session and updates it at the end.

**What it tracks**:
- Current level, week, day
- This week's goals and checklist
- Completed topics
- Identified weaknesses
- Vocabulary to review
- Assessment scores
- Next session plan

### Vocabulary Tracking (Spaced Repetition)

Maestro uses a **spaced repetition algorithm** to help you memorize vocabulary:

```bash
# Check words due today
python maestro/scripts/vocab_tracker.py --due-today

# Add new words
python maestro/scripts/vocab_tracker.py --add "estar,ubicación,emoción"

# Update after review
python maestro/scripts/vocab_tracker.py --update "estar:correct,ubicación:wrong"

# See statistics
python maestro/scripts/vocab_tracker.py --stats
```

Maestro will use these commands **automatically** during sessions.

### Weekly Reports

Every Friday (or end of Week X Day 5):

```bash
python maestro/scripts/progress_analyzer.py --generate-report weekly
```

Generates: `~/spanish-learning/weekly_reports/YYYY-WXX.md`

Contains:
- Summary of achievements
- Strengths and weaknesses
- Vocabulary mastery stats
- Next week goals
- Personalized recommendations

---

## 🎨 Unique Features

### 1. Dynamic Web Content

Maestro **searches the web** for authentic Spanish materials:
- Real restaurant menus (current prices!)
- Actual news articles
- Rental listings
- Social media posts
- Cultural events

**Example**:
```
You: "我想了解西班牙租房"
Maestro: [WebSearch: "anuncios alquiler Madrid 2025"]
Maestro: "我找到了几个马德里的真实租房广告..."
[Teaches vocabulary from REAL listings]
[Practice writing an inquiry email]
```

### 2. Adaptive Difficulty

Maestro adjusts based on your performance:
- Struggling? → Slows down, more examples, simpler exercises
- Excelling? → Increases challenge, introduces advanced content
- Always at the **edge of your ability** (optimal learning zone)

### 3. Regional Spanish

Learn BOTH Spain and Mexico Spanish:
- Vocabulary: "ordenador" (Spain) vs "computadora" (Mexico)
- Grammar: "vosotros" (Spain) vs "ustedes" (Mexico/LA)
- Pronunciation: distinción vs seseo
- Cultural differences

Every **Week X Day 5** includes regional comparison lesson.

### 4. Scenario-Based Learning

Not just grammar drills - **real situations**:
- 🏨 Checking into a hotel
- 🍽️ Ordering at a restaurant
- 🛍️ Shopping for clothes
- 🗺️ Asking for directions
- 💼 Job interview
- 👥 Making friends

### 5. Comprehensive Assessments

Every 5th day = assessment:
- 4 dimensions: Grammar, Vocabulary, Fluency, Comprehension
- Detailed feedback with specific examples
- Track progress over time
- Identify patterns in errors
- Advance when ready (3 consecutive assessments ≥80/100)

---

## 🗂️ File Structure

```
maestro/
├── SKILL.md                          # Core hub (v1.2.1 - optimized, 482 lines)
├── config/
│   └── language-templates.md        # Multilingual phrase templates (NEW)
├── workflows/                        # Modular workflows (NEW)
│   ├── structured-learning.md       # Type 1 sessions
│   ├── quick-practice.md            # Type 2 sessions
│   ├── assessment.md                # Type 3 sessions
│   └── initial-assessment.md        # New student evaluation
├── protocols/                        # Session protocols (NEW)
│   ├── session-start.md             # Opening protocol
│   ├── session-end.md               # Closing protocol
│   └── correction-principles.md     # Error correction guidelines
├── practice-types/                   # Practice strategies (NEW)
│   ├── exercises.md                 # All practice types
│   └── content-strategy.md          # Web search & content usage
├── curriculum/
│   ├── A1_curriculum.md             # Weeks 1-12 detailed
│   ├── A2_curriculum.md             # Weeks 13-24 detailed
│   ├── B1_curriculum.md             # Weeks 25-40 detailed
│   └── B2_curriculum.md             # Weeks 41-52 detailed
├── teaching_guides/
│   ├── assessment_rubrics.md        # Scoring standards
│   ├── grammar_reference.md         # 22 grammar topics (689 lines) ⭐ NEW
│   ├── regional_differences.md      # Spain vs Mexico vs LA
│   └── scenarios.md                 # 35 graded dialogues (865 lines) ⭐ NEW
├── scripts/
│   ├── vocab_tracker.py             # Spaced repetition (env var support) ⭐ NEW
│   ├── progress_analyzer.py         # Reports and analytics
│   ├── content_fetcher.py           # Web content retrieval
│   └── practice_generator.py        # Exercise generation
├── resources/
│   ├── cultural_notes.md            # Cultural guide (634 lines) ⭐ NEW
│   └── vocabulary_lists/
│       ├── A1_vocabulary.md         # 500+ beginner words
│       ├── A2_vocabulary.md         # 1200+ elementary words ⭐ NEW
│       ├── B1_vocabulary.md         # 1500+ intermediate words ⭐ NEW
│       └── B2_vocabulary.md         # 2000+ upper-intermediate ⭐ NEW
├── requirements.txt                  # Python dependencies
├── progress_template.md              # Template for students
└── README.md                         # This file!
```

**v1.2.1 Content Expansion** ⭐ NEW:
- 📚 Comprehensive teaching resources: +3900 lines of high-quality content
- 📖 Extended vocabulary: A1-B2 totaling 5200+ words
- 💬 35 graded dialogues across all CEFR levels
- 🌍 Cultural guide covering Spain, Mexico, Argentina, Latin America
- 📝 22 comprehensive grammar topics with 213+ examples

**v1.2.0 Architecture**:
- ✨ Progressive disclosure: Main SKILL.md optimized to 482 lines
- 🗂️ Modular organization: Workflows and protocols separated for efficiency
- 🌍 Multilingual templates: Support for 12+ languages
- 📈 Optimized token usage: 60-70% reduction in unnecessary context loading
- ✅ Aligned with Anthropic's 2025 best practices

---

## 🎓 Learning Philosophy

### The Maestro Approach

1. **Interactive, not passive** - Constant dialogue, not lectures
2. **Spiral learning** - Assess → Plan → Teach → Test → Feedback → Repeat
3. **Practical focus** - Real-world usage over academic grammar
4. **Data-driven** - Track progress, identify patterns, optimize
5. **Authentic materials** - Current, real Spanish content
6. **Cultural competence** - Language + culture together

### What Makes Maestro Different

| Traditional Apps | Maestro |
|-----------------|---------|
| Fixed lessons | Adapts to YOUR progress |
| Static content | Live web content |
| Grammar drills | Interactive scenarios |
| One-size-fits-all | Personalized feedback |
| No memory | Spaced repetition tracking |
| Single variant | Spain + Mexico + LA |

---

## 📈 Expected Timeline

**Casual learner** (3-4 sessions/week, 30-45 min each):
- A1 completion: ~3-4 months
- A2 completion: ~6-8 months
- B1 completion: ~12-15 months
- B2 completion: ~18-24 months

**Intensive learner** (daily sessions, 1 hour each):
- A1 completion: ~6-8 weeks
- A2 completion: ~3-4 months
- B1 completion: ~6-8 months
- B2 completion: ~10-12 months

**Note**: Varies by individual, prior language experience, and practice intensity.

---

## 🛠️ Troubleshooting

### Issue: Maestro doesn't activate
**Solution**: Say explicitly "我想学习西班牙语" or "Start Spanish lesson"

### Issue: Progress not saved
**Solution**: Check that `~/spanish-learning/progress.md` exists and is writable

### Issue: Python scripts not working
**Solution**:
```bash
cd ~/github/deadjoe/spanish/maestro
uv pip install -r requirements.txt
```

### Issue: Want to reset progress
**Solution**:
```bash
# Backup first
cp ~/spanish-learning/progress.md ~/spanish-learning/progress_backup.md

# Copy fresh template
cp ~/github/deadjoe/spanish/maestro/progress_template.md ~/spanish-learning/progress.md
```

---

## 🤝 Tips for Success

### Do's ✅
- ✅ Practice consistently (even 20 min/day better than 3 hours once/week)
- ✅ Speak out loud during practice (even if alone!)
- ✅ Review vocabulary daily (use spaced repetition)
- ✅ Ask questions when confused
- ✅ Embrace mistakes - they're learning opportunities
- ✅ Use Spanish outside lessons (music, movies, apps)
- ✅ Track your progress regularly
- ✅ Celebrate small wins!

### Don'ts ❌
- ❌ Don't rush through lessons just to "finish"
- ❌ Don't skip assessments (they identify gaps)
- ❌ Don't fear making errors in practice
- ❌ Don't compare your pace to others
- ❌ Don't study only grammar without speaking
- ❌ Don't ignore weaknesses - address them!

---

## 🌟 Success Stories & Goals

### A1 Completion
**You can**:
- Introduce yourself and have basic conversations
- Order food at restaurants
- Ask for directions
- Talk about your daily routine
- Handle simple everyday situations

### A2 Completion
**You can**:
- Tell stories about past experiences
- Describe future plans
- Express preferences and opinions
- Handle most travel situations
- Write simple emails and texts

### B1 Completion
**You can**:
- Discuss abstract topics
- Express and justify opinions
- Handle unexpected situations
- Understand most everyday conversations
- Write structured texts

### B2 Completion
**You can**:
- Interact fluently with native speakers
- Understand complex texts and implicit meanings
- Participate in professional meetings
- Write sophisticated essays and reports
- Function independently in Spanish-speaking environment
- **Live, work, or study in Spain/Latin America!**

---

## 📞 Support & Community

### Get Help
- **In-lesson questions**: Just ask! "这个语法点是什么意思?"
- **Technical issues**: Check troubleshooting section above
- **Feature requests**: Note for future skill updates

### Stay Motivated
- Set specific goals: "By March, I'll finish A1"
- Find language exchange partners
- Watch Spanish content with subtitles
- Join Spanish learning communities online
- Track your "streak" of consecutive days

---

## 🎉 Ready to Start?

### Your First Session

1. **Create workspace** (if not done):
   ```bash
   mkdir -p ~/spanish-learning
   cp maestro/progress_template.md ~/spanish-learning/progress.md
   ```

2. **Open Claude Code** and say:
   ```
   "我想开始学习西班牙语"
   ```

3. **Complete initial assessment** (20-30 minutes)
   - Maestro will ask about your goals
   - Test your current level
   - Create personalized learning plan

4. **Start Week 1 Day 1!**

---

## 📜 License & Credits

**Created by**: Joe (with Claude's assistance)
**Version**: 1.2.1
**Date**: January 2025
**For**: Personal use and learning

**Version History**:
- **v1.2.1** (2025-01): Content expansion (+3900 lines), comprehensive resources (cultural notes, extended vocabularies, 35 dialogues, 22 grammar topics)
- **v1.2.0** (2025-01): Multilingual support, progressive disclosure architecture, Anthropic best practices alignment
- **v1.1.0** (2024-12): Enhanced curriculum structure, Python analytics scripts
- **v1.0.0** (2024-11): Initial release

**Based on**:
- CEFR (Common European Framework of Reference for Languages)
- Communicative language teaching methodology
- Spaced repetition research
- Real-world Spanish usage

---

## 🚀 Let's Begin!

**"El viaje de mil millas comienza con un paso."**
*(The journey of a thousand miles begins with one step.)*

Open Claude Code and say:

```
"Hola, Maestro. 我准备好学习西班牙语了！"
```

¡Vamos! Let's go! 加油！

---

*Maestro - Your personal Spanish teacher, powered by AI* 🤖🇪🇸
