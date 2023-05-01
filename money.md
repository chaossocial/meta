---
layout: post
language: en
translation: geld
---

# Money

chaos.social runs entirely on donations to [chaos.social e.V.](/governance). We are currently financed for roughly **two
years** in advance – scroll down for detailled reporting. Thank you, everybody, for making chaos.social possible.

## How to donate

There are three ways of sending us money. In order of preference:

1. **Bank transfers** are hands-down the best way to send us money. Even better: do it as a standing order – having a
   somewhat regular income is what lets us sleep at night.<br>**Account holder:** chaos.social e.V.<br>**IBAN:**
   DE64830654080005279186<br>**BIC:** GENODEF1SLR<br><small>In a perfect world, we'd ask for standing orders with
   quarterly or lower frequencies, since anything past the 50th transaction every month starts costing us
   money.</small>
2. [PayPal](//paypal.me/chaossocial) also works. PayPal does take a cut, but that's fine, and it's more accessible from
   outside the EU.
3. If you absolutely have to, you can also use [liberapay](//liberapay.com/chaos.social) – but we'd prefer the other
   ways.<br><small>It's very hard for us to budget in any meaningful way with the way Liberapay handles donations, plus
   they are then sent via Stripe, which also takes a generous cut. Still better than nothing, but … not great.</small>

## Reporting

The important bit first: We're good. We're stable. We're currently financed for roughly
**{{ site.data.money.cbrTotals.prrTotal[0].aquantity.floatingPoint | divided_by:site.data.money.cbrSubreports[-1][1].prRows[1].prrAmounts[-1][0].aquantity.floatingPoint | divided_by:12 | round:1 }}
years** in advance.
We have **€&nbsp;{{ site.data.money.cbrTotals.prrTotal[0].aquantity.floatingPoint | monetary }}** in our bank account.
Last month, our server costs were
**€&nbsp;{{ site.data.money.cbrSubreports[-1][1].prRows[1].prrAmounts[-1][0].aquantity.floatingPoint | monetary }}**,
while we had an income of
**€&nbsp;{{ site.data.money.cbrSubreports[0][1].prRows[0].prrAmounts[-1][0].aquantity.floatingPoint | monetary }}**
in donations.

{% include money.html %}

## FAQ

**What happened before December 2022?** – We accepted donations in private before switching to a better fitting
[governance](/governance) model. Hence also the big income bump in January 2023: we transferred the balance of all the
donations before 2023 to our official account. (Whereas the big income bump in December 2022 is purely from us
announcing our new governance model and bank account.)

**What's with the domain cost?** The table above is built automatically from our bank statements. We put EUR 100 flat
into our account at our domain registrar's – that's more than the domain costs, and will be good for another year. While
the leftover money is still technically *ours*, it's not in our bank account, and since this page doesn't have to be up
to tax office standards, we decided to leave it like this.
