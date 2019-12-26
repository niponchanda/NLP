"""
Script name: segregate_finance_data.py
Description: The script segregate finance data
             from given mail data
author : Nipon Chanda
"""

# importing pandas
import pandas as pd

df = pd.read_csv('AllmailIncludingSpamandTrash.csv')
data = df.dropna(subset=['Date'])
data = data.dropna(subset=['From Name'])
data = data.dropna(subset=['From Address'])
data = data.dropna(subset=['To'])
data = data.dropna(subset=['Subject'])

#saving the dataframe
data.to_csv('filter1.csv')

df = pd.read_csv('filter1.csv', sep=',')
targets = ['Paytm', 'Flipkart', 'Uber Eats', 'PF', 'Bank of Baroda', 'YONO SBI',
           'Reserve Bank of Ind.', 'SBI CARD', 'HDFC Bank', 'Snapdeal', 'Myntra',
           'HDFC Bank Smart Statement', 'Google Pay', 'PhonePe', 'Team Razorpay',
           'TSAI Admin', 'YONO SBI', 'Paytm Mall', 'Paytm Payments Bank',
           'HDFC Bank Debit Card', 'ixigo', 'Acko', 'Zomato', 'Uber Support',
           'Amazon.in', 'Amazon Pay balance', 'Amazon', 'HDFC ERGO Car Insurance',
           'Kotak 811', 'PNB Housing', 'ICICI BANK', 'Uber', 'Kotak Mahindra Bank',
           'HDFC Bank InstaAlerts', 'Team Playo', 'Acko General Insurance',
           'Amazon Business', 'HappyEasyGo', 'Team Razorpay', 'Myntra Updates',
           'HDFC Bank PayZapp', 'ICICI Bank', 'Redwolf', 'HDFC Bank Smart Statement',
           'Snapdeal.com', 'SBI Card', 'SBI', 'Ola', 'HDFC Bank', 'bank']

df2 = df[df['From Name'].str.contains('Uber Receipts')]

for string in range(len(targets)):
    df1 = df[df['From Name'].str.contains(targets[string])]
    df2 = df2.append(df1)
df2.to_csv('finance_filter.csv')