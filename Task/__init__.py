from otree.api import *
import random
import itertools
import json


author = 'Christian König gen. Kersting'

doc = """
Demo of element hover tracking using oTree 2.6b0
"""


attributes_listA_small = [
    {
        "Investment Costs": "$30,000",
        "Savings compared to Gasoline Car": "$4.5 per 100 miles",
        "Battery Range": "120 miles",
        "Lifecycle Greenhouse Gas Emissions": "30kg emissions per 100 vehicle miles",
        "Adopters in the Neighborhood": "3% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$18,000",
        "Savings compared to Gasoline Car": "$5.3 per 100 miles + additional $6 savings on carbon tax",
        "Battery Range": "440 miles",
        "Lifecycle Greenhouse Gas Emissions": "30kg emissions per 100 vehicle miles",
        "Adopters in the Neighborhood": "3% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$6,000",
        "Savings compared to Gasoline Car": "$4.5 per 100 miles + additional $6 savings on carbon tax",
        "Battery Range": "280 miles",
        "Lifecycle Greenhouse Gas Emissions": "20kg emissions per 100 vehicle miles",
        "Adopters in the Neighborhood": "3% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$30,000",
        "Savings compared to Gasoline Car": "$6.2 per 100 miles + additional $1.5 savings on carbon tax",
        "Battery Range": "440 miles",
        "Lifecycle Greenhouse Gas Emissions": "20kg emissions per 100 vehicle miles",
        "Adopters in the Neighborhood": "3% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$6,000",
        "Savings compared to Gasoline Car": "$5.3 per 100 miles",
        "Battery Range": "120 miles",
        "Lifecycle Greenhouse Gas Emissions": "10kg emissions per 100 vehicle miles",
        "Adopters in the Neighborhood": "3% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$18,000",
        "Savings compared to Gasoline Car": "$6.2 per 100 miles",
        "Battery Range": "280 miles",
        "Lifecycle Greenhouse Gas Emissions": "10kg emissions per 100 vehicle miles",
        "Adopters in the Neighborhood": "3% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$30,000",
        "Savings compared to Gasoline Car": "$6.2 per 100 miles + additional $6 savings on carbon tax",
        "Battery Range": "280 miles",
        "Lifecycle Greenhouse Gas Emissions": "30kg emissions per 100 vehicle miles",
        "Adopters in the Neighborhood": "58% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$6,000",
        "Savings compared to Gasoline Car": "$4.5 per 100 miles + additional $1.5 savings on carbon tax",
        "Battery Range": "440 miles",
        "Lifecycle Greenhouse Gas Emissions": "30kg emissions per 100 vehicle miles",
        "Adopters in the Neighborhood": "58% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$6,000",
        "Savings compared to Gasoline Car": "$6.2 per 100 miles",
        "Battery Range": "120 miles",
        "Lifecycle Greenhouse Gas Emissions": "20kg emissions per 100 vehicle miles",
        "Adopters in the Neighborhood": "58% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$18,000",
        "Savings compared to Gasoline Car": "$5.3 per 100 miles + additional $1.5 savings on carbon tax",
        "Battery Range": "280 miles",
        "Lifecycle Greenhouse Gas Emissions": "20kg emissions per 100 vehicle miles",
        "Adopters in the Neighborhood": "58% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$18,000",
        "Savings compared to Gasoline Car": "$4.5 per 100 miles + additional $6 savings on carbon tax",
        "Battery Range": "120 miles",
        "Lifecycle Greenhouse Gas Emissions": "10kg emissions per 100 vehicle miles",
        "Adopters in the Neighborhood": "58% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$30,000",
        "Savings compared to Gasoline Car": "$5.3 per 100 miles",
        "Battery Range": "440 miles",
        "Lifecycle Greenhouse Gas Emissions": "10kg emissions per 100 vehicle miles",
        "Adopters in the Neighborhood": "58% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$18,000",
        "Savings compared to Gasoline Car": "$6.2 per 100 miles + additional $1.5 savings on carbon tax",
        "Battery Range": "120 miles",
        "Lifecycle Greenhouse Gas Emissions": "30kg emissions per 100 vehicle miles",
        "Adopters in the Neighborhood": "86% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$6,000",
        "Savings compared to Gasoline Car": "$5.3 per 100 miles",
        "Battery Range": "280 miles",
        "Lifecycle Greenhouse Gas Emissions": "30kg emissions per 100 vehicle miles",
        "Adopters in the Neighborhood": "86% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$30,000",
        "Savings compared to Gasoline Car": "$5.3 per 100 miles + additional $6 savings on carbon tax",
        "Battery Range": "120 miles",
        "Lifecycle Greenhouse Gas Emissions": "20kg emissions per 100 vehicle miles",
        "Adopters in the Neighborhood": "86% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$18,000",
        "Savings compared to Gasoline Car": "$4.5 per 100 miles",
        "Battery Range": "440 miles",
        "Lifecycle Greenhouse Gas Emissions": "20kg emissions per 100 vehicle miles",
        "Adopters in the Neighborhood": "86% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$30,000",
        "Savings compared to Gasoline Car": "$4.5 per 100 miles + additional $1.5 savings on carbon tax",
        "Battery Range": "280 miles",
        "Lifecycle Greenhouse Gas Emissions": "10kg emissions per 100 vehicle miles",
        "Adopters in the Neighborhood": "86% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$6,000",
        "Savings compared to Gasoline Car": "$6.2 per 100 miles + additional $6 savings on carbon tax",
        "Battery Range": "440 miles",
        "Lifecycle Greenhouse Gas Emissions": "10kg emissions per 100 vehicle miles",
        "Adopters in the Neighborhood": "86% of adopters in the neighborhood",
    },
]

attributes_listA_medium = [
    {
        "Investment Costs": "$32,000",
        "Savings compared to Gasoline Car": "$5.5 per 100 miles",
        "Battery Range": "120 miles",
        "Lifecycle Greenhouse Gas Emissions": "30kg emissions per 100 vehicle miles",
        "Adopters in the Neighborhood": "3% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$44,000",
        "Savings compared to Gasoline Car": "$6.4 per 100 miles + additional $6 savings on carbon tax",
        "Battery Range": "440 miles",
        "Lifecycle Greenhouse Gas Emissions": "30kg emissions per 100 vehicle miles",
        "Adopters in the Neighborhood": "3% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$56,000",
        "Savings compared to Gasoline Car": "$5.5 per 100 miles + additional $6 savings on carbon tax",
        "Battery Range": "280 miles",
        "Lifecycle Greenhouse Gas Emissions": "20kg emissions per 100 vehicle miles",
        "Adopters in the Neighborhood": "3% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$32,000",
        "Savings compared to Gasoline Car": "$7.7 per 100 miles + additional $1.5 savings on carbon tax",
        "Battery Range": "440 miles",
        "Lifecycle Greenhouse Gas Emissions": "20kg emissions per 100 vehicle miles",
        "Adopters in the Neighborhood": "3% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$56,000",
        "Savings compared to Gasoline Car": "$6.4 per 100 miles",
        "Battery Range": "120 miles",
        "Lifecycle Greenhouse Gas Emissions": "10kg emissions per 100 vehicle miles",
        "Adopters in the Neighborhood": "3% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$44,000",
        "Savings compared to Gasoline Car": "$7.7 per 100 miles",
        "Battery Range": "280 miles",
        "Lifecycle Greenhouse Gas Emissions": "10kg emissions per 100 vehicle miles",
        "Adopters in the Neighborhood": "3% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$32,000",
        "Savings compared to Gasoline Car": "$7.7 per 100 miles + additional $6 savings on carbon tax",
        "Battery Range": "280 miles",
        "Lifecycle Greenhouse Gas Emissions": "30kg emissions per 100 vehicle miles",
        "Adopters in the Neighborhood": "58% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$56,000",
        "Savings compared to Gasoline Car": "$5.5 per 100 miles + additional $1.5 savings on carbon tax",
        "Battery Range": "440 miles",
        "Lifecycle Greenhouse Gas Emissions": "30kg emissions per 100 vehicle miles",
        "Adopters in the Neighborhood": "58% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$56,000",
        "Savings compared to Gasoline Car": "$7.7 per 100 miles",
        "Battery Range": "120 miles",
        "Lifecycle Greenhouse Gas Emissions": "20kg emissions per 100 vehicle miles",
        "Adopters in the Neighborhood": "58% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$44,000",
        "Savings compared to Gasoline Car": "$6.4 per 100 miles + additional $1.5 savings on carbon tax",
        "Battery Range": "280 miles",
        "Lifecycle Greenhouse Gas Emissions": "20kg emissions per 100 vehicle miles",
        "Adopters in the Neighborhood": "58% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$44,000",
        "Savings compared to Gasoline Car": "$5.5 per 100 miles + additional $6 savings on carbon tax",
        "Battery Range": "120 miles",
        "Lifecycle Greenhouse Gas Emissions": "10kg emissions per 100 vehicle miles",
        "Adopters in the Neighborhood": "58% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$32,000",
        "Savings compared to Gasoline Car": "$6.4 per 100 miles",
        "Battery Range": "440 miles",
        "Lifecycle Greenhouse Gas Emissions": "10kg emissions per 100 vehicle miles",
        "Adopters in the Neighborhood": "58% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$44,000",
        "Savings compared to Gasoline Car": "$6.4 per 100 miles + additional $1.5 savings on carbon tax",
        "Battery Range": "120 miles",
        "Lifecycle Greenhouse Gas Emissions": "30kg emissions per 100 vehicle miles",
        "Adopters in the Neighborhood": "86% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$56,000",
        "Savings compared to Gasoline Car": "$5.5 per 100 miles",
        "Battery Range": "280 miles",
        "Lifecycle Greenhouse Gas Emissions": "30kg emissions per 100 vehicle miles",
        "Adopters in the Neighborhood": "86% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$32,000",
        "Savings compared to Gasoline Car": "$5.5 per 100 miles + additional $6 savings on carbon tax",
        "Battery Range": "120 miles",
        "Lifecycle Greenhouse Gas Emissions": "20kg emissions per 100 vehicle miles",
        "Adopters in the Neighborhood": "86% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$44,000",
        "Savings compared to Gasoline Car": "$6.4 per 100 miles",
        "Battery Range": "440 miles",
        "Lifecycle Greenhouse Gas Emissions": "20kg emissions per 100 vehicle miles",
        "Adopters in the Neighborhood": "86% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$32,000",
        "Savings compared to Gasoline Car": "$6.4 per 100 miles + additional $1.5 savings on carbon tax",
        "Battery Range": "280 miles",
        "Lifecycle Greenhouse Gas Emissions": "10kg emissions per 100 vehicle miles",
        "Adopters in the Neighborhood": "86% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$56,000",
        "Savings compared to Gasoline Car": "$7.7 per 100 miles + additional $6 savings on carbon tax",
        "Battery Range": "440 miles",
        "Lifecycle Greenhouse Gas Emissions": "10kg emissions per 100 vehicle miles",
        "Adopters in the Neighborhood": "86% of adopters in the neighborhood",
    },
]

