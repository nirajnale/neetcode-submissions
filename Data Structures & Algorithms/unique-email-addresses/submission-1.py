class Solution:
    def numUniqueEmails(self, emails):

        unique = set()

        for email in emails:

            local, domain = email.split('@')

            # ignore everything after +
            local = local.split('+')[0]

            # remove dots
            local = local.replace('.', '')

            normalized = local + '@' + domain

            unique.add(normalized)

        return len(unique)