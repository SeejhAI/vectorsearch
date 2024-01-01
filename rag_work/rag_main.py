import google.generativeai as genai
import os
import os
from dotenv import load_dotenv
import requests
load_dotenv()


DB_URI: str = os.getenv("DB_URI")
API_KEY: str = os.getenv("API_KEY")
genai.configure(
    api_key=API_KEY)
model = genai.GenerativeModel(
    model_name='gemini-pro')

response = model.generate_content(
          """User Suppose you are examiner and are going to take a test so you have to  generate a set of 20 multiple-choice questions MCQs on the subject of follwoing artical
    Each question should include 4  answer options, and please provide the correct answer for each question along with a brief explanation. 
    Ensure that the questions should be from given artical . 
    Please include a comment with each question to explain its relevance to the chosen 


If you feel stagnated in your work position, it is high time you learnt new skills. As we usher in 2024, you should set learning resolutions that will see you acquiring more skills that you can use either at work or as a side hustle, passive income, and other avenues.

In as much as you have other skills that you actively use in your daily life, it is time that you challenged yourself to do more. At the end of the day, you will be on the same page as other professionals in your line of work. Therefore, choose any of these skills and acquire them in 2024. You won’t regret your decision.

One of the most in-demand skills is data analysis. Companies are continually converting their data into digital formats for easy analysis and collaboration. Therefore, as a data analyst, you can play a huge role in helping them compile data and even provide it in a readable format that anyone can internalize. Irrespective of your career line, all industries require data analysts. You will need to be well-equipped with Microsoft Excel, SQL, Power BI, Tableau, R Studio, and other data visualization tools.

If you are in the marketing industry, gaining digital marketing and ecommerce skills can also be crucial for you. Most people nowadays even prefer making online purchases rather than going to physical shops. People even prefer searching on the internet so that they can get information about various things.

In digital marketing, you can learn strategies to put in place to attract the right audience on social media to your website or other platforms. Gaining skills in content writing, search engine optimization, the best influencer strategies, email marketing, social media marketing, and affiliate marketing can help you thrive in the marketing industry.

Currently the Institute of Business Management, Karachi is offering a diploma program for four months. Over the last two years, they have completed 12 batches successfully – resulting in 300 success stories. Many of the beneficiaries got a job promotion, job overseas or started a passive income channel. It is an ideal programme for all age groups.

Artificial intelligence is another great skill that can take you far. With the continuation of artificially developed programmes like ChatGPT and much more, you are sure that the future is bright in that industry. You can learn both artificial intelligence and machine learning all together.

There are many AI tools continually being used in different industries to make work easier. So, why not join the group and help your company grow? AI is revolutionizing different industries like healthcare, finance, etc.

Cybersecurity is another attractive skill that you can learn. With everything being digital, there are a lot of threats of cyberattacks. Therefore, you can be a valuable asset to your company or even be a cybersecurity consultant and help many other companies to have secure systems. Just imagine malware, spyware, or viruses disrupting a whole company, or even a bank getting such issues and leading to the loss of a large amount of money. So, guess how much you will be in demand when you gain the skill? Help safeguard valuable data assets for others!

Also, cybersecurity is diverse, and if you focus on it, you can grow since you will be more equipped with most infrastructure components. Indeed, cybersecurity expertise is highly sought after.

User experience and user interface design skills can also take you a long way. In this, you will need to gain skills on how you can boost seamless interactions between customers and digital products. For example, know how to make it easy for people to make online purchases – you think of end users. With this, you can also consider getting app development and web development skills to go hand in hand with UX and UI design skills. At the end of the day, you need to make it easy for people to make online purchases or even interact with digital products.

Another attractive skill to learn in 2024 is robotic process automation. In this, you will learn how best to automate tasks. For example, you can check how Zapier works to make processes take place easily. Therefore, you will be able to streamline workflows in your line of work and even boost business operations. However, there is a need to be careful to prevent any errors. You can also acquire artificial intelligence and machine learning skills to go hand in hand with robotic process automation.

Another skill you should consider getting is cloud computing. In this, you offer computing services through the internet. You can decide to be a cloud administrator or cloud engineer and work in different industries like finance, healthcare, education, and much more. You will be able to help people troubleshoot problems while online without necessarily going to them. Since it is broad, you will need to decide what you want to specialize in.

Acquiring blockchain skills can also go a long way in ensuring you prosper in your career. Blockchain is what is behind cryptocurrencies and much more. In simple terms, it operates as a decentralized and transparent digital ledger that makes it easy for seamless operations. Transactions are made across a specific network. Due to its complex nature, blockchain makes all the transactions secure and reduces potential risks. In the blockchain, you will learn more about wallets, cryptography, protocols, public key encryption, and much more.

Agile methodologies skills in 2024 can help you in your career. Most companies are shifting to use agile frameworks for seamless project management. You can also consider gaining skills in project management which go hand in hand with the agile methodologies that can help in easy project delivery. Through project management skills, you will be able to easily plan, execute, and deliver projects based on a certain budget and timeline; you also use relevant inputs to ensure the project works.

Lastly, you can focus on polishing your emotional intelligence skills. It is an interpersonal skill that fosters easy communication among colleagues, decision-making, conflict resolution, empathy, etc. You need to be able to know how to handle situations when faced with any issues. At times, we underestimate the importance of knowing how to bond with others, however, it is really important for the growth of any company, teamwork, and even the completion of projects. It teaches you how to react when things go wrong.

If you were not sure of the skills to gain in 2024, these 10 options can give you an idea. At the end of the day, you need to decide to spare time to gain the new skills that will help you in your career. Once you gain the relevant skills, be sure to use them and not just gain skills for the certificate. Gain skills so that you can help your company or work as a consultant and work with other companies to solve issues in real-time.""")
print(response.text)
    #  The opposite of hot is cold.'
        