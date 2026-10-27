import tkinter as tk
import random
import os

topics_data = {
    "ביולוגיה": {
        "גוף האדם": [
            {"q": "מהו תפקיד תאי הדם האדומים בגוף האדם?", "opts": ["הגנה מפני חיידקים", "הובלת חמצן לתאי הגוף", "קרישת דם", "ייצור נוגדנים"], "ans": 1},
            {"q": "איזה איבר בגוף אחראי על סינון רעלים וייצור מרה?", "opts": ["הכבד", "הכליות", "הלבלב", "הקיבה"], "ans": 0},
            {"q": "מהו תפקיד הלב במערכת ההובלה?", "opts": ["לשאוב דם לכל חלקי הגוף", "לייצר חמצן", "לפרק מזון", "לסנן רעלים"], "ans": 0},
            {"q": "איזו מערכת בגוף אחראית על הגנה מפני מחלות וזיהומים?", "opts": ["המערכת החיסונית", "מערכת העיכול", "מערכת הנשימה", "המערכת ההורמונלית"], "ans": 0},
            {"q": "איזה חלק במוח אחראי על שמירת שיווי המשקל וקואורדינציה?", "opts": ["המוח הגדול", "המוח הקטן (צ'רבלום)", "גזע המוח", "ההיפותלמוס"], "ans": 1}
        ],
        "תאים ואברועים": [
            {"q": "מה תפקיד המיטוכונדריה בתא?", "opts": ["ייצור אנרגיה (ATP)", "אחסון מים", "בניית דופן התא", "ייצור חלבונים"], "ans": 0},
            {"q": "מהו תפקיד גרעין התא?", "opts": ["ייצור אנרגיה", "שמירה על החומר הגינטי (DNA)", "הקניית צבע ירוק לתא", "סינון חומרים"], "ans": 1},
            {"q": "איזה אברון אחראי על ייצור חלבונים בתא?", "opts": ["ריבוזום", "ליזוזום", "מיטוכונדריה", "גרעינון"], "ans": 0},
            {"q": "אילו אברועים קיימים בתא צמח אך לא בתא בעל חיים?", "opts": ["מיטוכונדריה וריבוזומים", "קרום התא וגרעין", "דופן התא וכלורופלסטים", "ציטופלזמה בלבד"], "ans": 2}
        ],
        "אקולוגיה וסביבה": [
            {"q": "כיצד נקראים יצורים המייצרים לעצמם מזון בתהליך הפוטוסינתזה?", "opts": ["יצרנים (אוטוטרופים)", "צרכנים ראשוניים", "מפרקים", "טפילים"], "ans": 0},
            {"q": "מהו תפקידם של חיידקים ופטריות במערכת אקולוגית?", "opts": ["מפרקים", "יצרנים", "טורפי על", "מאביקים"], "ans": 0}
        ],
        "גנטיקה ותורשה": [
            {"q": "מהם ראשי התיבות של החומר התורשתי בתא?", "opts": ["RNA", "DNA", "ATP", "pH"], "ans": 1},
            {"q": "איזה מבנה יש למולקולת ה-DNA?", "opts": ["סליל כפול", "מעגל סגור", "ריבוע תלת-ממדי", "שרשרת ישרה יחידה"], "ans": 0}
        ],
        "מערכת העיכול והנשימה": [
            {"q": "איפה מתחיל תהליך העיכול בגוף האדם?", "opts": ["בפה (בעזרת הרוק והשיניים)", "בקיבה", "במעי הדק", "באיבר הוושט"], "ans": 0},
            {"q": "איזה שריר עיקרי אחראי על פעולת הנשימה ועליית/ירידת בית החזה?", "opts": ["הסרעפת", "הלב", "שריר הריאה", "הכבד"], "ans": 0}
        ],
        "מיקרואורגניזמים וחיידקים": [
            {"q": "האם כל החיידקים גורמים למחלות?", "opts": ["לא, רבים מהם חיוניים ואף מועילים לגוף", "כן, כולם רעילים", "רק חיידקי הים", "רק חיידקים שחורים"], "ans": 0},
            {"q": "לאיזו ממלכה שייכים חיידקים מבחינה ביולוגית?", "opts": ["פרוקריוטים (חד-תאיים חסרי גרעין אמיתי)", "אוקריוטים", "פטריות ענק", "צמחים עילאיים"], "ans": 0}
        ]
    },
    "כימיה": {
        "יסודות וסימולים": [
            {"q": "מהו הסימול הכימי של מים?", "opts": ["CO2", "H2O", "NaCl", "O2"], "ans": 1},
            {"q": "מהו הסימול הכימי של מלח בישול?", "opts": ["HCl", "NaOH", "NaCl", "H2SO4"], "ans": 2}
        ],
        "חומרים ותהליכים": [
            {"q": "איזה גז חיוני לנשימה ולתהליכי בעירה?", "opts": ["חמצן", "מימן", "חנקן", "הליום"], "ans": 0},
            {"q": "מהו מצב הצבירה של כספית בטמפרטורת החדר?", "opts": ["מוצק", "נוזל", "גז", "פלזמה"], "ans": 1}
        ],
        "מבנה האטום": [
            {"q": "אילו חלקיקים נמצאים בגרעין האטום?", "opts": ["פרוטונים וניטרונים", "אלקטרונים בלבד", "פרוטונים ואלקטרונים", "גרעינים זעירים"], "ans": 0},
            {"q": "מהו המטען החשמלי של ניטרון בתוך האטום?", "opts": ["חיובי", "שלילי", "ניטרלי (ללא מטען)", "משתנה"], "ans": 2}
        ],
        "תגובות כימיות וחומצות": [
            {"q": "מהו תוצר הלוואי העיקרי בתגובת סתירות (ניטרול) בין חומצה לבסיס?", "opts": ["מלח ומים", "גז חמצן בלבד", "פחמן שחור", "חומצה חזקה"], "ans": 0}
        ],
        "אנרגיה ומצבי צבירה": [
            {"q": "כיצד נקרא מעבר חומר ממצב נוזל לגז?", "opts": ["אידוי (או רתיחה)", "התכה", "הקפאה", "סובלימציה"], "ans": 0},
            {"q": "מה קורה למהירות החלקיקים בחומר כאשר מחממים אותו?", "opts": ["היא גדלה והם נעשים מהירים יותר", "היא קטנה", "החלקיקים נעצרים לחלוטין", "אין שינוי"], "ans": 0}
        ]
    },
    "מתמטיקה": {
        "כפל וחילוק": "infinite_mult_div",
        "חיבור וחיסור": "infinite_add_sub",
        "שברים ואחוזים": "infinite_fractions",
        "משוואות פשוטות": "infinite_equations",
        "חזקות ושורשים": "infinite_powers",
        "גיאומטריה ושטחים": "infinite_geometry"
    },
    "אנגלית": {
        "מילים יומיומיות": [
            {"word": "Apple", "translation": "תפוח"},
            {"word": "Dog", "translation": "כלב"}
        ],
        "מילים מתקדמות": [
            {"word": "Computer", "translation": "מחשב"},
            {"word": "Environment", "translation": "סביבה"}
        ],
        "פעלים נפוצים": [
            {"word": "Run", "translation": "לרוץ"},
            {"word": "Sleep", "translation": "לישון"}
        ],
        "שמות תואר והפכים": [
            {"word": "Big", "translation": "גדול"},
            {"word": "Cold", "translation": "קר"}
        ],
        "ביטויים לטיולים ונסיעות": [
            {"word": "Airport", "translation": "שדה תעופה"},
            {"word": "Ticket", "translation": "כרטיס"},
            {"word": "Hotel", "translation": "מלון"},
            {"word": "Passport", "translation": "דרכון"}
        ]
    }
}