attributes_listA_large = [
    {
        "Investment Costs": "$88,000",
        "Savings compared to Gasoline Car": "$6.4 per 100 miles",
        "Battery Range": "120 miles",
        "Lifecycle Greenhouse Gas Emissions": "30kg emissions per 100 vehicle miles",
        "Adopters in the Neighborhood": "3% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$100,000",
        "Savings compared to Gasoline Car": "$7.6 per 100 miles + additional $6 savings on carbon tax",
        "Battery Range": "440 miles",
        "Lifecycle Greenhouse Gas Emissions": "30kg emissions per 100 vehicle miles",
        "Adopters in the Neighborhood": "3% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$112,000",
        "Savings compared to Gasoline Car": "$6.4 per 100 miles + additional $6 savings on carbon tax",
        "Battery Range": "280 miles",
        "Lifecycle Greenhouse Gas Emissions": "20kg emissions per 100 vehicle miles",
        "Adopters in the Neighborhood": "3% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$88,000",
        "Savings compared to Gasoline Car": "$9.2 per 100 miles + additional $1.5 savings on carbon tax",
        "Battery Range": "440 miles",
        "Lifecycle Greenhouse Gas Emissions": "20kg emissions per 100 vehicle miles",
        "Adopters in the Neighborhood": "3% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$112,000",
        "Savings compared to Gasoline Car": "$7.6 per 100 miles",
        "Battery Range": "120 miles",
        "Lifecycle Greenhouse Gas Emissions": "10kg emissions per 100 vehicle miles",
        "Adopters in the Neighborhood": "3% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$100,000",
        "Savings compared to Gasoline Car": "$9.2 per 100 miles",
        "Battery Range": "280 miles",
        "Lifecycle Greenhouse Gas Emissions": "10kg emissions per 100 vehicle miles",
        "Adopters in the Neighborhood": "3% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$88,000",
        "Savings compared to Gasoline Car": "$9.2 per 100 miles + additional $6 savings on carbon tax",
        "Battery Range": "280 miles",
        "Lifecycle Greenhouse Gas Emissions": "30kg emissions per 100 vehicle miles",
        "Adopters in the Neighborhood": "58% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$112,000",
        "Savings compared to Gasoline Car": "$6.4 per 100 miles + additional $1.5 savings on carbon tax",
        "Battery Range": "440 miles",
        "Lifecycle Greenhouse Gas Emissions": "30kg emissions per 100 vehicle miles",
        "Adopters in the Neighborhood": "58% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$112,000",
        "Savings compared to Gasoline Car": "$9.2 per 100 miles",
        "Battery Range": "120 miles",
        "Lifecycle Greenhouse Gas Emissions": "20kg emissions per 100 vehicle miles",
        "Adopters in the Neighborhood": "58% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$100,000",
        "Savings compared to Gasoline Car": "$7.6 per 100 miles + additional $1.5 savings on carbon tax",
        "Battery Range": "280 miles",
        "Lifecycle Greenhouse Gas Emissions": "20kg emissions per 100 vehicle miles",
        "Adopters in the Neighborhood": "58% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$100,000",
        "Savings compared to Gasoline Car": "$6.4 per 100 miles + additional $6 savings on carbon tax",
        "Battery Range": "120 miles",
        "Lifecycle Greenhouse Gas Emissions": "10kg emissions per 100 vehicle miles",
        "Adopters in the Neighborhood": "58% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$88,000",
        "Savings compared to Gasoline Car": "$7.6 per 100 miles",
        "Battery Range": "440 miles",
        "Lifecycle Greenhouse Gas Emissions": "10kg emissions per 100 vehicle miles",
        "Adopters in the Neighborhood": "58% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$100,000",
        "Savings compared to Gasoline Car": "$7.6 per 100 miles + additional $1.5 savings on carbon tax",
        "Battery Range": "120 miles",
        "Lifecycle Greenhouse Gas Emissions": "30kg emissions per 100 vehicle miles",
        "Adopters in the Neighborhood": "86% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$112,000",
        "Savings compared to Gasoline Car": "$6.4 per 100 miles",
        "Battery Range": "280 miles",
        "Lifecycle Greenhouse Gas Emissions": "30kg emissions per 100 vehicle miles",
        "Adopters in the Neighborhood": "86% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$88,000",
        "Savings compared to Gasoline Car": "$6.4 per 100 miles + additional $6 savings on carbon tax",
        "Battery Range": "120 miles",
        "Lifecycle Greenhouse Gas Emissions": "20kg emissions per 100 vehicle miles",
        "Adopters in the Neighborhood": "86% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$100,000",
        "Savings compared to Gasoline Car": "$7.6 per 100 miles",
        "Battery Range": "440 miles",
        "Lifecycle Greenhouse Gas Emissions": "20kg emissions per 100 vehicle miles",
        "Adopters in the Neighborhood": "86% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$88,000",
        "Savings compared to Gasoline Car": "$7.6 per 100 miles + additional $1.5 savings on carbon tax",
        "Battery Range": "280 miles",
        "Lifecycle Greenhouse Gas Emissions": "10kg emissions per 100 vehicle miles",
        "Adopters in the Neighborhood": "86% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$112,000",
        "Savings compared to Gasoline Car": "$9.2 per 100 miles + additional $6 savings on carbon tax",
        "Battery Range": "440 miles",
        "Lifecycle Greenhouse Gas Emissions": "10kg emissions per 100 vehicle miles",
        "Adopters in the Neighborhood": "86% of adopters in the neighborhood",
    },
]

