# Language Templates for Multilingual Teaching

This file contains teaching language templates for different native languages. The system automatically selects the appropriate language based on user detection.

## Supported Languages

- English (en)
- Chinese Simplified (zh-CN)
- Chinese Traditional (zh-TW)
- French (fr)
- German (de)
- Japanese (ja)
- Korean (ko)
- Vietnamese (vi)
- Portuguese (pt)
- Italian (it)
- Russian (ru)
- Arabic (ar)

## Language Detection Protocol

1. **Explicit Declaration**: User states their language ("I speak English", "我说中文")
2. **First Message Detection**: Analyze first user message language
3. **Confirmation**: Ask user to confirm detected language
4. **Store in progress.md**: Save as `instruction_language: [code]`

## Language Usage Rules Template

The teaching language adapts based on user's native language while Spanish remains constant:

| Context | Language |
|---------|----------|
| Questions & Explanations | **User's Native Language** |
| Grammar Explanations | **User's Native Language** |
| Practice Instructions | **User's Native Language** |
| Teaching Content | **Spanish + English** |
| Example Sentences | **Spanish + English** |
| Corrections | **Spanish + User's Native Language** |
| Student Practice | **Spanish Only** |

## Common Phrases by Language

### English (en)
- Greeting: "Hello! Welcome back!"
- Lesson start: "Today we're going to learn..."
- Correction: "Good! But it should be '[correct]', because..."
- Encouragement: "Great job! Keep it up!"
- Question prompt: "Do you remember what we learned last time?"

### Chinese Simplified (zh-CN)
- Greeting: "你好！欢迎回来！"
- Lesson start: "今天我们要学习..."
- Correction: "很好！不过应该是'[correct]'，因为..."
- Encouragement: "干得好！继续加油！"
- Question prompt: "你还记得我们上次学了什么吗？"

### Chinese Traditional (zh-TW)
- Greeting: "你好！歡迎回來！"
- Lesson start: "今天我們要學習..."
- Correction: "很好！不過應該是'[correct]'，因為..."
- Encouragement: "幹得好！繼續加油！"
- Question prompt: "你還記得我們上次學了什麼嗎？"

### French (fr)
- Greeting: "Bonjour ! Bon retour !"
- Lesson start: "Aujourd'hui nous allons apprendre..."
- Correction: "Bien ! Mais ça devrait être '[correct]', parce que..."
- Encouragement: "Excellent travail ! Continue !"
- Question prompt: "Tu te souviens de ce qu'on a appris la dernière fois ?"

### German (de)
- Greeting: "Hallo! Willkommen zurück!"
- Lesson start: "Heute werden wir lernen..."
- Correction: "Gut! Aber es sollte '[correct]' sein, weil..."
- Encouragement: "Großartige Arbeit! Weiter so!"
- Question prompt: "Erinnerst du dich, was wir letztes Mal gelernt haben?"

### Japanese (ja)
- Greeting: "こんにちは！お帰りなさい！"
- Lesson start: "今日は...を学びます"
- Correction: "いいですね！でも'[correct]'であるべきです、なぜなら..."
- Encouragement: "素晴らしい！その調子で！"
- Question prompt: "前回学んだことを覚えていますか？"

### Korean (ko)
- Greeting: "안녕하세요! 다시 오신 것을 환영합니다!"
- Lesson start: "오늘은 ...을/를 배울 거예요"
- Correction: "좋아요! 하지만 '[correct]'이어야 해요, 왜냐하면..."
- Encouragement: "잘했어요! 계속하세요!"
- Question prompt: "지난번에 배운 것을 기억하세요?"

### Vietnamese (vi)
- Greeting: "Xin chào! Chào mừng trở lại!"
- Lesson start: "Hôm nay chúng ta sẽ học..."
- Correction: "Tốt! Nhưng nó phải là '[correct]', vì..."
- Encouragement: "Làm tốt lắm! Tiếp tục nhé!"
- Question prompt: "Bạn có nhớ những gì chúng ta đã học lần trước không?"

### Portuguese (pt)
- Greeting: "Olá! Bem-vindo de volta!"
- Lesson start: "Hoje vamos aprender..."
- Correction: "Bom! Mas deveria ser '[correct]', porque..."
- Encouragement: "Ótimo trabalho! Continue assim!"
- Question prompt: "Você se lembra do que aprendemos da última vez?"

### Italian (it)
- Greeting: "Ciao! Bentornato!"
- Lesson start: "Oggi impareremo..."
- Correction: "Bene! Ma dovrebbe essere '[correct]', perché..."
- Encouragement: "Ottimo lavoro! Continua così!"
- Question prompt: "Ti ricordi cosa abbiamo imparato l'ultima volta?"

### Russian (ru)
- Greeting: "Привет! Добро пожаловать обратно!"
- Lesson start: "Сегодня мы будем изучать..."
- Correction: "Хорошо! Но должно быть '[correct]', потому что..."
- Encouragement: "Отличная работа! Продолжай!"
- Question prompt: "Ты помнишь, что мы изучали в прошлый раз?"

### Arabic (ar)
- Greeting: "مرحبا! أهلا بعودتك!"
- Lesson start: "اليوم سنتعلم..."
- Correction: "جيد! لكن يجب أن يكون '[correct]'، لأن..."
- Encouragement: "عمل رائع! استمر!"
- Question prompt: "هل تتذكر ما تعلمناه المرة الماضية؟"

## Dynamic Language Selection

When teaching, Maestro should:

1. **Detect user language** from first interaction or progress.md
2. **Load appropriate template** from this file
3. **Adapt all explanations** to user's native language
4. **Keep Spanish content** unchanged (the target language)
5. **Use English as fallback** if user's language not supported

## Example Adaptation

### For Chinese Speaker:
```
Maestro: "今天我们要学习动词 'estar'（to be）。它用于描述位置和状态。"
Maestro: "例如：Estoy en casa (I am at home)"
Student: [practices in Spanish]
Maestro: "很好！不过应该是 'estás'，因为是第二人称单数。"
```

### For French Speaker:
```
Maestro: "Aujourd'hui nous allons apprendre le verbe 'estar' (être). Il est utilisé pour décrire la position et l'état."
Maestro: "Par exemple : Estoy en casa (Je suis à la maison)"
Student: [practices in Spanish]
Maestro: "Bien ! Mais ça devrait être 'estás', parce que c'est la deuxième personne du singulier."
```

### For German Speaker:
```
Maestro: "Heute werden wir das Verb 'estar' (sein) lernen. Es wird verwendet, um Position und Zustand zu beschreiben."
Maestro: "Zum Beispiel: Estoy en casa (Ich bin zu Hause)"
Student: [practices in Spanish]
Maestro: "Gut! Aber es sollte 'estás' sein, weil es die zweite Person Singular ist."
```

## Implementation Notes

- Store detected language in `~/spanish-learning/progress.md` as `instruction_language: [code]`
- Check language on every session start
- Allow user to change language: "Switch my instruction language to English"
- All curriculum content, grammar references, and scenarios remain language-neutral (Spanish examples with English translations)
- Only instructional text adapts to user's native language
