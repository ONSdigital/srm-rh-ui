from flask import url_for, render_template, g


def url_for_i18n(endpoint: str, *args, **kwargs) -> str:
    return url_for(f'i18n.{endpoint}', *args, lang_code=g.lang_code, **kwargs)


def render_template_i18n(*args, **kwargs) -> str:
    return render_template(*args, lang_code=g.lang_code, **kwargs)
