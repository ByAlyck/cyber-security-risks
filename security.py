import random

def risk_assessment():
    risks = {
        'Malware': {
            'weight': 0.4,
            'impact': 'High',
            'vulnerabilities': ['Outdated antivirus software', 'Unpatched operating system']
        },
        'Phishing Attack': {
            'weight': 0.3,
            'impact': 'Medium',
            'vulnerabilities': ['Lack of employee awareness', 'Weak email filtering']
        },
        'Data Breach': {
            'weight': 0.2,
            'impact': 'High',
            'vulnerabilities': ['Insufficient access controls', 'Insecure data storage']
        },
        'Denial of Service (DoS) Attack': {
            'weight': 0.1,
            'impact': 'Low',
            'vulnerabilities': ['Inadequate network bandwidth', 'Weak firewall configuration']
        }
    }
    
    for risk, details in risks.items():
        probability = random.uniform(0, 1)
        if probability < details['weight']:
            print(f"The risk of {risk} is high with a potential impact of {details['impact']}.")
            print("Vulnerabilities to address:")
            for vulnerability in details['vulnerabilities']:
                print(f"- {vulnerability}")
            print()
        else:
            print(f"The risk of {risk} is low.")
            print()
            
risk_assessment()