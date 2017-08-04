def domain_name(url):
    domain = url.split(".")
    if "www" in domain[0]:
        domain.pop(0)
    if "http" in domain[0]:
        domain = domain[0].split('//')
        domain.pop(0)
    return domain[0]