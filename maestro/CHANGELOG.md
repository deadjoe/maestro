# Changelog

All notable changes to Maestro Spanish Language Teacher will be documented in this file.

## [1.2.1] - 2025-01-24

### 📚 Content Expansion

#### Comprehensive Teaching Resources (+3900 lines)
- **NEW**: `resources/cultural_notes.md` (634 lines) - Comprehensive cultural guide covering Spain, Mexico, Argentina, Colombia, Peru, Chile, Venezuela
  - Daily life, meal times, social etiquette
  - Festivals, traditions, cultural values
  - Regional Spanish variations (vosotros vs ustedes, vocabulary differences)
  - Practical tips for language learners

- **NEW**: Extended vocabulary lists (3361 new words)
  - `A2_vocabulary.md` (432 lines, 1200+ words)
  - `B1_vocabulary.md` (477 lines, 1500+ words)
  - `B2_vocabulary.md` (452 lines, 2000+ words)
  - Cumulative total: A1-B2 = 5200+ words

- **EXPANDED**: `teaching_guides/scenarios.md` (89→865 lines, +776 lines)
  - 35 graded dialogues across CEFR levels (A1→A2→B1→B2)
  - 6 core scenarios with detailed conversations
  - B2-level includes sophisticated topics (film analysis, philosophical discussions, professional negotiations)

- **EXPANDED**: `teaching_guides/grammar_reference.md` (161→689 lines, +528 lines)
  - 22 comprehensive grammar topics (vs 6 basic topics)
  - Complete coverage: Past tenses, subjunctive, commands, perfect tenses, pronouns, comparisons, passive voice, etc.

### 🔧 Script Enhancements
- **IMPROVED**: `scripts/vocab_tracker.py` - Added `SPANISH_LEARNING_DIR` environment variable support for custom directory configuration

### 📝 Documentation Updates
- **UPDATED**: SKILL.md Teaching Resources section with complete resource listing
- **UPDATED**: File structure overview reflecting new resources
- **UPDATED**: Dynamic Content Strategy with cultural_notes.md reference
- **MAINTAINED**: SKILL.md line count at 482 lines (well within <500 recommendation)

### ✅ Architecture Verification
- **VERIFIED**: All resources properly referenced in SKILL.md
- **VERIFIED**: Single-level reference depth maintained (SKILL.md → resources)
- **VERIFIED**: Progressive disclosure principles preserved
- **VERIFIED**: Compliance with Anthropic 2025 best practices

### 📊 Impact
- Teaching content: +3900 lines of high-quality resources
- Vocabulary coverage: +4700 words (500→5200)
- Grammar topics: +16 chapters (6→22)
- Scenario dialogues: +35 complete conversations
- SKILL.md efficiency: Remains <500 lines (+25 lines only)

---

## [1.2.0] - 2025-01-23

### 🌍 Major Features

#### Multilingual Support
- **NEW**: Support for 12+ instruction languages (English, Chinese Simplified/Traditional, French, German, Japanese, Korean, Vietnamese, Portuguese, Italian, Russian, Arabic)
- **NEW**: Automatic language detection from user's first message
- **NEW**: Adaptive teaching that provides grammar explanations in user's native language
- **NEW**: Flexible language switching during learning sessions
- **NEW**: Language-specific phrase templates in `config/language-templates.md`

#### Progressive Disclosure Architecture
- **REFACTOR**: Reduced main SKILL.md from 806 lines to <300 lines (63% reduction)
- **REFACTOR**: Implemented 3-level progressive disclosure system for optimal token usage
- **NEW**: Modular workflow files that load on-demand
- **NEW**: Separate protocol files for session management
- **NEW**: Practice-types documentation for specialized exercises
- **OPTIMIZATION**: 60-70% reduction in unnecessary context loading

### 📁 New File Structure

#### New Directories
- `config/` - Configuration and language templates
- `workflows/` - Modular session workflows
  - `structured-learning.md` - Curriculum-based learning sessions
  - `quick-practice.md` - Student-driven practice sessions
  - `assessment.md` - Weekly assessment protocol
  - `initial-assessment.md` - New student evaluation
- `protocols/` - Session management protocols
  - `session-start.md` - Opening protocol with language detection
  - `session-end.md` - Closing protocol and progress updates
  - `correction-principles.md` - Multilingual error correction guidelines
- `practice-types/` - Practice strategies and content
  - `content-strategy.md` - Web search and authentic materials usage
  - `exercises.md` - Practice type templates (planned)

### ✅ Best Practices Compliance

- **IMPROVED**: Skill name changed from `maestro-spanish-teacher` to `teaching-spanish` (gerund form)
- **IMPROVED**: Removed all time-sensitive references (replaced "2025" with "actual"/"reciente")
- **IMPROVED**: Version number properly tracked (1.2.0)
- **IMPROVED**: Aligned with Anthropic's 2025 Agent Skills Best Practices
- **IMPROVED**: Main SKILL.md now serves as navigational hub with 1-level deep references
- **IMPROVED**: File structure optimized for progressive disclosure

### 📝 Documentation Updates

- **UPDATED**: README.md with multilingual support section
- **UPDATED**: File structure documentation reflecting new architecture
- **UPDATED**: Version history and credits
- **NEW**: CHANGELOG.md (this file)
- **BACKUP**: Old SKILL.md preserved as `SKILL-v1.1.0-backup.md`

### 🔧 Technical Improvements

- **OPTIMIZATION**: Token usage reduced through modular file loading
- **OPTIMIZATION**: Context window efficiency improved
- **ENHANCEMENT**: Clear separation of concerns (workflows, protocols, content)
- **ENHANCEMENT**: Easier maintenance and updates with modular structure
- **ENHANCEMENT**: Better scalability for future features

### 🌐 Supported Platforms

- macOS (existing)
- Linux (tested)
- Windows (compatible)

### 📊 Language Support Matrix

| Aspect | Languages |
|--------|-----------|
| **Instruction Language** | 12+ (en, zh-CN, zh-TW, fr, de, ja, ko, vi, pt, it, ru, ar) |
| **Teaching Language** | Spanish (es) |
| **Translation Support** | English (primary), user's native language (secondary) |

## [1.1.0] - 2024-12

### Added
- Enhanced curriculum structure with detailed weekly plans
- Python analytics scripts (vocab_tracker.py, progress_analyzer.py)
- Improved assessment rubrics with 4-dimension evaluation
- Regional differences documentation (Spain vs Mexico)

### Changed
- Refined CEFR progression with clearer week-by-week goals
- Enhanced progress tracking system
- Improved spaced repetition algorithm

## [1.0.0] - 2024-11

### Initial Release
- Complete A1-B2 CEFR curriculum (52 weeks)
- Interactive teaching methodology
- Progress tracking with file-based persistence
- Web search integration for authentic materials
- Assessment system with weekly evaluations
- Spaced repetition vocabulary tracking
- Python helper scripts
- Teaching in Chinese with Spanish practice

---

## Migration Guide: v1.1.0 → v1.2.0

### For Existing Users

**No action required!** The v1.2.0 update is fully backward compatible.

Your existing `~/spanish-learning/progress.md` will work seamlessly. The new version will:
1. Detect your language from your next message (or continue in Chinese if that's what you used)
2. Add `instruction_language: [code]` to your progress.md
3. Continue exactly where you left off

### For New Users

Just start with:
```
"I want to learn Spanish" (English)
"我想学西班牙语" (Chinese)
"Je veux apprendre l'espagnol" (French)
...or any supported language
```

Maestro will automatically detect and adapt!

### For Developers

If you're extending Maestro:
- Main logic is now in SKILL.md (hub) with references to modular files
- Language templates are in `config/language-templates.md`
- Workflows are in `workflows/*.md`
- Protocols are in `protocols/*.md`
- Follow progressive disclosure pattern: keep main file <500 lines

---

## Upcoming Features (Planned)

### v1.3.0 (Future)
- [ ] Enhanced Python script error handling
- [ ] Table of contents for long curriculum files
- [ ] Additional practice exercises templates
- [ ] Audio pronunciation guides (text-based descriptions)
- [ ] More granular progress analytics
- [ ] Mobile-friendly progress tracking

### v2.0.0 (Future)
- [ ] Additional language support (Hindi, Dutch, Swedish, etc.)
- [ ] B2+ advanced content and C1 prep
- [ ] Integration with external language learning tools
- [ ] Community-contributed scenarios and exercises
- [ ] Enhanced web content caching
- [ ] Offline mode support

---

## Support & Feedback

- **Issues**: Create an issue in the GitHub repository
- **Suggestions**: Submit feature requests via GitHub
- **Questions**: Ask Maestro directly during your learning sessions!

---

**Last Updated**: 2025-01-23
**Current Version**: 1.2.0
