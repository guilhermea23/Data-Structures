Music Player
Todo rebelde tem sua lista de músicas para lidar com os momentos de tensão nos preparativos antes de um ataque ao Império. O bom funcionamento deste é essencial para a vitória, mas o estagiário wookie acabou apagando a licença para uso do tocador oficial da Aliança, e você se voluntariou para criar uma nova versão com a GPL3!

Uma análise mais precisa feita por você indicou que os codecs de wav, mp2, mp3, ogg e outros formatos ainda estavam disponíveis no equipamento de áudio intergalático. Portanto, você não deve se preocupar com a reprodução das músicas em seus respectivos formatos mas sim em implementar o comportamento de um tocador - manipular a lista de músicas, adicionar e remover músicas da lista e etc.

Para isso, basta implementar as principais funcionalidades de um music player:

play começa a tocar as músicas da lista, na ordem da lista, a partir da música atual, caso já não esteja tocando (não tem efeito caso contrário).
stop interrompe a execução da música atual.
add id acrescenta a música id ao final da lista.
del id retira a primeira ocorrência da música id na lista, se houver e desde que não esteja tocando. Não interrompe a execução da música atual.
next id define que a música id, se presente na lista, será a próxima a ser tocada, desde que não seja a que esteja sendo tocada no momento. A ocorrência de id na lista é realocada para tanto.
list mostra os ids das músicas na lista, separados por vírgula, ou a mensagem "[vazia]" caso a lista esteja vazia.
current mostra o id da música atual (sendo tocada no momento), ou da próxima a ser tocada, caso nenhuma esteja no momento. Se a lista estiver vazia, apresente a mensagem: "Toque! Toque, Dijê!".
undo [*] desfaz os efeitos de uma instrução add, del, next ou play. Isoladamente, desfaz o efeito da última instrução. Havendo o argumento opcional *, desfaz o efeito de todas as instruções dadas até aquele ponto.
fight interrompe o programa para iniciar o ataque ao Império.
A comunicação com o sistema é simples, as funcionalidades são apresentadas como descritas acima e, sempre que uma música termina, o codec responsável por reproduzir a música envia uma mensagem ended  indicando que a reprodução dela terminou (obviamente, apenas uma música que estava sendo tocada pode terminar). Quando uma música termina, a próxima inicia imediatamente, e não é mais possível desfazer as instruções anteriores. O sistema recomeça a tocar a lista do início caso a última música termine e a batalha não tenha começado. 

Entrada
A entrada consiste de uma série de instruções, conforme descritas acima. É garantido que todo id é único e composto apenas por uma palavra (sem espaço). A entrada sempre termina com a instrução fight.

Saída
A saída consiste na apresentação das informações quando solicitadas ( instruções list e current). Termine a execução apresentando a mensagem: "Jedi Wagner, assuma o comando!".

