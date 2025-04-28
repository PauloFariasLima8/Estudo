
$(document).ready(function() {
    // Contador de usuários
    let counter = 20000;
    const target = 24000;
    const increment = 10;
    const speed = 50;

    const counterElement = $('.days');
    
    const updateCounter = () => {
        if (counter < target) {
            counter += increment;
            counterElement.text(counter.toLocaleString() + ' mil');
            setTimeout(updateCounter, speed);
        }
    };

    updateCounter();

    // Configuração original do countdown
    $(".countdown").countdown({
        date: "12 March 2024 18:30:00",
        format: "on"
    });
}); 