current_category = None
current_subtopic = None
current_level = None
flashcards = []
current_index = 0
score = 0
answered = False
timer_seconds = 15
timer_id = None
hint_used = False
total_questions_count = 10
wrong_questions_pool = []
is_review_mode = False

themes = {
    "dark": {"bg": "#0f172a", "fg": "#38bdf8", "btn_bg": "#334155", "text": "#ffffff"},
    "neon": {"bg": "#050505", "fg": "#00ffcc", "btn_bg": "#1a1a2e", "text": "#00ffcc"}
}
current_theme = "dark"

def load_high_score(key):
    if not os.path.exists("studylens_scores.txt"):
        return 0
    try:
        with open("studylens_scores.txt", "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split(":")
                if parts[0] == key:
                    return int(parts[1])
    except:
        pass
    return 0

def save_high_score(key, new_score):
    scores = {}
    if os.path.exists("studylens_scores.txt"):
        try:
            with open("studylens_scores.txt", "r", encoding="utf-8") as f:
                for line in f:
                    parts = line.strip().split(":")
                    if len(parts) == 2:
                        scores[parts[0]] = int(parts[1])
        except:
            pass
    if key not in scores or new_score > scores[key]:
        scores[key] = new_score
        with open("studylens_scores.txt", "w", encoding="utf-8") as f:
            for k, v in scores.items():
                f.write(f"{k}:{v}\n")

# מערכת דרגות חדשה שבה כל רמה דורשת בדיוק 50 נקודות נוספות
def get_player_rank_info(current_score):
    if current_score < 50:
        needed = 50 - current_score
        return f"🌱 טירון (Novice) | עוד {needed} נק' לרמה הבאה"
    elif current_score < 100:
        needed = 100 - current_score
        return f"📖 תלמיד משקיען (Scholar) | עוד {needed} נק' לרמה הבאה"
    elif current_score < 150:
        needed = 150 - current_score
        return f"💡 מומחה (Expert) | עוד {needed} נק' לרמה הבאה"
    elif current_score < 200:
        needed = 200 - current_score
        return f"🔬 פרופסור (Master) | עוד {needed} נק' לרמה הבאה"
    else:
        return "👑 אלוף עולם (Legend) - הגעת לפסגה!"

def generate_dynamic_question(category, subtopic, level):
    if category == "מתמטיקה":
        if subtopic == "גיאומטריה ושטחים":
            if level == "קל":
                side = random.randint(3, 10)
                correct = side * side
                q_text = f"מהו שטח ריבוע שצלעו היא {side} ס\"מ?"
            elif level == "בינוני":
                w = random.randint(4, 12)
                h = random.randint(3, 10)
                correct = w * h
                q_text = f"מהו שטח מלבן שרוחבו {w} ס\"מ ואורכו {h} ס\"מ?"
            else:
                r = random.randint(3, 8)
                correct = r * 4
                q_text = f"מהו היקף ריבוע שצלעו {r} ס\"מ?"
        elif subtopic == "כפל וחילוק":
            if level == "קל":
                num1 = random.randint(1, 10)
                num2 = random.randint(1, 10)
                correct = num1 * num2
                q_text = f"כמה זה {num1} כפול {num2}?"
            elif level == "בינוני":
                num1 = random.randint(5, 15)
                num2 = random.randint(2, 12)
                op = random.choice(["*", "/"])
                if op == "*":
                    correct = num1 * num2
                    q_text = f"כמה זה {num1} כפול {num2}?"
                else:
                    correct = random.randint(2, 10)
                    num1 = num2 * correct
                    q_text = f"כמה זה {num1} לחלק ב-{num2}?"
            else:
                num2 = random.randint(3, 15)
                correct = random.randint(10, 30)
                num1 = num2 * correct
                q_text = f"כמה זה {num1} לחלק ב-{num2}?"
                
        elif subtopic == "חיבור וחיסור":
            if level == "קל":
                num1 = random.randint(1, 20)
                num2 = random.randint(1, 20)
                correct = num1 + num2
                q_text = f"כמה זה {num1} ועוד {num2}?"
            elif level == "בינוני":
                num1 = random.randint(20, 100)
                num2 = random.randint(10, 50)
                op = random.choice(["+", "-"])
                if op == "+":
                    correct = num1 + num2
                    q_text = f"כמה זה {num1} ועוד {num2}?"
                else:
                    if num1 < num2: num1, num2 = num2, num1
                    correct = num1 - num2
                    q_text = f"כמה זה {num1} פחות {num2}?"
            else:
                num1 = random.randint(100, 500)
                num2 = random.randint(50, 250)
                op = random.choice(["+", "-"])
                if op == "+":
                    correct = num1 + num2
                    q_text = f"כמה זה {num1} ועוד {num2}?"
                else:
                    if num1 < num2: num1, num2 = num2, num1
                    correct = num1 - num2
                    q_text = f"כמה זה {num1} פחות {num2}?"
                    
        elif subtopic == "שברים ואחוזים":
            if level == "קל":
                perc = random.choice([10, 20, 50])
                base = random.choice([50, 100, 200])
                correct = int((perc / 100) * base)
                q_text = f"כמה הם {perc}% מהמספר {base}?"
            elif level == "בינוני":
                perc = random.choice([25, 75, 10])
                base = random.choice([120, 200, 300])
                correct = int((perc / 100) * base)
                q_text = f"כמה הם {perc}% מהמספר {base}?"
            else:
                perc = random.choice([15, 35, 65])
                base = random.choice([240, 400, 500])
                correct = int((perc / 100) * base)
                q_text = f"כמה הם {perc}% מהמספר {base}?"
                
        elif subtopic == "משוואות פשוטות":
            if level == "קל":
                a = random.randint(2, 4)
                correct = random.randint(2, 8)
                b = random.randint(1, 10)
                c = a * correct + b
                q_text = f"מהו x אם: {a}x + {b} = {c}?"
            elif level == "בינוני":
                a = random.randint(3, 7)
                correct = random.randint(4, 12)
                b = random.randint(2, 15)
                c = a * correct + b
                q_text = f"מהו x אם: {a}x + {b} = {c}?"
            else:
                a = random.randint(5, 10)
                correct = random.randint(8, 20)
                b = random.randint(5, 25)
                c = a * correct + b
                q_text = f"מהו x אם: {a}x + {b} = {c}?"
                
        else:
            if level == "קל":
                base_n = random.randint(2, 5)
                correct = base_n ** 2
                q_text = f"כמה שווה {base_n} בריבוע ({base_n}^2)?"
            elif level == "בינוני":
                base_n = random.randint(6, 12)
                correct = base_n ** 2
                q_text = f"כמה שווה {base_n} בריבוע ({base_n}^2)?"
            else:
                sq = random.choice([4, 9, 16, 25, 36, 49, 64, 81, 100])
                correct = int(sq ** 0.5)
                q_text = f"מהו השורש הריבועי של המספר {sq}?"

        options = [correct]
        while len(options) < 4:
            offset = random.randint(-6, 8)
            wrong = correct + offset
            if wrong != correct and wrong not in options and wrong >= 0:
                options.append(wrong)
        random.shuffle(options)
        return {
            "question": q_text,
            "options": [str(opt) for opt in options],
            "answer": options.index(correct)
        }

    elif category == "אנגלית":
        word_pool = topics_data["אנגלית"][subtopic]
        item = random.choice(word_pool)
        correct = item["translation"]
        q_text = f"מה הפירוש של המילה: {item['word']}?"
        all_trans = []
        for s in topics_data["אנגלית"].values():
            for w in s:
                all_trans.append(w["translation"])
        wrong_pool = [t for t in all_trans if t != correct]
        options = [correct] + random.sample(wrong_pool, min(3, len(wrong_pool)))
        random.shuffle(options)
        return {
            "question": q_text,
            "options": options,
            "answer": options.index(correct)
        }

def start_quiz(category, subtopic, level, custom_questions=None):
    global current_category, current_subtopic, current_level, flashcards, current_index, score, answered, total_questions_count, wrong_questions_pool, is_review_mode
    current_category = category
    current_subtopic = subtopic
    current_level = level
    
    if custom_questions:
        flashcards = custom_questions
        total_questions_count = len(flashcards)
        is_review_mode = True
    else:
        is_review_mode = False
        try:
            total_questions_count = int(q_count_entry.get())
            if total_questions_count < 1: total_questions_count = 1
            elif total_questions_count > 50: total_questions_count = 50
        except:
            total_questions_count = 10

        questions = []
        if category in ["מתמטיקה", "אנגלית"]:
            for _ in range(total_questions_count):
                questions.append(generate_dynamic_question(category, subtopic, level))
        else:
            base_pool = list(topics_data[category][subtopic])
            while len(base_pool) < total_questions_count:
                base_pool.extend(topics_data[category][subtopic])
            random.shuffle(base_pool)
            for item in base_pool[:total_questions_count]:
                questions.append({
                    "question": item["q"],
                    "options": item["opts"],
                    "answer": item["ans"]
                })
        flashcards = questions

    current_index = 0
    score = 0
    answered = False
    wrong_questions_pool = []
    
    show_game_screen()
    update_ui()

def update_timer():
    global timer_seconds, timer_id, answered
    if answered:
        return
    if timer_var.get() == 1:
        if timer_seconds > 0:
            timer_label.config(text=f"⏱️ זמן: {timer_seconds}ש'")
            timer_seconds -= 1
            timer_id = root.after(1000, update_timer)
        else:
            timer_label.config(text="⏱️ נגמר הזמן!", fg="#ef4444")
            check_answer(-1)
    else:
        timer_label.config(text="")

def check_answer(selected_option):
    global score, answered, timer_id, wrong_questions_pool
    if answered:
        return
    
    answered = True
    if timer_id:
        root.after_cancel(timer_id)
        
    correct_option = flashcards[current_index]["answer"]
    
    for i in range(4):
        if i == correct_option:
            btn_options[i].config(bg="#22c55e", fg="#ffffff")
        elif i == selected_option and selected_option != -1:
            btn_options[i].config(bg="#ef4444", fg="#ffffff")
            
    if selected_option == correct_option:
        score += 1
        feedback_label.config(text="כל הכבוד אלוף! 🎯", fg="#22c55e")
    else:
        feedback_label.config(text="לא נורא, תנסה שוב! 💪", fg="#ef4444")
        if not is_review_mode:
            wrong_questions_pool.append(flashcards[current_index])
        
    score_label.config(text=f"נקודות: {score}")
    global_rank_label.config(text=get_player_rank_info(score))
    game_rank_label.config(text=get_player_rank_info(score))
    
    root.after(1500, next_card)

def use_hint():
    global hint_used, answered
    if answered or hint_used:
        return
    hint_used = True
    correct_option = flashcards[current_index]["answer"]
    wrong_options = [i for i in range(4) if i != correct_option]
    to_hide = random.sample(wrong_options, 2)
    t = themes[current_theme]
    for idx in to_hide:
        btn_options[idx].config(text="", state=tk.DISABLED, bg=t["bg"])
    hint_btn.config(state=tk.DISABLED)

def next_card():
    global current_index, answered, timer_seconds, hint_used
    current_index += 1
    
    if current_index >= len(flashcards):
        feedback_label.config(text="🎉 סבב השאלות הסתיים!", fg="#38bdf8")
        percentage = int((score / len(flashcards)) * 100)
        
        hs_key = f"{current_category}_{current_subtopic}_{current_level}"
        old_hs = load_high_score(hs_key)
        is_new_record = score > old_hs
        if is_new_record:
            save_high_score(hs_key, score)
        
        record_text = f"🏆 שיא חדש: {score}!" if is_new_record else f"שיא קודם: {old_hs}"
        rank_text = get_player_rank_info(score)
        
        question_label.config(text=f"כל הכבוד אלוף! 🏆\nציון סופי: {score} מתוך {len(flashcards)} ({percentage}%)\n{record_text}\n{rank_text}")
        counter_label.config(text="סיום")
        timer_label.config(text="")
        game_rank_label.pack_forget()
        hint_btn.pack_forget()
        for btn in btn_options:
            btn.pack_forget()
        btn_exit_to_sub.pack_forget()
        
        if wrong_questions_pool and not is_review_mode:
            btn_review.pack(pady=5)
        
        btn_back_menu.pack(pady=5)
        btn_play_again.pack(pady=5)
        return

    answered = False
    hint_used = False
    hint_btn.config(state=tk.NORMAL)
    timer_seconds = 15
    update_ui()
    update_timer()

def start_review_quiz():
    btn_review.pack_forget()
    btn_play_again.pack_forget()
    btn_back_menu.pack_forget()
    game_rank_label.pack(pady=2)
    hint_btn.pack(pady=5)
    start_quiz(current_category, current_subtopic, current_level, custom_questions=wrong_questions_pool)

def restart_current_quiz():
    btn_play_again.pack_forget()
    btn_back_menu.pack_forget()
    btn_review.pack_forget()
    game_rank_label.pack(pady=2)
    hint_btn.pack(pady=5)
    start_quiz(current_category, current_subtopic, current_level)

def update_ui():
    card = flashcards[current_index]
    counter_label.config(text=f"שאלה {current_index + 1} מתוך {len(flashcards)}")
    score_label.config(text=f"נקודות: {score}")
    global_rank_label.config(text=get_player_rank_info(score))
    game_rank_label.config(text=get_player_rank_info(score))
    feedback_label.config(text="")
    question_label.config(text=card["question"])
    t = themes[current_theme]
    for i in range(4):
        btn_options[i].config(text=card["options"][i], bg=t["btn_bg"], fg=t["text"], state=tk.NORMAL)

def toggle_theme():
    global current_theme
    current_theme = "neon" if current_theme == "dark" else "dark"
    apply_theme()

def apply_theme():
    t = themes[current_theme]
    root.config(bg=t["bg"])
    for frame in [menu_frame, subtopic_frame, level_frame, game_frame, info_frame, count_frame]:
        frame.config(bg=t["bg"])
    theme_btn.config(text="🎨 מצב עיצוב: ניאון זוהר" if current_theme == "neon" else "🎨 מצב עיצוב: כהה קלאסי")

def show_menu_screen():
    game_frame.pack_forget()
    btn_back_menu.pack_forget()
    btn_play_again.pack_forget()
    btn_review.pack_forget()
    btn_exit_to_sub.pack_forget()
    hint_btn.pack_forget()
    game_rank_label.pack_forget()
    global_rank_label.pack(side=tk.TOP, pady=2)
    level_frame.pack_forget()
    subtopic_frame.pack_forget()
    menu_frame.pack(expand=True)

def show_subtopic_selection(category_name):
    global current_category
    current_category = category_name
    menu_frame.pack_forget()
    
    for widget in subtopic_frame.winfo_children():
        if widget != title_subtopic and widget != btn_back_to_cat_from_sub and widget != global_rank_label:
            widget.destroy()
            
    title_subtopic.config(text=f"בחר נושא ב-{category_name}")
    t = themes[current_theme]
    subtopics = list(topics_data[category_name].keys())
    for sub in subtopics:
        btn = tk.Button(subtopic_frame, text=sub, font=("Arial", 12, "bold"), width=26, height=2, bg=t["btn_bg"], fg=t["text"],
                        activebackground="#1abc9c", activeforeground="#ffffff", relief=tk.FLAT,
                        command=lambda s=sub: show_level_selection(s))
        btn.pack(pady=6)
        
    subtopic_frame.pack(expand=True)

def show_level_selection(subtopic_name):
    global current_subtopic
    current_subtopic = subtopic_name
    subtopic_frame.pack_forget()
    level_frame.pack(expand=True)
    title_level.config(text=f"הגדרות עבור: {subtopic_name}\n(שיא קודם שמור במערכת)")

def show_game_screen():
    level_frame.pack_forget()
    btn_back_menu.pack_forget()
    btn_play_again.pack_forget()
    btn_review.pack_forget()
    global_rank_label.pack_forget()
    game_frame.pack(expand=True, fill=tk.BOTH)
    t = themes[current_theme]
    game_rank_label.pack(pady=2)
    for btn in btn_options:
        btn.pack(pady=6)
    hint_btn.pack(pady=5)
    btn_exit_to_sub.pack(pady=10)

root = tk.Tk()
root.title("StudyLens - 50 Points Ranks Edition")
root.geometry("520x830")

menu_frame = tk.Frame(root)
subtopic_frame = tk.Frame(root)
level_frame = tk.Frame(root)
count_frame = tk.Frame(level_frame)
game_frame = tk.Frame(root)
info_frame = tk.Frame(game_frame)

# 1. StudyLens הכי למעלה
main_title_label = tk.Label(root, text="✨ StudyLens ✨", font=("Arial", 22, "bold"), fg="#38bdf8", bg="#0f172a")
main_title_label.pack(pady=5)

# 2. מתחתיו הדרגה שלך עם חישוב של 50 נקודות לכל רמה
global_rank_label = tk.Label(root, text=get_player_rank_info(score), font=("Arial", 11, "bold"), fg="#facc15", bg="#0f172a")
global_rank_label.pack(pady=2)

# 3. אחרי זה תפריט בחירת קטגוריה
menu_frame.pack(expand=True)

title_menu = tk.Label(menu_frame, text="בחר קטגוריה", font=("Arial", 15, "bold"), fg="#38bdf8", bg="#0f172a")
title_menu.pack(pady=10)

btn_bio = tk.Button(menu_frame, text="🧬 ביולוגיה", font=("Arial", 13, "bold"), width=26, height=2, bg="#10b981", fg="#ffffff", relief=tk.FLAT,
                    command=lambda: show_subtopic_selection("ביולוגיה"))
btn_bio.pack(pady=6)

btn_chem = tk.Button(menu_frame, text="🧪 כימיה", font=("Arial", 13, "bold"), width=26, height=2, bg="#8b5cf6", fg="#ffffff", relief=tk.FLAT,
                     command=lambda: show_subtopic_selection("כימיה"))
btn_chem.pack(pady=6)

btn_math = tk.Button(menu_frame, text="📐 מתמטיקה", font=("Arial", 13, "bold"), width=26, height=2, bg="#f59e0b", fg="#ffffff", relief=tk.FLAT,
                     command=lambda: show_subtopic_selection("מתמטיקה"))
btn_math.pack(pady=6)

btn_eng = tk.Button(menu_frame, text="🔤 אנגלית", font=("Arial", 13, "bold"), width=26, height=2, bg="#ec4899", fg="#ffffff", relief=tk.FLAT,
                    command=lambda: show_subtopic_selection("אנגלית"))
btn_eng.pack(pady=6)

theme_btn = tk.Button(menu_frame, text="🎨 החלף ערכת עיצוב", font=("Arial", 11, "bold"), bg="#475569", fg="#ffffff", relief=tk.FLAT,
                      command=toggle_theme)
theme_btn.pack(pady=15)

title_subtopic = tk.Label(subtopic_frame, text="", font=("Arial", 16, "bold"), fg="#38bdf8", bg="#0f172a")
title_subtopic.pack(pady=20)
btn_back_to_cat_from_sub = tk.Button(subtopic_frame, text="⬅️ חזרה לקטגוריות", font=("Arial", 11, "bold"), bg="#475569", fg="#ffffff", relief=tk.FLAT,
                                     command=show_menu_screen)
btn_back_to_cat_from_sub.pack(pady=15)

title_level = tk.Label(level_frame, text="", font=("Arial", 14, "bold"), fg="#38bdf8", bg="#0f172a", wraplength=460, justify="center")
title_level.pack(pady=10)

count_frame.pack(pady=5)
lbl_count = tk.Label(count_frame, text="כמות שאלות (1-50):", font=("Arial", 11), bg="#0f172a", fg="#ffffff")
lbl_count.pack(side=tk.LEFT, padx=10)
q_count_entry = tk.Entry(count_frame, font=("Arial", 11, "bold"), width=5, justify="center")
q_count_entry.insert(0, "10")
q_count_entry.pack(side=tk.LEFT)

timer_var = tk.IntVar(value=0)
timer_check = tk.Checkbutton(level_frame, text="⏱️ הפעל טיימר (15 שניות לשאלה)", variable=timer_var, font=("Arial", 11), fg="#facc15", bg="#0f172a", selectcolor="#1e293b", activebackground="#0f172a", activeforeground="#facc15")
timer_check.pack(pady=5)

btn_easy = tk.Button(level_frame, text="🟢 רמה קלה", font=("Arial", 12, "bold"), width=24, height=2, bg="#22c55e", fg="#ffffff", relief=tk.FLAT,
                     command=lambda: start_quiz(current_category, current_subtopic, "קל"))
btn_easy.pack(pady=6)

btn_medium = tk.Button(level_frame, text="🟡 רמה בינונית", font=("Arial", 12, "bold"), width=24, height=2, bg="#eab308", fg="#ffffff", relief=tk.FLAT,
                       command=lambda: start_quiz(current_category, current_subtopic, "בינוני"))
btn_medium.pack(pady=6)

btn_hard = tk.Button(level_frame, text="🔴 רמה קשה", font=("Arial", 12, "bold"), width=24, height=2, bg="#ef4444", fg="#ffffff", relief=tk.FLAT,
                     command=lambda: start_quiz(current_category, current_subtopic, "קשה"))
btn_hard.pack(pady=6)

btn_back_to_sub = tk.Button(level_frame, text="⬅️ חזרה לנושאים", font=("Arial", 11, "bold"), bg="#475569", fg="#ffffff", relief=tk.FLAT,
                            command=lambda: show_subtopic_selection(current_category))
btn_back_to_sub.pack(pady=10)

title_game = tk.Label(game_frame, text="🚀 משחק פעיל", font=("Arial", 14, "bold"), fg="#38bdf8", bg="#0f172a")
title_game.pack(pady=5)

info_frame.pack(pady=2)

counter_label = tk.Label(info_frame, text="", font=("Arial", 11, "bold"), fg="#94a3b8", bg="#0f172a")
counter_label.pack(side=tk.LEFT, padx=10)

score_label = tk.Label(info_frame, text="נקודות: 0", font=("Arial", 11, "bold"), fg="#facc15", bg="#0f172a")
score_label.pack(side=tk.LEFT, padx=10)

timer_label = tk.Label(info_frame, text="", font=("Arial", 11, "bold"), fg="#ef4444", bg="#0f172a")
timer_label.pack(side=tk.LEFT, padx=10)

game_rank_label = tk.Label(game_frame, text="", font=("Arial", 11, "bold"), fg="#facc15", bg="#0f172a")

feedback_label = tk.Label(game_frame, text="", font=("Arial", 12, "bold"), bg="#0f172a")
feedback_label.pack(pady=2)

hint_btn = tk.Button(game_frame, text="💡 רמז (פסול 2 תשובות)", font=("Arial", 10, "bold"), bg="#6366f1", fg="#ffffff", relief=tk.FLAT,
                     command=use_hint)

question_label = tk.Label(game_frame, text="", font=("Arial", 13, "bold"), wraplength=460, justify="center", bg="#0f172a", fg="#ffffff")
question_label.pack(pady=10)

btn_options = []
for i in range(4):
    btn = tk.Button(game_frame, text="", font=("Arial", 11), width=38, height=2, relief=tk.FLAT,
                    command=lambda idx=i: check_answer(idx))
    btn.pack(pady=5)
    btn_options.append(btn)

btn_exit_to_sub = tk.Button(game_frame, text="⬅️ חזרה לנושאים", font=("Arial", 11, "bold"), bg="#475569", fg="#ffffff", relief=tk.FLAT,
                            command=lambda: show_subtopic_selection(current_category))

btn_review = tk.Button(game_frame, text="🔁 עבור על השאלות שטעית בהן", font=("Arial", 11, "bold"), bg="#8b5cf6", fg="#ffffff", relief=tk.FLAT,
                       command=start_review_quiz)

btn_play_again = tk.Button(game_frame, text="🔄 שחק שוב", font=("Arial", 11, "bold"), bg="#22c55e", fg="#ffffff", relief=tk.FLAT,
                           command=restart_current_quiz)

btn_back_menu = tk.Button(game_frame, text="חזרה לתפריט הראשי 🏠", font=("Arial", 11, "bold"), bg="#0ea5e9", fg="#ffffff", relief=tk.FLAT,
                          command=show_menu_screen)

apply_theme()

root.mainloop()
