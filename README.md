# Informatica applicata al suono
## Relazione del progetto relativo al modulo “pyo”

<h3>Introduzione</h3>
<p> 
  Il progetto consiste nella simulazione di un synth FM attraverso il linguaggio Python. <br>
Ho deciso di realizzare una struttura iniziale composta da un segnale portante (carrier) e due diversi modulatori:
</p>
<p align="center">
    <img src="images/im1.png" alt="alt text" width="50%" height="50%">
</p>
<br>
<p>
  Dopo di che ho deciso di dare la possibilità all’utente di ampliare la struttura aggiungendo uno o due modulatori, uno per ciascun segnale modulante già presente. <br>
Si possono quindi ottenere altre due strutture oltre alla prima già rappresentata:
</p>
<br>
<p align="center">
    <img src="images/im2.png" alt="alt text" width="50%" height="50%">
</p>
<br>

<h3>Struttura del codice</h3>
<p> 
  Per realizzare le diverse strutture presentate precedentemente ho implementato due diverse classi, “Oscillator” e “Mysynth”:
</p>
<br>
<h4>Classe Oscillator</h4>
<p>
  La classe “Oscillator” è definita come sottoclasse della classe “PyoObject”. <br>
Ho deciso di utilizzarla nella classe “MySynth” per istanziare due diversi tipi di modulatori, infatti nel costruttore vengono richiamati i costruttori delle classi “Sine” e “LFO”. <br>
Attributi della classe:
</p>

<ul>
  <li>f: frequenza dell’oscillatore.</li>
  <li>ratio: fattore moltiplicativo della frequenza portante. Rappresenta il rapporto tra frequenza
del segnale modulate e frequenza del segnale portante.</li>
  <li>modulatore: oggetto di tipo intero o PyoObject, rappresenta il modulatore della frequenza
dell’oscillatore; ha valore di default uguale a zero, usato nel caso in cui l’oscillatore in
questione non venga modulato in frequenza.</li>
  <li>mulindex: fattore utilizzato per controllare l’ampiezza del segnale modulante, in modo tale
da controllare l’incidenza di quest’ultimo sul segnale modulato.</li>
  <li>tipooscillatore: attributo che consente di scegliere quale oggetto istanziare nella classe
Oscillator, in particolare il valore 1 istanzia un oggetto di tipo Sine mentre il valore 0 un oggetto di tipo LFO, in questo modo si possono ottenere diversi tipi di modulazione della portante.</li>
</ul>
<br>
<p>Metodi della classe:</p>
<ul>
  <li>ctrl(): questo metodo della classe “Oscillator” richiama il metodo ctrl() dell’oggetto “osc”
istanziato nel costruttore della classe, che può essere di due tipi, Sine o LFO. In questo modo si otterranno due diversi tipi di finestre di controllo; inoltre aggiunge due SLMap alla map_list che consentono di regolare i valori di ratio e mulindex.</li>
  <li>play(), stop(), out(): sovrascrivono i metodi che consentono di ascoltare, stoppare e mandare in output il segnale.</li>
  <li>setF, setMulindex, setRatio: metodi che consentono di modificare i valori degli attributi f, mulindex e ratio.</li>
</ul>
<br>

<h3>Classe MySynth</h3>
<p>
  La classe “MySynth” è definita come sottoclasse della classe “PyoObject”.
Istanzia oggetti della classe “Oscillator” e li utilizza come modulatori del segnale portante. Il segnale portante viene istanziato come oggetto della classe Sine:
</p>
<br>
<p><c>
  self._carrier=Sine(freq=self._freqcarrier+self._osc1+self._osc2, mul=self._ampcarrier)
</c></p>
<br>
<p>
  “freqcarrier” e “ampcarrier“ hanno valori diversi in base all’input dello strumento MIDI collegato (nel caso non ci fossero strumenti MIDI a disposizione l’interprete Python genera una tastiera virtuale). <br>
Attributi della classe:
</p>
<ul>
  <li>
    tiposynth: attributo che consente di scegliere il numero di modulatori da istanziare nella classe MySynth per poter realizzare le diverse strutture del synth presentate nell’introduzione. Assumerà in corrispondenza i valori 1, 2, 3 per istanziare 2, 3 o 4 modulatori.
  </li>
</ul>
<br>
<p>Metodi della classe:</p>
<ul>
  <li>
    ctrl(): questo metodo della classe “MySynth” richiama il metodo ctrl() della classe
“Oscillator” sugli oggetti “osc”, ovvero sui modulatori; inoltre richiama il metodo ctrl()
sull’oggetto “ampcarrier” in modo tale da poter controllare l’inviluppo del segnale portante.
  </li>
  <li>
    play(), stop(), out(): consentono di ascoltare, stoppare e mandare in output il segnale
portante.

  </li>
</ul>
<br>
<p>
  Ho deciso di non definire altri metodi della classe perché non sarebbero stati funzionali allo svolgimento del progetto.
</p>
<br>

<h3>Problematiche riscontrate nello svolgimento del progetto</h3>
<p>
  Le problematiche riscontrate nello svolgimento del progetto sono legate al metodo ctrl() degli oscillatori, infatti non è stato possibile creare una SLMap per alcuni attributi degli oggetti LFO e Sine istanziati nella classe “Oscillator”.
In particolare ho avuto difficoltà nella gestione del parametro type degli oggetti LFO, per questo motivo ho richiamato il metodo ctrl() dell’oggetto nella definizione del metodo ctrl() della classe “Oscillator”.
</p>

