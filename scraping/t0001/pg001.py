from re import compile, Pattern

ls = [
    "<a>This is a test button.</a>",
    "<a><span>This is a test button in a span tag.</span></a>",
    '<a><span>This is a <m>"test button"</m> in a span tag.</span></a>',
]
abp = compile(r"<.*?>")


def remtags(s: str, p: Pattern) -> str:
    r = p.search(s)
    if not r:
        return s
    else:
        return remtags(s[: r.start()] + s[r.end() :], p)


def remtags_in_list(l: list[str], p: Pattern) -> list:
    r = []
    for i in l:
        r.append(remtags(i, p))
    return r


print(remtags_in_list(ls, abp))

a = ls[-1]
p = abp
