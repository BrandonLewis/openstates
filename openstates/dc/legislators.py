from billy.scrape.legislators import LegislatorScraper, Legislator
import lxml.html

def get_field(doc, key):
    # get text_content of parent of the element containing the key
    elem = doc.xpath('//div[@id="member-info"]/p/strong[text()="%s"]/..' % key)
    if elem:
        return elem[0].text_content().replace(key, '').strip()
    else:
        return ''


class DCLegislatorScraper(LegislatorScraper):
    state = 'dc'

    def scrape(self, term, chambers):
        council_url = 'http://www.dccouncil.washington.dc.us/council'
        data = self.urlopen(council_url)
        doc = lxml.html.fromstring(data)
        doc.make_links_absolute(council_url)
        # page should have 13 unique council URLs
        urls = set(doc.xpath('//a[contains(@href, "/council/")]/@href'))
        assert len(urls) <= 13, "should have 13 unique councilmember URLs"

        for url in urls:
            data = self.urlopen(url)
            doc = lxml.html.fromstring(data)
            doc.make_links_absolute(url)

            name = doc.xpath('//h2/text()')[0]
            if 'Chairman' in name:
                district = 'Chairman'
            else:
                district = get_field(doc, 'Represents: ')

            if not district:
                district = 'At-Large'

            # party
            party = get_field(doc, "Political Affiliation:")
            if 'Democratic' in party:
                party = 'Democratic'
            else:
                party = 'Independent'

            photo_url = doc.xpath('//div[@id="member-thumb"]/img/@src')
            if photo_url:
                photo_url = photo_url[0]
            else:
                photo_url = ''

            office_address = get_field(doc, "Office:")
            phone = get_field(doc, "Tel:")
            phone, fax = phone.split(' | Fax: ')

            email = doc.xpath('//a[starts-with(text(), "Send an email")]/@href')[0].split(':')[1]

            legislator = Legislator(term, 'upper', district, name,
                                    party=party, url=url, email=email,
                                    photo_url=photo_url)
            legislator.add_office('capitol', 'Council Office',
                                  address=office_address, phone=phone,
                                  fax=fax)
            legislator.add_source(url)
            self.save_legislator(legislator)
