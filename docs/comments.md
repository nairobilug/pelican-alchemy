# Adding comments to your blog

## Disqus

Alchemy supports Disqus comments by default. Specify `DISQUS_SITENAME`
in your `pelicanconf.py` to enable comments integration.


## Other comment engines

Other comment engines may be integrated into Alchemy by overriding default
template for `include/comments.html`:

- Check the documentation for your comment provider and save the required HTML
  snippet as `any_directory/include/comments.html`. Example snippets for some
  comment engines are listed below.
- Set [THEME_TEMPLATES_OVERRIDES] to contain correct path to templates
  directory:

```python
THEME_TEMPLATES_OVERRIDES = ['any_directory']  # paths are relative to location of pelicanconf.py
```

[THEME_TEMPLATES_OVERRIDES]: https://docs.getpelican.com/en/stable/settings.html?highlight=THEME_TEMPLATES_OVERRIDES#themes


## Integration snippets for different comment engines

#### [isso](https://github.com/posativ/isso)

```html
<div id="isso_thread">
  <script data-isso="{{ ISSO_URL }}/" src="{{ ISSO_URL }}/js/embed.min.js"></script>
  <section id="isso-thread"></section>
</div>
```

> ISSO_URL may be provided via pelicanconf.py or replaced by hardcoded value
> in the template
