from abc import ABC, abstractmethod
import copy
from typing import Dict

from document import Document
from email import Email
from report import Report

# Registro de documentos (opcional)
class DocumentRegistry:
    _DOCUMENT_CACHE: Dict[str, Document] = {}

    @classmethod
    def initialize(cls):
        # Inicializar con algunos prototipos predefinidos
        monthly_report = Report()
        monthly_report.set_title("Monthly Report Template")
        monthly_report.set_author("System")
        monthly_report.set_creation_date("2025-03-01")
        monthly_report.set_department("All Departments")
        monthly_report.set_number_of_pages(5)
        monthly_report.set_report_data("<<Insert monthly data here>>")
        cls._DOCUMENT_CACHE["monthlyReportTemplate"] = monthly_report

        meeting_invitation = Email()
        meeting_invitation.set_title("Meeting Invitation Template")
        meeting_invitation.set_author("System")
        meeting_invitation.set_creation_date("2025-03-01")
        meeting_invitation.set_recipients("<<Recipients>>")
        meeting_invitation.set_subject("Meeting Invitation: <<Topic>>")
        meeting_invitation.set_body("Dear team,\n\nPlease join us for a meeting about <<Topic>> on <<Date>> at <<Time>>.\n\nBest regards,\n<<Your Name>>")
        meeting_invitation.set_has_attachments(False)
        cls._DOCUMENT_CACHE["meetingInvitationTemplate"] = meeting_invitation

    @classmethod
    def get_document(cls, document_id):
        cached_document = cls._DOCUMENT_CACHE.get(document_id)
        if cached_document:
            return cached_document.clone()
        return None

    @classmethod
    def add_document(cls, document_id, document):
        cls._DOCUMENT_CACHE[document_id] = document


# Inicializar el registro
DocumentRegistry.initialize()