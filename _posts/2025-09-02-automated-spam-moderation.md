---
layout: post
title:  "Automated spam moderation"
date:   2025-09-02 08:00:00
language: en
translation: automatisierte-spam-moderation
---

Mastodon’s moderation tooling is, after using it for a couple of years, … hard to describe in polite language. Normally,
this is just annoying, but when a big spam wave hits, it becomes an active hindrance to running a good instance.

So … we wrote [a script](https://github.com/chaossocial/meta/blob/master/bin/auto-moderator).

## What it does

The logic is straightforward: if a set number of people (with local reporters being given more weight than remote users)
report the same account for spam, and that account matches certain patterns, our script suspends them automatically.

Patterns include hard-coded spam phrases we’ve collected over months of manual cleanup (think „BTCTurboMiner Made Me
$500 in 3 Hours“, and the recent Mastodon admin verification scams), plus heuristics like posting identical content
repeatedly. The script is smart enough to strip @mentions when comparing posts, since spammers often blast the same
message at different people.

Different rule sets apply based on report patterns - we need fewer duplicate posts if there are more local reporters,
more evidence if it’s only remote reports, etc. The thresholds have been tuned based on months of spam wave patterns,
but we can also temporarily adjust them to respond to new spam waves.

For convenience, the script also auto-suspends accounts that are already suspended on their home instance (mostly to
clean up lingering notifications that do not get auto-removed).

**The script never touches local users or anyone followed by our users.** It only acts on external accounts that
multiple people have reported as spam and that have no other interactions with our instance. For anything more
complicated than “account we’ve never seen before bothers people”, we do the work ourselves, and always will.


## Why automated moderation


We usually check the moderation once or twice daily. In the time between, spam waves can dump hundreds of garbage posts
into federated timelines. Users shouldn’t have to wade through "BITCOIN MOONSHOT 🚀🚀🚀" and "hot singles in your area"
because we’re asleep or busy.

We take pride in running chaos.social well and handling all moderation tasks responsibly, which may sound like its in
conflict with automated moderation. But we believe that with the limits set on the script, having some automated
spam handling is a net positive.

In addition to the safety measures of never taking actions on local or local-followed accounts, we also check its
decisions regularly. At this point, the script’s been running for months without false positives. Turns out spam is
depressingly predictable. Sigh.

## How to help

If you get hit by spam, please report it. In the report form, **use the actual "spam" reason in the dropdown.** Include
multiple spammy posts from the same account if possible, so that fewer total reports will be needed in order to hit our
detection limits.

We’ve tried to make this script as safe as possible, and we’re writing about it here because we want to be as
transparent as possible about our work on chaos.social. It goes without saying, but: Please don’t abuse this trust. Help
us make chaos.social an even better place to hang out on <3

## tl;dr

Automated spam removal is active, with lots of safeguards. Report spam properly (use the spam option) and attach
multiple examples to help the robots handle obvious spam while we sleep.
