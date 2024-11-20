from crewai import Agent 
from Components.llms import *

llm = GPTLlm

class Agents:
    def __init__(self):
        pass
    def tren_searcher(self):
        return Agent(
            role="Pencari Tren",
            goal="Mencari tren terkini dari suatu topik untuk bahan menulis blog",
            backstory="Kamu adalah seorang pencari Tren yang meriset kondisi terkini di berbagai sumber secara online ",
            allow_delegation=False,
            verbose=True
            llm=llm,
        )
    def penulis(self):
        return Agent (
            role="Penulis Blog",
            goal="Menulis blog terkait dari topik yang menarik dan seru untuk dibaca",
            backstory="Kamu adalah seorang penulis handal diberbgai agensi selama bertahun-tahun ",
            allow_delegation=False,
            verbose=True
            llm=llm,
        )