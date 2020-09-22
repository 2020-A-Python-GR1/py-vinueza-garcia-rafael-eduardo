import scrapy 
import pandas as pd
import numpy as np
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class AraniaCrawlRanking2012(scrapy.Spider):
    name = 'ranking_universidades_2012'

    urls = [
        'https://cwur.org/2012.php'
    ]

    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url=url)

    def parse(self, response):

        titulos = response.css('table.table > thead > tr > th::text').extract()
        universidad_pais = response.css('table.table > tbody > tr > td > a::text').extract()
        datos = response.css('table.table > tbody > tr > td::text').extract()

        World_Rank = np.array([])
        Institution = np.array([])
        Location = np.array([])
        National_Rank = np.array([])
        Quality_of_Education = np.array([])
        Alumni_Employment = np.array([])
        Quality_of_Faculty = np.array([])
        Publications = np.array([])
        Influence = np.array([])
        Citations = np.array([])
        Patents = np.array([])
        Score = np.array([])
        
        i = 0
        while i < (len(datos) - 11):
            World_Rank = np.append(World_Rank, datos[i])
            Institution = np.append(Institution, datos[i + 1])
            Location = np.append(Location, datos[i + 2])
            National_Rank = np.append(National_Rank, datos[i + 3])
            Quality_of_Education = np.append(Quality_of_Education, datos[i + 4])
            Alumni_Employment = np.append(Alumni_Employment, datos[i + 5])
            Quality_of_Faculty = np.append(Quality_of_Faculty, datos[i + 6])
            Publications = np.append(Publications, datos[i + 7])
            Influence = np.append(Influence, datos[i + 8])
            Citations = np.append(Citations, datos[i + 9])
            Patents = np.append(Patents, datos[i + 10])
            Score = np.append(Score, datos[i + 11])
            i = i + 12

        datos = {
            'World_Rank': World_Rank,
            'Institution': Institution,
            'Location': Location,
            'National_Rank': National_Rank,
            'Quality_of_Education': Quality_of_Education,
            'Alumni_Employment': Alumni_Employment,
            'Quality_of_Faculty': Quality_of_Faculty,
            'Publications': Publications,
            'Influence': Influence,
            'Citations': Citations,
            'Patents': Patents,
            'Score': Score
        }

        data_frame = pd.DataFrame(datos, columns = ['World_Rank', 'Institution', 'Location', 'National_Rank', 'Quality_of_Education', 'Alumni_Employment','Quality_of_Faculty','Publications','Influence','Citations','Patents','Score'])
        data_frame = data_frame.replace({" - ": '0', " > 1000": '1001', '> 1000': '1001', ' >  1000':'1001', '101+': '102'})
        data_frame.to_csv('data_scrapy_2012.csv')
