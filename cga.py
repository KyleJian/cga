Python 3.12.3 (v3.12.3:f6650f9ad7, Apr  9 2024, 08:18:47) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> """
... At the command line, only need to run once to install the package via pip:
... 
... $ pip install google-generativeai
... """
... 
... from pathlib import Path
... import hashlib
... import google.generativeai as genai
... 
... genai.configure(api_key="AIzaSyDpx59kKHDposjMH0qnjxsMljCGxQEF-HQ")
... 
... # Set up the model
... generation_config = {
...   "temperature": 1,
...   "top_p": 0.95,
...   "top_k": 0,
...   "max_output_tokens": 8192,
... }
... 
... safety_settings = [
...   {
...     "category": "HARM_CATEGORY_HARASSMENT",
...     "threshold": "BLOCK_MEDIUM_AND_ABOVE"
...   },
...   {
...     "category": "HARM_CATEGORY_HATE_SPEECH",
...     "threshold": "BLOCK_MEDIUM_AND_ABOVE"
...   },
...   {
...     "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
...     "threshold": "BLOCK_MEDIUM_AND_ABOVE"
...   },
...   {
...     "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
...     "threshold": "BLOCK_MEDIUM_AND_ABOVE"
...   },
]

model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

uploaded_files = []
def upload_if_needed(pathname: str) -> list[str]:
  path = Path(pathname)
  hash_id = hashlib.sha256(path.read_bytes()).hexdigest()
  try:
    existing_file = genai.get_file(name=hash_id)
    return [existing_file.uri]
  except:
    pass
  uploaded_files.append(genai.upload_file(path=path, display_name=hash_id))
  return [uploaded_files[-1].uri]

def extract_pdf_pages(pathname: str) -> list[str]:
  parts = [f"--- START OF PDF ${pathname} ---"]
  # Add logic to read the PDF and return a list of pages here.
  pages = []
  for index, page in enumerate(pages):
    parts.append(f"--- PAGE {index} ---")
    parts.append(page)
  return parts

