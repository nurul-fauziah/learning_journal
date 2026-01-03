let currentAnswer = "";

function setAlarm() {
    const seconds = document.getElementById('alarm-timer').value;
    alert(`Active Reminder set for ${seconds} seconds! Don't close this tab.`);
    
    setTimeout(() => {
        triggerActiveReminder();
    }, seconds * 1000);
}

function triggerActiveReminder() {
    const overlay = document.getElementById('alarm-overlay');
    const questionEl = document.getElementById('alarm-question');
    
    // Fetch random question from server
    fetch('/api/random_question')
        .then(response => response.json())
        .then(data => {
            if(data) {
                currentAnswer = data.answer.toLowerCase();
                questionEl.innerText = data.question;
                overlay.style.display = 'flex';
                // Play sound (Perlu file audio di static/assets)
                // new Audio('/static/assets/alarm.mp3').play();
            } else {
                console.log("No questions available for alarm.");
            }
        });
}

function checkAlarmAnswer() {
    const input = document.getElementById('alarm-answer').value.toLowerCase();
    const feedback = document.getElementById('alarm-feedback');
    
    // Simple verification: cek apakah jawaban mengandung keyword dari summary
    // Untuk aplikasi production, bisa gunakan string similarity
    if (currentAnswer.includes(input) && input.length > 2) {
        document.getElementById('alarm-overlay').style.display = 'none';
        alert("Good job! Screen unlocked.");
        document.getElementById('alarm-answer').value = '';
        feedback.innerText = '';
    } else {
        feedback.innerText = "Incorrect. Try again to unlock!";
        // Hukuman: Alarm berbunyi lagi atau input di-clear
        document.getElementById('alarm-answer').classList.add('is-invalid');
    }
}
