from django.template import loader
from django.core.mail import send_mail
from django.conf import settings

from auth.models import Account


class DisasterRepository(object):

    def __init__(self, disaster):
        self.disaster = disaster
        self.lat = disaster.get("lat")
        self.lang = disaster.get("lang")
        self.diameter = disaster.get("diameter")


    def get_nearest_accounts(self):

        near_accounts = Account.objects.mongo_find(
            {
                "center_point":
                { "$near":
                    {
                        "$geometry": { "type": "Point",  "coordinates": [ self.lang, self.lat ] },
                        "$maxDistance": self.diameter + 10000
                    }
                }
            }
        )

        accounts_instances = list()
        for account in near_accounts:
            accounts_instances.append(Account.objects.get(id = account.get("id")))
        
        return accounts_instances


    def send_nearest_email(self):

        near_accounts = self.get_nearest_accounts()

        for account in near_accounts:
            context = {
                'email': account.user.email,
                'user': account.user,
                'disaster'  :   self.disaster,
                "lat"   : self.disaster.get("lat"),
                "lang"   : self.disaster.get("lang"),
                "site_name" :   "https://akef-test-ibm.eu-gb.mybluemix.net"
                }
            subject_template_name = 'auth/subject.txt'
            organizations_email_template_name = 'auth/disaster_email_to_organizations.html'
            people_email_template_name = 'auth/disaster_email_to_people.html'

            subject = loader.render_to_string(subject_template_name, context)
            # Email subject *must not* contain newlines
            subject = ''.join(subject.splitlines())
            

            if account.type == 'o':
                email = loader.render_to_string(organizations_email_template_name, context)
            else:
                email = loader.render_to_string(people_email_template_name, context)

            send_mail(subject, email, settings.DEFAULT_FROM_EMAIL, [account.user.email], fail_silently=False)