attributes_listB_small = [
    {
        "Investment Costs": "$30,000",
        "Savings compared to Gasoline Car": "$4.5 per 100 miles",
        "Battery Range": "120 miles",
        "Lifecycle Greenhouse Gas Emissions": "45% of emissions saved",
        "Adopters in the Neighborhood": "3% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$18,000",
        "Savings compared to Gasoline Car": "$5.3 per 100 miles + additional $6 savings on carbon tax",
        "Battery Range": "440 miles",
        "Lifecycle Greenhouse Gas Emissions": "45% of emissions saved",
        "Adopters in the Neighborhood": "3% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$6,000",
        "Savings compared to Gasoline Car": "$4.5 per 100 miles + additional $6 savings on carbon tax",
        "Battery Range": "280 miles",
        "Lifecycle Greenhouse Gas Emissions": "65% of emissions saved",
        "Adopters in the Neighborhood": "3% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$30,000",
        "Savings compared to Gasoline Car": "$6.2 per 100 miles + additional $1.5 savings on carbon tax",
        "Battery Range": "440 miles",
        "Lifecycle Greenhouse Gas Emissions": "65% of emissions saved",
        "Adopters in the Neighborhood": "3% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$6,000",
        "Savings compared to Gasoline Car": "$5.3 per 100 miles",
        "Battery Range": "120 miles",
        "Lifecycle Greenhouse Gas Emissions": "45% of emissions saved",
        "Adopters in the Neighborhood": "3% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$18,000",
        "Savings compared to Gasoline Car": "$6.2 per 100 miles",
        "Battery Range": "280 miles",
        "Lifecycle Greenhouse Gas Emissions": "45% of emissions saved",
        "Adopters in the Neighborhood": "3% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$30,000",
        "Savings compared to Gasoline Car": "$6.2 per 100 miles + additional $6 savings on carbon tax",
        "Battery Range": "280 miles",
        "Lifecycle Greenhouse Gas Emissions": "55% of emissions saved",
        "Adopters in the Neighborhood": "58% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$6,000",
        "Savings compared to Gasoline Car": "$4.5 per 100 miles + additional $1.5 savings on carbon tax",
        "Battery Range": "440 miles",
        "Lifecycle Greenhouse Gas Emissions": "55% of emissions saved",
        "Adopters in the Neighborhood": "58% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$6,000",
        "Savings compared to Gasoline Car": "$6.2 per 100 miles",
        "Battery Range": "120 miles",
        "Lifecycle Greenhouse Gas Emissions": "65% of emissions saved",
        "Adopters in the Neighborhood": "58% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$18,000",
        "Savings compared to Gasoline Car": "$5.3 per 100 miles + additional $1.5 savings on carbon tax",
        "Battery Range": "280 miles",
        "Lifecycle Greenhouse Gas Emissions": "65% of emissions saved",
        "Adopters in the Neighborhood": "58% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$18,000",
        "Savings compared to Gasoline Car": "$4.5 per 100 miles + additional $6 savings on carbon tax",
        "Battery Range": "120 miles",
        "Lifecycle Greenhouse Gas Emissions": "45% of emissions saved",
        "Adopters in the Neighborhood": "58% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$30,000",
        "Savings compared to Gasoline Car": "$5.3 per 100 miles",
        "Battery Range": "440 miles",
        "Lifecycle Greenhouse Gas Emissions": "45% of emissions saved",
        "Adopters in the Neighborhood": "58% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$18,000",
        "Savings compared to Gasoline Car": "$6.2 per 100 miles + additional $1.5 savings on carbon tax",
        "Battery Range": "120 miles",
        "Lifecycle Greenhouse Gas Emissions": "65% of emissions saved",
        "Adopters in the Neighborhood": "86% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$6,000",
        "Savings compared to Gasoline Car": "$5.3 per 100 miles",
        "Battery Range": "280 miles",
        "Lifecycle Greenhouse Gas Emissions": "65% of emissions saved",
        "Adopters in the Neighborhood": "86% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$30,000",
        "Savings compared to Gasoline Car": "$5.3 per 100 miles + additional $6 savings on carbon tax",
        "Battery Range": "120 miles",
        "Lifecycle Greenhouse Gas Emissions": "55% of emissions saved",
        "Adopters in the Neighborhood": "86% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$18,000",
        "Savings compared to Gasoline Car": "$4.5 per 100 miles",
        "Battery Range": "440 miles",
        "Lifecycle Greenhouse Gas Emissions": "55% of emissions saved",
        "Adopters in the Neighborhood": "86% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$30,000",
        "Savings compared to Gasoline Car": "$4.5 per 100 miles + additional $1.5 savings on carbon tax",
        "Battery Range": "280 miles",
        "Lifecycle Greenhouse Gas Emissions": "65% of emissions saved",
        "Adopters in the Neighborhood": "86% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$6,000",
        "Savings compared to Gasoline Car": "$6.2 per 100 miles + additional $6 savings on carbon tax",
        "Battery Range": "440 miles",
        "Lifecycle Greenhouse Gas Emissions": "65% of emissions saved",
        "Adopters in the Neighborhood": "86% of adopters in the neighborhood",
    },
]

attributes_listB_medium = [
    {
        "Investment Costs": "$32,000",
        "Savings compared to Gasoline Car": "$5.5 per 100 miles",
        "Battery Range": "120 miles",
        "Lifecycle Greenhouse Gas Emissions": "45% of emissions saved",
        "Adopters in the Neighborhood": "3% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$44,000",
        "Savings compared to Gasoline Car": "$6.4 per 100 miles + additional $6 savings on carbon tax",
        "Battery Range": "440 miles",
        "Lifecycle Greenhouse Gas Emissions": "45% of emissions saved",
        "Adopters in the Neighborhood": "3% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$56,000",
        "Savings compared to Gasoline Car": "$5.5 per 100 miles + additional $6 savings on carbon tax",
        "Battery Range": "280 miles",
        "Lifecycle Greenhouse Gas Emissions": "65% of emissions saved",
        "Adopters in the Neighborhood": "3% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$32,000",
        "Savings compared to Gasoline Car": "$7.7 per 100 miles + additional $1.5 savings on carbon tax",
        "Battery Range": "440 miles",
        "Lifecycle Greenhouse Gas Emissions": "65% of emissions saved",
        "Adopters in the Neighborhood": "3% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$56,000",
        "Savings compared to Gasoline Car": "$6.4 per 100 miles",
        "Battery Range": "120 miles",
        "Lifecycle Greenhouse Gas Emissions": "45% of emissions saved",
        "Adopters in the Neighborhood": "3% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$44,000",
        "Savings compared to Gasoline Car": "$7.7 per 100 miles",
        "Battery Range": "280 miles",
        "Lifecycle Greenhouse Gas Emissions": "45% of emissions saved",
        "Adopters in the Neighborhood": "3% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$32,000",
        "Savings compared to Gasoline Car": "$7.7 per 100 miles + additional $6 savings on carbon tax",
        "Battery Range": "280 miles",
        "Lifecycle Greenhouse Gas Emissions": "55% of emissions saved",
        "Adopters in the Neighborhood": "58% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$56,000",
        "Savings compared to Gasoline Car": "$5.5 per 100 miles + additional $1.5 savings on carbon tax",
        "Battery Range": "440 miles",
        "Lifecycle Greenhouse Gas Emissions": "55% of emissions saved",
        "Adopters in the Neighborhood": "58% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$56,000",
        "Savings compared to Gasoline Car": "$7.7 per 100 miles",
        "Battery Range": "120 miles",
        "Lifecycle Greenhouse Gas Emissions": "65% of emissions saved",
        "Adopters in the Neighborhood": "58% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$44,000",
        "Savings compared to Gasoline Car": "$6.4 per 100 miles + additional $1.5 savings on carbon tax",
        "Battery Range": "280 miles",
        "Lifecycle Greenhouse Gas Emissions": "65% of emissions saved",
        "Adopters in the Neighborhood": "58% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$44,000",
        "Savings compared to Gasoline Car": "$5.5 per 100 miles + additional $6 savings on carbon tax",
        "Battery Range": "120 miles",
        "Lifecycle Greenhouse Gas Emissions": "45% of emissions saved",
        "Adopters in the Neighborhood": "58% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$32,000",
        "Savings compared to Gasoline Car": "$6.4 per 100 miles",
        "Battery Range": "440 miles",
        "Lifecycle Greenhouse Gas Emissions": "45% of emissions saved",
        "Adopters in the Neighborhood": "58% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$44,000",
        "Savings compared to Gasoline Car": "$6.4 per 100 miles + additional $1.5 savings on carbon tax",
        "Battery Range": "120 miles",
        "Lifecycle Greenhouse Gas Emissions": "65% of emissions saved",
        "Adopters in the Neighborhood": "86% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$56,000",
        "Savings compared to Gasoline Car": "$5.5 per 100 miles",
        "Battery Range": "280 miles",
        "Lifecycle Greenhouse Gas Emissions": "65% of emissions saved",
        "Adopters in the Neighborhood": "86% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$32,000",
        "Savings compared to Gasoline Car": "$5.5 per 100 miles + additional $6 savings on carbon tax",
        "Battery Range": "120 miles",
        "Lifecycle Greenhouse Gas Emissions": "55% of emissions saved",
        "Adopters in the Neighborhood": "86% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$44,000",
        "Savings compared to Gasoline Car": "$6.4 per 100 miles",
        "Battery Range": "440 miles",
        "Lifecycle Greenhouse Gas Emissions": "55% of emissions saved",
        "Adopters in the Neighborhood": "86% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$32,000",
        "Savings compared to Gasoline Car": "$6.4 per 100 miles + additional $1.5 savings on carbon tax",
        "Battery Range": "280 miles",
        "Lifecycle Greenhouse Gas Emissions": "65% of emissions saved",
        "Adopters in the Neighborhood": "86% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$56,000",
        "Savings compared to Gasoline Car": "$7.7 per 100 miles + additional $6 savings on carbon tax",
        "Battery Range": "440 miles",
        "Lifecycle Greenhouse Gas Emissions": "65% of emissions saved",
        "Adopters in the Neighborhood": "86% of adopters in the neighborhood",
    },
]

