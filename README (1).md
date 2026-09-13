# NYC Historical Voter Turnout (Council Districts) — Three Data Questions

## Why I Chose This Dataset
I chose the NYC Open Data Historical Voter Turnout dataset because it's real, local (NYC),
and directly relevant to civic life: each row represents the voter turnout for one
geographic area in one election, and the columns describe how many people voted, didn't
vote, or weren't eligible, along with the resulting turnout rate. The original file
contained ~47,000 rows, most of them at the very granular "Election District" level
(44,000+ rows), so I filtered it down to just the "Council District" rows (935 rows,
covering 51 council districts across 19 elections from 2017–2024) to keep the dataset
focused and easy to reason about while still meeting the size requirements.

---

## Three Data Questions

# Question: How many Council District election records are General Elections vs Primary Elections?
#general_count = 0
#primary_count = 0
#
#for row in councilDistricts:
#    if "General" in row["Election"]:
#        general_count += 1
#    else:
#        primary_count += 1
#
#print("General:", general_count, "Primary:", primary_count)
#output: General: 408 Primary: 527

Why the data structure supports this question:
This works because the dataset is tabular: each row is one district-election result, and
the Election column stores the name of the election as text (e.g. "2024 General Election").
Checking whether that text contains the word "General" lets us split every record into two
categories and count each one.

# Question: How many Council District records are there for each election year?
#year_counts = {}
#for row in councilDistricts:
#    year = row["Year"]
#    year_counts[year] = year_counts.get(year, 0) + 1
#print(year_counts)
#output: 2017: 102, 2018: 153, 2019: 67, 2020: 103, 2021: 102, 2022: 153, 2023: 102, 2024: 153

Why the data structure supports this question:
This works because Year is a single column on every row, and each row is one
district-election observation. Counting how many rows fall under each year value shows how
many elections (and therefore how many district-level results) occurred in that year —
years with more elections (like primaries plus a general) naturally have more rows.

# Question: Within General Election records, how many Council Districts had turnout above 30% vs 30% or below?
#high = 0
#low = 0
#for row in councilDistricts:
#    if "General" in row["Election"]:
#        if float(row["Turnout"]) > 0.30:
#            high += 1
#        else:
#            low += 1
#print("High (>30%):", high, "Low (<=30%):", low)
#output: High (>30%): 202 Low (<=30%): 206

Why the data structure supports this question:
This works because we can filter rows using one column (Election contains "General") and
then summarize a second column (Turnout) within that subset. The dataset's "one row = one
district-election result" structure makes it possible to combine a filter with a numeric
threshold and get category counts within a subset of the data.

---

## What the Data Cannot Answer

A question I might want to answer is: "Which specific voters skipped an election, and why?"
This dataset cannot answer that because it only reports aggregate counts (Voted,
Did_Not_Vote, Not_Eligible_to_Vote) per geographic area per election — there are no
individual-level records, demographics, or reasons for not voting. The data also can't tell
us anything about the same person's behavior across multiple elections, since council
district boundaries and eligible populations are reported in bulk, not tied to individuals.
It would be misleading to assume that a low turnout percentage means residents don't care
about voting; it could just as easily reflect registration barriers, redistricting changes
between years, or an off-cycle/low-salience election with fewer contested races.
