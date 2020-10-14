from bs4 import *
import requests

class ScrapeTripadvisor:
    def __init__(self, site):
        self.request = requests.get(site).text
        self.summarized_reviews = []
        self.reviews = []
        self.soup = BeautifulSoup(self.request, 'html.parser')

    def scrape_hotel(self):
        """Scraping the latest reviews about a given hotel url"""
        for i in self.soup.find_all("div",
                                    class_="hotels-hotel-review-community-content-review-list-parts-ExpandableReview__containerStyles--3fFCE"):
            self.reviews.append(str(i)[
                                str(i).index('<q class="hotels-hotel-review-community-content-review-list-parts-ExpandableReview__reviewText--1OjOL"><span>') + len(
                                    '<q class="hotels-hotel-review-community-content-review-list-parts-ExpandableReview__reviewText--1OjOL"><span>'):str(i).index(
                                    '</span>')])

        for i in self.soup.find_all("a",
                                    class_="hotels-hotel-review-community-content-review-list-parts-ReviewTitle__reviewTitleText--2vGeO"):
            self.summarized_reviews.append(str(i)[str(i).index('><span><span>') + len('><span><span>'):str(i).index('</span></span></a>')])

        return self.summarized_reviews, self.reviews

    def scrape_restaurant(self):
        """Scraping the latest reviews about a given restaurant url"""
        for i in self.soup.find_all("span", class_="noQuotes"):
            self.summarized_reviews.append(str(i)[
                                           str(i).index('<span class="noQuotes">') + len('<span class="noQuotes">'):str(
                                               i).index('</span>')])

        for i in self.soup.find_all("p", class_="partial_entry"):
            if '<p class="partial_entry">Dear' not in str(i):
                i = str(i)[str(i).index('<p class="partial_entry">') + len('<p class="partial_entry">'):]
                i = i[:i.index('<')]
                self.reviews.append(i)

        return self.summarized_reviews, self.reviews

if __name__ == "__main__":
    print("[Scraping Restaurant Reviews] Please wait...")
    site = 'https://www.tripadvisor.com/Restaurant_Review-g562818-d2515772-Reviews-Gorbea_Restaurant-San_Agustin_Maspalomas_Gran_Canaria_Canary_Islands.html'
    sr = ScrapeTripadvisor(site)
    summarized_reviews, reviews = sr.scrape_restaurant()
    print(summarized_reviews)
    print(reviews)
    print()
    print("[Scraping Hotel Reviews] Please wait...")
    site = 'https://www.tripadvisor.com/Hotel_Review-g562819-d600110-Reviews-HD_Parque_Cristobal_Gran_Canaria-Playa_del_Ingles_Maspalomas_Gran_Canaria_Canary_Island.html'
    sh = ScrapeTripadvisor(site)
    summarized_reviews, reviews = sh.scrape_hotel()
    print(summarized_reviews)
    print(reviews)