attributes_listB_large = [
    {
        "Investment Costs": "$88,000",
        "Savings compared to Gasoline Car": "$6.4 per 100 miles",
        "Battery Range": "120 miles",
        "Lifecycle Greenhouse Gas Emissions": "45% of emissions saved",
        "Adopters in the Neighborhood": "3% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$100,000",
        "Savings compared to Gasoline Car": "$7.6 per 100 miles + additional $6 savings on carbon tax",
        "Battery Range": "440 miles",
        "Lifecycle Greenhouse Gas Emissions": "45% of emissions saved",
        "Adopters in the Neighborhood": "3% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$112,000",
        "Savings compared to Gasoline Car": "$6.4 per 100 miles + additional $6 savings on carbon tax",
        "Battery Range": "280 miles",
        "Lifecycle Greenhouse Gas Emissions": "65% of emissions saved",
        "Adopters in the Neighborhood": "3% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$88,000",
        "Savings compared to Gasoline Car": "$9.2 per 100 miles + additional $1.5 savings on carbon tax",
        "Battery Range": "440 miles",
        "Lifecycle Greenhouse Gas Emissions": "65% of emissions saved",
        "Adopters in the Neighborhood": "3% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$112,000",
        "Savings compared to Gasoline Car": "$7.6 per 100 miles",
        "Battery Range": "120 miles",
        "Lifecycle Greenhouse Gas Emissions": "45% of emissions saved",
        "Adopters in the Neighborhood": "3% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$100,000",
        "Savings compared to Gasoline Car": "$9.2 per 100 miles",
        "Battery Range": "280 miles",
        "Lifecycle Greenhouse Gas Emissions": "45% of emissions saved",
        "Adopters in the Neighborhood": "3% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$88,000",
        "Savings compared to Gasoline Car": "$9.2 per 100 miles + additional $6 savings on carbon tax",
        "Battery Range": "280 miles",
        "Lifecycle Greenhouse Gas Emissions": "55% of emissions saved",
        "Adopters in the Neighborhood": "58% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$112,000",
        "Savings compared to Gasoline Car": "$6.4 per 100 miles + additional $1.5 savings on carbon tax",
        "Battery Range": "440 miles",
        "Lifecycle Greenhouse Gas Emissions": "55% of emissions saved",
        "Adopters in the Neighborhood": "58% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$112,000",
        "Savings compared to Gasoline Car": "$9.2 per 100 miles",
        "Battery Range": "120 miles",
        "Lifecycle Greenhouse Gas Emissions": "65% of emissions saved",
        "Adopters in the Neighborhood": "58% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$100,000",
        "Savings compared to Gasoline Car": "$7.6 per 100 miles + additional $1.5 savings on carbon tax",
        "Battery Range": "280 miles",
        "Lifecycle Greenhouse Gas Emissions": "65% of emissions saved",
        "Adopters in the Neighborhood": "58% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$100,000",
        "Savings compared to Gasoline Car": "$6.4 per 100 miles + additional $6 savings on carbon tax",
        "Battery Range": "120 miles",
        "Lifecycle Greenhouse Gas Emissions": "45% of emissions saved",
        "Adopters in the Neighborhood": "58% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$88,000",
        "Savings compared to Gasoline Car": "$7.6 per 100 miles",
        "Battery Range": "440 miles",
        "Lifecycle Greenhouse Gas Emissions": "45% of emissions saved",
        "Adopters in the Neighborhood": "58% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$100,000",
        "Savings compared to Gasoline Car": "$7.6 per 100 miles + additional $1.5 savings on carbon tax",
        "Battery Range": "120 miles",
        "Lifecycle Greenhouse Gas Emissions": "65% of emissions saved",
        "Adopters in the Neighborhood": "86% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$112,000",
        "Savings compared to Gasoline Car": "$6.4 per 100 miles",
        "Battery Range": "280 miles",
        "Lifecycle Greenhouse Gas Emissions": "65% of emissions saved",
        "Adopters in the Neighborhood": "86% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$88,000",
        "Savings compared to Gasoline Car": "$6.4 per 100 miles + additional $6 savings on carbon tax",
        "Battery Range": "120 miles",
        "Lifecycle Greenhouse Gas Emissions": "55% of emissions saved",
        "Adopters in the Neighborhood": "86% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$100,000",
        "Savings compared to Gasoline Car": "$7.6 per 100 miles",
        "Battery Range": "440 miles",
        "Lifecycle Greenhouse Gas Emissions": "55% of emissions saved",
        "Adopters in the Neighborhood": "86% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$88,000",
        "Savings compared to Gasoline Car": "$7.6 per 100 miles + additional $1.5 savings on carbon tax",
        "Battery Range": "280 miles",
        "Lifecycle Greenhouse Gas Emissions": "45% of emissions saved",
        "Adopters in the Neighborhood": "86% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$112,000",
        "Savings compared to Gasoline Car": "$9.2 per 100 miles + additional $6 savings on carbon tax",
        "Battery Range": "440 miles",
        "Lifecycle Greenhouse Gas Emissions": "45% of emissions saved",
        "Adopters in the Neighborhood": "86% of adopters in the neighborhood",
    },
]

attributes_listC_small = [
    {
        "Investment Costs": "$30,000",
        "Savings compared to Gasoline Car": "$4.5 per 100 miles",
        "Battery Range": "120 miles",
        "Lifecycle Greenhouse Gas Emissions": "30kg emissions per 100 vehicle miles",
        "Adopters in the Neighborhood": "3% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$18,000",
        "Savings compared to Gasoline Car": "$5.3 per 100 miles",
        "Battery Range": "440 miles",
        "Lifecycle Greenhouse Gas Emissions": "30kg emissions per 100 vehicle miles",
        "Adopters in the Neighborhood": "3% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$6,000",
        "Savings compared to Gasoline Car": "$4.5 per 100 miles",
        "Battery Range": "280 miles",
        "Lifecycle Greenhouse Gas Emissions": "20kg emissions per 100 vehicle miles",
        "Adopters in the Neighborhood": "3% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$30,000",
        "Savings compared to Gasoline Car": "$6.2 per 100 miles",
        "Battery Range": "440 miles",
        "Lifecycle Greenhouse Gas Emissions": "20kg emissions per 100 vehicle miles",
        "Adopters in the Neighborhood": "3% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$6,000",
        "Savings compared to Gasoline Car": "$5.3 per 100 miles",
        "Battery Range": "120 miles",
        "Lifecycle Greenhouse Gas Emissions": "10kg emissions per 100 vehicle miles",
        "Adopters in the Neighborhood": "3% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$18,000",
        "Savings compared to Gasoline Car": "$6.2 per 100 miles",
        "Battery Range": "280 miles",
        "Lifecycle Greenhouse Gas Emissions": "10kg emissions per 100 vehicle miles",
        "Adopters in the Neighborhood": "3% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$30,000",
        "Savings compared to Gasoline Car": "$6.2 per 100 miles",
        "Battery Range": "280 miles",
        "Lifecycle Greenhouse Gas Emissions": "30kg emissions per 100 vehicle miles",
        "Adopters in the Neighborhood": "58% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$6,000",
        "Savings compared to Gasoline Car": "$4.5 per 100 miles",
        "Battery Range": "440 miles",
        "Lifecycle Greenhouse Gas Emissions": "30kg emissions per 100 vehicle miles",
        "Adopters in the Neighborhood": "58% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$6,000",
        "Savings compared to Gasoline Car": "$6.2 per 100 miles",
        "Battery Range": "120 miles",
        "Lifecycle Greenhouse Gas Emissions": "20kg emissions per 100 vehicle miles",
        "Adopters in the Neighborhood": "58% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$18,000",
        "Savings compared to Gasoline Car": "$5.3 per 100 miles",
        "Battery Range": "280 miles",
        "Lifecycle Greenhouse Gas Emissions": "20kg emissions per 100 vehicle miles",
        "Adopters in the Neighborhood": "58% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$18,000",
        "Savings compared to Gasoline Car": "$4.5 per 100 miles",
        "Battery Range": "120 miles",
        "Lifecycle Greenhouse Gas Emissions": "10kg emissions per 100 vehicle miles",
        "Adopters in the Neighborhood": "58% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$30,000",
        "Savings compared to Gasoline Car": "$5.3 per 100 miles",
        "Battery Range": "440 miles",
        "Lifecycle Greenhouse Gas Emissions": "10kg emissions per 100 vehicle miles",
        "Adopters in the Neighborhood": "58% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$18,000",
        "Savings compared to Gasoline Car": "$6.2 per 100 miles",
        "Battery Range": "120 miles",
        "Lifecycle Greenhouse Gas Emissions": "30kg emissions per 100 vehicle miles",
        "Adopters in the Neighborhood": "86% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$6,000",
        "Savings compared to Gasoline Car": "$5.3 per 100 miles",
        "Battery Range": "280 miles",
        "Lifecycle Greenhouse Gas Emissions": "30kg emissions per 100 vehicle miles",
        "Adopters in the Neighborhood": "86% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$30,000",
        "Savings compared to Gasoline Car": "$5.3 per 100 miles",
        "Battery Range": "120 miles",
        "Lifecycle Greenhouse Gas Emissions": "20kg emissions per 100 vehicle miles",
        "Adopters in the Neighborhood": "86% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$18,000",
        "Savings compared to Gasoline Car": "$4.5 per 100 miles",
        "Battery Range": "440 miles",
        "Lifecycle Greenhouse Gas Emissions": "20kg emissions per 100 vehicle miles",
        "Adopters in the Neighborhood": "86% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$30,000",
        "Savings compared to Gasoline Car": "$4.5 per 100 miles",
        "Battery Range": "280 miles",
        "Lifecycle Greenhouse Gas Emissions": "10kg emissions per 100 vehicle miles",
        "Adopters in the Neighborhood": "86% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$6,000",
        "Savings compared to Gasoline Car": "$6.2 per 100 miles",
        "Battery Range": "440 miles",
        "Lifecycle Greenhouse Gas Emissions": "10kg emissions per 100 vehicle miles",
        "Adopters in the Neighborhood": "86% of adopters in the neighborhood",
    },
]

