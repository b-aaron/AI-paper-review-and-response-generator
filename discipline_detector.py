"""
discipline_detector.py
Uses an LLM to detect the academic discipline of a research paper.
"""

from llm_client import LLMClient


_SYSTEM_PROMPT = (
    "You are an academic librarian with broad expertise across all scientific and "
    "humanistic disciplines. Given the full text (or an excerpt) of a research paper, "
    "identify the primary academic discipline or field it belongs to. "
    "Reply with a single, concise discipline name (e.g., 'Computer Science', "
    "'Molecular Biology', 'Economics', 'Materials Science', etc.). "
    "Do not include any explanation or additional text."
)

_USER_TEMPLATE = (
    "Please identify the primary academic discipline of the following research paper.\n\n"
    "--- PAPER TEXT (may be truncated) ---\n"
    "{paper_text}\n"
    "--- END OF PAPER TEXT ---\n\n"
    "Discipline:"
)

# How many characters of the paper to send to the LLM for discipline detection.
# Sending the full paper is expensive; the abstract + introduction are usually enough.
_MAX_CHARS = 8000


class DisciplineDetector:
    """Detect the academic discipline of a research paper using an LLM."""

    def __init__(self, llm_client: LLMClient):
        self.llm = llm_client

    def detect(self, paper_text: str) -> str:
        """
        Return the primary academic discipline of the paper.

        Parameters
        ----------
        paper_text : str
            Full or partial text of the research paper.

        Returns
        -------
        str
            The detected discipline (e.g., 'Computer Science').
        """
        excerpt = paper_text[:_MAX_CHARS]
        user_prompt = _USER_TEMPLATE.format(paper_text=excerpt)
        discipline = self.llm.chat(
            system_prompt=_SYSTEM_PROMPT,
            user_prompt=user_prompt,
            max_tokens=64,
        )
        return discipline.strip()
