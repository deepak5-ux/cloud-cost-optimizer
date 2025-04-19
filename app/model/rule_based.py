# app/model/rule_based.py

def rule_based_fallback(workload_type: str, traffic_level: str, budget: str) -> str:
    rule_map = {
        ('Web App', 'Low', 'Low'): 't2.micro',
        ('Web App', 'Medium', 'Medium'): 't3.medium',
        ('Web App', 'High', 'High'): 'm5.large',
        ('ML Training', 'High', 'High'): 'p3.2xlarge',
        ('ML Training', 'Medium', 'Medium'): 'g4dn.xlarge',
        ('Database', 'High', 'High'): 'r5.large',
        ('Database', 'Low', 'Low'): 't3.micro',
        ('Batch Job', 'Low', 'Low'): 't3.small',
        ('Batch Job', 'High', 'High'): 'c5.2xlarge',
        ('Media Server', 'High', 'High'): 'c5n.4xlarge',
    }
    return rule_map.get((workload_type, traffic_level, budget), 't3.medium')  # default fallback
