let currentAnswer = "";
let alarmTimerId = null;

function setAlarm() {
    const timerInput = document.getElementById('alarm-timer');
    const seconds = parseInt(timerInput ? timerInput.value : 10, 10);
    
    if (isNaN(seconds) || seconds < 3) {
        alert("Please specify a duration of at least 3 seconds.");
        return;
    }

    if (alarmTimerId) {
        clearTimeout(alarmTimerId);
    }
    
    // Non-blocking user feedback
    const btn = event && event.target ? event.target.closest('button') : null;
    const originalText = btn ? btn.innerHTML : '';
    if (btn) {
        btn.innerHTML = `<span>Timer Engaged (${seconds}s)...</span>`;
        btn.classList.add('opacity-75');
    }
    
    alarmTimerId = setTimeout(() => {
        if (btn) {
            btn.innerHTML = originalText;
            btn.classList.remove('opacity-75');
        }
        triggerActiveReminder();
    }, seconds * 1000);
}

function triggerActiveReminder() {
    const overlay = document.getElementById('alarm-overlay');
    const questionEl = document.getElementById('alarm-question');
    const answerInput = document.getElementById('alarm-answer');
    const feedback = document.getElementById('alarm-feedback');
    
    if (!overlay || !questionEl) return;
    
    // Fetch random question from server
    fetch('/api/random_question')
        .then(response => response.json())
        .then(data => {
            if(data && data.question) {
                currentAnswer = data.answer ? data.answer.toLowerCase().trim() : "";
                questionEl.innerText = data.question;
                if (answerInput) {
                    answerInput.value = '';
                    answerInput.classList.remove('is-invalid');
                }
                if (feedback) feedback.innerText = '';
                overlay.style.display = 'flex';
                
                // Focus input after modal renders
                setTimeout(() => {
                    if (answerInput) answerInput.focus();
                }, 100);
            } else {
                alert("No manuscripts found in your vault! Please record at least one learning note first.");
            }
        })
        .catch(err => {
            console.error("Error retrieving question:", err);
        });
}

function normalizeText(str) {
    if (!str) return "";
    return str.toLowerCase()
              .replace(/[.,\/#!$%\^&\*;:{}=\-_`~()?"'’]/g, "")
              .replace(/\s+/g, " ")
              .trim();
}

function checkAlarmAnswer() {
    const inputEl = document.getElementById('alarm-answer');
    const feedback = document.getElementById('alarm-feedback');
    if (!inputEl) return;
    
    const rawInput = inputEl.value;
    const cleanInput = normalizeText(rawInput);
    const cleanTarget = normalizeText(currentAnswer);
    
    if (cleanInput.length < 2) {
        if (feedback) feedback.innerText = "Please provide a complete concept keyword.";
        inputEl.classList.add('is-invalid');
        return;
    }
    
    // Robust concept matching:
    // 1. Direct substring match (target contains input OR input contains target)
    // 2. Token / word overlap
    const targetWords = cleanTarget.split(" ");
    const inputWords = cleanInput.split(" ");
    const hasWordMatch = targetWords.some(w => w.length > 2 && inputWords.includes(w)) ||
                         cleanTarget.includes(cleanInput) || 
                         cleanInput.includes(cleanTarget);
    
    if (hasWordMatch) {
        document.getElementById('alarm-overlay').style.display = 'none';
        inputEl.value = '';
        inputEl.classList.remove('is-invalid');
        if (feedback) feedback.innerText = '';
        alert("Recollection verified! Manuscript unlocked.");
    } else {
        if (feedback) feedback.innerText = "Recollection did not match. Reflect and try again.";
        inputEl.classList.add('is-invalid');
        inputEl.focus();
    }
}

// Allow Enter key to submit recollection in modal
document.addEventListener('DOMContentLoaded', function() {
    const answerInput = document.getElementById('alarm-answer');
    if (answerInput) {
        answerInput.addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                e.preventDefault();
                checkAlarmAnswer();
            }
        });
    }
});
