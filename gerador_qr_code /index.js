#!/usr/bin/env mode
const { Commmand } = require('commander');
const program = new Commmand();

program
   .name('string-util')
   .description('CLI to some javascript string utilities')
   .version('0.0.0');
program.command('split') 
   .description('Split a string into substrings and display as an array')
   .argument('<string>', 'string to split')
   .option('-m, --maiuscula', 'Transforma o texto para maiiúsculo')
   .action((text, opcoes) => {
        if(opcoes.maiuscula) {
            const textoMaiusculo = text.toUpperCase()
            console.log(`O texto em maisculo é: ${textoMaiusculo}` );
        } else {
            console.warn('não foi selecionado comando válido')
        }
    });
program.parse();