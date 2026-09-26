\# Business Entity Resolution



This project is developed for the Amazon ML Challenge 2026.



\## Problem



The goal is to identify matching business records across multiple noisy data sources.



The challenge contains:



\- Source 1: Reference business entities

\- Source 2: Noisy business records

\- Source 3: Noisy business records



The task is to identify which Source 2 and Source 3 records correspond to each Source 1 entity.



\## Project Pipeline



The overall pipeline consists of:



1\. Data Preprocessing / ETL

2\. Blocking / Candidate Generation

3\. Feature Engineering and Matching

4\. Final Matching Results

5\. Candidate Pair Generation



\## Preprocessing



The preprocessing stage handles all six source files:



```text

train\_source1.tsv

train\_source2.tsv

train\_source3.tsv



test\_source1.tsv

test\_source2.tsv

test\_source3.tsv

