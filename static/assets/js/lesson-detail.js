$(document).ready(function() {
    var incorrectQuestions = [];

    // Функция для воспроизведения текста на английском
    function speakText(text) {

    // Найти элемент с классом level-button
    const languageButton = document.querySelector('.language-button');
    // Извлечь значение data-level-id
    const languageId = languageButton.getAttribute('data-language-id');

    // Проверка languageId
    if (languageId !== '1') {
        return;
    }


    if ('speechSynthesis' in window) {
        text = text.toLowerCase();
        // Проверяем, является ли текст английским или числом (с учетом символа __)
        var englishPattern = /^[a-zA-Z0-9\s.,!?'_]+$/;
        if (englishPattern.test(text)) {
            var parts = text.split('__');
            var index = 0;

            function speakNextPart() {
                if (index < parts.length) {
                    var msg = new SpeechSynthesisUtterance();
                    msg.text = parts[index].trim();
                    msg.lang = 'en-US'; // Установите язык на английский
                    msg.onend = function(event) {
                        index++;
                        if (index < parts.length) {
                            setTimeout(speakNextPart, 400); // Пауза в 500 мс между частями
                        }
                    };
                    window.speechSynthesis.speak(msg);
                }
            }

            speakNextPart();
        } 
    } else {
        console.log('Ваш браузер не поддерживает Web Speech API');
    }
}


    // function speakText(text, voiceName = 'Google US English') {
    //     if ('speechSynthesis' in window) {
    //         text = text.toLowerCase();
    //         // Проверяем, является ли текст английским или числом (с учетом символа __)
    //         var englishPattern = /^[a-zA-Z0-9\s.,!?'_]+$/;
    //         if (englishPattern.test(text)) {
    //             var parts = text.split('__');
    //             var index = 0;

    //             function speakNextPart() {
    //                 if (index < parts.length) {
    //                     var msg = new SpeechSynthesisUtterance();
    //                     msg.text = parts[index].trim();
    //                     msg.lang = 'en-US'; // Установите язык на английский

    //                     // Получаем список голосов и выбираем тот, который совпадает с voiceName
    //                     const voices = window.speechSynthesis.getVoices();
    //                     const selectedVoice = voices[0];    //  выбираем первый голос
    //                     if (selectedVoice) {
    //                         msg.voice = selectedVoice;
    //                     }
    //                     else {
    //                         msg.voice = voices[0];
    //                     }

    //                     msg.onend = function(event) {
    //                         index++;
    //                         if (index < parts.length) {
    //                             setTimeout(speakNextPart, 400); // Пауза в 400 мс между частями
    //                         }
    //                     };

    //                     window.speechSynthesis.speak(msg);
    //                 }
    //             }

    //             // Вызов speakNextPart после загрузки голосов
    //             window.speechSynthesis.onvoiceschanged = function() {
    //                 speakNextPart();
    //             };

    //         } 
    //     } else {
    //         console.log('Ваш браузер не поддерживает Web Speech API');
    //     }
    // }







   // Для вопросов типа тест
   $('.lesson-test .buttons-row button').click(function() {
    var $this = $(this);
    var $currentTest = $this.closest('.test-container');
    var correctAnswer = $this.data('correct-answer');
    var chosenAnswer = $this.text();
    speakText(chosenAnswer)

    if (chosenAnswer === correctAnswer) {
        $this.addClass('correct-answer').removeClass('incorrect-answer');
        setTimeout(function() {
            $currentTest.addClass('completed correct');
            $currentTest.removeClass('active');
            showNextTest();
        }, 1000);
    } else {
        $this.addClass('incorrect-answer').removeClass('correct-answer');
        setTimeout(function() {
            $currentTest.addClass('completed incorrect');
            incorrectQuestions.push($currentTest); // Добавляем неправильный вопрос в массив
            $currentTest.removeClass('active');
            showNextTest();
        }, 1000);
    }
});

    // Для вопросов типа fill-in-the-blank
    $('.fill-in-the-blank .word').click(function() {
        var $this = $(this);
        var $currentTest = $this.closest('.test-container');
        var $chosenWords = $currentTest.find('.chosen-words');
        var correctAnswer = $currentTest.find('.fill-in-the-blank').data('correct-answer').split(' ');


        if (!$this.hasClass('chosen')) {
            $this.addClass('chosen');
            speakText($this.text())
            $chosenWords.append($('<span>').text($this.text()));
        }

        var chosenAnswer = $currentTest.find('.chosen-words span').map(function() {
            return $(this).text();
        }).get();

        if (chosenAnswer.length === correctAnswer.length) {
            if (chosenAnswer.join(' ') === correctAnswer.join(' ')) {
                $currentTest.find('.fill-in-the-blank button').addClass('correct-answer').removeClass('incorrect-answer');
                setTimeout(function() {
                    $currentTest.addClass('completed correct');
                    $currentTest.removeClass('active');
                    showNextTest();
                }, 1000);
            } else {
                $currentTest.find('.fill-in-the-blank button').addClass('incorrect-answer').removeClass('correct-answer');
                setTimeout(function() {
                    $currentTest.addClass('completed incorrect');
                    incorrectQuestions.push($currentTest); // Добавляем неправильный вопрос в массив
                    $currentTest.removeClass('active');
                    showNextTest();
                }, 1000);
            }
        }
     
    });

 


    // Для вопросов, где нужно ввести перевод
    $('.translation-question button').click(function() {
        var $currentTest = $(this).closest('.test-container');
        var correctAnswer = $currentTest.find('.correct-answer').val().replace(/\s+/g, '').toLowerCase(); // Удаляем пробелы и переводим в нижний регистр
        var userAnswer = $currentTest.find('.form-control').val().replace(/\s+/g, '').toLowerCase(); // Удаляем пробелы и переводим в нижний регистр
        speakText(userAnswer);
        if (userAnswer === correctAnswer) {
            $currentTest.find('.form-control').addClass('correct-answer').removeClass('incorrect-answer');
            setTimeout(function() {
                $currentTest.addClass('completed correct');
                $currentTest.removeClass('active');
                showNextTest();
            }, 1000);
        } else {
            $currentTest.find('.form-control').addClass('incorrect-answer').removeClass('correct-answer');
            setTimeout(function() {
                $currentTest.addClass('completed incorrect');
                incorrectQuestions.push($currentTest); // Добавляем неправильный вопрос в массив
                $currentTest.removeClass('active');
                showNextTest();
            }, 1000);
        }
    });


    // Обработчик клика на иконку воспроизведения текста вопроса
    $('.lesson-container .fa-volume-high').click(function() {
        var $this = $(this);
        var $currentTest = $this.closest('.test-container');
        var questionText = $currentTest.find('.listen_text').attr('listen-text');
        
        speakText(questionText);
    });

    // Обработчик клика на слова для выбора ответа
    $('.listen-test .word').click(function() {
        var $this = $(this);
        var $currentTest = $this.closest('.test-container');
        var $chosenWords = $currentTest.find('.chosen-words');
        var correctAnswer = $currentTest.find('.listen-test').data('correct-answer').split(' ');
        if (!$this.hasClass('chosen')) {
            $this.addClass('chosen');
            speakText($this.text())
            $chosenWords.append($('<span>').text($this.text()));
        }

        var chosenAnswer = $currentTest.find('.chosen-words span').map(function() {
            return $(this).text();
        }).get();

        if (chosenAnswer.length === correctAnswer.length) {
            if (chosenAnswer.join(' ') === correctAnswer.join(' ')) {
                $currentTest.find('.listen-test button').addClass('correct-answer').removeClass('incorrect-answer');
                setTimeout(function() {
                    $currentTest.addClass('completed correct');
                    $currentTest.removeClass('active');
                    showNextTest();
                }, 1000);
            } else {
                $currentTest.find('.listen-test button').addClass('incorrect-answer').removeClass('correct-answer');
                setTimeout(function() {
                    $currentTest.addClass('completed incorrect');
                    incorrectQuestions.push($currentTest); // Добавляем неправильный вопрос в массив
                    $currentTest.removeClass('active');
                    showNextTest();
                }, 1000);
            }
        }
     
    });








    function showNextTest() {
        var $nextTest = $('.test-container').not('.completed').first();
        var questionText = $nextTest.find('.badge.text-bg-info').text();
            speakText(questionText);
        if ($nextTest.length > 0) {
            $nextTest.addClass('active');
            
        } else if (incorrectQuestions.length > 0) {
            // Если есть неправильные вопросы, показываем их снова
            incorrectQuestions.forEach(function($question) {
                $question.removeClass('completed incorrect');
                $question.find('.fill-in-the-blank button').removeClass('correct-answer incorrect-answer'); // Сбрасываем цвет кнопок
                $question.find('.word').removeClass('chosen'); // Сбрасываем выбор слов для fill-in-the-blank
                $question.find('.chosen-words').empty(); // Очищаем выбранные слова для fill-in-the-blank
                $question.find('.buttons-row button').removeClass('correct-answer incorrect-answer'); // Сбрасываем кнопки для тестов
                $question.find('.form-control').removeClass('correct-answer incorrect-answer'); // Сбрасываем цвет кнопок
                $question.find('.form-control').val(''); //очишаем форму
                $question.find('.listen-test button').removeClass('correct-answer incorrect-answer'); // Сбрасываем цвет кнопок

            });
            incorrectQuestions[0].addClass('active');
            var questionText = incorrectQuestions[0].find('.badge.text-bg-info').text();
            speakText(questionText);
            incorrectQuestions = []; // Очищаем массив неправильных вопросов
        } else {
            alert("Сиз тестти бутурдунуз!")
          
            // Найти элемент с классом level-button
            const levelButton = document.querySelector('.level-button');
            
            // Извлечь значение data-level-id
            const levelId = levelButton.getAttribute('data-level-id');
            
            // window.location.assign('/level/' + levelId + '/');

            window.location.href = '/level/' + levelId + '/';
            // window.location.href = '/lesson'; // Перенаправление на главную страницу
        }
    }
    var firstQuestionText = $('.test-container.active').find('.badge.text-bg-info').text();
    speakText(firstQuestionText);
    


});
