<script src="https://kit.fontawesome.com/d914ec8c00.js" crossorigin="anonymous"></script>
<h1 align="center" style="font-size:36px; font-family:Poppins;" ><i class="fas fa-play-circle" style="cursor:pointer;"></i> Music Player </h1>
<p>Todo rebelde tem sua lista de músicas para lidar com os momentos de tensão nos preparativos antes de um ataque ao Império. O bom funcionamento deste é essencial para a vitória, mas o estagiário wookie acabou apagando a licença para uso do tocador oficial da Aliança, e você se voluntariou para criar uma nova versão com a GPL3!</p>

<p>Uma análise mais precisa feita por você indicou que os codecs de wav, mp2, mp3, ogg e outros formatos ainda estavam disponíveis no equipamento de áudio intergalático. Portanto, você não deve se preocupar com a reprodução das músicas em seus respectivos formatos mas sim em implementar o comportamento de um tocador - manipular a lista de músicas, adicionar e remover músicas da lista e etc.</p>

<p>Para isso, basta implementar as principais funcionalidades de um music player:</p>

```

</> play
  Começa a tocar as músicas da lista, na ordem da lista, a partir da música atual, caso já não esteja tocando (não tem efeito caso contrário).

</> stop
  Interrompe a execução da música atual.

</> add id
  Acrescenta a música id ao final da lista.

</> del id
  Retira a primeira ocorrência da música id na lista, se houver e desde que não esteja tocando. Não interrompe a execução da música atual.

</> next id
  Define que a música id, se presente na lista, será a próxima a ser tocada, desde que não seja a que esteja sendo tocada no momento. A ocorrência de id na lista é realocada para tanto.

</> list
  Mostra os ids das músicas na lista, separados por vírgula, ou a mensagem "[vazia]" caso a lista esteja vazia.

 </> current
    Mostra o id da música atual (sendo tocada no momento), ou da próxima a ser tocada, caso nenhuma esteja no momento. Se a lista estiver vazia, apresente a mensagem: "Toque! Toque, Dijê!".

</> undo [*]
  Desfaz os efeitos de uma instrução add, del, next ou play. Isoladamente, desfaz o efeito da última instrução. Havendo o argumento opcional *, desfaz o efeito de todas as instruções dadas até aquele ponto.

</> fight
  Interrompe o programa para iniciar o ataque ao Império.

```  
<br/>
A comunicação com o sistema é simples, as funcionalidades são apresentadas como descritas acima e, sempre que uma música termina, o codec responsável por reproduzir a música envia uma mensagem <strong>ended</strong>  indicando que a reprodução dela terminou (obviamente, apenas uma música que estava sendo tocada pode terminar). Quando uma música termina, a próxima inicia imediatamente, e não é mais possível desfazer as instruções anteriores. O sistema recomeça a tocar a lista do início caso a última música termine e a batalha não tenha começado. 
<br/>
<br/>
<br/>
<hr>
<h2 align="center"><i class="fas fa-door-open"></i> Entrada</h2>
<hr>
<p>A entrada consiste de uma série de instruções, conforme descritas acima. É garantido que todo id é único e composto apenas por uma palavra (sem espaço). A entrada sempre termina com a instrução fight.</p>
<br/>
<hr>
<h2 align="center"><i class="fas fa-door-closed"></i> Saída</h2>
<hr>
<p>A saída consiste na apresentação das informações quando solicitadas ( instruções list e current). Termine a execução apresentando a mensagem: "Jedi Wagner, assuma o comando!".</p>

<br/>
<br/>
<br/>
<div style="text-align:center; font-weigth: bold; font-size:2em;">
<label>Exemplos</label>
</div>
<table border=4px solid #121212;>
<tbody>
<tr boder=4px solid #121212>
<th border=4px solid #121212>Input</th>
<th border=4px solid #121212>Output</th>
</tr>
<tr boder=4px solid #121212>
<td>
add OyeComoVa<br/>
list<br/>
fight
</td>

<td>
OyeComoVa<br/>
Jedi Wagner, assuma o comando!
</td>


</tr>
<td>
add OyeComoVa<br/>
add SambaPaTi<br/>
current<br/>
list<br/>
fight
</td>

<td>
OyeComoVa<br/>
OyeComoVa,SambaPaTi<br/>
Jedi Wagner, assuma o comando!
</td>
<tr boder=4px solid #121212>


<tr boder=4px solid #121212>
<td>
add NaoExisteAmorEmSP<br/>
add Subirusdoistiozin<br/>
play<br/>
ended<br/>
ended<br/>
current<br/>
fight
</td>

<td>
NaoExisteAmorEmSP<br/>
Jedi Wagner, assuma o comando!
</td>
</tr>


<tr boder=4px solid #121212>
<td>
add Retrovisor<br/>
add Brejense<br/>
add EntaoPraQueOJardim<br/>
list<br/>
next Brejense<br/>
current<br/>
ended<br/>
current<br/>
fight
</td>

<td>
Retrovisor,Brejense,EntaoPraQueOJardim<br/>
Brejense<br/>
Brejense<br/>
Jedi Wagner, assuma o comando!
</td>
</tr>

<tr boder=4px solid #121212>
<td>
add MunRa<br/>
add NoSleepTillBrooklyn<br/>
add MalandroEhMalandro<br/>
add YoungWildFree<br/>
list<br/>
play<br/>
next MunRa<br/>
list<br/>
ended<br/>
current<br/>
next MunRa<br/>
list<br/>
fight
</td>
<td>
MunRa,NoSleepTillBrooklyn,MalandroEhMalandro,YoungWildFree<br/>
MunRa,NoSleepTillBrooklyn,MalandroEhMalandro,YoungWildFree<br/>
NoSleepTillBrooklyn<br/>
NoSleepTillBrooklyn,MunRa,MalandroEhMalandro,YoungWildFree<br/>
Jedi Wagner, assuma o comando!
</td>
</tr>

<tr boder=4px solid #121212>
<td>
add ApesarDeVoce<br/>
add Calice<br/>
add RodaViva<br/>
undo<br/>
add VaiPassar<br/>
add RodaViva<br/>
list<br/>
fight
</td>
<td>
ApesarDeVoce,Calice,VaiPassar,RodaViva<br/>
Jedi Wagner, assuma o comando!
</td>
</tr>

<tr boder=4px solid #121212>
<td>
add ApesarDeVoce<br/>
add Calice<br/>
add VaiPassar<br/>
add RodaViva<br/>
undo *<br/>
list<br/>
fight
</td>
<td>
[vazia]<br/>
Jedi Wagner, assuma o comando!
</td>
</tr>
</tbody>
</table>