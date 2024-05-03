import logging

import few_shots
from config import settings
from constants import SINGLE
from llm import ClassifierLlm


def main():
    logging.basicConfig(level=logging.INFO)
    logging.info("Model path: %s", settings.llm_model_path)

    category = "Industry"
    labels = [
        "Technology",
        "Healthcare",
        "Finance",
        "Manufacturing",
        "Retail",
        "Education",
        "Energy",
        "Agriculture",
        "Other"
    ]

    llm = ClassifierLlm(
        model_path=settings.llm_model_path,
        category=category,
        labels=labels,
        few_shots=few_shots.industry_single,
        classify_type=SINGLE
    )

    queries = [
        "How can virtual reality be used to create more immersive learning experiences?",
        "How are telemedicine appointments impacting healthcare costs?",
        "How is the rise of e-commerce affecting traditional brick-and-mortar stores' financial strategies?",
        "What are the most sustainable manufacturing practices to reduce energy consumption?",
        "How are retailers leveraging artificial intelligence to personalize the customer shopping experience?",
        "Can online education platforms be used to train farmers in new agricultural techniques?",
        "What are the ethical considerations surrounding the use of artificial intelligence in medical diagnosis?",
        "How can blockchain technology improve supply chain transparency in manufacturing?",
        "How can stores use renewable energy sources to power their operations?",
        "What are the challenges of ensuring equitable access to technology in educational settings?",
        "How can advancements in agricultural biotechnology lead to the development of new medicines?",
        "Are there new financial models that can encourage investment in renewable energy projects?  ",
        "How can manufacturers adapt their production lines to meet the changing demands of online retailers?",
        "How can consumers be assured that the food they buy is ethically and sustainably sourced?",
        "How can healthcare professionals be better trained to address the mental health needs of students? ",
        "What are the security risks associated with online financial transactions?",
        "How can technology be used to create more efficient and sustainable agricultural practices?",
        "What are the financial implications of offering buy-now-pay-later options to customers?",
        "How can schools incorporate energy conservation practices into their curriculum? ",
        "Can genetically modified crops be used to improve the nutritional value of food and combat malnutrition?",
        "How can virtual reality be used to create more immersive learning experiences?",
        "How are telemedicine appointments impacting healthcare costs?",
        "How is the rise of e-commerce affecting traditional brick-and-mortar stores' financial strategies?",
        "What are the most sustainable manufacturing practices to reduce energy consumption?",
        "How are retailers leveraging artificial intelligence to personalize the customer shopping experience?",
        "Can online education platforms be used to train farmers in new agricultural techniques?",
        "What are the ethical considerations surrounding the use of artificial intelligence in medical diagnosis?",
        "How can blockchain technology improve supply chain transparency in manufacturing?",
        "How can stores use renewable energy sources to power their operations?",
        "What are the challenges of ensuring equitable access to technology in educational settings?",
        "How can advancements in agricultural biotechnology lead to the development of new medicines?",
        "Are there new financial models that can encourage investment in renewable energy projects?  ",
        "How can manufacturers adapt their production lines to meet the changing demands of online retailers?",
        "How can consumers be assured that the food they buy is ethically and sustainably sourced?",
        "How can healthcare professionals be better trained to address the mental health needs of students? ",
        "What are the security risks associated with online financial transactions?",
        "How can technology be used to create more efficient and sustainable agricultural practices?",
        "What are the financial implications of offering buy-now-pay-later options to customers?",
        "How can schools incorporate energy conservation practices into their curriculum? ",
        "Can genetically modified crops be used to improve the nutritional value of food and combat malnutrition?",
        "How can big data analytics be used to optimize inventory management in retail stores?",
        "What are the potential environmental impacts of increased automation in manufacturing?",
        "How can financial institutions leverage artificial intelligence to detect and prevent fraud?",
        "What are the ethical implications of using genetically modified organisms (GMOs) in agriculture?",
        "How can educational institutions prepare students for the jobs of the future?",
        "What are the economic benefits of investing in renewable energy infrastructure?",
        "How can the healthcare industry use technology to improve patient outcomes?",
        "What are the challenges of ensuring cybersecurity in the manufacturing sector?",
        "How can retailers personalize the shopping experience for customers in physical stores?",
        "What role can government regulation play in promoting sustainable agricultural practices?",
        "How can financial literacy programs help individuals make informed financial decisions?",
        "What are the potential benefits of using 3D printing in manufacturing processes?",
        "How can the education sector bridge the digital divide and ensure equitable access to technology?",
        "What are the environmental implications of the fashion industry's current production practices?",
        "How can healthcare providers improve communication and collaboration with patients?",
        "What are the challenges of integrating artificial intelligence into financial markets?",
        "How can manufacturers use automation to improve worker safety?",
        "What are the benefits and drawbacks of vertical farming for agriculture?",
        "How can retailers leverage social media to reach new customers and build brand loyalty?",
        "What are the financial considerations for small businesses looking to adopt sustainable practices?",
        "How can educational institutions prepare students for the challenges of climate change?",
        "What are the ethical considerations surrounding the use of gene editing technologies in healthcare?",
        "How can financial institutions offer more inclusive financial products and services?",
        "What are the challenges of implementing sustainable supply chains in the manufacturing sector?",
        "How can farmers use technology to improve crop yields and reduce waste?",
        "How can the retail industry reduce its carbon footprint?",
        "What are the economic implications of an aging population on the healthcare system?",
        "How can financial institutions use data analytics to personalize financial products for customers?",
        "What are the potential benefits of artificial intelligence for personalized learning in education?",
        "How can the energy sector transition to a more sustainable and renewable energy mix?",
        "What are the ethical considerations surrounding the use of telemedicine in healthcare?",
        "How can manufacturers use robots to perform dangerous or repetitive tasks?",
        "What are the challenges of ensuring food security in a growing global population?",
        "How can retailers use data analytics to optimize pricing and promotions?",
        "What is the role of financial advisors in a world of increasingly automated financial services?",
        "How can educational institutions create a more inclusive learning environment for all students?",
        "What are the economic benefits of investing in early childhood education?",
        "How can the healthcare industry address the growing problem of antibiotic resistance?",
        "What are the regulatory challenges associated with cryptocurrency and other digital assets?",
        "How can manufacturers use the Internet of Things (IoT) to improve production efficiency?",
        "What are the ethical considerations surrounding the use of performance-enhancing drugs in agriculture?",
        "How can the retail industry create a seamless omnichannel shopping experience for customers?",
        "What are the financial implications of student loan debt on the overall economy?",
        "How can educational institutions promote critical thinking skills in students?",
        "What are the environmental and health impacts of air pollution from the energy sector?",
        "How can healthcare providers improve access to affordable healthcare for all citizens?",
        "What are the challenges of integrating artificial intelligence into the supply chain management process?",
        "How can manufacturers use recycled materials in their production processes to reduce waste?",
        "What are the benefits of using vertical integration in the agricultural industry?",
        "How can retailers leverage customer data to personalize marketing campaigns?",
        "What role can financial technology (FinTech) play in promoting financial inclusion?",
        "How can educational institutions prepare students for careers in the STEM fields?",
        "What are the ethical considerations surrounding the use of artificial intelligence in scientific research?",
        "How can financial institutions mitigate the risks associated with cyberattacks?",
        "What are the challenges of balancing economic growth with environmental sustainability in the manufacturing sector?",
        "How can farmers adapt to the changing climate and extreme weather events?",
        "How can the retail industry reduce its reliance on plastic packaging?",
        "What is the future of healthcare delivery models, such as telehealth and remote patient monitoring?",
        "How can financial institutions help individuals save for retirement?",
        "What are the potential benefits of using augmented reality (AR) in educational settings?",
        "What are the economic and social benefits of investing in renewable energy sources?",
        "What are the ethical considerations surrounding the use of human subjects in medical research?",
        "How can manufacturers use lean manufacturing principles to reduce waste and improve efficiency?",
        "How can advancements in agricultural technology improve food safety and traceability?",
        "How can retailers create a more sustainable supply chain by sourcing products locally?",
        "What is the role of government regulation in ensuring fair competition in the financial services industry?",
        "How can educational institutions provide students with the necessary skills for lifelong learning?",
        "What are the economic benefits of investing in infrastructure development?",
        "How can the healthcare industry address the growing shortage of healthcare professionals?",
        "What are the regulatory challenges associated with the development and use of autonomous vehicles?"
    ]
    for q in queries:
        print(llm.inference(q))


if __name__ == '__main__':
    main()