attributes_listC_medium = [
    {
        "Investment Costs": "$32,000",
        "Savings compared to Gasoline Car": "$5.5 per 100 miles",
        "Battery Range": "120 miles",
        "Lifecycle Greenhouse Gas Emissions": "30kg emissions per 100 vehicle miles",
        "Adopters in the Neighborhood": "3% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$44,000",
        "Savings compared to Gasoline Car": "$6.4 per 100 miles",
        "Battery Range": "440 miles",
        "Lifecycle Greenhouse Gas Emissions": "30kg emissions per 100 vehicle miles",
        "Adopters in the Neighborhood": "3% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$56,000",
        "Savings compared to Gasoline Car": "$5.5 per 100 miles",
        "Battery Range": "280 miles",
        "Lifecycle Greenhouse Gas Emissions": "20kg emissions per 100 vehicle miles",
        "Adopters in the Neighborhood": "3% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$32,000",
        "Savings compared to Gasoline Car": "$7.7 per 100 miles",
        "Battery Range": "440 miles",
        "Lifecycle Greenhouse Gas Emissions": "20kg emissions per 100 vehicle miles",
        "Adopters in the Neighborhood": "3% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$56,000",
        "Savings compared to Gasoline Car": "$6.4 per 100 miles",
        "Battery Range": "120 miles",
        "Lifecycle Greenhouse Gas Emissions": "10kg emissions per 100 vehicle miles",
        "Adopters in the Neighborhood": "3% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$44,000",
        "Savings compared to Gasoline Car": "$7.7 per 100 miles",
        "Battery Range": "280 miles",
        "Lifecycle Greenhouse Gas Emissions": "10kg emissions per 100 vehicle miles",
        "Adopters in the Neighborhood": "3% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$32,000",
        "Savings compared to Gasoline Car": "$7.7 per 100 miles",
        "Battery Range": "280 miles",
        "Lifecycle Greenhouse Gas Emissions": "30kg emissions per 100 vehicle miles",
        "Adopters in the Neighborhood": "58% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$56,000",
        "Savings compared to Gasoline Car": "$5.5 per 100 miles",
        "Battery Range": "440 miles",
        "Lifecycle Greenhouse Gas Emissions": "30kg emissions per 100 vehicle miles",
        "Adopters in the Neighborhood": "58% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$56,000",
        "Savings compared to Gasoline Car": "$7.7 per 100 miles",
        "Battery Range": "120 miles",
        "Lifecycle Greenhouse Gas Emissions": "20kg emissions per 100 vehicle miles",
        "Adopters in the Neighborhood": "58% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$44,000",
        "Savings compared to Gasoline Car": "$6.4 per 100 miles",
        "Battery Range": "280 miles",
        "Lifecycle Greenhouse Gas Emissions": "20kg emissions per 100 vehicle miles",
        "Adopters in the Neighborhood": "58% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$44,000",
        "Savings compared to Gasoline Car": "$5.5 per 100 miles",
        "Battery Range": "120 miles",
        "Lifecycle Greenhouse Gas Emissions": "10kg emissions per 100 vehicle miles",
        "Adopters in the Neighborhood": "58% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$32,000",
        "Savings compared to Gasoline Car": "$6.4 per 100 miles",
        "Battery Range": "440 miles",
        "Lifecycle Greenhouse Gas Emissions": "10kg emissions per 100 vehicle miles",
        "Adopters in the Neighborhood": "58% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$44,000",
        "Savings compared to Gasoline Car": "$6.4 per 100 miles",
        "Battery Range": "120 miles",
        "Lifecycle Greenhouse Gas Emissions": "30kg emissions per 100 vehicle miles",
        "Adopters in the Neighborhood": "86% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$56,000",
        "Savings compared to Gasoline Car": "$5.5 per 100 miles",
        "Battery Range": "280 miles",
        "Lifecycle Greenhouse Gas Emissions": "30kg emissions per 100 vehicle miles",
        "Adopters in the Neighborhood": "86% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$32,000",
        "Savings compared to Gasoline Car": "$5.5 per 100 miles",
        "Battery Range": "120 miles",
        "Lifecycle Greenhouse Gas Emissions": "20kg emissions per 100 vehicle miles",
        "Adopters in the Neighborhood": "86% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$44,000",
        "Savings compared to Gasoline Car": "$6.4 per 100 miles",
        "Battery Range": "440 miles",
        "Lifecycle Greenhouse Gas Emissions": "20kg emissions per 100 vehicle miles",
        "Adopters in the Neighborhood": "86% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$32,000",
        "Savings compared to Gasoline Car": "$6.4 per 100 miles",
        "Battery Range": "280 miles",
        "Lifecycle Greenhouse Gas Emissions": "30kg emissions per 100 vehicle miles",
        "Adopters in the Neighborhood": "86% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$56,000",
        "Savings compared to Gasoline Car": "$7.7 per 100 miles",
        "Battery Range": "440 miles",
        "Lifecycle Greenhouse Gas Emissions": "30kg emissions per 100 vehicle miles",
        "Adopters in the Neighborhood": "86% of adopters in the neighborhood",
    },
]

attributes_listC_large = [
    {
        "Investment Costs": "$88,000",
        "Savings compared to Gasoline Car": "$6.4 per 100 miles",
        "Battery Range": "120 miles",
        "Lifecycle Greenhouse Gas Emissions": "30kg emissions per 100 vehicle miles",
        "Adopters in the Neighborhood": "3% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$100,000",
        "Savings compared to Gasoline Car": "$7.6 per 100 miles",
        "Battery Range": "440 miles",
        "Lifecycle Greenhouse Gas Emissions": "30kg emissions per 100 vehicle miles",
        "Adopters in the Neighborhood": "3% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$112,000",
        "Savings compared to Gasoline Car": "$7.6 per 100 miles",
        "Battery Range": "280 miles",
        "Lifecycle Greenhouse Gas Emissions": "20kg emissions per 100 vehicle miles",
        "Adopters in the Neighborhood": "3% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$88,000",
        "Savings compared to Gasoline Car": "$9.2 per 100 miles",
        "Battery Range": "440 miles",
        "Lifecycle Greenhouse Gas Emissions": "20kg emissions per 100 vehicle miles",
        "Adopters in the Neighborhood": "3% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$112,000",
        "Savings compared to Gasoline Car": "$9.2 per 100 miles",
        "Battery Range": "120 miles",
        "Lifecycle Greenhouse Gas Emissions": "10kg emissions per 100 vehicle miles",
        "Adopters in the Neighborhood": "3% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$100,000",
        "Savings compared to Gasoline Car": "$7.6 per 100 miles",
        "Battery Range": "280 miles",
        "Lifecycle Greenhouse Gas Emissions": "10kg emissions per 100 vehicle miles",
        "Adopters in the Neighborhood": "3% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$88,000",
        "Savings compared to Gasoline Car": "$9.2 per 100 miles",
        "Battery Range": "280 miles",
        "Lifecycle Greenhouse Gas Emissions": "30kg emissions per 100 vehicle miles",
        "Adopters in the Neighborhood": "58% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$112,000",
        "Savings compared to Gasoline Car": "$9.2 per 100 miles",
        "Battery Range": "440 miles",
        "Lifecycle Greenhouse Gas Emissions": "30kg emissions per 100 vehicle miles",
        "Adopters in the Neighborhood": "58% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$112,000",
        "Savings compared to Gasoline Car": "$9.2 per 100 miles",
        "Battery Range": "120 miles",
        "Lifecycle Greenhouse Gas Emissions": "20kg emissions per 100 vehicle miles",
        "Adopters in the Neighborhood": "58% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$100,000",
        "Savings compared to Gasoline Car": "$7.6 per 100 miles",
        "Battery Range": "280 miles",
        "Lifecycle Greenhouse Gas Emissions": "20kg emissions per 100 vehicle miles",
        "Adopters in the Neighborhood": "58% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$100,000",
        "Savings compared to Gasoline Car": "$6.4 per 100 miles",
        "Battery Range": "120 miles",
        "Lifecycle Greenhouse Gas Emissions": "10kg emissions per 100 vehicle miles",
        "Adopters in the Neighborhood": "58% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$88,000",
        "Savings compared to Gasoline Car": "$7.6 per 100 miles",
        "Battery Range": "440 miles",
        "Lifecycle Greenhouse Gas Emissions": "10kg emissions per 100 vehicle miles",
        "Adopters in the Neighborhood": "58% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$100,000",
        "Savings compared to Gasoline Car": "$7.6 per 100 miles",
        "Battery Range": "120 miles",
        "Lifecycle Greenhouse Gas Emissions": "30kg emissions per 100 vehicle miles",
        "Adopters in the Neighborhood": "86% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$112,000",
        "Savings compared to Gasoline Car": "$6.4 per 100 miles",
        "Battery Range": "280 miles",
        "Lifecycle Greenhouse Gas Emissions": "30kg emissions per 100 vehicle miles",
        "Adopters in the Neighborhood": "86% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$88,000",
        "Savings compared to Gasoline Car": "$6.4 per 100 miles",
        "Battery Range": "120 miles",
        "Lifecycle Greenhouse Gas Emissions": "20kg emissions per 100 vehicle miles",
        "Adopters in the Neighborhood": "86% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$100,000",
        "Savings compared to Gasoline Car": "$7.6 per 100 miles",
        "Battery Range": "440 miles",
        "Lifecycle Greenhouse Gas Emissions": "20kg emissions per 100 vehicle miles",
        "Adopters in the Neighborhood": "86% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$88,000",
        "Savings compared to Gasoline Car": "$7.6 per 100 miles",
        "Battery Range": "280 miles",
        "Lifecycle Greenhouse Gas Emissions": "30kg emissions per 100 vehicle miles",
        "Adopters in the Neighborhood": "86% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$112,000",
        "Savings compared to Gasoline Car": "$9.2 per 100 miles",
        "Battery Range": "440 miles",
        "Lifecycle Greenhouse Gas Emissions": "30kg emissions per 100 vehicle miles",
        "Adopters in the Neighborhood": "86% of adopters in the neighborhood",
    },
]

