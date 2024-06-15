const sounds = {
    vowels: [
        { symbol: 'ɑ', sound: 'hot', desc: 'hot' },
        { symbol: 'æ', sound: 'cat', desc: 'cat' },
        { symbol: 'ʌ', sound: 'but', desc: 'but' },
        { symbol: 'ɛ', sound: 'bed', desc: 'bed' },
        { symbol: 'eɪ', sound: 'say', desc: 'say' },
        { symbol: 'ɚ', sound: 'bird', desc: 'bird' },
        { symbol: 'ɪ', sound: 'ship', desc: 'ship' },
        { symbol: 'i', sound: 'sheep', desc: 'sheep' },
        { symbol: 'ə', sound: 'about', desc: 'about' },
        { symbol: 'oʊ', sound: 'boat', desc: 'boat' },
        { symbol: 'ʊ', sound: 'foot', desc: 'foot' },
        { symbol: 'u', sound: 'food', desc: 'food' },
        { symbol: 'aʊ', sound: 'cow', desc: 'cow' },
        { symbol: 'aɪ', sound: 'time', desc: 'time' },
        { symbol: 'ɔɪ', sound: 'boy', desc: 'boy' }
    ],
    consonants: [
        { symbol: 'b', sound: 'book', desc: 'book' },
        { symbol: 'tʃ', sound: 'chair', desc: 'chair' },
        { symbol: 'd', sound: 'day', desc: 'day' },
        { symbol: 'f', sound: 'fish', desc: 'fish' },
        { symbol: 'g', sound: 'go', desc: 'go' },
        { symbol: 'h', sound: 'home', desc: 'home' },
        { symbol: 'dʒ', sound: 'job', desc: 'job' },
        { symbol: 'k', sound: 'key', desc: 'key' },
        { symbol: 'l', sound: 'lion', desc: 'lion' },
        { symbol: 'm', sound: 'moon', desc: 'moon' },
        { symbol: 'n', sound: 'nose', desc: 'nose' },
        { symbol: 'ŋ', sound: 'sing', desc: 'sing' }
    ]
};

const createButton = (symbol, sound, desc) => {
    const button = document.createElement('button');
    button.className = 'sound-button';
    button.innerHTML = `${symbol}<br><span>${desc}</span>`;
    button.addEventListener('click', () => speakText(sound));
    return button;
};

const speakText = (text) => {
    if ('speechSynthesis' in window) {
        const msg = new SpeechSynthesisUtterance();
        msg.text = text;
        msg.lang = 'en-US';
        window.speechSynthesis.speak(msg);
    } else {
        console.log('Ваш браузер не поддерживает Web Speech API');
    }
};

const vowelsContainer = document.getElementById('vowels');
sounds.vowels.forEach(sound => {
    vowelsContainer.appendChild(createButton(sound.symbol, sound.sound, sound.desc));
});

const consonantsContainer = document.getElementById('consonants');
sounds.consonants.forEach(sound => {
    consonantsContainer.appendChild(createButton(sound.symbol, sound.sound, sound.desc));
});
