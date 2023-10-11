#!/bin/bash
set -e

bundle exec jekyll build
rsync -avz --info=progress2 -h _site/ root@blog.chaos.social:/var/www/blog/
