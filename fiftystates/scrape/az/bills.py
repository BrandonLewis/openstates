import datetime
import re

import lxml.html

from fiftystates.scrape.bills import BillScraper, Bill

class AZBillScraper(BillScraper):

    state = 'az'

    def scrape(self, chamber, session):
        chamber = {'lower': 'allhouse', 'upper': 'allsenate'}[chamber]
        session_id = self.metadata['session_details'][session]['session_id']

        url = 'http://www.azleg.gov/Bills.asp?format=print&view=%s&Session_ID=%s'
        url = url % (chamber, session_id)

        print url

        with self.urlopen(url) as data:
            pass

