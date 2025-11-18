# Maestro Quick Start Guide 🚀

## 5-Minute Setup

### Step 1: Verify Installation

You're already in the right place! Check that everything is here:

```bash
cd ~/github/deadjoe/spanish/maestro
ls -la
# You should see: SKILL.md, curriculum/, scripts/, teaching_guides/, etc.
```

### Step 2: Install Dependencies (Already Done!)

```bash
# Dependencies are already installed
python3 scripts/vocab_tracker.py --help  # Test - should show help
```

### Step 3: Create Your Learning Workspace

```bash
# Create your personal learning directory
mkdir -p ~/spanish-learning/{weekly_reports,practice_materials/{news,dialogues,exercises}}

# Copy progress template
cp progress_template.md ~/spanish-learning/progress.md

# Verify
ls ~/spanish-learning/
# Should see: progress.md, weekly_reports/, practice_materials/
```

### Step 4: Move maestro/ to Claude Skills Directory

**IMPORTANT**: For Claude Code to recognize this as a Skill, move it to the appropriate location:

```bash
# Option 1: Check if you have a skills directory
ls ~/.config/claude/skills/ 2>/dev/null

# Option 2: Or check in Documents
ls ~/Documents/Claude/skills/ 2>/dev/null

# If skills directory exists, move maestro there:
# mv ~/github/deadjoe/spanish/maestro ~/.config/claude/skills/
# OR
# mv ~/github/deadjoe/spanish/maestro ~/Documents/Claude/skills/

# For now, keep it where it is for testing - Claude Code should find it
```

### Step 5: Start Learning!

Open **Claude Code** and say any of these:

```
"我想开始学习西班牙语"
"I want to learn Spanish"
"Start Spanish lesson"
"Quiero aprender español"
```

Maestro will automatically activate! 🎉

---

## Your First Session

### What Will Happen:

1. **Greeting**: Maestro introduces itself
2. **Initial Assessment** (~20 minutes):
   - Your learning goals
   - Current Spanish level test
   - Vocabulary test (10-15 words)
   - Basic grammar test
   - Simple conversation
3. **Level Determination**: A1 / A2 / B1 / B2
4. **First Lesson Begins!**

### Example First Session:

```
You: "我想开始学习西班牙语"

Maestro: "¡Hola! 你好！我是 Maestro，你的西班牙语老师。
         我会通过互动对话和实践来帮你学习西班牙语，
         而不是填鸭式的语法教学。

         在开始之前，我需要了解你的水平。
         我们先做个简单的评估，大约20分钟，好吗？"

You: "好的"

Maestro: "太好了！第一个问题：
         你学西班牙语的目标是什么？旅游、工作、兴趣还是其他？"

[... assessment continues ...]

Maestro: "评估完成！根据你的表现，我建议从 A1 级别开始。
         我已经创建了你的学习计划和进度文件。

         现在，让我们开始 Week 1 Day 1: 西班牙语字母和基本问候！
         准备好了吗？"

You: "准备好了！"

Maestro: "很好！首先，西班牙语有27个字母..."
```

---

## Common Commands

### During Structured Learning:

```
"开始今天的课程"  - Continue structured curriculum
"继续学习"        - Same as above
"复习一下"        - Review previous lesson
"我不太懂"        - Ask for clarification
```

### For Quick Practice:

```
"我想练习..."
"我想练习在餐厅点餐"
"我想复习 ser 和 estar 的区别"
"给我一些练习题"
```

### Checking Progress:

```
"我的进度怎么样？"
"我掌握了多少词汇？"
"我还有哪些薄弱点？"
```

### Asking Questions:

```
"ser 和 estar 有什么区别？"
"这个语法点是什么意思？"
"墨西哥人会怎么说这个？"
```

---

## Using Python Scripts Manually

### Vocabulary Tracker:

```bash
# See words due for review today
python3 ~/github/deadjoe/spanish/maestro/scripts/vocab_tracker.py --due-today

# Add new words
python3 ~/github/deadjoe/spanish/maestro/scripts/vocab_tracker.py --add "hola,gracias,adiós"

# Check statistics
python3 ~/github/deadjoe/spanish/maestro/scripts/vocab_tracker.py --stats
```

