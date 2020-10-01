import scrapy 
import pandas as pd
import numpy as np
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class AraniaCrawlRanking2018(scrapy.Spider):
    name = 'ranking_universidades_2018'

    urls = [
        'https://cwur.org/2018-19.php'
    ]

    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url=url)

    def parse(self, response):

        titulos = response.css('table.table > thead > tr > th::text').extract()
        universidad_pais = response.css('table.table > tbody > tr > td > a::text').extract()
        datos_numericos = response.css('table.table > tbody > tr > td::text').extract()

        World_Rank = np.array([])
        Institution = np.array([])
        Location = np.array([])
        National_Rank = np.array([])
        Quality_of_Education = np.array([])
        Alumni_Employment = np.array([])
        Quality_of_Faculty = np.array([])
        Research_Output = np.array([])
        Quality_Publications = np.array([])
        Influence = np.array([])
        Citations = np.array([])
        Score = np.array([])

        i = 0
        while i < (len(universidad_pais) - 1):
            Institution = np.append(Institution, universidad_pais[i])
            Location = np.append(Location, universidad_pais[i + 1])
            i = i + 2
        
        i = 0
        while i < (len(datos_numericos) - 9):
            World_Rank = np.append(World_Rank, datos_numericos[i])
            National_Rank = np.append(National_Rank, datos_numericos[i + 1])
            Quality_of_Education = np.append(Quality_of_Education, datos_numericos[i + 2])
            Alumni_Employment = np.append(Alumni_Employment, datos_numericos[i + 3])
            Quality_of_Faculty = np.append(Quality_of_Faculty, datos_numericos[i + 4])
            Research_Output = np.append(Research_Output, datos_numericos[i + 5])
            Quality_Publications = np.append(Quality_Publications, datos_numericos[i + 6])
            Influence = np.append(Influence, datos_numericos[i + 7])
            Citations = np.append(Citations, datos_numericos[i + 8])
            Score = np.append(Score, datos_numericos[i + 9])
            i = i + 10

        datos = {
            'World_Rank': World_Rank,
            'Institution': Institution,
            'Location': Location,
            'National_Rank': National_Rank,
            'Quality_of_Education': Quality_of_Education,
            'Alumni_Employment': Alumni_Employment,
            'Quality_of_Faculty': Quality_of_Faculty,
            'Research_Output': Research_Output,
            'Quality_Publications': Quality_Publications,
            'Influence': Influence,
            'Citations': Citations,
            'Score': Score
        }

        data_frame = pd.DataFrame(datos, columns = ['World_Rank', 'Institution', 'Location', 'National_Rank', 'Quality_of_Education', 'Alumni_Employment','Quality_of_Faculty','Research_Output','Quality_Publications','Influence','Citations','Score'])
        data_frame = data_frame.replace({" - ": '0', " > 1000": '1001', '> 1000': '1001', ' >  1000':'1001', '101+': '102'})
        data_frame.to_csv('data_scrapy_2018.csv')

