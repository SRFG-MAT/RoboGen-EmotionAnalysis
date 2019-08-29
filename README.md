# RoboGen-EmotionAnalysis

Dieses Projekt beinhaltet zwei unabhängige Projekte:
1) Mimic Emotion Analysis with OpenCV and DLib: zur Erkennung/Analyse von Mimik und Sprache
2) Emotion Detection Speech: Sprache-zu-Text Transformation und Text wird als Emotion interpretiert

# Mimic Emotion Analysis with OpenCV and DLib

Vorraussetzungen
Je nachdem welches Programm ausgeführt werden soll (EmotionDetection vs. EmotionDetectionDlib - genauere Beschreibung in Projektstruktur: 8 Programme) muss eine weitere Bibliothek installiert werden. OpenCV und Sklearn (pip install opencv/sklearn) für Python sind Grundvoraussetzungen für beide Programme. Dlib wird nur für das zweite Programm (EmotionDetectionDlib) benötigt. Hier muss auf das jeweilige Betriebssystem Rücksicht genommen werden, weshalb hier keine weiteren Anleitungen niedergeschrieben werden.

Quellen
Die MEA wurde aus einem bereits existierenden Projekt abgeleitet. Paul van Gent hat hierbei ein Programm geschrieben, dass mit Hilfe der DLib-Library Bilder in 68 Features transfomiert und anhand einer Distanzmessung die Emotion prediktiert. Für das komplette Tutorial bitte auf folgende Seite gehen: http://www.paulvangent.com/2016/08/05/emotion-recognition-using-facial-landmarks/. Es wird darauf hingewiesen, dass dieses Projekt auf bereits zwei vorhergehenden Projekten/Tutorials aufbaut. Diese sind in dem Link referenziert.

Was Trainings-/Bildmaterial für das Erstellen des Models betrifft gibt es mehrere mögliche Quellen. Diese Datensätze sind jedoch nicht nur für diesen Use Case erstellt worden und müssen somit vorverarbeitet/angepasst werden.

