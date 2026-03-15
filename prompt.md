# Prompt to Build a Python AI Lead Generation Agent

## Project Goal

Write a complete Python program that acts as an automated lead generation agent for a developer who builds and sells AI agents to businesses. The purpose of the program is to automatically go online, discover potential companies that may benefit from AI automation solutions, collect publicly available contact information, and save the discovered leads in a structured dataset that can later be used for outreach or marketing campaigns.


## General Requirements

The program must be written entirely in Python and must only use free and open-source libraries. It must not rely on paid APIs, paid lead databases, or premium SaaS tools. The system should operate using publicly accessible information from websites and directories. The code should be clean, readable, modular, and well commented so that another developer can easily understand and extend the project.

---

## Target Industries

The agent should focus on industries that are likely to benefit from AI automation services. Examples include consulting firms, law firms, recruitment agencies, marketing agencies, SaaS startups, software companies, small technology firms, and businesses that manage large volumes of documents or data. These industries often have workflows that can be improved with AI assistants, document analysis systems, knowledge base search tools, or automation agents.

---

## Lead Discovery Sources

The program should search for businesses using publicly available online sources. Examples of such sources include business listing services like Google Maps, startup directories, and publicly listed company websites. The system should gather initial business listings that include at least the company name, location if available, and the company website URL. If possible, the program should also attempt to find a contact page link from the company website.

---

## Website Crawling and Data Extraction

Once a company website is discovered, the program should automatically visit the website and scan the HTML content of the homepage and other important pages such as the contact page, about page, or team page. The goal is to identify publicly available contact information and contextual details about the company. The system should analyze the page content and attempt to extract email addresses using regular expressions.

---

## Email Detection

When scanning website content, the program should search for email patterns within the text. If multiple email addresses are found, all of them should be stored. However, the program should prioritize general business contact emails such as “info”, “contact”, “hello”, “sales”, or “support” because these are more likely to reach the correct department. The program should ensure that duplicate email addresses are removed from the dataset.

---

## Additional Company Information

In addition to extracting emails, the program should attempt to collect other useful information from the website. This includes the company description, services offered, and any text that indicates the type of business or industry. This information will help evaluate whether the company might benefit from AI automation tools.

---

## Python Libraries to Use

The agent should rely on widely used open-source Python libraries. The program should use libraries such as:

* Requests (Python library) for downloading web pages
* BeautifulSoup for parsing HTML content
* Selenium if interaction with dynamic web pages is required
* Pandas for organizing and storing collected lead data

These libraries will help the program gather and process information efficiently.

---

## Lead Processing Workflow

The program should include a main function that loops through many discovered businesses. For each business, the agent should collect the website URL, crawl the website pages, extract email addresses, gather company information, and store the results in a structured dataset. The workflow should repeat continuously or for a large batch of companies to gradually build a database of potential clients.

---

## Lead Dataset Structure

The collected lead dataset should include the following fields:

* company name
* company website URL
* email address or addresses
* company location if available
* short company description
* industry or service category
* lead priority or potential score

This structure ensures the data is useful for later outreach and marketing.

---

## Data Storage

After processing each batch of companies, the program should save the collected leads in structured files. The system should export the dataset in both CSV and JSON formats so that it can easily be used with spreadsheets, CRM systems, or email marketing tools.

---

## Lead Qualification

The agent should include a simple filtering or scoring step that analyzes the company website text to determine whether the company is a strong potential client for AI automation. This can be done by searching for keywords related to consulting services, legal work, recruiting, marketing, document processing, analytics, or data management. If such keywords appear frequently, the program should mark the lead as a high-potential lead.

---

## Error Handling

The program must include error handling so that it continues running even if a website fails to load or returns an error. If a page cannot be accessed or no email is found, the agent should skip that entry and move on to the next company instead of crashing.

---

## Polite Web Scraping

To reduce the risk of being blocked by websites, the program should implement polite scraping behavior. This includes adding delays between requests, avoiding excessive request rates, and respecting normal browsing patterns. These measures help ensure the agent runs smoothly over time.

---

## Expandability

The code should be written in a modular structure so that additional features can be added later. Future improvements might include AI analysis of company websites, automated email outreach generation, scheduled daily lead discovery, or integration with a customer relationship management system.

---

## Final Result

The final output of the program should be a continuously growing list of potential business leads that can be used to sell AI automation services. The system should function as a lightweight lead generation tool that runs locally and gradually builds a valuable contact database without relying on paid services.
