class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        res = set()
        for email in emails:
            local_name, domain_name = email.split("@")
            local_name = local_name.split("+")[0].replace(".", "")
            res_emails = f"{local_name}@{domain_name}"
            res.add(res_emails)
        return len(res)
