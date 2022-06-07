---
mainfont: Lato-Regular.ttf
mainfontoptions:
- Scale=1.0
- BoldFont=Lato-Bold.ttf
- ItalicFont=Lato-Italic.ttf
- BoldItalicFont=Lato-BoldItalic.ttf
---

# Projekt zaliczeniowy - Algorytmy uczenia maszynowego
>imie i nazwisko ładnie
 
## Problem
Podejmowanym problemem jest znalezienie dopasowań wirusów do ich gospodarzy - bakterii, na podstawie genomów wymienionych organizmów. Poprzez dopasowanie rozumiane jest to, że dany wirus infekuje konkretną bakterię.

## Wprowadzenie
### Biologiczne znaczenie przewidywania par wirus-host
Większość całej wirosfery stanowią bakteriofagi - wirusy, które w sposób szczególny zakażają bakterie. Specyficzność infekcji i interakcje między nimi można opisać jako dopasowanie wirus-gospodarz. Aby zbadać różnorodność wirusów i ustalić ich taksonomię, do niedawna stosowano przede wszystkim hodowlę laboratoryjną takich par. Jest to również jedyny sposób na kompleksowe scharakteryzowanie cyklu infekcyjnego wirusa lub jego interakcji z komórką gospodarza na poziomie molekularnym. @coclet_global_2021 Jednak hodowla takich par jest często trudna, ponieważ oba organizmy wymagają często specyficznych warunków do wzrostu. Poza poznawaniem różnorodności, identyfikacja par pozwala również na:
 -  zrozumienie koewolucji fagów i ich gospodarzy, 
 -  projektowanie eksperymentów w celu zbadania interakcji fag-gospodarz, 
 -  wnioskowanie o sieciach zakażeń krzyżowych fag-bakteria, 
 -  badanie potencjalnej roli fagów w horyzontalnym transferze genów, rozprzestrzenianiu czynników wirulencji i rozprzestrzenianiu oporności bakterii na antybiotyki
 
Wiele wymienionych powyżej zastosowań bezpośrednio przyczynia się do badań nad ludzkim zdrowiem - na przykład, wiemy, że bakterie stanowią one bardzo ważną część mikrobiomu w jelitach, a bakteriofagi ciągle na niego wpływają. Poprzez właśnie takie interakcje, powodowane są zmiany w składzie i liczebności społeczności bakteryjnej, co jest ściśle związane z takimi chorobami, jak zespół jelita drażliwego (IBS), nieswoiste zapalenie jelit (IBD), rak jelita grubego (CRC), zakażenie Clostridium difficile (CDI), otyłość i zaburzenia neurologiczne. Niestety, siły, które kształtują skład tych społeczności bakteryjnych, pozostają niewystarczająco poznane, co spowalnia rozwój terapii i biomarkerów opartych na mikrobiomie. @sutton_gut_2019

W ostatnich latach rozwój sekwencjonowania następnej generacji (next-generation sequencing) był bardzo dynamiczny i wpłynął na odkrywanie wirusów, uniezależniając je od izolacji wirusów w laboratorium. Ze względu na to, że mikroby i wirusy mogą być bezpośrednio sekwencjonowane bez hodowli, ilość danych metagenomicznych do przetworzenia stale rośnie. @paez-espino_uncovering_2016 W związku z tym pojawia się poważny problem - podczas gdy hodowane wirusy są nieodłącznie związane z jednym ze swoich gospodarzy, tj. z tym, z którego wirus został wyizolowany, nie dotyczy to fagów identyfikowanych wyłącznie na podstawie metagenomów. Jeśli więc większość fagów pochodzących z metagenomów nie jest związana z konkretnym gospodarzem, stwarza to zupełnie nowe wyzwanie dla bioinformatyków, polegające na stworzeniu metod efektywnego i dokładnego przewidywania par wirus-gospodarz na podstawie danych metagenomicznych. @coclet_global_2021 @roux_imgvr_2021

