"""
--
-- 30/12/2015
-- Criador: Miguel Otavio Bordignon
--
Pig Latin is a language game, 
where you move the first letter of the word to the end and add "ay." 
So "Python" becomes "ythonpay." 
To write a Pig Latin translator in Python, here are the steps we'll need to take:
1. Ask the user to input a word in English.
2. Make sure the user entered a valid word.
3. Convert the word from English to Pig Latin.
4. Display the translation result."""

chave = 'ay'

palavra = raw_input('Entre com uma palavra:')

if  palavra.isalpha() and len(palavra) > 0 :
    print 'Palavra recebida:', palavra
    primeira = palavra[0]
    nova_palavra = palavra[1:len(palavra)]
    nova_palavra = nova_palavra + primeira + chave
    print 'Palavra traduzida:', nova_palavra.lower()
else:
    print 'Entre com uma palavra valida'
    