attributes_listD_small = [
    {
        "Investment Costs": "$30,000",
        "Savings compared to Gasoline Car": "$4.5 per 100 miles",
        "Battery Range": "120 miles",
        "Lifecycle Greenhouse Gas Emissions": "45% of emissions saved",
        "Adopters in the Neighborhood": "3% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$18,000",
        "Savings compared to Gasoline Car": "$5.3 per 100 miles",
        "Battery Range": "440 miles",
        "Lifecycle Greenhouse Gas Emissions": "45% of emissions saved",
        "Adopters in the Neighborhood": "3% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$6,000",
        "Savings compared to Gasoline Car": "$4.5 per 100 miles",
        "Battery Range": "280 miles",
        "Lifecycle Greenhouse Gas Emissions": "65% of emissions saved",
        "Adopters in the Neighborhood": "3% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$30,000",
        "Savings compared to Gasoline Car": "$6.2 per 100 miles",
        "Battery Range": "440 miles",
        "Lifecycle Greenhouse Gas Emissions": "65% of emissions saved",
        "Adopters in the Neighborhood": "3% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$6,000",
        "Savings compared to Gasoline Car": "$5.3 per 100 miles",
        "Battery Range": "120 miles",
        "Lifecycle Greenhouse Gas Emissions": "45% of emissions saved",
        "Adopters in the Neighborhood": "3% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$18,000",
        "Savings compared to Gasoline Car": "$6.2 per 100 miles",
        "Battery Range": "280 miles",
        "Lifecycle Greenhouse Gas Emissions": "45% of emissions saved",
        "Adopters in the Neighborhood": "3% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$30,000",
        "Savings compared to Gasoline Car": "$6.2 per 100 miles",
        "Battery Range": "280 miles",
        "Lifecycle Greenhouse Gas Emissions": "55% of emissions saved",
        "Adopters in the Neighborhood": "58% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$6,000",
        "Savings compared to Gasoline Car": "$4.5 per 100 miles",
        "Battery Range": "440 miles",
        "Lifecycle Greenhouse Gas Emissions": "55% of emissions saved",
        "Adopters in the Neighborhood": "58% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$6,000",
        "Savings compared to Gasoline Car": "$6.2 per 100 miles",
        "Battery Range": "120 miles",
        "Lifecycle Greenhouse Gas Emissions": "65% of emissions saved",
        "Adopters in the Neighborhood": "58% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$18,000",
        "Savings compared to Gasoline Car": "$5.3 per 100 miles",
        "Battery Range": "280 miles",
        "Lifecycle Greenhouse Gas Emissions": "65% of emissions saved",
        "Adopters in the Neighborhood": "58% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$18,000",
        "Savings compared to Gasoline Car": "$4.5 per 100 miles",
        "Battery Range": "120 miles",
        "Lifecycle Greenhouse Gas Emissions": "45% of emissions saved",
        "Adopters in the Neighborhood": "58% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$30,000",
        "Savings compared to Gasoline Car": "$5.3 per 100 miles",
        "Battery Range": "440 miles",
        "Lifecycle Greenhouse Gas Emissions": "45% of emissions saved",
        "Adopters in the Neighborhood": "58% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$18,000",
        "Savings compared to Gasoline Car": "$6.2 per 100 miles",
        "Battery Range": "120 miles",
        "Lifecycle Greenhouse Gas Emissions": "65% of emissions saved",
        "Adopters in the Neighborhood": "86% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$6,000",
        "Savings compared to Gasoline Car": "$5.3 per 100 miles",
        "Battery Range": "280 miles",
        "Lifecycle Greenhouse Gas Emissions": "65% of emissions saved",
        "Adopters in the Neighborhood": "86% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$30,000",
        "Savings compared to Gasoline Car": "$5.3 per 100 miles",
        "Battery Range": "120 miles",
        "Lifecycle Greenhouse Gas Emissions": "55% of emissions saved",
        "Adopters in the Neighborhood": "86% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$18,000",
        "Savings compared to Gasoline Car": "$4.5 per 100 miles",
        "Battery Range": "440 miles",
        "Lifecycle Greenhouse Gas Emissions": "55% of emissions saved",
        "Adopters in the Neighborhood": "86% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$30,000",
        "Savings compared to Gasoline Car": "$4.5 per 100 miles",
        "Battery Range": "280 miles",
        "Lifecycle Greenhouse Gas Emissions": "65% of emissions saved",
        "Adopters in the Neighborhood": "86% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$6,000",
        "Savings compared to Gasoline Car": "$6.2 per 100 miles",
        "Battery Range": "440 miles",
        "Lifecycle Greenhouse Gas Emissions": "65% of emissions saved",
        "Adopters in the Neighborhood": "86% of adopters in the neighborhood",
    },
]

attributes_listD_medium = [
    {
        "Investment Costs": "$32,000",
        "Savings compared to Gasoline Car": "$5.5 per 100 miles",
        "Battery Range": "120 miles",
        "Lifecycle Greenhouse Gas Emissions": "45% of emissions saved",
        "Adopters in the Neighborhood": "3% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$44,000",
        "Savings compared to Gasoline Car": "$6.4 per 100 miles",
        "Battery Range": "440 miles",
        "Lifecycle Greenhouse Gas Emissions": "45% of emissions saved",
        "Adopters in the Neighborhood": "3% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$56,000",
        "Savings compared to Gasoline Car": "$5.5 per 100 miles",
        "Battery Range": "280 miles",
        "Lifecycle Greenhouse Gas Emissions": "65% of emissions saved",
        "Adopters in the Neighborhood": "3% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$32,000",
        "Savings compared to Gasoline Car": "$7.7 per 100 miles",
        "Battery Range": "440 miles",
        "Lifecycle Greenhouse Gas Emissions": "65% of emissions saved",
        "Adopters in the Neighborhood": "3% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$56,000",
        "Savings compared to Gasoline Car": "$6.4 per 100 miles",
        "Battery Range": "120 miles",
        "Lifecycle Greenhouse Gas Emissions": "45% of emissions saved",
        "Adopters in the Neighborhood": "3% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$44,000",
        "Savings compared to Gasoline Car": "$7.7 per 100 miles",
        "Battery Range": "280 miles",
        "Lifecycle Greenhouse Gas Emissions": "45% of emissions saved",
        "Adopters in the Neighborhood": "3% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$32,000",
        "Savings compared to Gasoline Car": "$7.7 per 100 miles",
        "Battery Range": "280 miles",
        "Lifecycle Greenhouse Gas Emissions": "55% of emissions saved",
        "Adopters in the Neighborhood": "58% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$56,000",
        "Savings compared to Gasoline Car": "$5.5 per 100 miles",
        "Battery Range": "440 miles",
        "Lifecycle Greenhouse Gas Emissions": "55% of emissions saved",
        "Adopters in the Neighborhood": "58% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$56,000",
        "Savings compared to Gasoline Car": "$7.7 per 100 miles",
        "Battery Range": "120 miles",
        "Lifecycle Greenhouse Gas Emissions": "65% of emissions saved",
        "Adopters in the Neighborhood": "58% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$44,000",
        "Savings compared to Gasoline Car": "$6.4 per 100 miles",
        "Battery Range": "280 miles",
        "Lifecycle Greenhouse Gas Emissions": "65% of emissions saved",
        "Adopters in the Neighborhood": "58% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$44,000",
        "Savings compared to Gasoline Car": "$5.5 per 100 miles",
        "Battery Range": "120 miles",
        "Lifecycle Greenhouse Gas Emissions": "45% of emissions saved",
        "Adopters in the Neighborhood": "58% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$32,000",
        "Savings compared to Gasoline Car": "$6.4 per 100 miles",
        "Battery Range": "440 miles",
        "Lifecycle Greenhouse Gas Emissions": "45% of emissions saved",
        "Adopters in the Neighborhood": "58% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$44,000",
        "Savings compared to Gasoline Car": "$6.4 per 100 miles",
        "Battery Range": "120 miles",
        "Lifecycle Greenhouse Gas Emissions": "65% of emissions saved",
        "Adopters in the Neighborhood": "86% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$56,000",
        "Savings compared to Gasoline Car": "$5.5 per 100 miles",
        "Battery Range": "280 miles",
        "Lifecycle Greenhouse Gas Emissions": "65% of emissions saved",
        "Adopters in the Neighborhood": "86% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$32,000",
        "Savings compared to Gasoline Car": "$5.5 per 100 miles",
        "Battery Range": "120 miles",
        "Lifecycle Greenhouse Gas Emissions": "55% of emissions saved",
        "Adopters in the Neighborhood": "86% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$44,000",
        "Savings compared to Gasoline Car": "$6.4 per 100 miles",
        "Battery Range": "440 miles",
        "Lifecycle Greenhouse Gas Emissions": "55% of emissions saved",
        "Adopters in the Neighborhood": "86% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$32,000",
        "Savings compared to Gasoline Car": "$6.4 per 100 miles",
        "Battery Range": "280 miles",
        "Lifecycle Greenhouse Gas Emissions": "65% of emissions saved",
        "Adopters in the Neighborhood": "86% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$56,000",
        "Savings compared to Gasoline Car": "$7.7 per 100 miles",
        "Battery Range": "440 miles",
        "Lifecycle Greenhouse Gas Emissions": "65% of emissions saved",
        "Adopters in the Neighborhood": "86% of adopters in the neighborhood",
    },
]

