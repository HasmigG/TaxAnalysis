# TaxAnalysis
Group Project - 3

Data source:
https://www.irs.gov/statistics/soi-tax-stats-individual-income-tax-statistics-2021-zip-code-data-soi-0

Documentation: https://ucivirtdatapt-ddm6542.slack.com/files/U069P0W3TGS/F06TDKJKDS7/21zpdoc.docx

Peoject Overview: 

  We began this project with the intention of visualizing what tax payers at different income levels donated to charity, over the span of 9 years. As we dug into the data, a very obvious change became apparent, which changed the focus of the project, although the purpose remains the same. How do people in different income brackets donate to charity? What outside influences might cause those behaviour to change? 
  In order to use and interact with this project, you will need to read this documentation and interact with the website that is rendered by our code. It is important to understand how our data is represented and formated. Although our columns will not be visible on the website we have created, they do run the backend, so here is a brief outline of what they represent:
  year- 2012 to 2021
  State- all 50 are represented
  new_agi_stub - this is the division of income brackets that the IRS has set up to determine tax         liability:
                    1 = $1 under $25,000
                    2 = $25,000 under $50,000
                    3 = $50,000 under $75,000
                    4 = $75,000 under $100,000
                    5 = $100,000 under $200,000
                    6 = $200,000 or more
  Returns - total number of returns (for a given state, by an agi_stub)
  Single - number of tax returns filed under the status single
  Joint - number of tax returns filed under the status joint
  Head of Household - number of tax returns filed under the status is head of household
  AGI_Amt - adjusted gross income of filer
  Itemized_Ded_Returns - number of returns that were itemized
  Itemized_Ded_Amt - total dollars, in thousands 
  Charitable_retuns - number of filings that contained charitable donations
  Charitable_Amt - total dollars, in thousands

  There were two years that tax payers were allowed to claim charitable contributions even if they filed a standard return, but that contribution was capped at $500. This information is captured in the columns: Std_Ded_Charity_Returns, Std_Ded_Charity_Amt, Std_Ded_Returns, and Std_Ded_Amt. These are comperable to the Itemized columns, but only have data for 20/21.

  The ethical considerations that were made in this project began with the IRS. Because the data was compiled using individual tax returns, and it was seperated by zipcode in its origional format, care had to be taken to protect the privacy of individuals. It is conceivable, in smaller counties, that if the entire dataset were released, individual identities (and therefore incomes) of outliers could be determined. Therefore, when there were less than one hundred returns were filed in a zipcode, these were pushed to an aggregate column labeled 99999, whcih we compleatly eliminated from our data. Similarly, in cases where there were less than 20 returns in a particular AGI_stub, that group was eliminated for that year, in that zipcode. Further, if one return made up more than a set percentage of the total for an AGI_stub, that return was eliminated from that group. The percentage used as a threshold was not released, to further protect the privacy of taxpayers. 

  Sources and help:
  
