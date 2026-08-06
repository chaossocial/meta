set shell := ["bash", "-euo", "pipefail", "-c"]
set quiet
set fallback
set default-list

# Install dependencies
[group('development')]
install *args:
    bundle install {{ args }}

# Build the site into _site
[group('development')]
build *args:
    bundle exec jekyll build {{ args }}

# Run the development server
[group('development')]
serve *args:
    bundle exec jekyll serve {{ args }}