attributes_listD_large = [
    {
        "Investment Costs": "$88,000",
        "Savings compared to Gasoline Car": "$6.4 per 100 miles",
        "Battery Range": "120 miles",
        "Lifecycle Greenhouse Gas Emissions": "45% of emissions saved",
        "Adopters in the Neighborhood": "3% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$100,000",
        "Savings compared to Gasoline Car": "$7.6 per 100 miles",
        "Battery Range": "440 miles",
        "Lifecycle Greenhouse Gas Emissions": "45% of emissions saved",
        "Adopters in the Neighborhood": "3% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$112,000",
        "Savings compared to Gasoline Car": "$7.6 per 100 miles",
        "Battery Range": "280 miles",
        "Lifecycle Greenhouse Gas Emissions": "65% of emissions saved",
        "Adopters in the Neighborhood": "3% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$88,000",
        "Savings compared to Gasoline Car": "$9.2 per 100 miles",
        "Battery Range": "440 miles",
        "Lifecycle Greenhouse Gas Emissions": "65% of emissions saved",
        "Adopters in the Neighborhood": "3% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$112,000",
        "Savings compared to Gasoline Car": "$9.2 per 100 miles",
        "Battery Range": "120 miles",
        "Lifecycle Greenhouse Gas Emissions": "45% of emissions saved",
        "Adopters in the Neighborhood": "3% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$100,000",
        "Savings compared to Gasoline Car": "$7.6 per 100 miles",
        "Battery Range": "280 miles",
        "Lifecycle Greenhouse Gas Emissions": "45% of emissions saved",
        "Adopters in the Neighborhood": "3% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$88,000",
        "Savings compared to Gasoline Car": "$9.2 per 100 miles",
        "Battery Range": "280 miles",
        "Lifecycle Greenhouse Gas Emissions": "55% of emissions saved",
        "Adopters in the Neighborhood": "58% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$112,000",
        "Savings compared to Gasoline Car": "$9.2 per 100 miles",
        "Battery Range": "440 miles",
        "Lifecycle Greenhouse Gas Emissions": "55% of emissions saved",
        "Adopters in the Neighborhood": "58% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$112,000",
        "Savings compared to Gasoline Car": "$9.2 per 100 miles",
        "Battery Range": "120 miles",
        "Lifecycle Greenhouse Gas Emissions": "65% of emissions saved",
        "Adopters in the Neighborhood": "58% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$100,000",
        "Savings compared to Gasoline Car": "$7.6 per 100 miles",
        "Battery Range": "280 miles",
        "Lifecycle Greenhouse Gas Emissions": "65% of emissions saved",
        "Adopters in the Neighborhood": "58% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$100,000",
        "Savings compared to Gasoline Car": "$6.4 per 100 miles",
        "Battery Range": "120 miles",
        "Lifecycle Greenhouse Gas Emissions": "55% of emissions saved",
        "Adopters in the Neighborhood": "58% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$88,000",
        "Savings compared to Gasoline Car": "$7.6 per 100 miles",
        "Battery Range": "440 miles",
        "Lifecycle Greenhouse Gas Emissions": "55% of emissions saved",
        "Adopters in the Neighborhood": "58% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$100,000",
        "Savings compared to Gasoline Car": "$7.6 per 100 miles",
        "Battery Range": "120 miles",
        "Lifecycle Greenhouse Gas Emissions": "65% of emissions saved",
        "Adopters in the Neighborhood": "86% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$112,000",
        "Savings compared to Gasoline Car": "$6.4 per 100 miles",
        "Battery Range": "280 miles",
        "Lifecycle Greenhouse Gas Emissions": "65% of emissions saved",
        "Adopters in the Neighborhood": "86% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$88,000",
        "Savings compared to Gasoline Car": "$6.4 per 100 miles",
        "Battery Range": "120 miles",
        "Lifecycle Greenhouse Gas Emissions": "55% of emissions saved",
        "Adopters in the Neighborhood": "86% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$100,000",
        "Savings compared to Gasoline Car": "$7.6 per 100 miles",
        "Battery Range": "440 miles",
        "Lifecycle Greenhouse Gas Emissions": "55% of emissions saved",
        "Adopters in the Neighborhood": "86% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$88,000",
        "Savings compared to Gasoline Car": "$7.6 per 100 miles",
        "Battery Range": "280 miles",
        "Lifecycle Greenhouse Gas Emissions": "65% of emissions saved",
        "Adopters in the Neighborhood": "86% of adopters in the neighborhood",
    },
    {
        "Investment Costs": "$112,000",
        "Savings compared to Gasoline Car": "$9.2 per 100 miles",
        "Battery Range": "440 miles",
        "Lifecycle Greenhouse Gas Emissions": "65% of emissions saved",
        "Adopters in the Neighborhood": "86% of adopters in the neighborhood",
    },
]

attributes_listE = [
    {
        "Carbon Tax on Gasoline": "No tax",
        "Subsidy on EV Price": "$3750 tax credit",
        "Climate Label on Cars": "Voluntary label",
        "New Adopters in Neighborhood": "53% of gasoline drivers in your community switched to an EV"
    },
    {
        "Carbon Tax on Gasoline": "$240 per tCO2: about 45% gas price increase",
        "Subsidy on EV Price": "$3750 tax credit",
        "Climate Label on Cars": "Voluntary label",
        "New Adopters in Neighborhood": "12% of gasoline drivers in your community switched to an EV"
    },
    {
        "Carbon Tax on Gasoline": "$240 per tCO2: about 45% gas price increase",
        "Subsidy on EV Price": "No subsidy",
        "Climate Label on Cars": "Mandatory label",
        "New Adopters in Neighborhood": "12% of gasoline drivers in your community switched to an EV"
    },
    {
        "Carbon Tax on Gasoline": "$60 per tCO2: about 15% gas price increase",
        "Subsidy on EV Price": "$3750 tax credit",
        "Climate Label on Cars": "No label",
        "New Adopters in Neighborhood": "81% of gasoline drivers in your community switched to an EV"
    },
    {
        "Carbon Tax on Gasoline": "$60 per tCO2: about 15% gas price increase",
        "Subsidy on EV Price": "No subsidy",
        "Climate Label on Cars": "Mandatory label",
        "New Adopters in Neighborhood": "53% of gasoline drivers in your community switched to an EV"
    },
    {
        "Carbon Tax on Gasoline": "$240 per tCO2: about 45% gas price increase",
        "Subsidy on EV Price": "$3750 tax credit",
        "Climate Label on Cars": "Voluntary label",
        "New Adopters in Neighborhood": "81% of gasoline drivers in your community switched to an EV"
    },
    {
        "Carbon Tax on Gasoline": "No tax",
        "Subsidy on EV Price": "No subsidy",
        "Climate Label on Cars": "Voluntary label",
        "New Adopters in Neighborhood": "53% of gasoline drivers in your community switched to an EV"
    },
    {
        "Carbon Tax on Gasoline": "$240 per tCO2: about 45% gas price increase",
        "Subsidy on EV Price": "No subsidy",
        "Climate Label on Cars": "Voluntary label",
        "New Adopters in Neighborhood": "12% of gasoline drivers in your community switched to an EV"
    },
    {
        "Carbon Tax on Gasoline": "$60 per tCO2: about 15% gas price increase",
        "Subsidy on EV Price": "$7500 tax credit",
        "Climate Label on Cars": "No label",
        "New Adopters in Neighborhood": "53% of gasoline drivers in your community switched to an EV"
    },
    {
        "Carbon Tax on Gasoline": "No tax",
        "Subsidy on EV Price": "No subsidy",
        "Climate Label on Cars": "No label",
        "New Adopters in Neighborhood": "81% of gasoline drivers in your community switched to an EV"
    },
    {
        "Carbon Tax on Gasoline": "$60 per tCO2: about 15% gas price increase",
        "Subsidy on EV Price": "No subsidy",
        "Climate Label on Cars": "No label",
        "New Adopters in Neighborhood": "81% of gasoline drivers in your community switched to an EV"
    },
    {
        "Carbon Tax on Gasoline": "$240 per tCO2: about 45% gas price increase",
        "Subsidy on EV Price": "$7500 tax credit",
        "Climate Label on Cars": "Mandatory label",
        "New Adopters in Neighborhood": "81% of gasoline drivers in your community switched to an EV"
    },
    {
        "Carbon Tax on Gasoline": "No tax",
        "Subsidy on EV Price": "$7500 tax credit",
        "Climate Label on Cars": "Voluntary label",
        "New Adopters in Neighborhood": "12% of gasoline drivers in your community switched to an EV"
    },
    {
        "Carbon Tax on Gasoline": "$240 per tCO2: about 45% gas price increase",
        "Subsidy on EV Price": "$7500 tax credit",
        "Climate Label on Cars": "No label",
        "New Adopters in Neighborhood": "12% of gasoline drivers in your community switched to an EV"
    },
    {
        "Carbon Tax on Gasoline": "$60 per tCO2: about 15% gas price increase",
        "Subsidy on EV Price": "$7500 tax credit",
        "Climate Label on Cars": "Voluntary label",
        "New Adopters in Neighborhood": "12% of gasoline drivers in your community switched to an EV"
    },
    {
        "Carbon Tax on Gasoline": "No tax",
        "Subsidy on EV Price": "$3750 tax credit",
        "Climate Label on Cars": "Mandatory label",
        "New Adopters in Neighborhood": "53% of gasoline drivers in your community switched to an EV"
    },
    {
        "Carbon Tax on Gasoline": "No tax",
        "Subsidy on EV Price": "$7500 tax credit",
        "Climate Label on Cars": "Mandatory label",
        "New Adopters in Neighborhood": "53% of gasoline drivers in your community switched to an EV"
    },
    {
        "Carbon Tax on Gasoline": "$60 per tCO2: about 15% gas price increase",
        "Subsidy on EV Price": "$3750 tax credit",
        "Climate Label on Cars": "Mandatory label",
        "New Adopters in Neighborhood": "53% of gasoline drivers in your community switched to an EV"}
]


