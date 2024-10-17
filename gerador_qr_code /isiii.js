const premio = 150.00;
const apostas = [10.00, 80.00, 12.00, 60.00, 90.00, 10.00];
let somaApostas = 0;
let index = 0;
while ((somaApostas < premio ) && (index <= apostas.length -1)) {
    const valorAposta = apostas[index];
    somaApostas += valorAposta;
    if(somaApostas >= premio3) {
        console.log(`Pagar o prêmio de ${premio}`);
    } else {
        console.warn(`Apostas ainda está em ${somaApostas}`);
    }
    index = index + 1;
}