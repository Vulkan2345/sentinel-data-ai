import re
from typing import List, Dict, Any

# Expresiones regulares comunes para PII y Secretos
REGEX_PATTERNS = {
    "Email": r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+",
    "AWS API Key": r"(?i)AKIA[0-9A-Z]{16}",
    "Google Cloud Key": r"(?i)AIza[0-9A-Za-z_-]{35}",
    "Credit Card": r"\b(?:\d[ -]*?){13,16}\b"
}

def detect_regex(text: str) -> List[Dict[str, Any]]:
    findings = []
    lines = text.split("\n")
    
    for line_idx, line in enumerate(lines, 1):
        for data_type, pattern in REGEX_PATTERNS.items():
            matches = re.finditer(pattern, line)
            for match in matches:
                findings.append({
                    "type": data_type,
                    "match_value": "****" + match.group(0)[-4:] if len(match.group(0)) > 4 else "****",
                    "line_number": line_idx,
                    "severity": "HIGH" if "Key" in data_type else "MEDIUM"
                })
                
    return findings

def analyze_with_gemini(text: str) -> str:
    # TODO: Integración real con google-generativeai usando settings.GEMINI_API_KEY
    # Por ahora se simula para no bloquear la ejecución si no hay API Key configurada
    return "Análisis de Gemini pendiente"

def analyze_content(text: str) -> Dict[str, Any]:
    regex_findings = detect_regex(text)
    gemini_summary = analyze_with_gemini(text)
    
    return {
        "regex_findings": regex_findings,
        "ai_summary": gemini_summary,
        "total_findings": len(regex_findings)
    }
