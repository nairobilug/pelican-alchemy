# pelican-alchemy

A clean, functional, and lean theme for the [Pelican](http://getpelican.com) static site generator. Inspired by [crowsfoot](http://github.com/porterjamesj/crowsfoot), powered by [clean-blog](https://github.com/BlackrockDigital/startbootstrap-clean-blog).

![Screenshot](/screenshot.png "Screenshot")

---

## Installation

    $ git clone git@github.com:nairobilug/pelican-alchemy.git

Then set the pelican config variable `THEME` to the `alchemy` folder inside the cloned path.

## Theme Options

| Config                    | Type       | Description               |
| ------------------------- | ---------- | ------------------------- |
| SITE_TAGLINE              | TEXT       | Site tagline/slogan       |
| SITE_DESCRIPTION          | TEXT       | <head> meta description   |
| SITE_IMAGE                | URL        | Site (profile) image      |
| SHOW_ARTICLE_AUTHOR       | BOOL       | Show article authors      |
| SHOW_FAVICONS             | BOOL       | Show site favicons [^1]   |
| SHOW_FOOTER_ARCHIVES      | BOOL       | Show `Archives` link      |
| SHOW_FOOTER_AUTHORS       | BOOL       | Show `Authors` link       |
| SHOW_FOOTER_CATEGORIES    | BOOL       | Show `Categories` link    |
| SHOW_FOOTER_TAGS          | BOOL       | Show `Tags` link          |
| SHOW_HEADER_PAGES         | BOOL       | Show Pages in header      |
| GITHUB_ADDRESS            | URL        | Github icon               |
| TWITTER_ADDRESS           | URL        | Twitter icon              |
| GOOGLE_ADDRESS            | URL        | Google+ icon              |
| EMAIL_ADDRESS             | EMAIL      | Email (`mailto:`)         |
| FACEBOOK_ADDRESS          | URL        | Facebook icon             |
| DISQUS_SITENAME           | TEXT       | Disqus comments           |

An RSS icon will also appear on the nav if `FEED_ALL_ATOM` is set.

## Structure

The theme follows the following structure:

    ├── static
    │   ├── css
    │   └── images
    └── templates
        ├── archives.html         // to display archives
        ├── period_archives.html  // to display time-period archives
        ├── article.html          // processed for each article
        ├── author.html           // processed for each author
        ├── authors.html          // must list all the authors
        ├── categories.html       // must list all the categories
        ├── category.html         // processed for each category
        ├── index.html            // the index (list all the articles)
        ├── page.html             // processed for each page
        ├── tag.html              // processed for each tag
        └── tags.html             // must list all the tags. Can be a tag cloud.

## Live Demo

[nairobilug.or.ke](http://nairobilug.or.ke)

## License

MIT License

[^1]: http://realfavicongenerator.net "realfavicongenerator.net"
