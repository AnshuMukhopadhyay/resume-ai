ROLE_BUZZWORDS = {

    "Data Science": [
        "python", "machine learning", "deep learning", "pandas",
        "numpy", "sql", "statistics", "data analysis",
        "data visualization", "model", "prediction", "regression",
        "classification", "scikit-learn"
    ],

    "Python Developer": [
        "python", "flask", "django", "fastapi",
        "rest api", "backend", "oop", "sql",
        "api development"
    ],

    "Java Developer": [
        "java", "spring", "spring boot", "hibernate",
        "microservices", "rest api", "jpa", "sql",
        "backend development"
    ],

    "Web Designing": [
        "html", "css", "javascript", "responsive design",
        "bootstrap", "ui", "ux", "frontend",
        "web development"
    ],

    "DevOps Engineer": [
        "docker", "kubernetes", "aws", "cloud",
        "ci/cd", "linux", "jenkins",
        "infrastructure", "automation"
    ],

    "HR": [
        "recruitment", "talent acquisition",
        "employee engagement", "payroll",
        "hr policies", "onboarding",
        "communication"
    ],

    "Sales": [
        "sales", "lead generation", "crm",
        "negotiation", "customer relationship",
        "business development", "targets"
    ],

    "Mechanical Engineer": [
        "autocad", "solidworks", "manufacturing",
        "thermodynamics", "mechanical design",
        "production", "quality control"
    ],

    "Civil Engineer": [
        "autocad", "construction", "site management",
        "structural analysis", "estimation",
        "project execution"
    ],

    "Electrical Engineering": [
        "power systems", "electrical machines",
        "circuit analysis", "matlab",
        "control systems"
    ],

    "Business Analyst": [
        "excel", "sql", "data analysis",
        "business intelligence", "reporting",
        "stakeholder communication"
    ],

    "Database": [
        "sql", "database design", "normalization",
        "indexing", "performance tuning",
        "stored procedures"
    ],

    "Hadoop": [
        "hdfs", "mapreduce", "hive",
        "spark", "big data",
        "distributed systems"
    ],

    "ETL Developer": [
        "etl", "data warehousing", "sql",
        "informatica", "data pipelines",
        "data integration"
    ],

    "Blockchain": [
        "blockchain", "smart contracts",
        "solidity", "ethereum",
        "cryptography", "web3"
    ],

    "Testing": [
        "manual testing", "test cases",
        "bug tracking", "software testing",
        "sdlc", "qa"
    ],

    "Automation Testing": [
        "selenium", "test automation",
        "python", "java", "ci/cd",
        "automation frameworks"
    ],

    "Network Security Engineer": [
        "network security", "firewalls",
        "cybersecurity", "ethical hacking",
        "linux", "penetration testing"
    ],

    "Operations Manager": [
        "operations management",
        "process optimization",
        "team management",
        "planning", "execution"
    ],

    "PMO": [
        "project management", "scheduling",
        "risk management", "stakeholder management",
        "project coordination"
    ],

    "SAP Developer": [
        "sap", "abap", "erp",
        "sap modules", "business processes"
    ],

    "DotNet Developer": [
        ".net", "c#", "asp.net",
        "mvc", "sql server",
        "backend development"
    ],

    "Health and fitness": [
        "fitness training", "nutrition",
        "workout planning", "personal training",
        "client coaching"
    ],

    "Arts": [
        "creativity", "visual design",
        "illustration", "art direction",
        "design thinking"
    ],

    "Advocate": [
        "legal research", "drafting",
        "court procedures", "legal documentation",
        "case analysis"
    ]
}

def extract_buzzwords(text, role):
    text = text.lower()
    return list({
        bw for bw in ROLE_BUZZWORDS.get(role, [])
        if bw in text
    })
