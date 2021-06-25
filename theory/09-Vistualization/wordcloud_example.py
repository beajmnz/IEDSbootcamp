#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 17:00:50 2021

@author: Bea Jimenez <bea.jimenez@alumni.ie.edu>
"""

from wordcloud import WordCloud

# Create list of words
text = 'Smart (stylized as smart) is a German automotive brand and division of \
   Daimler AG. The marque is based in Böblingen, Germany. It produces microcars \
   and subcompacts, primarily the Fortwo and Forfour. The primary assembly plant \
   is the Smartville in Hambach, France. Renault-owned Revoz, based in Novo \
   Mesto, Slovenia, has also assembled Smart vehicles. Smart is marketed in \
   46 countries around the world, and production of the Fortwo had surpassed \
   1.7 million units by early 2015.The name Smart derives from the cooperation \
   of the Swiss company Swatch with Mercedes-Benz: "Swatch Mercedes ART". In \
   its branding, the company lowercases its logotype and the logo incorporating \
   a "c" and an arrow for the car\'s "cute" "compact" and "forward \
   thinking" styling respectively. The design concept for the marque\'s \
   automobiles began at Mercedes-Benz in the early-1970s to late-1980s. After \
   brief backing by Volkswagen, the first model was released by Daimler-Benz \
   in October 1998. Several variants on the original design have been \
   introduced, with the original being the "Fortwo". In March 2019, Geely \
   and Daimler AG announced the creation of an equally owned global joint \
   venture called the Smart Automobile Co., Ltd., aimed at producing \
   Smart-badged cars in China to be marketed globally.'


wordcloud = WordCloud().generate(text)
wordcloud.to_file("wikipedia_wordcloud.jpg")
