# pelican-alchemy

A clean, functional theme for [Pelican](http://getpelican.com). Inspired by [crowsfoot](http://github.com/porterjamesj/crowsfoot), and powered by [clean-blog](https://github.com/BlackrockDigital/startbootstrap-clean-blog) (Bootstrap).

Live demo: [nairobilug.or.ke](http://nairobilug.or.ke)

![Screenshot](/screenshot.png "Screenshot")

---

## Installation

    $ git clone git@github.com:nairobilug/pelican-alchemy.git

Then set the pelican config variable `THEME` to the `alchemy` folder inside the cloned path.

### Theme Options

| Config                    | Type       | Description               |
| ------------------------- | ---------- | ------------------------- |
| SITE_TAGLINE              | TEXT       | Site tagline/slogan       |
| SITE_DESCRIPTION          | TEXT       | HEAD meta description     |
| SITE_IMAGE                | URL        | Site (profile) image      |
| SHOW_ARTICLE_AUTHOR       | BOOL       | Show article authors      |
| SHOW_FAVICONS             | BOOL       | Show favicons [^1]        |
| SHOW_FOOTER_ARCHIVES      | BOOL       | Show `Archives` link      |
| SHOW_FOOTER_AUTHORS       | BOOL       | Show `Authors` link       |
| SHOW_FOOTER_CATEGORIES    | BOOL       | Show `Categories` link    |
| SHOW_FOOTER_TAGS          | BOOL       | Show `Tags` link          |
| SHOW_HEADER_PAGES         | BOOL       | Show 'Pages' links        |
| HEADER_LINKS              | LIST       | `('title', 'url')` list   |
| GITHUB_ADDRESS            | URL        | Github link icon          |
| TWITTER_ADDRESS           | URL        | Twitter link icon         |
| GOOGLE_ADDRESS            | URL        | Google+ link icon         |
| EMAIL_ADDRESS             | EMAIL      | Email link (`mailto:`)    |
| FACEBOOK_ADDRESS          | URL        | Facebook link icon        |
| DISQUS_SITENAME           | TEXT       | Disqus comments           |

An RSS icon will also appear on the nav if `FEED_ALL_ATOM` is set.

## License

MIT License

[^1]: http://realfavicongenerator.net "realfavicongenerator.net"
