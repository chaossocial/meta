---
layout: post
title:  "Ein Jahr chaos.social!"
date:   2018-04-15 10:00:00
language: de
translation: one-year-chaos-social
---

chaos.social ist heute ein Jahr alt! Letztes Jahr, am 15. April, haben wir die Registrierung für euch [geöffnet](https://chaos.social/@ordnung/1003), nachdem wir am 13. April lostooteten:

<div class="toot two-toots">
<iframe src="https://chaos.social/@rami/1/embed" class="mastodon-embed" style="max-width: 100%; border: 0" width="400" height="170"></iframe><script src="https://chaos.social/embed.js" async="async"></script>
<iframe src="https://chaos.social/@rixx/2/embed" class="mastodon-embed" style="max-width: 100%; border: 0" width="400" height="170"></iframe><script src="https://chaos.social/embed.js" async="async"></script>
</div>

Seitdem sind wir ganz schön gewachsen. Mittlerweile nutzen über 2000 Menschen unsere Instanz und über 2000 weitere Instanzen sind im Fediverse mit uns verbunden. Das ist auch ordentlich gewachsen. Mastodon föderiert nicht nur (ziemlich) nahtlos mit den schon altbekannten Föderationsteilen wie GNUSocial, sondern auch mit den neueren wie z.B. PeerTube. Es steht nie still, und jeden Monat finden sich neue spannende Erweiterungen und Möglichkeiten im und ums Fediverse.

## Wir?

Wir hatten chaos.social als eine der Instanzen für die Chaos-Community angefangen, und fühlen uns da auch nach wie vor den Prinzipien der Transparenz von öffentlichen Daten, Schutz von privaten Daten, und Dezentralität verpflichtet.
* Transparenz: Wir haben schon früh angefangen, alles instanzspezifische transparent zu machen: Wir haben ein [Repo](https://github.com/chaossocial/about), in dem unsere öffentlichen Texte und Regeln einsehbar sind, damit Änderungen transparent sind. Unsere eigenen [Anpassungen](https://github.com/chaossocial/custom) an der Instanz sind auch öffentlich – danke hier besonders [@rash](https://chaos.social/@rash) (Fairydustelefant, Sticker, …) und [@blinry](https://chaos.social/@blinry) (Fairydustfavicon) für die Verschönerungen!
* Schutz: Wir haben eine Reihe von Regeln, die auf guten Umgang abzielen, und die wir auch nach Notwendigkeit anpassen. Während wir bereit sind, diese auch durchzusetzen, haben wir das nur sehr selten gemusst. Über das letzte Jahr gab es insgesamt 50 Reports, also nicht mal einen pro Woche (einige davon aber in derselben Sache von mehreren Menschen). 68% davon gingen gegen Accounts von anderen Instanzen.
* Dezentralität: Wir sind ganz froh, nicht zu groß gewachsen zu sein. Die Hardware könnte es aktuell noch eine weile ab (s.u.), aber sozial muss sich jeder Schwapp neuer Nutzerinnen erst mal akklimatisieren. Für weitere Diskussion von Dezentralität des Fediverses guckt euch btw. mal die Ergebnisse von [Leahs Untersuchung](https://chaos.social/@leah/99837391793032137) über die Verteiltheit der Instanzen auf Netz/Hoster-Ebene an.

## Nutzung

![User development over the last year]({{ "/assets/images/users.png"}})
![Toots per hour over the last year]({{ "/assets/images/toots.png"}})

Anfangs gab es natürlich eine große Signup-Welle. Neugierige aller Art, unter anderem auch angelockt durch rixx' [Talk](https://media.ccc.de/v/gpn17-8575-mammut_statt_vogel) auf der GPN und sein [Interview](https://netzpolitik.org/2017/interview-die-anfangsphase-des-alternativen-sozialen-netzwerks-mastodon-ist-vorueber/) mit netzpolitik.org.
Man sieht die Durststrecke im letzten Sommer ganz gut – nach anfänglicher Begeisterung sah es etwas aus, als würden Mastodon den weg vieler sozialer Netze gehen und bis auf ein paar wenige Nutzerinnen total versanden. Die Instanz lief zwar, und war auch ein sehr netter Unterhaltungsort, aber gleichzeitg auch etwas schläfrig. Über die letzten Monate gings aber gut ab - Ausrutscher seitens Twitter, prominente Features über die Facebook-Sache, vielleicht auch die Werbung auf dem Congress … wir wachsen. Die lokale Timeline ist gut gefüllt.

## Infrastruktur

Um die Instanz zu betreiben, braucht es auch eine entsprechende Infrastruktur auf der sie laufen kann. Die besteht bei uns aktuell aus einem per Ansible konfigurierten virtuellen Server der auf [Leahs](https://chaos.social/@leah) Infrastruktur bei Hetzner läuft. Seit unserem Start vor einem Jahr ist diese VM mit der Zahl der Nutzerinnen immer weiter mit gewachsen, damit für euch alles weiter flüssig läuft. Aktuell hat die VM 12GB RAM, 4 CPU-Kerne und 120GB SSD Storage. Letzterer droht uns immer mal wieder voll zu laufen, weswegen wir in unregelmäßigen Abständen die alten Medien von Remote Instanzen löschen, um nicht immer weiter Speicher ergänzen zu müssen. Aber keine Sorge, solltet ihr einen alten Toot aufrufen, werden die Daten einfach wieder von der ürsprünglichen Instanz nachgeladen.

Damit uns keine großen Probleme drohen, wenn dabei oder bei anderen Arbeiten doch mal etwas schief geht, legen wir tägliche Backups des Systems an. Natürlich haben wir auch Monitoring auf die Erreichbarkeit der Instanz, und, wie ihr oben sehen konntet, die Entwicklung ihrer Größe und Nutzung.

Was die Zukunft für die Infrastruktur bringt, wird sich zeigen. Aktuell skaliert das Setup mit nur einem Server noch gut für uns, aber wir sind trotzdem auch weiterhin dabei die notwendigen Stellschrauben zu suchen und anzupassen damit ihr beim Benutzen der Instanz nicht einschlaft.

## Wie weiter?

Wir sind mit chaos.social soweit ganz glücklich. Wenn die Instanz weiter wächst, werden wir auf neue (soziale wie technische) Herausforderungen stoßen, und die weiter mit aller möglicher Transparenz und Experimentierfreudigkeit angehen.

Falls ihr uns dabei finanziell (Hosting-Kosten und Domain-Kosten) unterstützen könnt und wollt, werft mal einen Blick auf unseren [liberapay-Account](https://liberapay.com/chaos.social/). 

Und falls ihr dieses Jahr auf der GPN seid, gibt es vielleicht wieder einen Vortrag, aber auf jeden Fall ein Nutzerinnentreffen :)