### Progress Analyzer:

```bash
# See current progress
python3 ~/github/deadjoe/spanish/maestro/scripts/progress_analyzer.py --stats

# Generate weekly report
python3 ~/github/deadjoe/spanish/maestro/scripts/progress_analyzer.py --generate-report weekly

# Analyze weaknesses
python3 ~/github/deadjoe/spanish/maestro/scripts/progress_analyzer.py --analyze weaknesses
```

**Note**: Maestro will use these scripts **automatically** during sessions. You rarely need to run them manually.

---

## Typical Learning Flow

### Week Structure:

- **Day 1-4**: New content + practice
- **Day 5**: Assessment + regional differences

### Daily Session (~30-45 minutes):

1. **Opening** (5 min): Review last lesson
2. **Objectives** (2 min): Today's goals
3. **Teaching** (10-15 min): New content
4. **Practice** (20-30 min): Interactive exercises
5. **Closing** (5 min): Summary + update progress

### Monthly Rhythm:

- **Week 1**: New topic introduction
- **Week 2**: Expansion and practice
- **Week 3**: Application and integration
- **Week 4**: Review and consolidation

---

## Tips for First Week

### Do:
✅ Complete all 5 days of Week 1
✅ Practice speaking out loud (even if alone!)
✅ Review your progress.md daily
✅ Ask questions when confused
✅ Embrace mistakes

### Don't:
❌ Rush through just to finish
❌ Skip Day 5 assessment
❌ Be afraid to make errors
❌ Study in silence - speak!

---

## Quick Reference

### Your Files:
- **Progress file**: `~/spanish-learning/progress.md`
- **Vocabulary data**: `~/spanish-learning/vocabulary_data.json`
- **Weekly reports**: `~/spanish-learning/weekly_reports/`
- **Practice materials**: `~/spanish-learning/practice_materials/`

### Skill Files:
- **Main skill**: `~/github/deadjoe/spanish/maestro/SKILL.md`
- **Curriculum**: `~/github/deadjoe/spanish/maestro/curriculum/`
- **Scripts**: `~/github/deadjoe/spanish/maestro/scripts/`

### Key Numbers:
- **Total weeks**: 52 (A1→B2)
- **Days per week**: 5
- **Total vocabulary**: 4000+ words
- **Assessment frequency**: Every 5th day
- **Advancement requirement**: 3 consecutive assessments ≥80/100

---

## Troubleshooting

### Maestro doesn't activate?
```
Say explicitly: "我想学习西班牙语" or "Use maestro skill"
```

### Progress not saving?
```bash
# Check file exists and is writable
ls -la ~/spanish-learning/progress.md
# If not, copy template:
cp ~/github/deadjoe/spanish/maestro/progress_template.md ~/spanish-learning/progress.md
```

### Scripts don't work?
```bash
# Check Python and packages
python3 --version  # Should be 3.x
python3 -c "import requests" # Should not error
```

### Want to start over?
```bash
# Backup current progress
cp ~/spanish-learning/progress.md ~/spanish-learning/progress_backup_$(date +%Y%m%d).md
# Copy fresh template
cp ~/github/deadjoe/spanish/maestro/progress_template.md ~/spanish-learning/progress.md
```

---

## Next Steps

After your first session:

1. ✅ **Review** your `progress.md` file
2. ✅ **Check** vocabulary due for review
3. ✅ **Plan** your next session
4. ✅ **Practice** a little Spanish each day
5. ✅ **Enjoy** the journey!

---

## Need Help?

### During Sessions:
- Just ask Maestro: "我有个问题..."
- Request clarification: "请再解释一遍"
- Ask for examples: "给我一些例子"

### Outside Sessions:
- Re-read README.md for detailed info
- Check curriculum files for week plans
- Review teaching guides for specific topics

---

## Ready? Let's Go! 🎉

```
Open Claude Code and say:

"Hola, Maestro. 我准备好学习西班牙语了！"
```

**¡Buena suerte! 加油！Good luck!** 🇪🇸🤖

---

*From zero to fluent Spanish - your journey starts now!*
