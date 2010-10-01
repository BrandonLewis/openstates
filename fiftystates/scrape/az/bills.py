import datetime
import re

import lxml.etree

from fiftystates.scrape.bills import BillScraper, Bill

class AZBillScraper(BillScraper):

    state = 'az'

    def get_session_id(self, session):
        return self.metadata['session_details'][session]['session_id']

    def scrape_bill(self, chamber, session, bill_id):
        bill_url = 'http://azleg.gov/xml/billinfo.asp?Session=%s&Bill=%s' % (
            self.get_session_id(session), bill_id)

        with self.urlopen(bill_url) as data:
            pass


    def scrape(self, chamber, session):
        session_id = self.get_session_id(session)
        chamber_letter = {'lower': 'H', 'upper': 'S'}[chamber]

        url = 'http://azleg.gov/xml/bills.asp?session=' + session_id

        with self.urlopen(url) as data:
            doc = lxml.etree.fromstring(data)
            for bill in doc.xpath('//bill'):
                number, old_title, cur_title = bill.xpath('*/text()')
                if number[0] == chamber_letter:
                    self.scrape_bill(chamber, session, number)

