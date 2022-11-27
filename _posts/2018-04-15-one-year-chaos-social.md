---
layout: post
title:  "One year chaos.social!"
date:   2018-04-15 10:00:00
language: en
translation: ein-jahr-chaos-social
---

chaos.social celebrates its birthday today! We opened registration last year [on April 15th](https://chaos.social/@ordnung/1003) after sending our first toots on April 13th:  

<div class="toot two-toots">
<iframe src="https://chaos.social/@rami/1/embed" class="mastodon-embed" style="max-width: 100%; border: 0" width="400" height="170"></iframe><script src="https://chaos.social/embed.js" async="async"></script>
<iframe src="https://chaos.social/@rixx/2/embed" class="mastodon-embed" style="max-width: 100%; border: 0" width="400" height="170"></iframe><script src="https://chaos.social/embed.js" async="async"></script>
</div>

Since then, we've grown quite a bit. Since a few days ago, more than 2000 people call our instance their home, and we're connected to more than 2000 other instances in the Fediverse. Which has grown itself a lot, too! Mastodon doesn't only federate (nearly) seamlessly with the old and established federation parts like GNUSocial, but also with the newcomers like PeerTube. There's always something new going on and barely a month passes without new federtion parts and possibilites.

## And you are  …?

We started chaos.social as an instance for the Chaos community around CCC, and we're still committed to its principles of transparency for public data, protection of private data, and decentralisation.
* Transparency: We started early on to make everything of interest about our instance transparent: We have a [repository](https://github.com/chaossocial/about) with our public descriptions and rules to make changes transparent. We also publish any [changes and customisations](https://github.com/chaossocial/custom) we run. Special thanks go to [@rash](https://chaos.social/@rash) for the Fairydust elephant and [@blinry](https://chaos.social/@blinry) for our favicon!
* Protection: We have a set of rules to help with a good culture and constructive interactions on chaos.social. While we're willing to adapt and enforce these rules as necessary, we haven't had to do so a lot. During the last year, there were only 50 reports (not even one per week), and some of them concerned the same post or user. 68% of the reports concerned users from other instances.
* Decentralisation: We're happy not to have grown too much or too fast. While our hardware could cope with more users (see below for details), every new wave of users has to get used to Mastodon and our instance. For more information of decentralisation of the Fediverse as a whole, check out the results of [Leah looking into network layer distribution of Fediverse instances](https://chaos.social/@leah/99837391793032137)!

## Usage


![User development over the last year]({{ "/assets/images/users.png"}})
![Toots per hour over the last year]({{ "/assets/images/toots.png"}})

Initially, we had a large amount of sign ups. Curious people wanting to try out the hot new thing, and some also came due to rixx's [talk](https://media.ccc.de/v/gpn17-8575-mammut_statt_vogel) at GPN and his [interview](https://netzpolitik.org/2017/interview-die-anfangsphase-des-alternativen-sozialen-netzwerks-mastodon-ist-vorueber/) with netzpolitik.org.
There was a noticeable and visible period of little growth last summer. For a while it seemed like Mastodon would slowly wither and die like many other social networks before, leaving only a handful of users too stubborn to leave. Our instance was still a very nice place, but a bit slow and sleepy. Ever since fall and winter though, that time is over. Maybe due to the current Facebook debate (it's certainly helping) and various gaffes by Twitter, … we're growing, and our local timeline is very much alive.

## Infrastructure

A reliable instance needs reliable infrastructure to run on. In our case, this is a virtual server on Leah's infrastructure which is hosted at Hetzner. chaos.social has grown continuously since one year ago, and to provide a fast and smooth experience, the VM has grown with it. Currently it has 12GB RAM, 4 CPU cores and 120GB SSD storage. The storage is periodically on the verge of filling up, which is when we delete old media from remote instances to avoid adding more storage all the time. But don't worry, if you look at an old toot where we've deleted old media, it's just fetched again from the remote instance.

To be safe in case of emergencies or for when the administration goes wrong somehow, we have daily system backups. Of course, we also have monitoring for the availability of the server (and various other things), as well as the stats on growth and usage you saw above.

We'll see how the infrastructure requirements change in the future. Our single server setup is still working well at our size, but we're always looking for places to improve, so that you'll continue to have a great experience on chaos.social.

## Now what?

We're happy with chaos.social. We'll run into new (social and technical) challenges as our instance grows, but we'll continue to figure out solutions transparently and happy to try out new things.

If you can and want to help us financially (we pay for the server and the domain after all), have a look at our [liberapay account](https://liberapay.com/chaos.social/).

And if you're attending GPN this year, we might have a new presentation, but at the very least a user meetup.