### Aktualne podejścia przewidywań @coclet_global_2021
Obecnie, nie ma uniwersalnego rozwiązania, które dawałoby znacząco lepsze wyniki niż inne metody. Przyczyna leży  w nadal nie do końca poznanej złożoności problemu oraz różnorodności metod, które można wykorzystać do przewidywania. Istnieją trzy główne kategorie metod, a w każdej z nich istnieje wiele cech, które służą do wyszukiwania dopasowań, co stwarza możliwość opracowania różnorodnych podejść. Każda kategoria ma swoje charakterystyczne zalety i ograniczenia: 

-  **Metody oparte na przyrównaniach sekwencji** wykazują ogólnie wysoką specyficzność/dokładność i są w stanie zidentyfikować gospodarzy fagów niezwiązanych z genomem referencyjnym faga, ale zazwyczaj są silnie uzależnione od bazy danych genomu gospodarza, co często prowadzi do niskiego współczynnika czułości. Dodatkowo, są one bardzo powolne w działaniu, ponieważ rdzeniem przyrównań są narzędzia lokalnego przyrównywania sekwencji pochodzących z biologicznych baz danych, np. BLAST.

-  **Metody wolne od przyrównań sekwencji (alignment-free)** są niezależne od referencyjnych baz danych i dlatego są w stanie zidentyfikować gospodarzy dla zupełnie nowych fagów bez powiązanych z nimi genomów referencyjnych. W porównaniu z innymi metodami wiąże się to jednak z wysokim odsetkiem wyników fałszywie pozytywnych i często wymaga dodatkowych testów statystycznych. Natomiast, ich dużą przewagą jest szybkość działania, która jest o rzędy wielkości większa względem metod opartych na przyrównaniu sekwencji.

-  **Metody integracyjne** mają większą dokładność i czułość dzięki uwzględnianiu i integrowaniu wielu sygnałów, ale średnio wymagają dłuższego czasu obliczeń, ponieważ wymagają wyników z kilku indywidualnych podejść predykcyjnych, np. mogą używać klasyfikatorów uczenia maszynowego w połączeniu z przyrównaniami sekwencji. 

### Cel pracy
Celem jest opracowanie metody przewidywania par wirus-gospodarz w zależności od lokalnych fluktuacji składu sekwencji zarówno w sekwencjach gospodarza, jak i wirusa. Metoda ta ma mieć charakter hybrydowy (integracyjny), ponieważ łączy wykorzystanie cech składu sekwencji z technikami uczenia maszynowego. Część uczenia maszynowego jest obsługiwana przez narzędzie o nazwie fastDNA @menegaux_continuous_2019, którego oryginalnym zastosowaniem jest wolna od przyrównań klasyfikacja taksonomiczna krótkich sekwencji metagenomicznych. Dodatkowo, opracowywana metoda będzie najbardziej zbliżona do podejścia zastosowanego w narzędziu WIsH (Who is the host?) @galiez_wish_2017 i celem będzie również uzyskanie lepszej skuteczności przewidywań od tego narzędzia.

## Metody
### Zestaw danych
Jako zestaw danych wykorzystywany jest zestaw porównawczy składający się z 820 kompletnych sekwencji genomów fagów i 2698 kompletnych sekwencji genomów bakterii, które zostały pobrane z bazy danych NCBI RefSeq, które wykorzystuje Edwards. @edwards_computational_2016 Informacje o gospodarzu zostały pobrane z pola "host" w rekordzie RefSeq faga, a fagi, których gospodarz nie miał całkowicie zsekwencjonowanego genomu, zostały usunięte. W ten sposób uzyskano 820 fagów ze 153 różnymi gospodarzami bakteryjnymi. W celu lepszego zarządzania tymi plikami, utworzone zostały pliki json z metadanymi tych genomów, w których znajdują się:

 - numer akcesyjny z bazy NCBI
 - pełna nazwa organizmu
 - NCBI Taxonomy ID
 - poziomy taksonomiczne
 - dla metadanych wirusów - ich prawidłowy gospodarz
 
