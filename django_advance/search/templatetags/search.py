from django import template
register = template.Library()


@register.simple_tag
def url_replace(request, field, value):
    """GETパラメータを一部を置き換える"""

    # GETパラメーターをコピーする（辞書になっている）
    url_dict = request.GET.copy()

    # GETパラメーター辞書['page'] = 1
    url_dict[field] = str(value)

    return url_dict.urlencode()