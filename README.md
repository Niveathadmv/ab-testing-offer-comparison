## ab-testing-offer-comparison
### A/B Test: Which Offer Gets More Customers to Buy?
I wrote about A/B testing for small businesses in this article: [A/B Testing for Sales Funnel Optimization: Product Offers and Pricing Strategies for Small Businesses](https://medium.com/technology-hits/a-b-testing-for-sales-funnel-optimization-product-offers-and-pricing-strategies-for-small-734340ff5465)

This repo is the hands-on part. I ran a small A/B test in Python on made-up data to show how it works.

## The Problem

Say you run an online jewellery store and want more visitors to buy. You can't decide between two offers:

Offer A (what you run today): 20% off on orders above ₹1,000
Offer B (the new idea): Buy 2, Get 1 Free

Sales go up and down from day to day just by chance, so a few days of sales won't tell us which offer is better. An A/B test can help. You show each offer to a random half of the visitors, then compare how many in each half bought.

The question I wanted to answer: does Offer B get more visitors to buy or is the difference just a luck?

## The Data

The data is made up. generate_data.py creates 28,000 visitors and randomly shows each one Offer A or Offer B. I set the real buying rates myself (3.0% for A, 3.6% for B), so I could check that the test finds the difference I introduced.

Each row has a visitor id, the offer they're part of and purchased (1 if they bought, 0 if not).

## What I Did
Worked out how many visitors I need (sample_size.py). To spot a rise from 3.0% to 3.6%, I need about 13,900 visitors in each group.
Created the data (generate_data.py).
Compared the two groups with a z-test for proportions (ab_test.py). It gives a p-value and a likely range for the improvement.
Made a bar chart (chart.py).
Results

<img width="772" height="596" alt="image" src="https://github.com/user-attachments/assets/2d42523d-e855-4c82-be04-117bf47134db" />


Offer A: 444 buyers out of 14,066 visitors (3.16%)
Offer B: 508 buyers out of 13,934 visitors (3.65%)

B is ahead by about 0.5 percentage points. The p-value is 0.024, which is below 0.05, so the gap is probably not luck. The real improvement is likely somewhere between 0.06 and 0.92 percentage points.

Offer B performs better, but we’re not sure exactly how much better. The improvement could be small or more noticeable.

What a Business Would Do With This

Go with Offer B if the goal is more buyers. Before rolling it out, I'd also check profit, since Buy 2 Get 1 Free is a bigger discount than 20% off.

## Note:
* The data is made up, so the numbers only show how the method works.
* I only looked at how many visitors bought but not revenue or profit.
* It's one test. A real test should run for full weeks and be checked for things like seasonality.

## Where this works

Any time you have two versions and a yes/no result: prices, shipping offers, email subject lines, landing pages, sign-up forms.