Te metadane są ekstensywnie używane na każdym etapie działania programu i co najważniejsze, pozwalają ocenić prawdziwość przewidywań.
Do uczenia modelu jak i testów jest używany ten sam zestaw danych - nie jest to problemem, ponieważ model jest uczony jedynie na genomach gospodarzy, a z kolei jego ewaluacja i testy są wykonywane przy użyciu **losowych fragmentów** o określonej długości z genomów wirusów, które mają na celu symulować odczyty z sekwencjonowania metagenomicznego.

### fastDNA @menegaux_continuous_2019

fastDNA to narzędzie służące do klasyfikacji taksonomicznej krótkich odczytów z sekwencjonowania metagenomicznego. Nie wykorzystuje ono jednak żadnego z klasycznych podejść obliczeniowych do klasyfikacji taksonomicznej, takich jak lokalne przyrównania sekwencji względem bazy referencyjnej sekwencji (BLAST), mapowanie krótkich odczytów (Burrows-Wheeler aligner - BWA), ale przekształca zadanie w problem klasyfikacji wielu klas z wykorzystaniem uczenia maszynowego, gdzie źródłem danych są przekształcenia k-merów sekwencji. W celu przekształcenia sekwencji do postaci odpowiedniej dla metod uczenia maszynowego fastDNA wykorzystuje ciągłe osadzanie sekwencji. Natomiast wykorzystywaną metodą klasyfikacji jest model liniowy, w którym wykorzystywana jest generalizowana wielowymiarowa funkcja logistyczna.

#### Osadzanie odczytów

Sekwencję DNA można zakodować w postaci wektora w $N$ wymiarach ($N = 4^k$, ponieważ na każdą pozycję sekwencji długości $k$ przypada jeden z nukleotydów $\{A, C, G, T\}$). Okazuje się, że nie jest to optymalna reprezentacja, ponieważ stawia duże wyzwanie obliczeniowe zarówno w czasie treningu modeli wykorzystujących dane w takiej formie, jak i w czasie testu - spowodowane jest to tym, że macierz wag o wymiarach $N \times T$ musi być składowana w pamięci dla ewaluacji $T$ gatunków.
fastDNA optymalizuje ten krok poprzez osadzanie zbioru odczytów DNA do przestrzeni $\mathbb{R}^d$, gdzie $d\ll N$. W tym celu nadal wyodrębniany jest skład k-merów każdego odczytu, ale zastępowane jest $N$-wymiarowe kodowanie one-hot każdego k-meru kodowaniem $d$-wymiarowym, zoptymalizowanym do rozwiązania zadania. Podejście to jest podobne do, na przykład, modelu fastText dla sekwencji języka naturalnego (a sam fastDNA jest w praktyce zmodyfikowaną wersją fastText). @bojanowski2016enriching @joulin2016bag Warto zwrócić uwagę, że są wprowadzone pewne zmiany w porównaniu do metod przetwarznania języka naturalnego (NLP) z fastText w celu optymalizacji pod kątem sekwencji DNA:

-  w danych sekwencji DNA nie istnieje pojęcie "słowa", czyli grupy liter ograniczonych przestrzenią. W związku z tym stosowana jest rozproszona reprezentacja tylko nakładających się k-merów, a nie słów
- słownictwo jest inne, ponieważ ma ono znaną wielkość ($4^k$) i jest gęsto reprezentowane (powtarzające się) dla stosunkowo małych wartości $k$. Przy większych wartościach $k$ $k$-mery stają się rzadkie, a pojedyncze długie $k$-mery mogą być dyskryminujące. 

