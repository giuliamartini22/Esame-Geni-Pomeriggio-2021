Grafo semplice, pesato e non orientato (Graph)
Nodi: tutte le localizzazioni (tabella classification, colonna localization)
Archi: Ogni localizzazione contiene un insieme di geni, i quali possono essere collegati tra di loro attraverso la tabella 
interactions. I vertici corrispondenti a due localizzazioni saranno collegati da un arco se e solo se esiste almeno una 
interazione che coinvolge due geni, rispettivamente della prima della seconda localizzazione (o nell’ordine inverso).

Il peso di ciascun arco dovrà essere un numero intero, pari al numero di tipi (Type) diversi di interazioni tra i geni associati 
alle due localizzazioni.