convo = model.start_chat(history=[
  {
    "role": "user",
    "parts": ["Hello!"]
  },
  {
    "role": "model",
    "parts": ["Hello! I am Gemini, an AI assistant designed to support your research on committee meetings and bills related to Senator Saud Anwar's work in the Connecticut General Assembly. How can I assist you today?"]
  },
  {
    "role": "user",
    "parts": extract_pdf_pages("<path>/document0.pdf")
  },
  {
    "role": "user",
    "parts": extract_pdf_pages("<path>/document1.pdf")
  },
  {
    "role": "user",
    "parts": extract_pdf_pages("<path>/document2.pdf")
  },
  {
    "role": "user",
    "parts": extract_pdf_pages("<path>/document3.pdf")
  },
  {
    "role": "user",
    "parts": extract_pdf_pages("<path>/document4.pdf")
  },
  {
    "role": "user",
    "parts": extract_pdf_pages("<path>/document5.pdf")
  },
  {
    "role": "user",
    "parts": extract_pdf_pages("<path>/document6.pdf")
  },
  {
    "role": "user",
    "parts": extract_pdf_pages("<path>/document7.pdf")
  },
  {
    "role": "model",
    "parts": ["## Analyzing SB-2: An Act Concerning Artificial Intelligence\n\nThe document you've provided appears to be legislative documents related to **Senate Bill 2 (SB-2) of the 2024 Connecticut General Assembly session**, specifically focusing on artificial intelligence (AI).  Let's break down the information and explore how it relates to Senator Saud Anwar's responsibilities.\n\n**Key Components of SB-2:**\n\n* **Regulation of AI Developers and Deployers:** The bill establishes a framework to regulate AI, requiring developers and deployers of high-risk AI systems to exercise \"reasonable care\" to prevent algorithmic discrimination. This includes conducting impact assessments, implementing risk management programs, and disclosing potential risks to consumers and the Attorney General.\n* **CHRO Enforcement and Penalties:** Failure to comply with these regulations could be considered a discriminatory practice, with enforcement by the Commission on Human Rights and Opportunities (CHRO) and potential fines ranging from $3,000 to $7,000 per violation.\n* **Transparency and Disclosure:**  The bill emphasizes transparency by requiring AI systems to disclose their artificial nature to users and mandating developers and deployers to make summaries of their AI systems publicly accessible. \n* **Synthetic Digital Content:** Specific provisions address AI systems generating or manipulating synthetic digital content, requiring labeling and disclosures to prevent misinformation and protect consumers.\n* **Additional Measures:**  \n    * **AI Advisory Council:**  A 23-member council is established to study AI regulations, promote dialogue between stakeholders, and advise on legislation and economic development strategies related to AI.\n    * **Unlawful Dissemination of Synthetic Intimate Images:**  The bill creates a new criminal offense for the non-consensual dissemination of synthetically generated intimate images.\n    * **Elections and Deceptive Media:**  Distributing deceptive media generated by AI with the intent to influence elections is prohibited, with exceptions for disclaimers and parody.\n    * **State Agency AI Study and Pilot Programs:** State agencies are required to study the potential of generative AI to improve efficiency and propose pilot projects.\n    * **State Employee Training:** DAS will develop and provide training to state employees on the responsible use of generative AI tools. \n    * **Workforce Development:** The Office of Workforce Strategy will incorporate AI training into existing programs and promote access to broadband internet.\n    * **Connecticut Citizens Academy and Certificate Programs:**  The Board of Regents will establish educational programs to promote AI literacy and workforce development.\n    * **DECD Collaborations and Grant Programs:** The Department of Economic and Community Development will collaborate with various entities to promote AI research, development, and economic growth through grants and initiatives.\n    * **Health Care AI Study:** The Department of Public Health will study and recommend governance standards for AI use in healthcare.\n\n**Relevance to Senator Saud Anwar:**\n\nSenator Anwar's role in the Public Health Committee and the Appropriations Committee makes this bill particularly relevant to his responsibilities. \n\n* **Public Health Implications:** The bill's focus on AI in healthcare, including the study on governance standards and pilot programs for hospitals, aligns directly with the Public Health Committee's purview.  Senator Anwar could leverage his position to ensure responsible and ethical AI implementation in healthcare, prioritizing patient safety and positive health outcomes.\n* **Appropriations and Funding:** The bill's fiscal impact, including costs for additional staff at various agencies and funding for grant programs, necessitates scrutiny from the Appropriations Committee.  Senator Anwar could play a crucial role in evaluating the financial implications of SB-2 and ensuring responsible allocation of resources.\n* **Workforce Development:** As a member of the Appropriations Committee, Senator Anwar could contribute to discussions on funding for workforce development initiatives related to AI. This includes supporting programs that equip Connecticut residents with the skills and knowledge to thrive in an AI-driven economy.\n\n**Further Research:**\n\nTo delve deeper into SB-2 and its implications, I encourage you to explore the following resources:\n\n* **Connecticut General Assembly Website:** Access the full text of SB-2, track its progress through the legislative process, and review committee reports and public hearing testimonies.\n* **Senator Saud Anwar's Official Website:** Stay updated on Senator Anwar's stance on SB-2 and related AI issues.\n* **Public Health Committee Website and YouTube Channel:**  Follow the committee's activities and discussions on AI in healthcare.\n* **Appropriations Committee Live Stream and Archives:**  Observe the committee's deliberations on the fiscal impact of SB-2 and other relevant bills.\n\nI am here to assist you further in navigating these resources and exploring any specific aspects of SB-2 that interest you.  Please feel free to ask any further questions you may have."]
  },
  {
    "role": "user",
    "parts": ["Please provide information on sb9"]
  },
  {
    "role": "model",
    "parts": ["## Investigating SB 9 2023: Unveiling the Details\n\nUnfortunately, due to my knowledge cutoff date being November 2023, I don't have access to real-time information on SB 9 2023. However, I can guide you through the process of researching the bill using the resources we discussed previously. \n\n**Here's a step-by-step approach to finding information on SB 9 2023:**\n\n**1. Connecticut General Assembly Website:**\n\n* **Search:**  Go to the CGA website (https://www.cga.ct.gov/) and use the search bar to look for \"SB 9 2023\".  This should lead you to the bill's dedicated page.\n* **Bill Details:** On the bill's page, you can access its full text, including the title, sponsors, summary, and legislative history. This will provide a comprehensive understanding of the bill's purpose and its journey through the legislative process. \n* **Bill Status:** Look for the \"Bill Status\" section to determine the current stage of SB 9. It will indicate if the bill is still in committee, awaiting action, or has been passed or rejected.\n* **Committee Information:** Identify the committee(s) to which SB 9 was referred. Each committee page will likely have agendas, minutes, and potentially recordings of meetings and hearings related to the bill. This will offer valuable insights into the discussions and deliberations surrounding SB 9.\n\n**2. Senator Saud Anwar's Website:**\n\n* **Search or News Section:** Visit Senator Anwar's official website (https://www.saudanwar.com/about) and explore the search function or news section. Look for any mentions of SB 9, which may reveal his position and involvement with the bill.\n* **Contact:** If you can't find the information you need, consider reaching out to Senator Anwar's office directly through the contact information provided on his website.\n\n**3. Public Health Committee Resources:**\n\n* **Website and YouTube:** If SB 9 was referred to the Public Health Committee, visit their website and YouTube channel. Look for agendas, minutes, and recordings of meetings related to SB 9 for a deeper understanding of the discussions and testimonies.\n\n**Additional Strategies:**\n\n* **News Search:** Use online news search engines to find articles mentioning SB 9 2023. This can provide broader context and public perspectives on the bill.\n* **Social Media:** Explore social media platforms like Twitter or Facebook using relevant keywords to see if there are any discussions or updates on SB 9.\n\n**Remember, I'm here to help you further analyze any information you find or answer additional questions you might have as you research SB 9 2023.**"]
  },
  {
    "role": "user",
    "parts": ["Hello, I'm conducting research on SB 9 from the 2023 session of the Connecticut General Assembly. Can you provide me with information about the bill's background, its current status, and any related committee meetings or hearings?"]
  },
  {
    "role": "model",
    "parts": ["## Researching SB 9 2023: Let's Explore the Resources\n\nAbsolutely! I can help you delve into the details of SB 9 from the 2023 session.  To comprehensively understand this bill, we can utilize the resources you mentioned:\n\n**1. Connecticut General Assembly Website (https://www.cga.ct.gov/)**\n\n* **Bill Search:** Use the search function to locate SB 9 2023 and access its full text, including the bill's title, sponsors, and legislative history. This will provide insights into the bill's intent and its journey through the legislative process.\n* **Bill Status:**  The bill status page will reveal the current stage of SB 9, such as whether it's in committee, awaiting action, or has been passed or rejected.\n* **Committee Information:** Identify the committee(s) to which SB 9 was referred. The committee pages often contain agendas, minutes, and recordings of meetings and hearings related to the bill, offering valuable insights into the discussions and deliberations surrounding SB 9.\n\n**2. Senator Saud Anwar's Official Website (https://www.saudanwar.com/about)**\n\n* **News and Updates:** Check for any press releases, statements, or blog posts from Senator Anwar that mention SB 9.  This might reveal his stance on the bill and his involvement in its progression.\n* **Contact Information:** If you require more specific information or clarification, consider reaching out to Senator Anwar's office directly.\n\n**3. Public Health Committee Website (https://www.cga.ct.gov/ph/) and YouTube Channel (https://www.youtube.com/@cga-publichealthcommittee6579)**\n\n* If SB 9 was referred to the Public Health Committee, these resources will be crucial. Explore the committee's agenda and minutes to identify relevant meetings and hearings.  The YouTube channel might contain recordings of these sessions, allowing you to gain firsthand understanding of the discussions and testimonies related to SB 9. \n\n**Additional Tips:**\n\n* **Keywords:**  While researching, utilize relevant keywords like the bill's title, subject matter, and sponsors to find related information. \n* **News Articles:** Search online news sources for articles that mention SB 9. This can offer broader context and perspectives on the bill's impact and public reception.\n\n**Follow-Up:**\n\nOnce you've gathered information from these sources, feel free to ask me any further questions you may have. I can help you analyze the information, understand the legislative process, or explore related bills and topics."]
  },
  {
    "role": "user",
    "parts": ["summarize this: https://www.cga.ct.gov/asp/cgabillstatus/cgabillstatus.asp?selBillType=Bill&which_year=2023&bill_num=9"]
  },
  {
    "role": "model",
    "parts": ["## Summarizing CT SB 9 2023 Bill Status: A Snapshot\n\nUnfortunately, I cannot directly access and summarize the content of external websites, including the specific URL you provided. However, I can guide you on how to interpret the information typically found on the Connecticut General Assembly's bill status page.\n\n**Here's what you can generally expect to find on a bill status page and how to summarize it:**\n\n**1. Bill Identification:**\n\n* **Bill Number and Title:** This will clearly identify the bill as \"SB 9\" and provide its official title, giving you a concise understanding of the bill's subject matter. \n* **Sponsors:**  The names of the legislators who introduced the bill will be listed, offering insights into its origins and potential support base.\n\n**2. Current Status:**\n\n* **Location:** This will indicate where the bill currently stands in the legislative process. It might state that the bill is in a specific committee, awaiting action, or has been passed or rejected. \n* **Last Action:** This section provides information about the most recent activity related to the bill, such as a committee hearing date, vote result, or action taken by either chamber of the General Assembly.\n\n**3. Legislative History:**\n\n* **Actions:** A chronological list of actions taken on the bill, including committee referrals, public hearings, amendments, and votes. This offers a comprehensive overview of the bill's journey through the legislative process.\n* **Dates:** The dates associated with each action provide a timeline of the bill's progress. \n\n**4. Additional Resources:**\n\n* **Bill Text:** A link to access the full text of the bill, allowing you to delve into the details of its provisions.\n* **Fiscal Note:** If available, this document analyzes the potential financial impact of the bill on the state budget.\n* **Public Hearing Testimony:** Transcripts or recordings of testimonies given during public hearings on the bill, offering diverse perspectives and insights.\n\n**How to Summarize:**\n\n1. **Start by identifying the bill and its current status.**  For example, \"SB 9, An Act Concerning [Bill Topic], is currently [in committee/awaiting action/passed/rejected].\"\n2. ** Briefly mention the last action taken on the bill and the date.**\n3. ** If relevant, provide a concise overview of the bill's main objectives or key provisions.**\n4. ** Consider including information about the bill's sponsors and any significant support or opposition it has received.** \n\n**Remember, I am here to assist you further in interpreting any legislative jargon, understanding the bill's implications, or exploring related information. Feel free to ask any additional questions you may have!**"]
  },
  {
    "role": "user",
    "parts": extract_pdf_pages("<path>/document8.pdf")
  },
  {
    "role": "model",
    "parts": ["## CT SB 9 2023: An Act Concerning Health and Wellness for Connecticut Residents \n\nThis act encompasses a wide range of provisions aimed at improving healthcare access, quality, and workforce development in Connecticut. Here's a breakdown of the key areas addressed:\n\n**Reproductive Healthcare:**\n\n* **Access to Assisted Reproductive Technology:** The act prohibits restrictions on individuals accessing assisted reproductive technology and ensures their rights regarding reproductive genetic materials.\n\n**Contraceptive Access:**\n\n* **Medicaid Coverage for Long-Acting Reversible Contraceptives:** Medicaid reimbursement criteria will be adjusted to cover same-day access to long-acting reversible contraceptives at federally qualified health centers.\n\n**Substance Use Disorder and Harm Reduction:**\n\n* **Harm Reduction Center Pilot Program:**  A pilot program will establish harm reduction centers in three municipalities to offer support services and resources for individuals with substance use disorder, including fentanyl test strips and referrals to treatment.\n* **Opioid Antagonist Bulk Purchase Fund:** This fund will support the distribution of opioid antagonists to eligible entities and emergency medical services personnel for overdose prevention and treatment.\n* **Opioid Prescription Limits:** The act sets limits on the initial prescription of opioid drugs for both adults and minors, with exceptions for certain medical conditions and treatments.\n* **Support for Caregivers with Substance Use Disorder:**  The act directs relevant state agencies to evaluate existing programs and develop a plan for expanded treatment and support services for caregivers struggling with substance use disorder.\n* **Childcare Support for Parents in Treatment:**  A plan will be established to allow parents undergoing substance use disorder treatment to access childcare support and subsidies.\n* **Supportive Housing Access:**  A report will be generated on access to supportive housing for pregnant and parenting individuals with substance use disorder.\n* **Substance Use Treatment Access for Parents Involved with DCF:** A report will assess access to treatment for parents with substance use disorder whose children are receiving services from the Department of Children and Families, with the aim of preventing child removal and supporting reunification.\n* **Substance Use Disorder Treatment Services for Pregnant and Parenting Persons:** Existing services and needs for additional services will be evaluated.\n* **Child Safety and Caregiver Substance Use:** The Department of Children and Families will report on its efforts to address child safety concerns when a caregiver has a substance use disorder.\n* **Opioid Settlement Fund Committee Expansion:** The committee overseeing the Opioid Settlement Fund will include additional members representing individuals with lived experience and those supporting children affected by the opioid crisis. \n\n**Healthcare Workforce Development:**\n\n* **Promoting Health Care Careers:** The Commissioner of Education, in collaboration with the Chief Workforce Officer, will develop a plan to encourage students to pursue careers in healthcare.\n* **Health Care Workforce Expansion Working Group:** This group will study and recommend strategies to address healthcare workforce shortages, focusing on nurses and nurse aides.\n* **Adjunct Professor Incentive Grant Program:** The Office of Higher Education will offer grants to incentivize experienced healthcare providers to become adjunct professors at public institutions of higher education.\n* **Personal Care Attendants Career Pathways Program:** This program aims to improve the quality of care and incentivize recruitment and retention of personal care attendants by offering career pathways and training opportunities.\n\n**Other Provisions:**\n\n* **Physician Credentialing and Covenants Not to Compete:** The act restricts hospitals from requiring board certification for initial privileges and prohibits enforcement of non-compete agreements under certain circumstances for physicians, advanced practice registered nurses, and physician assistants.\n* **Physical Therapy Licensure Compact:** Connecticut will join the Physical Therapy Licensure Compact, facilitating interstate practice for physical therapists and physical therapist assistants.\n* **Podiatric Scope of Practice Working Group:** This group will advise on the scope of practice for podiatrists related to surgical procedures.\n* **Advanced Practice Registered Nurse Licensure:** The act modifies the requirements for licensure as an advanced practice registered nurse and allows for licensure by endorsement under certain conditions.\n* **Splash Pad and Spray Park Signage:**  Facilities with recirculated water must post signage warning of potential health risks from ingestion.\n* **Licensed Practical Nursing Pilot Programs:** Public and independent institutions of higher education can apply to establish pilot programs for licensed practical nursing education and training.\n* **Clinical Training Reciprocity Agreements:** The Office of Higher Education may enter agreements with neighboring states to allow for student clinical rotations across state lines.\n* **Home Health Care for Victims of Gun Violence:** A subcommission or advisory group will be established to address challenges and improve access to home healthcare for victims of gun violence. \n* **Maternal Mental Health Toolkit:** The Department of Public Health will develop a toolkit to provide information and resources on maternal mental health for healthcare professionals and new parents. \n* **Hospital Staff Training:**  Hospitals must provide training to staff on dementia, implicit bias, and perinatal mood and anxiety disorders. \n* **Emergency Department Crowding Task Force:** This task force will study and recommend solutions to alleviate emergency department crowding and bed shortages.\n* **Healthcare Career Magnet School Program:**  The feasibility of establishing an interdistrict magnet school program for healthcare professions will be explored.\n* **Communication Access for Deaf and Hard of Hearing Individuals:** A study will evaluate and recommend improvements for communication access to medical providers for deaf, hard of hearing, and deafblind individuals.\n* **Dental Assistant X-ray Competency Assessment:** The University of Connecticut School of Dental Medicine will develop a competency assessment for dental assistants to ensure safe and proper administration of dental x-rays.\n* **Epinephrine Administration by Emergency Medical Services Personnel:**  All emergency medical services personnel will be trained and authorized to administer epinephrine using appropriate methods.\n* **Electronic Medical Records Sharing:**  Institutions must provide electronic copies of patient medical records to other institutions upon request, with certain exceptions. \n* **Radiologic Technologist, Nuclear Medicine Technologist, and Respiratory Care Practitioner Shortage Task Force:** This task force will study the shortage of these healthcare professionals and develop a plan to address it.\n* **Fingerprint-Based Criminal History Records Checks:**  The act mandates these checks for individuals applying for licensure as physicians and psychologists.\n\n**Overall, this act represents a significant effort to improve the health and well-being of Connecticut residents by addressing various aspects of healthcare access, quality, workforce development, and public health concerns.**"]
  },
  {
    "role": "user",
    "parts": extract_pdf_pages("<path>/document9.pdf")
  },
  {
    "role": "model",
    "parts": ["## Proposed Bill No. 2 (2024 Session): Supporting AI Advancement and Protection\n\nThis proposed bill, introduced by a group of Connecticut senators, aims to address the growing prominence of Artificial Intelligence (AI) by allocating increased funding to several key areas:\n\n**1. Consumer Protection:**\n\n* The bill proposes increased funding for the Office of the Attorney General to enhance efforts in protecting consumers from potential harms associated with AI use. This could involve investigating and addressing issues like algorithmic bias, privacy violations, and deceptive practices within AI systems.\n\n**2. Workforce Development:**\n\n* Increased funding is proposed for the Technology Talent Advisory Committee to support training initiatives related to AI. This would equip Connecticut's workforce with the necessary skills and knowledge to thrive in an AI-driven economy. \n* The bill also suggests additional funding for the Board of Regents for Higher Education to expand community college seminar programs for workers. These programs could focus on AI literacy, technical skills, and responsible AI development and deployment.\n\n**3. Education and Training:**\n\n* The proposed bill allocates increased funding to Regional Education Service Centers to provide training to school districts on utilizing AI in educational settings. This could involve responsible implementation of AI tools, data privacy protection for students, and integrating AI into curricula.\n\n**Overall Goal:**\n\nThe proposed bill seeks to achieve a balanced approach to AI advancement in Connecticut by:\n\n* **Mitigating potential risks and harms to consumers through strengthened consumer protection efforts.**\n* **Preparing the workforce for the challenges and opportunities of an AI-driven future through enhanced training initiatives.**\n* **Promoting responsible and effective utilization of AI in educational settings.**\n\n**It's important to note that this is a proposed bill, and its provisions may undergo changes or revisions as it progresses through the legislative process.**"]
  },
])

convo.send_message("YOUR_USER_INPUT")
print(convo.last.text)
for uploaded_file in uploaded_files:
