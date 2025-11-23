# Changelog

All notable changes to Maestro Spanish Language Teacher will be documented in this file.

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
