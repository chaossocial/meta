---
layout: post
title:  "Automatisierte Spam-Moderation"
date:   2025-09-02 08:00:00
language: de
translation: automated-spam-moderation
---

Wenn ihr mal einen richtig schönen Rant hören wollt, dann fragt uns in einer ruhigen Minute, wie wir das
Moderations-Interface von Mastodon so finden. Die höfliche Kurzfassung ist: Nach vielen Jahren intensiver Nutzung ist es
meistens nur nervig, aber wenn eine große Spam-Welle aufschlägt, macht es uns aktiv das Leben schwer.

Weil der Spam im Fediverse nicht weniger wird, haben wir da jetzt ein
[Skript](https://github.com/chaossocial/meta/blob/master/bin/auto-moderator) für.

## Das Skript

Das Skript ist im Kern einfach: Wenn eine bestimmte Anzahl von Leuten (wobei lokale Meldungen stärker gewichtet werden
als Meldungen von anderen Instanzen) denselben Account wegen Spam melden, und dieser Account bestimmten Mustern folgt,
blockt unser Skript ihn automatisch.

Ein Teil der Prüfung geht ganz stumpf auf feste Spam-Texte, die wir immer wieder beobachten (wie die aktuell beliebten
Verifizierungs-Scammer). Daneben prüfen wir aber auch, ob der Account z.B. denselben Text immer wieder postet (um
@mentions bereinigt, natürlich, da Spammer gerne denselben Text an verschiede Accounts schicken).

Außerdem prüfen wir, wie oben schon erwähnt, auch, wie viele Posts von wie vielen Accounts gemeldet werden, wobei wir
bei lokalen Meldungen niedrige Schwellwerte einsetzen. Diese Schwellwerte haben wir über die vergangenen Monate
justiert, können sie aber auch jederzeit weiter anpassen, zum Beispiel um vorübergehend schneller auf eine neue
Spam-Welle zu reagieren.

Der Bequemlichkeit halber sperrt das Skript auch automatisch Accounts, die auf ihrer Heiminstanz bereits gesperrt sind
(hauptsächlich um Benachrichtigungen aufzuräumen, die nicht automatisch entfernt werden).

**Das Skript blockt niemals lokale Accounts oder jemanden, dem lokale Accounts folgen.** Es reagiert wirklich
ausschließlich auf Accounts, die mehrfach als Spam gemeldet wurden und keine anderen Interaktionen mit unserer Instanz
haben. Alles, was komplizierter ist als „ein Account, den wir noch nie gesehen haben, nervt Leute“, ist weiterhin
Handarbeit.

## Warum automatisierte Moderation?

Im Schnitt gucken wir ein- bis zweimal täglich in unsere Moderations-Inbox. In der Zeit dazwischen können natürlich
richtig nervige Mengen von Spam aufkommen – aber wir haben schlicht nicht die Zeit, 365 Tage im Jahr alle paar Stunden
nach neuen Reports zu sehen. Leute auf unserer Instanz sollen sich aber nicht durch unendlich "BITCOIN MOONSHOT 🚀🚀🚀"
und "heiße Singles in deiner Nähe" kämpfen müssen, weil wir gerade schlafen oder (Schock, Horror) ein Leben abseits des
Internets haben.

Die Moderationsarbeit, die wir auf chaos.social leisten, ist für uns ein zentraler Teil der Instanz, und wir sehen darin
eine große Verantwortung. Automatisierte Moderation ist für uns deshalb wirklich nur für stupide Spamerkennung eine
Option – aber da ist sie, unserer Meinung nach, eine feine Sache.

Abgesehen von unseren oben beschriebenen Sicherheitsregeln, die das Skript nur gegen uns gänzlich unbekannten Accounts
handeln lassen, prüfen wir natürlich auch regelmäßig die Entscheidungen des Skripts. Mittlerweile läuft das Skript seit
Monaten, und verhält sich dabei sehr pflegeleicht. Spam ist halt deprimierend vorhersehbar. Seufz.

## Helft mit

Wenn ihr Spam abbekommt, meldet ihn bitte. **Gebt beim Melden als Grund "Spam" an.** Wählt möglichst **mehrere
Spam-Posts** aus, damit wir so schnell wie möglich genug Belege haben, dass der Account ein Spam-Account ist.

Wir haben uns bemüht, das Skript so sicher wie möglich zu machen, und weil wir so transparent wie möglich arbeiten
möchten, schreiben wir hier darüber. Es versteht sich zwar von selbst, aber: Bitte missbraucht dieses Vertrauen nicht.
Helft uns, chaos.social weiter zu einem entspannten (und spamfreien) online-Wohnzimmer zu machen.

## tl;dr

Wir entfernen Spam-Accounts automatisiert, mit vielen Sicherheitsvorkehrungen. Helft uns, indem ihr Spam meldet, und
dabei die Kategorie "Spam" wählt und möglichst mehrere Posts anhängt. Dann kann das Skript sich um den offensichtlichen
Spam kümmern, wenn wir grad nicht am Rechner sind.