Cohn-Kanade Dataset (http://www.consortium.ri.cmu.edu/ckagree/): Hierbei handelt es sich um zwei Datensätze (CK und CK+). Letzterer liefert mehr Bildmaterial und ist daher für uns von mehr Relefanz. Paul van Gent liefert in einem seiner Tutorien bereits drei verschiedene Algorithmen mit, mit denen der Datensatz vorbereitet werden kann.

Ein Datensatzpool mit verschiedenstem Bildmaterial, dass potenziell in das Programm eingespeißt werden kann ist unter folgendem Link zu finden: http://pics.psych.stir.ac.uk/2D_face_sets.htm. Es können dort verschiedene Datensätze von unterschiedlichen Instituten gefunden werden, die Fokus auf unterschiedliche Emotionen, etc. gesetzt haben. Die Form, in der die Daten gespeichert worden sind, variieren sehr stark. Man sollte weiters darauf achten, dass die Menge der jeweiligen Klassen, was Bildmaterial betrifft, sich nicht zu sehr unterscheiden. Dies könnte ansonsten zu einem unvorteilhaft trainierten Model führen.

Unter dem oben genannten Datensatzpool kann der Pain Dataset by CMU (http://www.consortium.ri.cmu.edu/data/pain/README) gefunden werden. Dieser beinhaltet jene, von Paul Eckman, definierten Emotionen und Bilder von Schmerz. Dies ist der zweite Datensatz, der für das Trainieren des Models verwendet wurde.

Sollte neben diesen Datensätzen noch weitere benötigt werden, ist hier eine Liste von potenziellen Erweiterungen:

http://vis-www.cs.umass.edu/lfw/#download

http://www.kasrl.org/jaffe.html

http://cvit.iiit.ac.in/projects/IMFDB/

http://www.cs.columbia.edu/CAVE/databases/pubfig/

http://vision.ucsd.edu/~iskwak/ExtYaleDatabase/ExtYaleB.html

http://grail.cs.washington.edu/projects/deepexpr/ferg-db.html

http://app.visgraf.impa.br/database/faces/

http://mohammadmahoor.com/affectnet/

Jeder der oben genannten Datensätze braucht mehr oder weniger Zeit (2 Stunden bis zu 2 Tage), um gedownloaded zu werden. Es sollte somit mit ausreichend Zeit gerechnet werden!

Projektstruktur
Das Projekt besteht aus vier Foldern, die jeweils weitere Folder inkludieren, 8 Programmen, zwei SAV-Files, 4 XML-Files und einem Dat-File.

Von den vier Foldern ist eig. nur das "dataset" von Relevanz. Dieser Folder beinhaltet die sortierten und bearbeiteten Bilder, die für das Trainieren des Models notwendig sind. Die Struktur des Folders ist so aufgeteilt, dass die 6 Grundemotionen, sowie die Schmerzbilder in unterschiedlichen Folders vorzufinden sind. Dies erlaubt verschiedene Emotionen zu exkludieren bzw. neues Material unabhängig von den anderen Emotionen zu inkludieren (bitte darauf achten, dass die Anzahl der Daten nicht zu sehr differenzieren).

Die 8 Programme:

- EmotionDetection.py: Eine primitive Form der Emotionsanalyse mit der Hilfe von FischerFaceRecognizer. Der Vorteil hier ist der minimierte Aufwand, bis das Projekt starten kann. Es muss u.a. kein DLib installiert werden, dass je nach Betriebssystem länger dauern kann

- EmotionDetectionDlib.py: Dies ist die "aufgepimpte" Version von EmotionDetection.py, die mit DLib arbeitet. Die Implementierung wurde so gewählt, dass das Training des Models in einem separaten Programm passiert, um den Start der MEA zu beschleunigen.

- Experiments.py: Hierbei handelt es sich um ein Programm das lediglich als Hilfe zur Implementierung von EmotionDetectionDlib.py verwendet worden ist. 

- ExtractingFaces.py: Eines jener Programme das für die Vorbereitung des CK+ Datensatzes verwendet worden ist. (wird als letztes ausgeführt)

- FaceDetectionWebCam.py: Dieses Programm kann für das Verständnis des EmotionDetectionDlib.py-Programms verwendet werden. Es zeigt in der WebCam an, wie die 68 Features generiert werden.

- OrganisingDataset.py: Das erste Programm für die Vorbereitung des CK+ Datensatzes. Extrahiert die Bilder aus source_images und die Textinformationen aus source_emotion.

- SeeExtractedTrainingParameters.py: Ein weiteres Programm, dass für das weitere Verständnis von EmotionDetectionDlib.py entwickelt worden ist. Dient zum Verständnis welche Daten und deren Form in das Model eingespeißt werden.

- TrainAndSaveModel.py: Dieses Programm ladet alle Trainingsdaten und Trainiert anschließend das Model (Support Vector Machine - SVM). Der Prozess kann etwas Zeit in Anspruch nehmen (abhängig von der Hardware)
Die zwei SAV-Files sind bereits trainierte Modelle. EDModel.sav stellt jenes Model dar, dass nur ausgewählte Emotionen beinhaltet (Fear, Happiness, Pain, Neutral, Sadness und Surprise). Wiederum das zweite SAV-File (EmotionPredictionModel_All.sav) wurde mit der Hilfe von allen Emotionen trainiert.

Die 4 XML-Files sind einerseits notwendig um die CK+ Daten vorzubereiten, sowie auch um bei den zwei Programmen (EmotionDetection + DLib) die Gesichter der Webcam zu erkennen. Es wird prinzipell nur das "alt" verwendet. Es können jedoch auch die anderen drei verwendet werden. Der Unterschied sollte sich, wenn überhaupt, in Grenzen halten.
Das Dat-File (shape_predictor_68_face_landmarks.dat) dient für die Generierung der 68-Features, die für das Dlib-Programm notwendig sind.

TrainAndSaveModels.py
Wie bereits oben kurz beschrieben, trainiert dieses Programm das Model für das Programm EmotionDetectionDlib.py. Das Programm kann prinzipiell so beschrieben werden, dass es alle Bilder aus dem generierten Datensatz entnimmt und aus jedem Bild einen 4x68 Vektor generiert. Die vier Spalten spiegeln die x- und y-Koordinate wieder, sowie die Normalisierte Distanz zum Mittelpunkt des Gesichts (sehr häufig die Nase) wie auch den Winkel von x und y. Nachdem die Features für jedes Bild berechnet wurden, werden diese in die SVM von Sklearn eingespeißt. Die Funktion make_sets dient nur dazu die Daten zu laden (data und labels). Im letzten Schritt wird das trainierte Model via der Bibliothek Joblib gespeichert.
Die Featurewahl sowie auch die SVM wurden vom Tutorial übernommen. Dieses beschreibt relativ verständlich warum diese Faktoren gewählt worden sind.

EmotionDetectionDlib.py
Nachdem das File EDModel.sav erschaffen worden ist (ist dem nicht der Fall bitte das Programm TrainAndSaveModels.py ausführen), kann das Programm EmotionDetectionDlib.py ausgeführt werden. Dieses ladet im ersten Schritt den FaceCascade-Classifier (um Gesichter zu erkennen), die Dlib-Featureextrahierung, das vortrainierte Model wie auch den Kamerastream. Das Programm befindet sich anschließend in einer Dauerschleife, die via 'q' beendet werden kann und systematisch eine Gesichtserkennung laufen lässt. Wird ein Gesicht erkannt, werden die Frames analysiert, die 4x68 Features werden berechnet und anschließend wird eine Emotion prediktiert. Da die Genauigkeit von Mensch zu Mensch unterschiedlich ist (verschiedene Gesichtsformen und Ausdrücke von Befindlichkeiten) wurde eine List eingebaut, die den Mode der letzten 5 Werte berechnet. Dies stabilisiert den Prozess, was explizite Emotionen betrifft, macht es jedoch nicht möglich auf Mikroausdrücke zu reagieren. Nachdem die häufigste Emotion berechnet worden ist, wird diese auf dem Videoausgang geschrieben (oberhalb des Rechteckes).

Nächste Schritte/Verbesserungen
Um die MEA noch weiter zu verbessern können weitere Schritte getätigt werden. Diese inkludieren u.a. die Erweiterung der Trainingsdatensätze sowie das Verwenden von Deep Learning. Im besten Fall sollte beides gemacht werden, wobei vor allem die Erweiterung der Datensätze sehr viel Zeit in anspruch nehmen wird (Download benötigt einiges an Zeit und auch die Extrahierung, Sortierung und Adaptierung an das benötigte Bildformat beanspruchen bereits in deren einzelnen Schritten Zeit).


# Emotion Detection Speech

Um aus Worten emotionale Assoziationen extrahieren zu können, wurde das Projekt EmotionDetectionSpeech entwickelt. Es wird hierbei im Sinne eines Wörterbuchverfahrens die am stärksten ausgedrückte Emotion definiert. Es wurde versucht anderweitige Datensätze zu finden, die ein komplexeres Verfahren/Model erlauben würden, jedoch scheiterte dieses Vorangehen anhand der fehlenden Datensätze. Sollte dies jedoch gewollt werden, müsste im ersten Schritt ein eigener Datensatz generiert werden bzw. eine semantische Übersetzung eines bereits existierenden Englischen Datensatzes (LINK: https://github.com/sarnthil/unify-emotion-datasets/tree/master/datasets).

Aufbau
Das Projekt beinhaltet 6 Programme und 8 MP3-Files.

Die 6 Programme bestehen aus

- Emotion_Dictionary.py: Dieses Dictionary ist eine kondensierte Version des Emotion_Dictionary_Various_Emotions.py

- Emotion_Dictionary_Various_Emotions.py: Hierbei handelt es sich um ein Wörterbuch, dass Eckmans 6 Hauptemotionen, aufgeteilt mit Plutchiks Rad der Emotionen, beinhaltet.

- Main_Programm.py: Dies ist das Hauptprogramm.

- Processing_Audio.py: Der Sprachbefehl wird in diesem Programm in Text via Google Cloud Speech API transformiert.

- Speech_Experiment.py: Aus Programm zum experimentieren, wenn gewollt

- Various_Functions.py: Hierbei handelt es sich um eine Summation von verschiedenen Funktionen, die verwendet werden. U.a. Preprocessing, etc.

8 MP3-Files dienen lediglich der Audiowiedergabe für eine spezielle Emotion.

Programmverlauf
Nach dem Laden der einzelnen Libraries geht das Programm in eine Dauerschleife über, die via den Kommandos/Aussagen "aus" und "programm beenden" beendet werden kann. Alle anderen Aussagen werden auf emotionelle Komponenten/Wörter analysiert. Hierfür wird als erstes das Audio-Signal in Text via Google Cloud Speech Transformiert. Anschließend wird der Text vorbereitet. In der aktuellen Version werden lediglich die Satzzeichen entfernt sowie auch alles in Kleinbuchstaben transformiert. Anschließend wird jedes Wort mit dem Wörterbuch verglichen. Das sich am ähnlichste Wort wird anschließend als Hauptemotion gespeichert. Dies folgt auch der Theorie von Eckman die aussagt, dass immer eine Emotion in einem Satz vorkommt (u.a. auch Assoziationen, die Personen mit einem Wort verbinden - somit nichts kulturelles, sondern subjektives/persönliches). Nachdem die Hauptemotion bestimmt worden ist (sollte ein wieteres Wort gefunden werden, mit einem equivalenten Wert, wird dieser nicht mehr berücksichtigt. Die erste erkannte Emotion ist der "Hauptauslöser") wird auf Negierungen analysiert. Sollte eine Negierung gefunden werden, wird die Hauptemotion zu dessem Gegenteil umgewandelt (dies basiert u.a. auf der Theorie von Plutchis).

Wurde die Emotion nun endgültig berechnet, wird ein MP3-File abgespielt. Dieses ist auf eine positive Unterstützung der jeweiligen Emotion ausgelegt.

Weitere Schritte/Verbesserung
Da dieses Programm nur einem Dictionary-Approach folgt ist auch die Effektivität nur begrenzt gegeben. Wie bereits oben erwähnt wäre es vermutlich sinnvoll, wenn man Trainingsdatensätze erstellt und diese via dem Konzept der Wortvektoren trainiert.