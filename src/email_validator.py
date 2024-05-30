def is_valid_email(email):
    if '@' not in email:
        return False
    local, domain = email.split('@')
    if invalid_local_part(local) or invalid_domain_part(domain):
        return False

    return True


def invalid_local_part(local):
    return not local


def invalid_domain_part(domain):
    return '.' not in domain or domain.startswith('.')