Dzięki wyżej wymienionym zmianom, zmniejszone są wymagania pamięciowe dotyczące przechowywania modelu, co przyspiesza czas klasyfikacji, gdy $d < T$, ponieważ macierz $N \times T$ wag jest zastąpiona przez macierz $N \times d$ embeddingów i macierz $d \times T$ wag, które dodatkowo są stałej wielkości (co jest ułatwieniem w implementacji).

#### Uczenie osadzania

Problem jaki podejmuje fastDNA jest zdefiniowany jako wieloklasowy problem klasyfikacji, gdzie każdy z $T$ gatunek bakterii jest traktowany jako klasa i do tych klas musi zostać zaklasyfikowany odczyt. 
Rozważa się uczenie macierzy $M$ osadzeń i linowego modelu $W\in\mathbb{R}^{T\times d}$, który jest macierzą wag. W tym celu, na podstawie podawanych przykładów zakodowanych sekwencji transformowana jest punktacja przewidywań na prawdpodobieństwa za pomocą funkcji softmax, która jest uogólnieniem funkcji logistycznej dla wielowymiarowych danych. Dzięki temu jest minimalizowane ryzyko empiryczne przy użyciu straty entropii krzyżowej, która mierzy wydajność modelu klasyfikacyjnego, dającego wyniki predykcji z przedziału 0-1. Strata entropii krzyżowej rośnie, gdy przewidywane prawdopodobieństwo odbiega od rzeczywistego zaklasyfikowania, dlatego idealny model miałby wartość straty równą 0. Funkcja celu dla przewidywań jest iteratywnie optymalizowana metodą stochastyczną (stochastic gradient descend - SGD), co jest najbardziej optymalnym podejściem do polepszania wyniku, ponieważ genomy z zestawu treningowego są analizowane po kolei. Warto zauważyć, że gdy $d < T$, to problem jest zwykle niewypukły i SGD może być zbieżne tylko do lokalnego optimum.

### Workflow
```{.mermaid theme=neutral height=400 width=1000 format=pdf}

graph  TD;

	subgraph make model
	sq6[create working directory]-->sq7[filter host genomes by criteria];
	sq7[filter host genomes by criteria]-->sq8[save chosen genomes and TaxID list];
	sq8[save chosen genomes and TaxID list]-->sq9[run fastDNA training module];
	sq9[run fastDNA training module]-->sq10[remove temporary genomes file];
	end
	
	subgraph random sampling
	sq14["read query (virus) genomes"]-->sq15[sample random fragments];
	sq15[sample random fragments]-->di{"N < N treshold"};
	di{N<N treshold}-- No --> sq15[sample random fragments];
	di{N<N treshold}-- Yes --> sq16[save sequence fragments to file]
	end
	
	subgraph workflow2
	sq11[create working directory]-->sq12[run random sampling];
	sq12[run random sampling]-->sq13[run fastDNA predict-prob module];
	sq12-...-sq14
	end

	subgraph scoring
	sq17[load fastDNA predic-prob results]-->sq18[score results];
	sq18[score results]-->sq19[calculate evaluation];
	sq19[calculate evaluation] --for every scoring function-->sq18;
	sq19[calculate evaluation]-->sq20[choose function with best evaluation as final result]
	end
	
	subgraph main
		 sq[read metadata] -->sq2[run make model];
		 sq2[run make model]-->sq3[run workflow2];
		 sq2[run make model]-..-sq6
		 sq3[run workflow2]-->sq4[run scoring];
		 sq3[run workflow2]-..-sq11;
		 sq4[run scoring]-->sq5[dump result to json];
		 sq4-...-sq17
	end
```
#### Trening modelu i optymalizacja
#### Przewidywanie par
## Wyniki
### dokładność (accuracy)
### Czułość (recall)
### precyzja (precision)
### specyficzność (specificity)
### miara F1 (F1-score)
### jednoskowa wizualizacja przewidywań
### Porównanie z WIsH
## Bibliografia
