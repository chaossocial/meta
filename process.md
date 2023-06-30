---
layout: post
language: en
translation: prozess
---

# Reports and moderation

There's a lot of behind-the-scenes work involved in handling reports and moderation. This page is meant to inform our
users on what to expect from the process, and how to make our work easier.

## To report or not to report

Reports are meant to prompt us moderators to take action on something that is going wrong – so if you've come across
something on the Fediverse that is upsetting, there's a good chance that a report is the right next step. Reports are in
particular always encouraged for anything that **harms our users**, **violates our instance rules**, or if you need our
help in a specific situation.

Content moderation in a federated system is tricky: our instance rules apply first and foremost to you, **our users**,
and to a lesser degree to **people interacting with our users**. As the Fediverse is vast and our moderation
capacity limited, in most cases we will not take moderation actions when the reported case does not impact our users in
any way – keep in mind that we have limited moderation choices when dealing with users on other instances (see below).
However, you also have the option to report users on other instances to *their* server moderators.

If you're just annoyed by somebody, but they aren't being abusive or breaking our rules: block them or mute them and
move on.

However, if you're not sure if you're just annoyed or if there's a bigger problem: **Err on the side of reporting**. We
can always decide to close a report without further action, but we can't decide to act on something we don't know about.

## How to report

If there is only one thing we can convey on this page, then it's this: Please **be specific and provide context** in
your reports. To do so:

- Use the reporting interface rather than DMs to our admin account,
- include the offending post(s) you're reporting, and
- write a few words, even if you think the context is blindingly obvious.

We receive plenty of empty reports that contain no message and no posts. Our workload is such that we cannot investigate
reports like that – we'd have to open that account, and hunt around for potentially problematic posts in the past weeks,
while hoping that the problem did not occur in replies, DMs or other less visible contexts. We just don't have the
  time to do that – so if you want us to act, give us something to act on.

And also, *please* provide some sort of context. "This dude jumped into my replies" may be obvious to you in the moment,
but we'd have to open the original post and hunt around (sometimes in the database) to see if there was e.g. a deleted
original post. Often discussions refer to corners of the Internet (or the world) we know little about, so without
context, we get to start a small research project to find out if an obscure podcast is a nazi front. Share your context
with us, and we can act much faster and more decisively.

Please make only one report per problem/account.

**Special case:** If you'd like us [to block an entire instance](/federation), please report the admin account and/or
examples of particularly bad posts and users, even if that takes multiple reports.

## Our moderation process

When we receive a new report, we typically act on it within a few hours, and in the vast majority of cases within a day.
Please note that in most cases you **won't receive a reply**. Mastodon's moderation interface does not have an option to
notify users that their reports have been resolved, and DMing everybody about their reports turned out to be too much
work many years ago.

### Step 1: Validity

Our first step in receiving a report is to check if it can be discarded immediately. Reasons for this may be:

- The report is empty (without text or included posts), see above.
- The report text is clearly addressed to the other instance's moderation team.
- The reported post(s) don't break our instance rules. Examples:
   - New users frequently report properly tagged nudity, which we do not have any rules against.
   - Some reports are more of a therapeutic vent about a heated discussion.

### Step 2: Remote users

When it's clear that the report is actionable, the next check is to see if the reported user is on chaos.social or on a
different instance. As mentioned above, our rules apply first to our users, and we have limited tools in dealing with
users on other instances. 

We can **limit** users on other instances, which is effectively a shadow ban. They can still interact with users on
chaos.social, but the interactions will only be visible to users who follow them. We are **extremely reluctant** to
limit users, as the action is very opaque and leads to tons of frustration down the road. It also leads to awkward
situations where the reported user can continue to make, for example, inappropriate comments on our users' posts, and
they will just not be able to see them. We mostly limit users when they seem to spam hashtags.

However, the only other real action we can take against users on other instances is to **block** them. An instance-wide
block is a rough decision to make, as it prevents everybody on our instance from ever interacting with that user, and
that user from ever seeing anything on chaos.social again (via that account, of course). We block users on other
instances primarily as a way of **preventing harm** from our users – so users on other instances with opinions we would
not host on chaos.social may still not be blocked as long as they keep to themselves, but will end up blocked when they
start harassing our users. (So reports are still helpful, even if we don't act on them immediately, because they make
future block decisions easier).

If we decide not to block a user on a different instance, we may still reach out to their moderators to get a sense of
their moderation decisions. We may also advise the reporting user to block that user or instance.

### Step 3: Local users

Handling reports against users on chaos.social is both easier and harder: It's easier because we can just check and
apply our instance rules. It's harder because it hits close to home and we feel responsible for and to our users.

Notably, for most rule violations, we start by **talking to the user** in question, reminding them of the rules, and
asking them to confirm that they understand what is going on. In most cases this is enough and ends with an apology or
an edited post. In some other cases this leads the reported user to figure out that they are not actually in agreement
with our rules, and amicably move their account to a different instance. This kind of interaction makes up the bulk of
our moderation on local users.

For more serious or repeat infractions we will send a **formal warning**. Sadly, Mastodon only sends warnings via email,
rather than also showing them in the interface, so this means we have to monitor our bounces and hope the email doesn't
land in their spam folder. This also makes it a bad tool for slowing down users who are getting too heated in a
discussion, as they'll probably not see the warning until later. Depending on the severity, we will keep the report open
and ask the user to confirm that they got our warning. Warnings are one of the many ways that Mastodon's content
moderation is half-baked and not very useful, sadly.

Finally, in severe cases, we'll move to **freeze the account**. Frozen accounts cannot post anymore, but users can still
retrieve archives, move to different instances and so on. Freezing can be both the precursor to a serious discussion and
a final chance, or just a time for the user to move their account off of chaos.social within a set amount of days. The
only accounts we delete outright are openly malicious users (which due to the closed nature of our instance basically
never happens), everybody else gets at least a chance to export their data and move away in peace. Sadly, Mastodon does
not **show users as frozen**, so to the outside world, it looks like we're doing nothing, which sucks.

### Step 4: Public comments

We have a simple rule: **We do not publicly comment on moderation decisions concerning individual users** (rather than
entire instances).

We have this rule because any alternative would be worse – commenting on only some cases would introduce case-by-case
decisions that we'd be guaranteed to get wrong much of the time. It would also be often tempting to comment e.g. on
frozen accounts, or the currently hotly discussed user, and we do not think that any good can come off that.

However, if you have questions about our moderation decisions, please [contact us](/contact) via DM or email, and we'll
be willing to talk things through, explain our reasons, and listen to your concerns. This offer is open to both our
users and other instance's moderators.

## A final request

Content moderation is infinitely, recursively tricky, especially when doing it for a community, and doubly so when
trying to find good (rather than easy) solutions to problems. It's a lot of work, often in very stressful and
high-pressure situations. We're trying to get this right, and we think we're generally doing a good job, but:

Please be patient with us. We will make mistakes. **Talk to us** when you're unhappy, or when you have questions.

And thank you for your trust.
