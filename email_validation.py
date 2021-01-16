def is_email(email):
    '''Function to determine if a given string is a valid email address'''

    if email.count('@') == 1:
        # Splits function into local address and domain
        # sample@gmail.com ==> local = 'sample', domain = '@gmail.com'
        local = email[0: email.index('@')]
        domain = email[email.index('@'):]

    else:
        return False

    # Ensures the email has a local address and domain
    if len(local) > 0 and len(domain) > 0:

        # A local address cannot begin with the following characters
        if local[0] != ['-', '_', '.', '0', '1', '2', '3', '4', '5', '6',
            '7', '8', '9']:

            # A local address cannot contain the following characters
            # Need for loop bc 'in' can only take a string
            for x in ['<', '>', '(' , ')', '[', ']', ';', ':', ',', '@', 
                R'\ ']:

                if x in local:
                    return False
        else:
            return False

        # The length of web address cannot be longer than 64 and must contain
        # and an extension beginning in a period (e.g. '.com')
        if len(domain) < 64 and domain.count('.') == 1:

            # stores the domain name without the extension
            domain_name = domain[1:domain.index('.')]

            # '-' is the only non-alphanumeric character that can be in a
            # domain and therefore, it is easiest just to remove it
            if '-' in domain_name:
                domain_name = domain_name.remove('-')
            else:
                pass
            
            # Determines if the domain is alphanumeric
            if domain_name.isalnum():
                return True
            else:
                return False
        else:
            return False
    else:
        return False