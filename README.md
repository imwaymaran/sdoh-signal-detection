# SDOH Signal Detection

> NLP pipeline to detect Social Determinants of Health (SDOH) signals in user messages.

## Overview

Brief description of the problem and why it matters.

## Problem Statement

What SDOH is, why detecting it in informal text matters,
and what this project specifically does.

## Domains

This project detects the following adverse Social Determinants of Health:

| Domain | Description |
| -------- | ------------- |
| Employment | Unemployment, underemployment, disability |
| Family Violence | Physical, emotional, or psychological abuse within family or intimate partner relationships |
| Food Insecurity | Inability to afford food, hunger, reliance on food assistance |
| Housing Insecurity | Financial instability, homelessness, unstable living situation |
| Transportation | Distance barriers, lack of transport resources |

## Dataset

All data is labeled at two levels:

- **SDOH flag** (`sdoh`): 1 if any SDOH signal is present, 0 otherwise
- **Domain flag** (per domain): binary label for each of the 5 domains

### Data Sources

Data is collected from two sources:

**1. Synthetic Data**
Generated using a free LLM API. Prompts were designed to produce informal,
emotionally authentic messages reflecting adverse SDOH signals across all 5 domains.
Synthetic data was used to ensure class balance and cover linguistic patterns
underrepresented in scraped data.

**2. Reddit (Scraped)**
Collected from domain-relevant subreddits using the Reddit public JSON API.

| Domain | Subreddits |
| -------- | ------------ |
| Employment | r/unemployment, r/povertyfinance, r/Assistance |
| Family Violence | r/domesticviolence, r/survivorsofabuse, r/abusiverelationships |
| Food Insecurity | r/foodpantry, r/povertyfinance, r/Assistance |
| Housing Insecurity | r/homeless, r/eviction, r/poverty |
| Transportation | r/NoCarLife, r/transit, r/povertyfinance |

### Annotation Guidelines

A fragment is labeled positive for a domain if it contains a signal of adverse
social circumstance related to that domain. Labels reflect the presence of a
problem, not merely a mention.

| Domain | Positive signal examples |
| -------- | -------------------------- |
| Employment | Job loss, inability to work, financial stress tied to employment status |
| Family Violence | Abuse, fear of partner or family member, feeling unsafe at home |
| Food Insecurity | Skipping meals due to cost, relying on food banks, inability to afford food |
| Housing Insecurity | Eviction, homelessness, inability to pay rent, unstable living situation |
| Transportation | Missing appointments due to transport, cannot afford transit, distance as barrier |

### Data Collection Process

#### Reddit Data

Raw Reddit posts were processed as follows:

1. Posts with empty or removed body text were discarded
2. Posts shorter than 50 words were discarded
3. Relevant fragments were manually selected from qualifying posts
4. Each fragment was manually labeled at both the SDOH and domain level

#### Synthetic Data

### Dataset Statistics (to be filled after data collection)

## Methodology

### Text Preprocessing

### Model Architecture

### Training

### Evaluation

## Results (to be filled)

## Project Structure

## Setup & Installation

## Usage

## Limitations & Future Work

## References
