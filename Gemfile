source "https://rubygems.org"

gem "jekyll", "~> 4.4.1"

# Ruby 3.4+ requires these standard library gems to be explicitly included
gem "erb"
gem "base64"
gem "csv"
gem "logger"

group :jekyll_plugins do
  gem "jekyll-feed", "~> 0.12"
end

# Manually downgrading sassc, as 2.2.0 has a really phenomenal bug that misplaces the libsass.so file
# into the incorrect bundler directory. The other option is to manually symlink the two, and ain't nobody
# got time for that.
# Tracking at https://github.com/sass/sassc-ruby/issues/146
gem "sassc", "< 2.2.0"
