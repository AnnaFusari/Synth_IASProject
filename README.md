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