# Constants
class Constants(BaseConstants):
    name_in_url = 'Task'
    players_per_group = None
    blocks = ['A', 'B', 'C', 'D', 'E']
    trials_per_block = 18
    num_rounds = 90

    # Add block-specific texts
    block_texts = {
        'A': 'Please note for the following decisions: In addition to the attributes above, '
             'consider that the government introduced a carbon tax on gasoline.',
        'B': 'Please note for the following decisions: In addition to the attributes above, '
             'consider that the government introduced a carbon tax on gasoline.',
        'C': '',
        'D': '',
    }

    affirmative_text = 'Well done on completing the block!'


# Subsession
class Subsession(BaseSubsession):
    pass


# Group
class Group(BaseGroup):
    pass


# Player
class Player(BasePlayer):

    def store_tracking_data(self, payload):
        HoverEvent.create(
            player=self,
            element_id=payload["element_id"],
            enter_time=payload["enter_time"],
            leave_time=payload["leave_time"],
            duration=payload["duration"],
            attributeType=payload["attributeType"],
            attributeValue=payload["attributeValue"],
        )

    # Add a field to store the radio button decision
    choice = models.StringField(
        choices=["Yes", "No"],
        widget=widgets.RadioSelectHorizontal,
    )

    current_task = models.IntegerField(initial=0)
    block = models.StringField()
    current_task_pol = models.IntegerField(initial=0)

    car = models.StringField()


# Extra model for tracking hover events
class HoverEvent(models.ExtraModel):
    player = models.Link(Player)
    element_id = models.StringField()
    enter_time = models.FloatField()
    leave_time = models.FloatField()
    duration = models.IntegerField()
    attributeType = models.StringField()
    attributeValue = models.StringField()


# Custom export function
def custom_export(players):
    print("DEBUG: custom_export function called")
    yield ["session", "participant_code", "round_number", "block", "current_task", "id_in_group",
           "element_id", "enter_time", "leave_time", "duration", "attributeType", "attributeValue", "choice"]
    for player in players:
        print(f"DEBUG: Exporting data for player {player.id_in_group}")
        for e in HoverEvent.filter(player=player):
            yield [
                player.session.code,
                player.participant.code,
                player.round_number,
                player.block,
                player.current_task,
                player.id_in_group,
                e.element_id,
                e.enter_time,
                e.leave_time,
                e.duration,
                e.attributeType,
                e.attributeValue,
                player.choice,  # Include the choice variable
            ]


def creating_session(subsession: Subsession):
    if subsession.round_number == 1:
        for p in subsession.get_players():
            tasks = ['TaskPage'] * Constants.num_rounds + ['PolicyPage']
            random.shuffle(tasks)
            task_rounds = dict(zip(tasks, range(1, len(tasks) + 1)))
            p.participant.task_rounds = task_rounds

    if subsession.round_number <= Constants.num_rounds:
        trials_per_block = Constants.trials_per_block

        for p in subsession.get_players():
            block_order = Constants.blocks.copy()

            # Check if 'E' is in the list before trying to remove it
            if 'E' in block_order:
                block_order.remove('E')

            # Shuffle the order of blocks (excluding Block E)
            random.shuffle(block_order)

            # Decide whether Block E should be placed before or after the shuffled blocks
            if random.choice([True, False]):
                block_order = ['E'] + block_order
            else:
                block_order = block_order + ['E']

            randomized_sequence = []

            # Generate a sequence that completes all trials for each block before moving on to the next block
            for block in block_order:
                block_sequence = [(block, trial_number) for trial_number in range(1, trials_per_block + 1)]
                random.shuffle(block_sequence)
                randomized_sequence.extend(block_sequence)

            p.participant.task_rounds = randomized_sequence
            p.participant.vars['randomized_sequence'] = randomized_sequence


# Page with Blocks A, B, C, D, E
class TaskPage(Page):
    form_model = 'player'
    form_fields = ['choice']

    @staticmethod
    def vars_for_template(player: Player):
        # Ensure that randomized_sequence is set before trying to access it
        if 'randomized_sequence' not in player.participant.vars:
            print("DEBUG: 'randomized_sequence' not found in participant.vars. Calling creating_session.")

        current_task_tuple = player.participant.task_rounds[player.round_number - 1]

        print("Randomized Sequence:", player.participant.vars['randomized_sequence'])

        if not isinstance(current_task_tuple, tuple) or len(current_task_tuple) != 2:
            # Handle the case where current_task_tuple is not a tuple of length 2
            current_task_tuple = ('', 0)

        block, trial_number = current_task_tuple
        print(f"DEBUG: current_task_tuple: {current_task_tuple}, block: {block}, trial_number: {trial_number}")

        player.block = block
        player.current_task = trial_number

        # Get the block-specific text from Constants
        block_text = Constants.block_texts.get(block, 'Default block text')

        policy_block = block == 'E'
        product_block = player.block in ['A', 'B', 'C', 'D']

        # Check if it's the very first trial and the block is A, B, C, or D
        product_first = player.round_number == 1 and player.block in ['A', 'B', 'C', 'D']
        product_second = not product_first and player.round_number == 19 and player.block in ['A', 'B', 'C', 'D']

        first_block_was_policy = False
        if player.round_number == 1 and policy_block:
            first_block_was_policy = True

        # Specify the rounds where the message is supposed to be visually attractive -> first trials of each block
        attractive_rounds = {1, 19, 37, 55, 73}
        # Check if trial_number is in attractive_rounds = first trial of the block
        is_first_trial_of_block = player.round_number in attractive_rounds

        # Well done rounds
        well_done = {19, 37, 55, 73}
        completed_block = player.round_number in well_done

        # Conditionally choose the attributes lists based on the "car" value and block
        if player.participant.vars['car'] == 'Small':
            attributes_list = {
                'A': attributes_listA_small,
                'B': attributes_listB_small,
                'C': attributes_listC_small,
                'D': attributes_listD_small,
                'E': attributes_listE,
            }
        elif player.participant.vars['car'] == 'Medium':
            attributes_list = {
                'A': attributes_listA_medium,
                'B': attributes_listB_medium,
                'C': attributes_listC_medium,
                'D': attributes_listD_medium,
                'E': attributes_listE,
            }
        elif player.participant.vars['car'] == 'Luxury':
            attributes_list = {
                'A': attributes_listA_large,
                'B': attributes_listB_large,
                'C': attributes_listC_large,
                'D': attributes_listD_large,
                'E': attributes_listE,
            }

        try:
            if block == 'E':
                attributes = attributes_listE[trial_number - 1]
            else:
                # Retrieve the attributes_list for the given block
                current_attributes_list = attributes_list[block]
                if not current_attributes_list:
                    print("DEBUG: current_attributes_list is empty. Available blocks:", attributes_list.keys())
                    raise KeyError(f"Block {block} not found in attributes_list")

                # Retrieve the attributes for the given trial_number
                attributes = current_attributes_list[trial_number - 1]
        except KeyError:
            print("DEBUG: KeyError occurred. Available blocks:", attributes_list.keys())
            raise

        keys_list = list(attributes.keys())
        random.shuffle(keys_list)
        shuffled_attributes = {key: attributes[key] for key in keys_list}

        return {
            "attributes": shuffled_attributes,
            "current_task": trial_number,  # Set current_task to the extracted trial_number
            "block": block,  # Include the block information
            "block_text": block_text,  # Include the block-specific text,
            "is_first_trial_of_block": is_first_trial_of_block,
            "completed_block": completed_block,
            "policy_block": policy_block,
            "product_first": product_first,
            "product_second": product_second,
            "first_block_was_policy": first_block_was_policy,
            "product_block": product_block,
        }

    def live_method(player, data):
        player.store_tracking_data(data)

    def store_tracking_data(self, data):
        pass


# Page sequence
page_sequence = [TaskPage]