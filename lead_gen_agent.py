import time
import random
from discovery import discover_leads
from crawler import crawl_website
from utils import extract_emails, prioritize_emails, score_lead, save_leads, get_company_description

def main():
    print("--- Starting AI Lead Generation Agent ---")

    # Configuration
    target_industries = [
        "law firm",
        "marketing agency",
        "recruitment agency",
        "consulting firm",
        "SaaS startup"
    ]
    target_locations = ["London", "New York", "San Francisco"]

    # Step 1: Discover Leads
    print(f"Discovering leads for industries: {', '.join(target_industries)}")
    # For demonstration, we'll just pick a subset to avoid too many requests
    discovered_leads = discover_leads(target_industries[:2], target_locations[:1])
    print(f"Discovered {len(discovered_leads)} potential leads.")

    processed_leads = []

    # Step 2: Process each lead
    for i, lead in enumerate(discovered_leads):
        print(f"\n[{i+1}/{len(discovered_leads)}] Processing: {lead['name']} ({lead['website']})")

        try:
            # Polite delay between websites
            if i > 0:
                delay = random.uniform(5, 10)
                print(f"  Waiting {delay:.2f} seconds...")
                time.sleep(delay)

            # Crawl website
            site_data = crawl_website(lead['website'])

            if site_data:
                all_text = site_data['all_text']

                # Extract and prioritize emails
                emails = extract_emails(all_text)
                prioritized_emails = prioritize_emails(emails)

                # Score the lead
                score = score_lead(all_text, lead['industry'])

                # Get description
                description = get_company_description(all_text)

                # Update lead data
                lead_info = {
                    'company_name': lead['name'],
                    'website_url': lead['website'],
                    'emails': prioritized_emails,
                    'location': lead['location'],
                    'description': description,
                    'industry': lead['industry'],
                    'priority_score': score
                }

                processed_leads.append(lead_info)
                print(f"  Found {len(prioritized_emails)} emails. Score: {score}")
            else:
                print(f"  Could not extract data from {lead['website']}")

        except Exception as e:
            print(f"  Error processing {lead['name']}: {e}")
            continue

    # Step 3: Save Results
    if processed_leads:
        save_leads(processed_leads)
        print("\n--- Lead Generation Task Completed ---")
    else:
        print("\n--- No leads were processed successfully ---")

if __name__ == "__main__":
    main()
