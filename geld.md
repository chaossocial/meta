---
layout: post
language: de
translation: money
---

# Geld

Der Betrieb von chaos.social ist ausschließlich spendenfinanziert. Die Spenden gehen an den [chaos.social
e.V.](/verein). Wir sind derzeit für ungefähr
**{{ site.data.money.cbrTotals.prrTotal[0].aquantity.floatingPoint | divided_by:site.data.money.cbrSubreports[-1][1].prRows[1].prrAmounts[-1][0].aquantity.floatingPoint | divided_by:12 | round:1 }}
Jahre** vorfinanziert (einen ausführlichen Bericht findet ihr
weiter unten). Danke euch allen!

## Wie spenden?

Es gibt verschiedene Möglichkeiten, uns Geld zukommen zu lassen:

1. Ab liebsten sind uns **Überweisungen** – und noch lieber natürlich **Daueraufträge**. Halbwegs vorhersehbares
   Einkommen lässt uns nachts ruhig schlafen.<br>**Kontoinhaberin:** chaos.social e.V.<br>**IBAN:**
   DE64830654080005279186<br>**BIC:** GENODEF1SLR<br><small>Wenn wir uns wirklich alles wünschen dürften: Da wir jeden
   Monat ab der 50. Buchung Geld zahlen, sind besonders Daueraufträge mit einem größeren Turnus (Quartal+) gerne
   gesehen.</small>
2. Auch in Ordnung ist [PayPal](//paypal.me/chaossocial). Da gehen zwar Gebühren ab, aber dafür ist es für euch
   schneller geklickt.
3. Im allergrößten Notfall geht auch [liberapay](//liberapay.com/chaos.social) – aber uns ist wirklich alles andere
   lieber.<br><small>Liberapay gibt den Anschein eines regelmäßigen, wöchentlichen Einkommens, obwohl das Geld auf einmal
   abgebucht wird – sodass für uns überhaupt nicht überschaubar ist, wie viel Geld wir warum bekommen. Die Auszahlung
   läuft auch über Stripe, sodass da noch mal ordentliche Zahlungsgebühren fällig werden. Alles besser als nichts, aber
   eben nicht sehr gut.</small>

## Finanzbericht

Das wichtige zuerst: Alles ist gut. Die Finanzen sind stabil. Wir sind derzeit für etwa
**{{ site.data.money.cbrTotals.prrTotal[0].aquantity.floatingPoint | divided_by:site.data.money.cbrSubreports[-1][1].prRows[1].prrAmounts[-1][0].aquantity.floatingPoint | divided_by:12 | round:1 }}
Jahre** vorfinanziert. 
Auf unserem Konto liegen **€&nbsp;{{ site.data.money.cbrTotals.prrTotal[0].aquantity.floatingPoint | monetary }}**.
Letzten Monat betrugen unsere Serverkosten
**€&nbsp;{{ site.data.money.cbrSubreports[-1][1].prRows[1].prrAmounts[-1][0].aquantity.floatingPoint | monetary }}**,
und wir hatten ein Spendenaufkommen von
**€&nbsp;{{ site.data.money.cbrSubreports[0][1].prRows[0].prrAmounts[-1][0].aquantity.floatingPoint | monetary }}**.

### Jahresübersicht

{% include money.html data=site.data.money_per_year date_width=4 %}

<small>*(Tabelle betriebsbedingt auf Englisch.)*</small>

### Einzelne Monate

{% include money.html data=site.data.money date_width=7 %}

<small>*(Tabelle betriebsbedingt auf Englisch.)*</small>

## FAQ

**Was war vor Dezember 2022?** – Vor unserer [Vereinsgründung](/verein) haben wir privat Spenden angenommen. Daher auch
die beiden dicken ersten Monate: Im Januar haben wir die vorher gesammelten Spenden aufs Vereinskonto übertragen, und im
Dezember haben wir die Vereinsgründung und Kontoverbindung veröffentlicht.

**Diese Domainkosten sehen komisch aus …** – Die Tabelle oben wird automatisch aus unserem Kontoauszug gebaut, und wir
haben glatte hundert Euro an unseren Registrar überwiesen. Klar ist das mehr, als die Domain kostet, und reicht noch ein
weiteres Jahr. Das übrige Geld ist natürlich technisch gesehen immer noch unseres, aber es ist eben nicht auf unserem
Konto, und da diese Seite der Transparenz und nicht der Steuererklärung dient, lassen wirs jetzt einfach so.
