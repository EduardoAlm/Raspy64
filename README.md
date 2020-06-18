# Raspy64

O objectivo deste projecto é a construção de um protótipo de sistema que simule um distribuidor de raspadinhas digitais mantendo a segurança e privacidade dos seus utilizadores. 
Para o efeito deste projecto as raspadinhas serão grátis e atribuídas a cada utilizador que esteja a utilizar o sistema de hora a hora. 


De modo a obter uma maior segurança o protótipo contém:

    * Sistemas de autenticação fortes;
    * Efectua o registo de forma segura (2Factor Auth (email/password e SMS code));
    * Guarda as credenciais dos utilizadores cifradas com uma cifra reconhecida;
    * Cifra as comunicações entre o utilizador e o servidor;
    * Garante a integridade das comunicações entre utilizador e servidor;
    * Aplica um mecanismo de oblivious transfer para o calculo do valor final da raspadinha de forma a manter a confidencialidade do resultado.

